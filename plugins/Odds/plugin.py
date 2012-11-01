###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import urllib2
import json
import xmltodict
import datetime
import time
import re

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class Odds(callbacks.Plugin):
    """Add the help for "@plugin help Odds2" here
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

    def odds(self, irc, msg, args, optsport, optteam):
        """[sport] <team>
        Display wager Odds for sport. Valid sports: MLB, NHL, NCAAB, NBA, NFL and NCAAF. Optional: to
        display only a specific event, place in the team.
        """

        optsport = optsport.upper()
        validsports = { 'MLB': '204',
                        'NHL': '523',
                        'NCAAB': '525',
                        'NBA': '217',
                        'NFL': '203',
                        'NCAAF': '592'
                        }

        if not optsport in validsports: 
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " sportname must be one of the following: %s" % (validsports.keys()))
            return

        url = 'http://www.bettingexpress.com/lines/cgi/lines.cgi?tem=parse&sport=%s&ct=text/xml' % (validsports[optsport])

        try:
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
        except URLError, e:
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " fetching bettingexpress.com URL: %s" % (e.reason))
            return
        except HTTPError, e:
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " fetching bettingexpress.com URL: %s" % (e.code))
            return

        try:
            response_data = response.read()
            xmldata = xmltodict.parse(response_data)
        except:
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " Failed to read and parse XML response data.")
            return

        #games = xmldata.get('ParseLines', {'ParseLines':None}).get('Game', None)
        games = xmldata['ParseLines']

        # check if we have anything or did not find the keys within the dict. 
        if len(games) < 1 or games == None:
            irc.reply(ircutils.mircColor("ERROR:", 'red') + " I did not find any entries in data.")
            return

        if optsport == "NFL":
            for game in games['Game']:
                awayTeam = game.get('AwayTeam', None)
                homeTeam = game.get('HomeTeam', None)
                total = game.get('Total', None)
                line = game.get('Line', None)
                atMl = game.get('AwayTeamMoneyLine', None)
                htMl = game.get('HomeTeamMoneyLine', None)
                date = game.get('Date', None)
                
                if awayTeam != None and homeTeam != None and total != None and line != None and date != None:
                    aTeam, awayCity = self._tsplit(awayTeam, ('('))
                    hTeam, homeCity = self._tsplit(homeTeam, ('('))
                    date1,date2 = date.split() # time is date time, split by space.
                    
                    if atMl != "OFF" and htMl != "OFF" and atMl < htMl: # no line placement, so we use moneyline to determine.     
                        output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(aTeam, hTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    elif atMl != "OFF" and htMl != "OFF" and atMl > htMl:
                        output = "{0}[-{1}] @ {2}  o/u: {3}  {4}/{5}  {6}".format(aTeam, ircutils.bold(abs(float(line))), hTeam,total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    else:
                        output = "{0} @ {1}[{2}]  o/u: {3}  {4}/{5}  {6}".format(aTeam, hTeam, ircutils.bold(line.strip()), total, self._fpm(atMl), self._fpm(htMl), self._timeFmt(date2))
                    
                    irc.reply(output)
                
        elif optsport == "MLB":
            # get date for checking against events
            today = datetime.date.today().strftime("%m/%d/%Y") # 2012-06-30
        
            for game in games['Game']:
                htML = game.get('HomeTeamMoneyLine', None)
                atML = game.get('AwayTeamMoneyLine', None)
                awayTeam = game.get('AwayTeam', None)
                homeTeam = game.get('HomeTeam', None)
                total = game.get('Total', None)
                date = game.get('Date', None) # if date1 == today:

                if awayTeam != None and homeTeam != None and date != None:
                    ateam, acity, apitcher = self._tsplit(awayTeam, ('(',')'))
                    hteam, hcity, hpitcher = self._tsplit(homeTeam, ('(',')'))
                    date1,date2 = date.split()

                    if date1 == today: # so we only print today.
                        output = ateam + "(" + apitcher + ")" + ircutils.bold(" @ ") + hteam + "(" + hpitcher + ")" 
                        output += "  " + ircutils.underline("o/u") + ": " + total 
                        output += "  " + self._fpm(atML) + "/" + self._fpm(htML) 
                        output += "  " + self._timeFmt(date2)
            
                        irc.reply(output)
        else:
            irc.reply("I have not done odds for: %s" % optsport)            

    odds = wrap(odds, [('somethingWithoutSpaces'), optional('somethingWithoutSpaces')])

Class = Odds


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
