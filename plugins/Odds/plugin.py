###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import urllib2
import datetime
import time
from xml.etree import ElementTree

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class Odds(callbacks.Plugin):
    """Add the help for "@plugin help Odds" here
    This should describe *how* to use this plugin."""
    threaded = True

    def _timeFmt(self, string):
        """This converts 24hr time into 12hr time."""
        return time.strftime('%I:%M %p', time.strptime(string, '%H:%M'))


    def _fpm(self, string):
        """Format the string for output with color."""
        try:
            if float(str(string).replace('.0','')) > 0:
                string = ircutils.mircColor((str(string)), 'green')
            else:
                string = ircutils.mircColor((str(string)), 'red')
            return string
        except:
            return ircutils.bold(string)


    ## {{{ http://code.activestate.com/recipes/577616/ (r5)
    def _tsplit(self, string, delimiters):
        """Behaves str.split but supports multiple delimiters."""
    
        delimiters = tuple(delimiters)
        stack = [string,]
    
        for delimiter in delimiters:
            for i, substring in enumerate(stack):
                substack = substring.split(delimiter)
                stack.pop(i)
                for j, _substring in enumerate(substack):
                    stack.insert(i+j, _substring)
            
        return stack
        
    ####################
    # public functions.#
    ####################
    
    def odds(self, irc, msg, args, optsport, optteam):
        """[sport] <team>
        Display wager Odds for sport. Valid sports: MLB, NHL, NCB, NBA, NFL and NCF. For NCB/NCF, you must specify team.
        ex: odds NCF Alabama.
        """
        
        today = datetime.date.today().strftime("%m/%d/%Y") # get date for checking against games only today. Useful for MLB.

        optsport = optsport.upper()
        validsports = { 'MLB': '204',
                        'NBA': '200',
                        'NFL': '203',
                        'NCF': '206'
                        }

        if not optsport in validsports: 
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " sportname must be one of the following: %s" % (validsports.keys()))
            return

        url = 'http://www.bettingexpress.com/lines/cgi/lines.cgi?tem=parse&sport=%s&ct=text/xml' % (validsports[optsport])

        try:
            request = urllib2.Request(url, headers={"Accept" : "application/xml"})
            u = urllib2.urlopen(request)
        except:
            irc.reply("Failed to open: %s" % url)
            return

        try:
            tree = ElementTree.parse(u)
            root = tree.getroot()
            games = tree.findall('Game')
        except:
            irc.reply("ERROR: I was unable to process XML entries for: %s" % optsport)
            return
        
        if len(games) < 1 or games == None: # last check to make sure we have at least one.
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " I did not find any entries for: %s" % optsport)
            return
            
        if optsport == "NCF":
            if not optteam or len(optteam) < 1:
                irc.reply("For NCF odds, you must have a team/string to search for that is longer than one character. Ex: odds NCF bama")
                return
            
            counter = 0 # since we're searching for a string, a bad search string
            outputList = [] # make a list to output search results.
            
            for entry in games: # now transform into a dict so we can parse.
                game = dict()
                for elem in entry:
                    game[elem.tag] = elem.text
                
                if optteam.lower() in game.get('AwayTeam', None).lower() or optteam.lower() in game.get('HomeTeam', None).lower(): # if we find a match, now go through the routine.
                    awayTeam = game.get('AwayTeam', None)
                    homeTeam = game.get('HomeTeam', None)
                    total = game.get('Total', None)
                    line = game.get('Line', None)
                    atMl = game.get('AwayTeamMoneyLine', None)
                    htMl = game.get('HomeTeamMoneyLine', None)
                    date = game.get('Date', None)
                    
                    if htMl != None and atMl != None and awayTeam != None and homeTeam != None and total != None and line != None and date != None:
                        date1,date2 = date.split() # time is date time, split by space.
                        
                        if atMl != "OFF" and htMl != "OFF" and atMl < htMl: # no line placement, so we use moneyline to determine.     
                            output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(awayTeam, homeTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                        elif atMl != "OFF" and htMl != "OFF" and atMl > htMl:
                            output = "{0}[-{1}] @ {2}  o/u: {3}  {4}/{5}  {6}".format(awayTeam, ircutils.bold(abs(float(line))), homeTeam,total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                        else:
                            output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(awayTeam, homeTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    
                        outputList.append(output) # append to output.
                
            # now, output our list from above. 
            if len(outputList) < 1:
                irc.reply("I did not find any results in {0} matching '{1}'".format(ircutils.underline(optsport), ircutils.bold(optteam)))
                return
            else:
                for each in outputList:
                    if counter >= self.registryValue('maximumOutput'):
                        irc.reply("I've reached the maxmium of {0} results searching '{1}'. Please narrow your search string.".format(self.registryValue('maximumOutput'), optteam))
                        return
                    else:
                        counter += 1
                        irc.reply(each)
                
        elif optsport == "NFL":
            for entry in games:
                game = dict()
                for elem in entry:
                    game[elem.tag] = elem.text
                
                awayTeam = game.get('AwayTeam', None)
                homeTeam = game.get('HomeTeam', None)
                total = game.get('Total', None)
                line = game.get('Line', None)
                atMl = game.get('AwayTeamMoneyLine', None)
                htMl = game.get('HomeTeamMoneyLine', None)
                date = game.get('Date', None)
                
                if htMl != None and atMl != None and awayTeam != None and homeTeam != None and total != None and line != None and date != None:
                    aTeam, awayCity = awayTeam.split('(', 1) 
                    hTeam, homeCity = homeTeam.split('(', 1)
                    date1,date2 = date.split() # time is date time, split by space.
                    
                    if atMl != "OFF" and htMl != "OFF" and atMl < htMl: # no line placement, so we use moneyline to determine.     
                        output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(aTeam, hTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    elif atMl != "OFF" and htMl != "OFF" and atMl > htMl:
                        output = "{0}[-{1}] @ {2}  o/u: {3}  {4}/{5}  {6}".format(aTeam, ircutils.bold(abs(float(line))), hTeam,total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    else:
                        output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(aTeam, hTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    
                    irc.reply(output)
                
        elif optsport == "MLB":
            for entry in games:
                game = dict()
                for elem in entry:
                    game[elem.tag] = elem.text
                    
                htMl = game.get('HomeTeamMoneyLine', None)
                atMl = game.get('AwayTeamMoneyLine', None)
                awayTeam = game.get('AwayTeam', None)
                homeTeam = game.get('HomeTeam', None)
                total = game.get('Total', None)
                date = game.get('Date', None)

                if htMl != None and atMl != None and awayTeam != None and homeTeam != None and total != None and date != None:
                    ateam, acity, apitcher = self._tsplit(awayTeam, ('(',')')) # they wrap team(Pitcher) and we split using a special tsplit
                    hteam, hcity, hpitcher = self._tsplit(homeTeam, ('(',')'))
                    date1,date2 = date.split()

                    if date1 == today: # so we only print today.
                        output = "{0}({1}) @ {2}({3})  o/u: {4}  {5}/{6}  {7}".format(ateam, apitcher, hteam, hpitcher, total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
            
                        irc.reply(output)

        elif optsport == "NBA":
            for entry in games:
                game = dict()
                for elem in entry:
                    game[elem.tag] = elem.text
                    
                htMl = game.get('HomeTeamMoneyLine', None)
                atMl = game.get('AwayTeamMoneyLine', None)
                awayTeam = game.get('AwayTeam', None)
                homeTeam = game.get('HomeTeam', None)
                total = game.get('Total', None)
                date = game.get('Date', None)

                if htMl != None and atMl != None and awayTeam != None and homeTeam != None and total != None and date != None:
                    ateam, awaycity = awayTeam.split('(', 1)
                    hteam, homecity = homeTeam.split('(', 1)
                    date1,date2 = date.split()

                    if date1 == today: # so we only print today.
                        output = "{0}({1}) @ {2}({3})  o/u: {4}  {5}/{6}  {7}".format(ateam, awaycity.replace(')',''), hteam, homecity.replace(')',''),\
                            total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
            
                        irc.reply(output)

        else:
            irc.reply("I have not done odds for: %s" % optsport)            

    odds = wrap(odds, [('somethingWithoutSpaces'), optional('somethingWithoutSpaces')])

Class = Odds


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
