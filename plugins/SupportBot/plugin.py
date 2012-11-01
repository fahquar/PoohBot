###
# encoding: utf-8
# Copyright (c) 2011, Arne Babenhauserheide
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
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

from threading import Timer

from time import time, sleep

writers = []

def greet(irc, nick, wait):
    """Write a greeting message"""
    irc.reply("Hi, "+nick+"! How are you today? If you are bored, feel free to harass PoohBear until he shows up.")

def thank(irc, nick):
    """Write a motivating message"""
    irc.reply("Welcome back, "+nick+"! Thank you for everything! :)")

class SupportBot(callbacks.Plugin):
    """The SupportBot welcomes new users who say something after 30s, if no other user wrote after the new user. It’s main goal is to tell the user that a real user should drop by soon.
    Just ignore it: It will work on its own."""
    threaded = True
    def __init__(self, irc):
          self.__parent = super(SupportBot, self)
          self.__parent.__init__(irc)
          self.watchnicks = ["qwebirc"]
          self.thanknicks = []# ["p0s", "toad"]
          self.wait = 5

    def doJoin(self, irc, msg):
        """Check if the user needs to be greeted."""
        if not True in (msg.nick.startswith(nick) for nick in self.watchnicks + self.thanknicks):
            return
        channels = msg.args[0].split(',')
        # only greet a person once.
        if msg.nick in writers:
            return

        if True in (msg.nick.startswith(nick) for nick in self.thanknicks):
            return thank(irc, msg.nick)

        writers.append(msg.nick)
        t = Timer(self.wait, self.conditionalMessage, [irc, msg])
        t.start()

    def doPart(self, irc, msg):
        """Remove the user from the list of writers."""
        if not True in (msg.nick.startswith(nick) for nick in self.watchnicks):
            return
        while msg.nick in writers:
            writers.remove(msg.nick)

    def conditionalMessage(self, irc, msg):
        global writers
        writernotme = [nick != msg.nick for nick
                       in writers[writers.index(msg.nick):]]
        otherwriters = True in writernotme
        if not otherwriters and msg.nick in writers:
            greet(irc, msg.nick, self.wait)
            # slice writers
        else:
            print "someone posted within", self.wait, "seconds. No need to greet.", writers[writers.index(msg.nick):], "writernotme", writernotme, "otherwriters?", otherwriters
        writers = writers[writers.index(msg.nick)+1:]

    def doPrivmsg(self, irc, msg):
        print msg
        global writers
        channel = msg.args[0]
        if msg.command == 'PRIVMSG' and irc.isChannel(channel):
            writers.append(msg.nick)
            print writers
        return msg


Class = SupportBot


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
