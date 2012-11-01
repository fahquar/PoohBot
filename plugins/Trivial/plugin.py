###
# Copyright (c) 2007, Benjamin N. Rubin
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###

import supybot.utils as utils
import supybot.conf as conf
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.ircmsgs as ircmsgs
import random, datetime, time
#from pysqlite3 import dbapi2 as sqlite
import sqlite3 as sqlite
from operator import itemgetter # sorted()
from array import array
from types import *
import supybot.log as log


class Question:
    def __init__(self,id=0, question=None,answer=None):
        self.rng = random.Random()
        self.rng.seed()
        self.question = question
        self.answer = answer
        self.id = id
        # Clean up answer, remove leading/trailing spaces and make lowercase
        self.answer = self.answer.strip().lower()
        if self.answer.endswith("\r\n"):
            self.answer = self.answer.rstrip("\r\n")
        self.hint = ""
        
        # Generate blanks for hint field
        for i in range(len(self.answer)):
            if self.answer[i].isalnum():
                self.hint += str(conf.supybot.plugins.Trivial.blankchar)
            else:
                self.hint +=answer[i]
    
    def check(self,guess=None):
        # Clean up guess, remove rtrailing spaces and make lowercase
        guess = guess.rstrip().lower()

        # Prevent string index out of range exceptions by padding right side of guess with spaces
        if len(guess) < len(self.answer):
            guess += " "*(len(self.answer) - len(guess))

        newHint = ""
        for j in range(len(self.answer)):
            if guess[j] == self.answer[j] and self.hint[j] in (str(conf.supybot.plugins.Trivial.blankchar)," "):
                newHint += guess[j]
            else:
                newHint += self.hint[j]
        self.hint = newHint
        return
    
##    def newHint(self):
##        if self.hint == "":
##            return
##        # Generate a new hint with some letters already filled in
##        #length = len(self.answer)//3   # One third of the answer will be revealed
##        length = 3
##        i = 0
##        while i < length:
##            pos = self.rng.randint(0,length)
##            if self.answer[pos] != self.hint[pos] and self.answer[pos] != '.':
##                #once again, need to convert the hint to an array
##                hintArray = array('c',self.hint)
##                hintArray[pos] = self.answer[pos]
##                self.hint = hintArray.tostring()
##                i += 1
    
    def isCorrect(self,guess=None):
        if self.answer == guess.rstrip().lower():
            return True
        else:
            return False

class Player:
    def __init__(self,nick,hostmask):
        self.nick = nick
        self.hostmask = hostmask
        self.db = sqlite.connect(str(conf.supybot.plugins.Trivial.db), check_same_thread = False)
    
    # Get the primary key of a player.  Search on both hostmask and nick
    def getPlayerID(self,nick,hostmask):
        cur = self.db.cursor()
        cur.execute("""SELECT id FROM trivia_player WHERE nick = "%s" OR  """)
        maxID=cur.fetchall()[0][0]

class Scoreboard:
    def __init__(self,player):
        self.scores = {}
        self.scores[player] = 0
    
    def add(self,player,amount):
        if player not in self.scores:
            self.scores[player] = amount
        else:
            self.scores[player] += amount
    
    def getSorted(self):
        our_list = self.scores.items()
        our_list.sort()
        k = {}   
        for item in our_list:
                k[item[0]] = item[1]
        return k
    
class Trivial(callbacks.Plugin):
    """Add the help for "@plugin help Trivial" here
    This should describe *how* to use this plugin."""
    #threaded = True
    def __init__(self,irc):
        self.__parent = super(Trivial, self)
        self.__parent.__init__(irc)
        self.db = sqlite.connect(str(conf.supybot.plugins.Trivial.db), check_same_thread = False)
        self.running = {}
        self.rng = random.Random()
        self.rng.seed()
        self.curQuestion = {}
        self.lastHint = {}
        self.scores = {}
    
    def add5(self,irc,msg,args):
        channel = msg.args[0]
        self.scores[channel].add(msg.nick,5)
        irc.queueMsg(ircmsgs.privmsg(msg.args[0],(self.getFormattedScores(channel))))
    
    def start(self,irc,msg,args):
        """Start a round of trivia if one is not already running"""
        if (self.running.get(msg.args[0]) == True):
            irc.error('Trivia is already running!')
            return
        self.running[msg.args[0]] = True
        irc.queueMsg(ircmsgs.privmsg(msg.args[0],'Starting a new round of Trivia!'))
        # Start a new round for the current channel only
        self.lastHint[msg.args[0]] = None
        #self.scores[msg.args[0][update(msg.args[1],0)
        self.scores[msg.args[0]] = Scoreboard(msg.nick)
        self.ask(irc,msg)
        
        return
    
    def stop(self,irc,msg,args):
        """Stop a round of trivia"""
        if (self.running.get(msg.args[0]) == False):
            irc.error('There is no game started!')
            return
        self.running[msg.args[0]] = False
        self.curQuestion.pop(msg.args[0])
        irc.queueMsg(ircmsgs.privmsg(msg.args[0],'Quitting Trivia'))
        irc.queueMsg(ircmsgs.privmsg(msg.args[0],("Scores: %s" % self.getFormattedScores(msg.args[0]))))
        return

    def getQuestion(self):
        cur = self.db.cursor()
        cur.execute("SELECT max(id) FROM trivia_question")
        maxID=cur.fetchall()[0][0]
        enabled = False
        while enabled != True:
            id = self.rng.randint(0,maxID)
            cur.execute("SELECT id,question,answer,enabled FROM trivia_question where id = %s" % id)
            q = cur.fetchall()[0]
            enabled = True
        return Question(q[0],q[1],q[2])
        
    def ask(self, irc, msg):
        channel = msg.args[0]
        if channel not in self.curQuestion:
            self.curQuestion[channel] = self.getQuestion()
        irc.queueMsg(ircmsgs.privmsg(channel,u"%s: %s?" % (ircutils.bold(self.curQuestion[channel].id), self.curQuestion[channel].question)))
        irc.queueMsg(ircmsgs.privmsg(channel,ircutils.bold("Answer:  ") + self.curQuestion[channel].hint))
       
       # Print answer to log for debugging purposes only
        log.critical(self.curQuestion[channel].answer)
        return
    
    def getFormattedScores(self,channel):
        scores = self.scores[channel].getSorted()
        format = None
        for player in scores:
            if format == None:
                format = '%s: %s' % (player,scores[player])
            else:
                format = '%s: %s, %s' % (player,scores[player],format)
        return format
    
    def score(self,irc,msg,args):
        irc.queueMsg(ircmsgs.privmsg(msg.args[0],("Scores: %s" % self.getFormattedScores(msg.args[0]))))
    
    def doPrivmsg(self, irc, msg):
        channel = msg.args[0]
        # Ignore messages that start with the command qualifier
        if msg.args[1].startswith('@'):
            return
        # Don't parse non-command messages if a trivia game isn't running 
        # or if there is no active question
        if channel not in self.running or channel not in self.curQuestion:
            return

        else:
            self.curQuestion[channel].check(msg.args[1])
            if self.curQuestion[channel].isCorrect(msg.args[1]) == False:
                if self.lastHint[channel] != self.curQuestion[channel].hint:
                    irc.queueMsg(ircmsgs.privmsg(channel,ircutils.bold("Answer:  ") + self.curQuestion[channel].hint))
                    self.lastHint[channel] = self.curQuestion[channel].hint
                
            else:
                # Answer is correct, assign points
                irc.queueMsg(ircmsgs.privmsg(channel,ircutils.bold("Answer:  ")  + "%s is correct!!" % self.curQuestion[channel].answer))
                irc.queueMsg(ircmsgs.privmsg(channel,"%s gets 5 points!!" % ircutils.bold(msg.nick)))
                self.scores[channel].add(msg.nick,5)
                irc.queueMsg(ircmsgs.privmsg(msg.args[0],("Scores: %s" % self.getFormattedScores(msg.args[0]))))
                self.curQuestion.pop(channel)
                self.ask(irc,msg)
        return

##    def hint(self,irc,msg,args):from operator import itemgetter
##        """Give a hint!"""
##        self.curQuestion[msg.args[0]].newHint()
##        irc.reply(self.curQuestion[msg.args[0]].hint)

    def addquestion(self,irc,msg,args):
        """<question>*<answer>   Add a question to the database. Separate 
        question and answer by an asterisk (*).  Please omit the question 
        mark from the end of the question."""
        cur = self.db.cursor()
        cur.execute("SELECT max(id) FROM trivia_question")
        maxID=cur.fetchall()[0][0]
        
        cur.execute('INSERT INTO trivia_question (id,question,answer,added,author_id,category_id,enabled) values (%s,"%s","%s","%s",1,1,"False")' %
                    (maxID + 1,str( ' '.join(args).split('*')[0]),str(' '.join(args).split('*')[1]),str(datetime.datetime.now())))
        self.db.commit()
        
        irc.reply("Question added to database.  Moderation Pending")
        

Class = Trivial
