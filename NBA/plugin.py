# -*- coding: utf-8 -*-
###
# Copyright (c) 2012, spline
# All rights reserved.
#
###

from BeautifulSoup import BeautifulSoup
import urllib2
import urllib
import re
import datetime
import time
import mechanize
import string
import collections
from itertools import izip, groupby, count
import sqlite3
import json

#supybot libs.
import supybot.utils as utils
from supybot.commands import *
import supybot.ircdb as ircdb
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

# specific subclass for average http://stackoverflow.com/a/3897106
class AvgDict(dict):
    def __init__(self):
        self._total = 0.0
        self._count = 0

    def __setitem__(self, k, v):
        if k in self:
            self._total -= self[k]
            self._count -= 1
        dict.__setitem__(self, k, v)
        self._total += v
        self._count += 1

    def __delitem__(self, k):
        v = self[k]
        dict.__delitem__(self, k)
        self._total -= v
        self._count -= 1

    def average(self):
        if self._count:
            return self._total/self._count

class NBA(callbacks.Plugin):
    """
    General NBA functions for IRC.
    """
    threaded = True

    def _validate(self, date, format):
        """Return true or false for valid date based on format."""
        try:
            datetime.datetime.strptime(date, format) 
            return True
        except ValueError:
            return False

    def _daysSince(self, string):
        a = datetime.date.today()
        b = datetime.datetime.strptime(string, "%B %d, %Y")
        b = b.date()
        delta = b - a
        delta = abs(delta.days)
        return delta

    def _dateFmt(self, string):
        """Return a short date string from a full date string."""
        return time.strftime('%m/%d', time.strptime(string, '%B %d, %Y'))
        
    def _b64decode(self, string):
        """Returns base64 encoded string."""
        import base64
        return base64.b64decode(string)
        
    # smart_truncate from http://stackoverflow.com/questions/250357/smart-truncate-in-python
    def _smart_truncate(self, text, length, suffix='...'):
        """Truncates `text`, on a word boundary, as close to the target length it can come."""

        slen = len(suffix)
        pattern = r'^(.{0,%d}\S)\s+\S+' % (length-slen-1)
        if len(text) > length:
            match = re.match(pattern, text)
            if match:
                length0 = match.end(0)
                length1 = match.end(1)
                if abs(length0+slen-length) < abs(length1+slen-length):
                    return match.group(0) + suffix
                else:
                    return match.group(1) + suffix
        return text

    def _shortenUrl(self, url):
        posturi = "https://www.googleapis.com/urlshortener/v1/url"
        headers = {'Content-Type' : 'application/json'}
        data = {'longUrl' : url}

        data = json.dumps(data)
        request = urllib2.Request(posturi,data,headers)
        response = urllib2.urlopen(request)
        response_data = response.read()
        shorturi = json.loads(response_data)['id']
        return shorturi
         
    # http://code.activestate.com/recipes/303279/#c7
    def _batch(self, iterable, size):
        c = count()
        for k, g in groupby(iterable, lambda x:c.next()//size):
            yield g

    def _remove_strong(self, string):
        string = re.sub('<strong>.*?</strong>','', string).strip()
        return string

    def _getAge(self, d):
        """ Calculate age from date """
        delta = datetime.datetime.now() - datetime.datetime.strptime(d, "%b %d, %Y") # Feb 22, 1986
        years, days = divmod(delta.days, 365.25)
        return '%dy, %dd' % (years, days)

    def _strip_html(self, string):
        string = re.sub("<.*?>", "", string)
        string = re.sub(r'\s\s+', ' ', string)
        return string

    def _millify(self, num):
        for x in ['','k','M','B','T']:
            if num < 1000.0:
                return "%3.1f%s" % (num, x)
            num /= 1000.0

    def _validteams(self):
        """Returns a list of valid teams for input verification."""
        db_filename = self.registryValue('dbLocation')
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            query = "select team from nba"
            cursor.execute(query)
            teamlist = []
            for row in cursor.fetchall():
                teamlist.append(str(row[0]))

        return teamlist
        
    def _translateTeam(self, db, column, optteam):
        """Translates optteam into proper string using database"""
        db_filename = self.registryValue('dbLocation')
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            query = "select %s from nba where %s='%s'" % (db, column, optteam)
            cursor.execute(query)
            row = cursor.fetchone()
            
            return (str(row[0]))

    def updateplugin(self, irc, msg, args):
        if not ircdb.checkCapability(msg.prefix, 'admin'):
            irc.reply("Must be an admin to run this.")
        else:
            import subprocess,os
            cmd = 'git pull'
            repoDir = os.path.abspath(os.path.dirname(__file__))
            pipe = subprocess.Popen(cmd, shell=True, cwd=repoDir,stdout = subprocess.PIPE,stderr = subprocess.PIPE )
            (out, error) = pipe.communicate()
            pipe.wait()
            irc.reply(out)
            irc.reply(error)
            return 
            
    updateplugin = wrap(updateplugin)
    
    
    ###############################
    ### PUBLIC FUNCTIONS ##########
    ###############################
    

    def nbateams(self, irc, msg, args):
        """Display a list of NBA teams for input."""
        
        teams = self._validteams()
        irc.reply("Valid teams are: %s" % (string.join([item for item in teams], " | ")))        
    
    nbateams = wrap(nbateams)

    
    def nbadraft(self, irc, msg, args, optyear, optround):
        """[year] [round]
        Display NBA draft information for year and round. Defaults to the latest draft and first round.
        Specify YYYY and round (1 or 2 most years) to show results for other years. Year must be 1960 or beyond.
        Ex: 1979 8 or 2011 2
        """
              
        if optyear: # if optyear is there, test for valid and if after 2003.
            testdate = self._validate(str(optyear), '%Y')
            if not testdate:
                irc.reply("Invalid year. Must be YYYY.")
                return
            if optyear < 1959:
                irc.reply("Error: Year must be after 1959. You put in: %s" % optyear)
                return
                 
        url = self._b64decode('aHR0cDovL3d3dy5iYXNrZXRiYWxsLXJlZmVyZW5jZS5jb20vZHJhZnQvTkJBXw==') + '%s.html' % optyear
        
        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to fetch: %s" % url)
            return
            
        soup = BeautifulSoup(html)
        
        if not soup.find('table', attrs={'id':'stats'}):
            irc.reply("Sorry, I could not find a table to parse. Perhaps something changed with formatting?")
            return

        table = soup.find('table', attrs={'id':'stats'}) 
        rows = table.findAll('tr', attrs={'class':''}) # empty class on the picks. stops polluting up them

        nbadraft = collections.defaultdict(list)

        for row in rows:
            tds = row.findAll('td')
            if len(tds) > 0: # cheap trick here.
                draftRound = str(row.findPrevious('th', attrs={'colspan':'2', 'class':'bold_text over_header'}, text=re.compile('^Round.*?')).replace('Round','').strip()) # need the re due to matches
                pickNum = tds[0].getText()
                team = tds[1].getText()
                player = tds[2].getText()
                appendString = "{0} - {1} - {2}".format(pickNum, team, ircutils.bold(player))
                nbadraft[draftRound].append(appendString)

        output = nbadraft.get(str(optround), None)
        
        if output:
            irc.reply("{0} NBA Draft Class Round {1} :: {2}".format(ircutils.bold(optyear),optround, string.join([item for item in output], " | ")))
        else:
            irc.reply("I did not find any draftees in round {0} for year {1}".format(optround, optyear))
            return
            
    nbadraft = wrap(nbadraft, [('int'), ('int')])

    
    def nbainjury(self, irc, msg, args, optlist, optteam):
        """<--details> [TEAM]
        Show all injuries for team. Example: NYK or BOS. Use --details to 
        display full table with team injuries.
        """
        
        details = False
        for (option, arg) in optlist:
            if option == 'details':
                details = True
        
        optteam = optteam.upper().strip()
        
        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return
        
        lookupteam = self._translateTeam('roto', 'team', optteam) 

        url = self._b64decode('aHR0cDovL3JvdG93b3JsZC5jb20vdGVhbXMvaW5qdXJpZXMvbmJh') + '/%s/' % lookupteam

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to grab: %s" % url)
            return

        soup = BeautifulSoup(html)
        
        if soup.find('div', attrs={'class': 'player'}):
            team = soup.find('div', attrs={'class': 'player'}).find('a').text
        else:
            irc.reply("No injuries found for: %s" % optteam)
            return
        table = soup.find('table', attrs={'align': 'center', 'width': '600px;'})
        t1 = table.findAll('tr')

        object_list = []

        for row in t1[1:]:
            td = row.findAll('td')
            d = collections.OrderedDict()
            d['name'] = td[0].find('a').text
            d['position'] = td[2].renderContents().strip()
            d['status'] = td[3].renderContents().strip()
            d['date'] = td[4].renderContents().strip().replace("&nbsp;", " ")
            d['injury'] = td[5].renderContents().strip()
            d['returns'] = td[6].renderContents().strip()
            object_list.append(d)

        if len(object_list) < 1:
            irc.reply("No injuries for: %s" % optteam)

        if details:
            irc.reply(ircutils.underline(str(team)) + " - " + str(len(object_list)) + " total injuries")
            irc.reply("{0:25} {1:3} {2:15} {3:<7} {4:<15} {5:<10}".format("Name","POS","Status","Date","Injury","Returns"))

            for inj in object_list:
                output = "{0:27} {1:<3} {2:<15} {3:<7} {4:<15} {5:<10}".format(ircutils.bold( \
                    inj['name']),inj['position'],inj['status'],inj['date'],inj['injury'],inj['returns'])
                irc.reply(output)
        else:
            irc.reply(ircutils.underline(str(team)) + " - " + str(len(object_list)) + " total injuries")
            irc.reply(string.join([item['name'] + " (" + item['returns'] + ")" for item in object_list], " | "))

    nbainjury = wrap(nbainjury, [getopts({'details':''}), ('somethingWithoutSpaces')])

    
    def nbateamtrans(self, irc, msg, args, optteam):
        """[team]
        Shows recent NBA transactions for [team]. Ex: NYY
        """
        
        optteam = optteam.upper().strip()

        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return
            
        lookupteam = self._translateTeam('eid', 'team', optteam) 
        
        url = self._b64decode('aHR0cDovL20uZXNwbi5nby5jb20vbmJhL3RlYW10cmFuc2FjdGlvbnM=') + '?teamId=%s&wjb=' % lookupteam

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to load: %s" % url)
            return
        
        html = html.replace('<div class="ind tL"','<div class="ind"').replace('<div class="ind alt"','<div class="ind"')

        soup = BeautifulSoup(html)
        t1 = soup.findAll('div', attrs={'class': 'ind'})

        if len(t1) < 1:
            irc.reply("No transactions found for %s" % optteam)
            return

        for item in t1:
            if "href=" not in str(item):
                trans = item.findAll(text=True)
                irc.reply("{0:8} {1}".format(ircutils.bold(str(trans[0])), str(trans[1])))

    nbateamtrans = wrap(nbateamtrans, [('somethingWithoutSpaces')])
    
    
    def nbavaluations(self, irc, msg, args):
        """
        Display current NBA team valuations from Forbes.
        """
        
        url = self._b64decode('aHR0cDovL3d3dy5mb3JiZXMuY29tL25iYS12YWx1YXRpb25zL2xpc3Qv')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to load: %s" % url)
            return
 
        soup = BeautifulSoup(html)
        tbody = soup.find('tbody', attrs={'id':'listbody'})
        rows = tbody.findAll('tr')

        object_list = []

        for row in rows:
            rank = row.find('td', attrs={'class':'rank'})
            team = rank.findNext('td')
            value = team.findNext('td')
            yrchange = value.findNext('td')
            debtvalue = yrchange.findNext('td')
            revenue = debtvalue.findNext('td')
            operinc = revenue.findNext('td')
            d = collections.OrderedDict()
            d['rank'] = rank.renderContents().strip()
            d['team'] = team.find('h3').renderContents().strip()
            d['value'] = value.renderContents().strip()
            d['yrchange'] = yrchange.renderContents().strip()
            d['debtvalue'] = debtvalue.renderContents().strip()
            d['revenue'] = revenue.renderContents().strip()
            d['operinc'] = operinc.renderContents().strip()
            object_list.append(d)
        
        irc.reply(ircutils.mircColor("Current NBA Team Values", 'red'))
        
        for N in self._batch(object_list, 7):
            irc.reply(' '.join(str(str(n['rank']) + "." + " " + ircutils.bold(n['team'])) + " (" + n['value'] + "M)" for n in N))        
            
    nbavaluations = wrap(nbavaluations)


    def nbaarrests(self, irc, msg, args):
        """
        Display the last 5 NBA arrests.
        """    
    
        url = self._b64decode('aHR0cDovL2FycmVzdG5hdGlvbi5jb20vY2F0ZWdvcnkvcHJvLWJhc2tldGJhbGwv')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to open: %s" % url)
            return
            
        html = html.replace('&nbsp;',' ').replace('&#8217;','’')

        soup = BeautifulSoup(html)
        lastDate = soup.findAll('span', attrs={'class':'time'})[0] 
        divs = soup.findAll('div', attrs={'class':'entry'})

        append_list = []

        for div in divs:
            title = div.find('h2')
            datet = div.find('span', attrs={'class':'time'})
            datet = self._dateFmt(str(datet.getText()))
            arrestedFor = div.find('strong', text=re.compile('Team:'))    
            if arrestedFor:
                matches = re.search(r'<strong>Team:.*?</strong>(.*?)<br />', arrestedFor.findParent('p').renderContents(), re.I|re.S|re.M)
                if matches:
                    college = matches.group(1).replace('(MLB)','').strip()
                else:
                    college = "None"
            else:
                college = "None"
            
            append_list.append(ircutils.bold(datet) + " :: " + title.getText() + " - " + college) # finally add it all
        
        daysSince = self._daysSince(str(lastDate.getText()))
        irc.reply("{0} days since last NBA arrest".format(ircutils.mircColor(daysSince, 'red')))
        
        for each in append_list[0:6]:
            irc.reply(each)

    nbaarrests = wrap(nbaarrests)


    def nbadailyleaders(self, irc, msg, args):
        """
        Display daily NBA leaders in total performance.
        """
        
        url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9kYWlseWxlYWRlcnM=')

        try:
            request = urllib2.Request(url)
            html = (urllib2.urlopen(request)).read()
        except:
            irc.reply("Failed to open: %s" % url)
            return

        soup = BeautifulSoup(html)

        if not soup.find('div', attrs={'class':'mod-content'}):
            irc.reply("Something broke in formatting. Error looking up NBA Daily Leaders.")
            return

        h2 = soup.find('div', attrs={'class':'mod-content'}).find('h2')

        append_list = []

        tables = soup.findAll('table', attrs={'id':'topleaders'})
        for table in tables:
            rows = table.findAll('tr')[0] # only need the first of the rows since it has the name.
            for row in rows:
                player = row.find('strong')
                append_list.append(player.getText())
            
        # create object output. use split/join method for multiple spaces with h2. then join the append_list.
        output = "{0} :: {1}".format(ircutils.bold(" ".join(h2.getText().split())), string.join([item for item in append_list], " | "))
        irc.reply(output)
        
    nbadailyleaders = wrap(nbadailyleaders)


    def nbaawards(self, irc, msg, args, optdate):
        """<year>
        Display various NBA awards for current (or previous) year. Use YYYY for year. Ex: 2011
        """
        
        if optdate: 
            testdate = self._validate(optdate, '%Y')
            if not testdate:
                irc.reply("Invalid year. Must be YYYY.")
                return
        else:
            url = self._b64decode('aHR0cDovL3d3dy5iYXNrZXRiYWxsLXJlZmVyZW5jZS5jb20vYXdhcmRzLw==')
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            html = response.read()
            soup = BeautifulSoup(html)
            link = soup.find('h2', text="NBA Awards Voting").findNext('a')['href'].strip()
            optdate = ''.join(i for i in link if i.isdigit())

        url = self._b64decode('aHR0cDovL3d3dy5iYXNrZXRiYWxsLXJlZmVyZW5jZS5jb20vYXdhcmRzLw==') + 'awards_%s.html' % optdate

        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            html = response.read()
        except:
            irc.reply("Failure to load: %s" % url)
            return
        
        soup = BeautifulSoup(html)
        
        mvp = soup.find('h2', text="Most Valuable Player").findNext('a').text
        roy = soup.find('h2', text="Rookie of the Year").findNext('a').text
        dpoy = soup.find('h2', text="Defensive Player of the Year").findNext('a').text
        sixth = soup.find('h2', text="Sixth Man of the Year").findNext('a').text
        mip = soup.find('h2', text="Most Improved Player").findNext('a').text

        output = "{0} NBA Awards :: MVP: {1}  ROY: {2}  DPOY: {3}  SIXTH: {4}  MIP: {5}".format(optdate, \
                ircutils.bold(mvp), ircutils.bold(roy), ircutils.bold(dpoy), ircutils.bold(sixth), ircutils.bold(mip)) 

        irc.reply(output)
    
    nbaawards = wrap(nbaawards, [optional('somethingWithoutSpaces')])


    def nbaschedule(self, irc, msg, args, optteam):
        """[team]
        Display the last and next five upcoming games for team.
        """
        
        optteam = optteam.upper().strip()

        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return
            
        lookupteam = self._translateTeam('yahoo', 'team', optteam) # (db, column, optteam)
        
        url = self._b64decode('aHR0cDovL3Nwb3J0cy55YWhvby5jb20vbmJhL3RlYW1z') + '/%s/calendar/rss.xml' % lookupteam
        
        self.log.info(url)

        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
            html = response.read()
        except:
            irc.reply("Cannot open: %s" % url)
            return

        # clean this stuff up
        html = html.replace('<![CDATA[','') #remove cdata
        html = html.replace(']]>','') # end of cdata
        html = html.replace('EDT','') # tidy up times
        html = html.replace('\xc2\xa0',' ') # remove some stupid character.

        soup = BeautifulSoup(html)
        items = soup.find('channel').findAll('item')
        
        append_list = []

        for item in items:
            title = item.find('title').renderContents().strip() # title is good.
            day, date = title.split(',')
            desc = item.find('description') # everything in desc but its messy.
            desctext = desc.findAll(text=True) # get all text, first, but its in a list.
            descappend = (''.join(desctext).strip()) # list transform into a string.
            if not descappend.startswith('@'): # if something is @, it's before, but vs. otherwise.
                descappend = 'vs. ' + descappend
            descappend += " [" + date.strip() + "]"
            append_list.append(descappend) # put all into a list.

        self.log.info(str(append_list))

        descstring = string.join([item for item in append_list], " | ")
        output = "{0} {1}".format(ircutils.bold(optteam), descstring)
        irc.reply(output)

    nbaschedule = wrap(nbaschedule, [('somethingWithoutSpaces')])


    def nbapowerrankings(self, irc, msg, args):
        """
        Display this week's NBA Power Rankings.
        """
        
        url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9wb3dlcnJhbmtpbmdz')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
            html = html.replace("evenrow", "oddrow")
        except:
            irc.reply("Failed to fetch: %s" % url)
            return

        soup = BeautifulSoup(html)

        table = soup.find('table', attrs={'class': 'tablehead'})
        prdate = table.find('td', attrs={'colspan': '5'}).renderContents()
        t1 = table.findAll('tr', attrs={'class': 'oddrow'})

        if len(t1) < 30:
            irc.reply("Failed to parse NBA Power Rankings. Did something break?")
            return

        object_list = []

        for row in t1:
            rowrank = row.find('td', attrs={'class': 'pr-rank'}).renderContents()
            rowteam = row.find('div', attrs={'style': re.compile('^padding.*')}).find('a').text
            rowrecord = row.find('span', attrs={'class': 'pr-record'}).renderContents()
            rowlastweek = row.find('span', attrs={'class': 'pr-last'}).renderContents().replace("Last Week", "prev") 

            d = collections.OrderedDict()
            d['rank'] = int(rowrank)
            d['team'] = str(rowteam)
            d['record'] = str(rowrecord)
            d['lastweek'] = str(rowlastweek)
            object_list.append(d)

        if prdate:
            irc.reply(ircutils.mircColor(prdate, 'blue'))

        for N in self._batch(object_list, 6):
            irc.reply(' '.join(str(str(n['rank']) + "." + " " + ircutils.bold(n['team'])) + " (" + n['lastweek'] + ")" for n in N))
        
    nbapowerrankings = wrap(nbapowerrankings)


    def nbacareerleaders(self, irc, msg, args, optcategory):
        """[category]
        Display career leaders in a specific stat. Stats include:
        points, rebounds, assists, steals, blocks
        """

        optcategory = optcategory.lower().strip()

        statcategories = { 'points':'pts', 'games':'g', 'minutesplayed':'mp', 'fieldgoals':'fg',
                           'fieldgoalattempts':'fga', 'fieldgoalpct':'fg_pct', '3pts':'fg3', '3ptattempts':'fg3a',
                           '3ptpct':'fg3_pct', 'freethrows':'ft', 'freethrowattempts':'fta', 'freethrowpct':'ft_pct',
                           'offensiverebounds':'orb', 'defensiverebounds':'drb',
                           'totalrebounds':'trb', 'assists':'ast', 'steals':'stl',
                           'blocks':'blk', 'turnovers':'tov', 'personalfouls':'pf',
                           'points':'pts', 'minutespergame':'min_per_g', 'pointspergame':'pts_per_g',
                           'reboundspergame':'trb_per_g', 'assistspergame':'ast_per_g', 'stealspergame':'stl_per_g',
                           'blockspergame':'blk_per_g', 'playerefficiencyrating':'per', 'trueshootingpct':'ts_pct', 
                           'effectivefgpct':'efg_pct', 'offreboundpct':'orb_pct', 'defreboundpct':'def_pct', 
                           'totalreboundpct':'trb_pct', 'assistpct':'ast_pct', 'stealpct':'stl_pct', 'blockpct':'blk_pct',
                           'turnoverpct':'tov_pct', 'usagepct':'usg_pct', 'offrating':'off_rtg', 'defrating':'def_rtg',
                           'offwinshares':'ows', 'defwinshares':'dws', 'winshares':'ws', 'winsharesper48min':'ws_per_48',
                         }

        if optcategory not in statcategories:
            irc.reply("Stat must be one of: %s" % statcategories.keys())
            return
        
        url = self._b64decode('aHR0cDovL3d3dy5iYXNrZXRiYWxsLXJlZmVyZW5jZS5jb20vbGVhZGVycw==') + '/%s_career.html' % statcategories[optcategory]

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failure to fetch: %s" % url)
            return

        html = html.replace('</a>*','*</a>')

        soup = BeautifulSoup(html)
        h2 = soup.find('h2', text='NBA')
        table = h2.findNext('table', attrs={'data-crop':'50'})
        rows = table.findAll('tr')

        object_list = []

        for row in rows[1:11]:
            rank = row.find('td', attrs={'align':'right'})
            player = rank.findNext('td')
            stat = player.findNext('td')
            if player['class'] == "bold_text": # conditional if the player is active (in BOLD)
                player = ircutils.underline(player.find('a').renderContents().upper())
            else:
                player = player.find('a').renderContents()
            d = collections.OrderedDict()
            d['rank'] = rank.renderContents().strip()
            d['player'] = player
            d['stat'] = stat.renderContents().strip()
            object_list.append(d)

        output = "NBA Career Leaders for: " + optcategory + " (* indicates HOF; "
        output += ircutils.underline("UNDERLINE") + " indicates active.)"
        irc.reply(output)

        for N in self._batch(object_list, 5):
            irc.reply(' '.join(str(str(n['rank']) + " " + ircutils.bold(n['player'])) + " (" + n['stat'] + ") " for n in N))

    nbacareerleaders = wrap(nbacareerleaders, [('somethingWithoutSpaces')])


    def nbateampayrolls(self, irc, msg, args, optteam):
        """[team|top10]
        Display payroll total for team. Ex: NYK . Use top10 to show the Top 10 team salaries.
        """

        optteam = optteam.upper()
                
        usetop10 = False

        if optteam == "TOP10":
            usetop10 = True
        elif optteam != "TOP10" and optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return

        url = self._b64decode('aHR0cDovL2hvb3BzaHlwZS5jb20vc2FsYXJpZXMuaHRt')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Could not fetch: %s" % url)
        
        html = html.replace('<br />','')
        html = html.replace('&nbsp;', ' ')
        html = html.replace('#f2f5f7', '#FFFFFF')

        # soup time.
        soup = BeautifulSoup(html)
        table = soup.find('table', attrs={'width':'301'})
        rows = table.findAll('tr', attrs={'bgcolor':'#FFFFFF'})

        object_list = []

        for row in rows:
            team = row.find('td').find('a').find('font')
            salary = team.findNext('div', attrs={'align':'center'}).find('font')
            d = collections.OrderedDict()
            d['team'] = self._translateTeam('team', 'fulltrans', team.renderContents())
            d['salary'] = salary.renderContents().replace('$','').replace(',','')
            object_list.append(d)

        if usetop10:
            out_list = []

            for each in object_list[0:9]:
                out_list.append(ircutils.bold(each['team']) + " " + self._millify(float(each['salary'])))
            
            irc.reply("Top10 NBA Team Salaries: %s" % (string.join([item for item in out_list], " | ")))
        else:
            for each in object_list:
                if optteam == each['team']:
                    irc.reply("Team salary for %s is currently: %s" % (ircutils.bold(optteam), ircutils.bold(self._millify(float(each['salary'])))))

    nbateampayrolls = wrap(nbateampayrolls, [('somethingWithoutSpaces')])


    def nbadepthchart(self, irc, msg, args, optteam):
        """[team]
        Display depth chart for team.
        """
        optteam = optteam.upper().strip()

        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return
            
        url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS90ZWFtL2RlcHRoL18vbmFtZQ==') + '/%s/' % optteam

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Cannot load URL: %s" % url)
            return

        html = html.replace('evenrow', 'oddrow')
        html = html.replace('<b>','')
        html = html.replace('</b>','')

        soup = BeautifulSoup(html)
        table = soup.find('table', attrs={'class':'tablehead'})
        rows = table.findAll('tr', attrs={'class':re.compile(r'^oddrow')})
        header = soup.find('h1', attrs={'class':'h2'})

        object_list = []

        for row in rows:
            pos = row.find('td')
            player = row.findAll('a')
            d = collections.OrderedDict()
            d['pos'] = pos.renderContents()
            d['player'] = string.join([item.renderContents() for item in player], " | ")
            object_list.append(d)

        irc.reply("{0}".format(ircutils.bold(header.renderContents().strip())))

        for each in object_list:
            irc.reply("{0} - {1}".format(ircutils.bold(each['pos']), each['player']))

    nbadepthchart = wrap(nbadepthchart, [('somethingWithoutSpaces')])


    def nbaroster(self, irc, msg, args, optteam):
        """[team]
        Display the current roster for team.
        """

        optteam = optteam.upper()

        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return
        
        url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS90ZWFtL3Jvc3Rlci9fL25hbWU=') + '/%s/' % optteam

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Failed to fetch: %s" % url)
            return

        html = html.replace('<br />','')
        html = html.replace('&nbsp;', ' ')
        html = html.replace('evenrow', 'oddrow')

        soup = BeautifulSoup(html)
        header = soup.find('h1', attrs={'class':'h2'})
        table = soup.find('table', attrs={'class':'tablehead'})
        rows = table.findAll('tr', attrs={'class':re.compile(r'^oddrow')})
        coach = soup.find('tr', attrs={'class':'total'}).find('td').find('strong', text="Coach:").findNext('a')

        object_list = []

        for row in rows:
            number = row.find('td')
            player = number.findNext('td', attrs={'class':'sortcell'}).find('a')
            pos = player.findNext('td')
            d = collections.OrderedDict()
            d['number'] = number.renderContents()
            d['player'] = player.renderContents()
            d['pos'] = pos.renderContents()
            object_list.append(d)

        if header and coach:
            output = "{0} - Coach: {1}".format(ircutils.underline(header.renderContents().strip()), ircutils.bold(coach.string.strip().replace("  "," ")))
            irc.reply(output)

        the_roster = string.join(["#" + str(item['number']) + " " + ircutils.bold(item['player']) + " (" + item['pos'] + ") " for item in object_list], " | ")
        irc.reply(the_roster)

    nbaroster = wrap(nbaroster, [('somethingWithoutSpaces')])


    def nbastandings(self, irc, msg, args, optlist, optdiv):
        """<--expanded|--vsdivision> [atlantic|central|southeast|northwest|pacific|southwest]
        Display divisional standings for a division. Use --expanded or --vsdivision
        to show extended stats.
        """

        expanded, vsdivision = False, False
        for (option, arg) in optlist:
            if option == 'expanded':
                expanded = True
            if option == 'vsdivision':
                vsdivision = True

        optdiv = optdiv.lower() # lower to match keys. values are in the table to match with the html.
        
        leaguetable =   { 
                            'atlantic': 'Eastern Conference ATLANTIC',
                            'central': 'Eastern Conference CENTRAL',
                            'southeast': 'Eastern Conference SOUTHEAST',
                            'northwest': 'Western Conference NORTHWEST',
                            'pacific': 'Western Conference PACIFIC',
                            'southwest': 'Western Conference SOUTHWEST' 
                        }

        if optdiv not in leaguetable:
            irc.reply("Division must be one of: %s" % leaguetable.keys())
            return

        if expanded:
            url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9zdGFuZGluZ3MvXy90eXBlL2V4cGFuZGVk')
        elif vsdivision:
            url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9zdGFuZGluZ3MvXy90eXBlL3ZzLWRpdmlzaW9u')
        else:
            url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9zdGFuZGluZ3M=')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Problem opening up: %s" % url)
            return
        
        soup = BeautifulSoup(html) # one of these below will break if formatting changes. 
        div = soup.find('div', attrs={'class':'mod-container mod-table mod-no-header'}) # div has all
        table = div.find('table', attrs={'class':'tablehead'}) # table in there
        rows = table.findAll('tr', attrs={'class':re.compile('^oddrow.*?|^evenrow.*?')}) # rows are each team

        object_list = [] # list for ordereddict with each entry.
        lengthlist = collections.defaultdict(list) # sep data structure to determine length. 

        for row in rows: # this way, we don't need 100 lines to match with each column. works with multi length. 
            league = row.findPrevious('tr', attrs={'class':'stathead'}) 
            header = row.findPrevious('tr', attrs={'class':'colhead'}).findAll('td')
            tds = row.findAll('td')
    
            d = collections.OrderedDict()
            division = str(league.getText() + " " + header[0].getText())
    
            if division == leaguetable[optdiv]: # from table above. only match what we need.
                for i,td in enumerate(tds):
                    if i == 0: # manual replace of team here because the column doesn't say team.
                        d['TEAM'] = str(tds[0].getText())
                        lengthlist['TEAM'].append(len(str(tds[0].getText()).replace('  ',' ').replace('&mdash;','-').replace('&nbsp;&#189;','.5'))) # replace the html entities here for display and below.
                    else:
                        d[str(header[i].getText())] = str(td.getText()).replace('  ',' ').replace('&mdash;','-').replace('&nbsp;&#189;','.5') # add to ordereddict + conv multispace to one.
                        lengthlist[str(header[i].getText())].append(len(str(td.getText()).replace('  ',' ').replace('&mdash;','-').replace('&nbsp;&#189;','.5'))) # add key based on header, length of string.
                object_list.append(d)

        if len(object_list) > 0: # now that object_list should have entries, sanity check.
            object_list.insert(0,object_list[0]) # cheap way to copy first item again because we iterate over it for header.
        else: # bailout if something broke.
            irc.reply("Something broke returning mlbstandings.")
            return
            
        for i,each in enumerate(object_list):
            if i == 0: # to print the duplicate but only output the header of the table.
                headerOut = ""
                for keys in each.keys(): # only keys on the first list entry, a dummy/clone.
                    headerOut += "{0:{1}}".format(ircutils.underline(keys),max(lengthlist[keys])+4, key=int) # normal +2 but bold eats up +2 more, so +4.
                irc.reply(headerOut)
            else: # print the division now.
                tableRow = ""
                for inum,k in enumerate(each.keys()):
                    if inum == 0: # team here, which we want to bold.
                        tableRow += "{0:{1}}".format(ircutils.bold(each[k]),max(lengthlist[k])+4, key=int) #+4 since bold eats +2.
                    else: # rest of the elements outside the team.
                        tableRow += "{0:{1}}".format(each[k],max(lengthlist[k])+2, key=int)
                irc.reply(tableRow) 


    nbastandings = wrap(nbastandings, [getopts({'expanded':'', 'vsdivision':''}), ('somethingWithoutSpaces')])


    def nbacoach(self, irc, msg, args, optteam):
        """[team]
        Display the manager for team. Ex: BOS
        """
        
        optteam = optteam.upper().strip()

        if optteam not in self._validteams():
            irc.reply("Team not found. Must be one of: %s" % self._validteams())
            return

        url = self._b64decode('aHR0cDovL2VzcG4uZ28uY29tL25iYS9jb2FjaGVz')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Cannot fetch URL: %s" % url)
            return

        html = html.replace('class="evenrow', 'class="oddrow')

        soup = BeautifulSoup(html)
        rows = soup.findAll('tr', attrs={'class':'oddrow'})

        object_list = []

        for row in rows:
            manager = row.find('td').find('a')
            exp = manager.findNext('td')
            record = exp.findNext('td')
            team = record.findNext('td').find('a')

            d = collections.OrderedDict()
            d['manager'] = manager.renderContents().strip().replace("  "," ") # some of these coach strings are double spaced, for whatever reason.
            d['exp'] = exp.renderContents().strip()
            d['record'] = record.renderContents().strip()
            d['team'] = self._translateTeam('team', 'fulltrans', team.renderContents().strip())
            object_list.append(d)

        for each in object_list:
            if each['team'] == optteam:
                output = "The coach of {0} is {1}({2}) with {3} years experience.".format( \
                    ircutils.bold(each['team']), ircutils.bold(each['manager']), each['record'], each['exp'])
                irc.reply(output)

    nbacoach = wrap(nbacoach, [('somethingWithoutSpaces')])

    # !seasonstats rondo
    #  14.8 PT   .485 of 11.9 FG   .615 of 5.0 FT   .250 of 0.7 3P   4.9/1.3 RB   9.55 AS   0.00 BL   1.64 ST   3.73 TO   2.09 PF   36.9 MN   22/22 GS

    def nbastats(self, irc, msg, args, optlist, optplayer):
        """[Player Name]
        Fetches NBA stats for Player Name. Ex: LeBron James
        """

        lastgamenum = '1' # bare minimum one to show one stat.

        if optlist:
            for (key, value) in optlist:
                if key == 'last':
                    lastgamenum = value

        # don't tally more than five. 
        if lastgamenum > 5:
            irc.reply("Maxmimum last games to total is 5. Please specify 5 or less.")
            return

        (returncode, url) = self._yahooFind(optplayer) # will return number found, url or string of players.

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Error fetching: %s" % url)
            return

        # mingle html before parse.
        html = html.replace('ysprow1','ysprow2')
        html = html.replace('&nbsp;', '')

        soup = BeautifulSoup(html)
        playername = soup.find('li', attrs={'class':'player-name', 'itemprop':'name'}).renderContents() # grab playername quickly.
        rows = soup.findAll('tr', attrs={'class':'ysprow2'})

        object_list = []

        for row in rows[0:int(lastgamenum)]:
            date = row.find('td')
            opp = date.findNext('td')
            score = opp.findNext('td').find('a')
            gs = score.findNext('td')
            minutes = gs.findNext('td')
            fg = minutes.findNext('td').findNext('td')
            fga = fg.findNext('td')
            fgp = fga.findNext('td')
            threept = fgp.findNext('td').findNext('td')
            threepta = threept.findNext('td')
            threeptpct = threepta.findNext('td')
            ft = threeptpct.findNext('td').findNext('td')
            fta = ft.findNext('td')
            ftp = fta.findNext('td')
            orb = ftp.findNext('td').findNext('td')
            drb = orb.findNext('td')
            trb = drb.findNext('td')
            asst = trb.findNext('td').findNext('td')
            to = asst.findNext('td')
            stl = to.findNext('td')
            blk = stl.findNext('td')
            pf = blk.findNext('td')
            pts = pf.findNext('td')
            
            # now put into an od.
            d = collections.OrderedDict()
            d['date'] = date.renderContents().strip() # Jun 9
            d['opp'] = opp.renderContents().strip() # @ MIA
            d['score'] = score.renderContents() # L 88-101
            d['gs'] = gs.renderContents().strip() # 1 (games started)
            d['minutes'] = minutes.renderContents().strip() # 42:25
            d['fg'] = fg.renderContents().strip() # everything down is an int
            d['fga'] = fga.renderContents().strip()
            d['fgp'] = fgp.renderContents().strip()
            d['threept'] = threept.renderContents().strip()
            d['threepta'] = threepta.renderContents().strip()
            d['threeptpct'] = threeptpct.renderContents().strip()
            d['ft'] = ft.renderContents().strip()
            d['fta'] = fta.renderContents().strip()
            d['ftp'] = ftp.renderContents().strip()
            d['orb'] = orb.renderContents().strip()
            d['drb'] = drb.renderContents().strip()
            d['trb'] = trb.renderContents().strip()
            d['asst'] = asst.renderContents().strip()
            d['to'] = to.renderContents().strip()
            d['stl'] = stl.renderContents().strip()
            d['blk'] = blk.renderContents().strip()
            d['pf'] = pf.renderContents().strip()
            d['pts'] = pts.renderContents().strip()
            object_list.append(d)

        if int(lastgamenum) > 1: # if we're showing more than one game, we need to count and average.
            count = '0'
            avgpts = AvgDict() # avgdict subclass.

            for xx in object_list: # we limit the amount in object_list via the for loop above.
                a[count] = int(xx['pts'])
                output = "{0} {1} {2} {3}".format(playername, xx['minutes'], xx['fg'], xx['pts'])
                count += "1"
                irc.reply(output)
        
            averagemins = a.average()
            irc.reply(averagemins)

    nbastats = wrap(nbastats, [getopts({'last':('int')}), ('text')])

    def nbainfo(self, irc, msg, args, optplayer):
        """<player>
        Fetch NBA player information and stats
        """

        (returncode, url) = self._yahooFind(optplayer) # will return number found, url or string of players.
        
        self.log.info(url)

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Error fetching: %s" % url)
            return

        # soup to parse out details.
        soup = BeautifulSoup(html)

        playerdiv = soup.find('div', attrs={'class':'player-info'})
        playerteam = soup.find('li', attrs={'class':'team-name'}).find('span', attrs={'itemprop':'affiliation'}).renderContents().strip()
        playername = playerdiv.find('li', attrs={'class':'player-name'}).renderContents().strip()
        playeruninum = playerdiv.find('li', attrs={'itemprop':'uniformNumber'}).renderContents().strip()
        playerpos = playerdiv.find('li', attrs={'itemprop': 'jobTitle'}).renderContents().strip()
        playerdob = playerdiv.find('li', attrs={'class':'born'}).find('time').renderContents().strip()
        playerheight = playerdiv.find('li', attrs={'class':'height'})
        playerweight = playerdiv.find('li', attrs={'class':'weight'})
        playercollege = playerdiv.find('li', attrs={'class':'college'}).find('span', attrs={'itemprop':'alumniOf'}).renderContents() # <span itemprop="alumniOf">
        playerdraft = playerdiv.find('li', attrs={'class':'draft'})
        playerinjury = playerdiv.find('p', attrs={'class':'injury'})

        # cheap method to strip strong from strings
        if playerheight:
            playerheight = self._remove_strong(playerheight.renderContents())
        if playerweight:
            playerweight = self._remove_strong(playerweight.renderContents())
        if playerdraft:
            playerdraft = self._remove_strong(playerdraft.renderContents())

        if playerdob:
            playerage = self._getAge(playerdob)

        output = "{0} {1} {2} {3} {4} {5} {6} {7} DOB: {8} ({9})".format( \
                playername, playerteam, playeruninum, playerpos, playerheight, playerweight, playercollege, playerdraft, playerdob, playerage) 
        irc.reply(output)

    nbainfo = wrap(nbainfo, [('text')])
    
    def _playerIDlocate(self, field, optplayer):

        db_filename = self.registryValue('dbLocation')

        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            sql = "select %s from players where name='%s'" % (field, optplayer.lower())
            self.log.info(sql)
            cursor.execute(sql)
            id = str(cursor.fetchone()[0])
            cursor.close()
                
            if id and id.isdigit(): # we did find one and not null.
                self.log.info("We did find an ID in nba.sql: %s" % id)
                return id
            else:
                self.log.info("We did not find an id.")
                return "Not found"
            
    def _playerIDinject(self, field, optid, optplayer):
        
        db_filename = self.registryValue('dbLocation')
        
        # check to see if we already have name in database. If we do, change the SQL.
        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            sql = "select name from players where name = ?"
            cursor.execute(sql, (optplayer.lower(),))
            id = cursor.fetchone()
            
            if id: # if we already have the name, only insert the field and value.
                self.log.info("We already have a name in players: %s" % optplayer)
                insertsql = "update players set %s='%s' where name='%s'" % (field, optid, optplayer)
            else: # otherwise, insert the player + field.
                self.log.info("We don't have name in players: %s" % optplayer)
                insertsql = "insert into players ('name','%s') values ('%s', '%s')" % (field, optplayer, optid)

        with sqlite3.connect(db_filename) as conn:
            cursor = conn.cursor()
            self.log.info(insertsql)
            cursor.execute(insertsql)
            conn.commit()
            cursor.close()
            
            #sql = "insert into %s (id, player) values (:optid, :optplayer)" % db
            #cursor.execute(sql, {'optid':optid, 'optplayer':optplayer.lower()})

    # start yahoofind.
    def _yahooFind(self, optplayer):
        """Use Yahoo to find a NBA player. Maintain the player id relationship within a sqlite3 db."""
        
        optplayer = optplayer.lower().strip() # lower to search. we keep names lower in db.
        
        idlookup = self._playerIDlocate('yid', optplayer) # check if we already have the player in the db.

        if idlookup != "Not found": # if we do have the player, it will return just the id.
            return ('1','http://sports.yahoo.com/nba/players/%s/' % idlookup) # with the id, return 1 for a single player and the url.

        # If we did not find the player, search via yahoo and mechanize.
        url = 'http://sports.yahoo.com/nba/players'
        br = mechanize.Browser()
        br.set_handle_robots(False) # ignore robots
        br.open(url)
        br.select_form(name="player-search")
        br["query"] = optplayer
        res = br.submit()
        content = res.read()

        if "No players found" in content:
            return (0, ("No player found for %s" % optplayer))

        soup = BeautifulSoup(content)
        foundp = soup.findAll('tr', attrs={'class':re.compile('ysprow.*')})

        if len(foundp) > 1: # if more than one, return the number and matches.
            object_list = []
            for foundrow in foundp:
                player = foundrow.findAll('td')[0].find('a').text.strip()
                pos = foundrow.findAll('td')[1].text.strip()
                team = foundrow.findAll('td')[2].find('a').text.strip()
                object_list.append(player + " " + pos + " " + team)
            playersfound = string.join([item for item in object_list], " | ") # put all found players into a single string
            return (str(len(foundp)), playersfound) # this will return the number + matching players in a string

        if len(foundp) == 1:
            pn = foundp[0].find('td').find('a').string.strip() # get their full name.
            link = foundp[0].find('td').find('a')['href'].strip() # /nba/players/4149
            pid = ''.join(i for i in link if i.isdigit()) # just get the digits of above.
            self._playerIDinject('yid', pid, pn.lower()) # inject into db.
            return (str(len(foundp)), ('http://sports.yahoo.com' + link)) # return 1 + link as if we found it in the database, after adding. 
    
    # find via rotoworld.    
    def _rotoFind(self, optplayer):

        optplayer = optplayer.lower().strip() # lower to search. we keep names lower in db.
        idlookup = self._playerIDlocate('rid', optplayer) # check if we already have the player in the db.

        if idlookup != "Not found": # if we do have the player, it will return just the id.
            return ('1','http://rotoworld.com/player/nba/%s/' % idlookup) # with the id, return 1 for a single player and the url.

        # if we didn't find, now search.
        (first, last) = optplayer.split(" ", 1) #playername needs to be "Last, First"
        name = last + ', ' + first

        url = 'http://rotoworld.com/content/playersearch.aspx?searchname=%s' % urllib.quote(name)
        self.log.info(url)
        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()

        soup = BeautifulSoup(the_page)
        pn = soup.find('div', attrs={'class':'playercard',  'style':'display:none;', 'id': re.compile('^cont_.*')}) # check to see if we found someone
        
        if not pn:
            return (0, ("No player found for %s" % optplayer))
        else:
            link = response.geturl()
            pid = ''.join(i for i in link if i.isdigit()) # just get the digits of above.
            self._playerIDinject('rid', pid, optplayer.lower()) # inject into db.
            return (1, (link)) # we did find a player, so redirect

    def nbacontract(self, irc, msg, args, optplayer):
        """[player]
        Display NBA contract for Player Name. Ex: Ray Allen
        """

        self.log.info("Trying to find: %s" % optplayer)
        (returncode, url) = self._rotoFind(optplayer) # will return number found, url or string of players.

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read() 
        except:
            irc.reply("Failed to open: %s" % url)
            return

        soup = BeautifulSoup(html)
        pn = soup.find('div', attrs={'class':'playercard',  'style':'display:none;', 'id': re.compile('^cont_.*')})

        # check if there. exit if not.
        if not pn:
            irc.reply("No contract found for: %s" % player)
            return

        # if we did find, go deeper.
        p1 = pn.find('div', attrs={'class': 'report'}).renderContents().strip()
        h1 = soup.find('h1').renderContents().strip()
        contract = re.sub('<[^<]+?>', '', p1).strip()

        irc.reply(ircutils.mircColor(h1, 'red') + ": " + contract)

    nbacontract = wrap(nbacontract, [('text')])

    def nbaplayernews(self, irc, msg, args, player):
        """[player]
        Display NBA player news for player. Ex: Ray Allen
        """

        #playername needs to be "Allen, Ray"
        (first, last) = player.split(" ", 1)
        name = last + ', ' + first

        url = 'http://rotoworld.com/content/playersearch.aspx?searchname=%s' % urllib.quote(name)

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read() 
        except:
            irc.reply("Something broke trying to read: %s" % url)
            return

        soup = BeautifulSoup(html)
        pn = soup.findAll('div', attrs={'class': 'playernews'})

        if not pn:
            irc.reply("News for player: %s not found." % player)
            return

        for entry in pn[0:2]:
            report = entry.find('div', attrs={'class': 'report'}).renderContents().strip()
            #impact = entry.find('div', attrs={'class': 'impact'})
            date = entry.find('span', attrs={'class': 'date'}).renderContents().strip()
            source = entry.find('div', attrs={'class': 'source'}).renderContents().strip()
            source = re.sub('<[^<]+?>', '', source).strip() # remove html tags

            irc.reply(ircutils.mircColor(player, 'orange') + " (" + date + ") " + report + " " + ircutils.mircColor(source, 'blue'))

    nbaplayernews = wrap(nbaplayernews, [('text')])

    def nbarumors(self, irc, msg, args):
        """
        Display the latest NBA rumors.
        """
        
        url = self._b64decode('aHR0cDovL20uZXNwbi5nby5jb20vbmJhL3J1bW9ycz93amI9')

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read() 
        except:
            irc.reply("Something broke trying to read: %s" % url)
            return
        
        html = html.replace('<div class="ind alt">', '<div class="ind">')

        soup = BeautifulSoup(html)
        t1 = soup.findAll('div', attrs={'class': 'ind'})

        if len(t1) < 1:
            irc.reply("No NBA rumors found. Check formatting?")
            return

        for t1rumor in t1[0:7]:
            item = t1rumor.find('div', attrs={'class': 'noborder bold tL'}).renderContents()
            item = re.sub('<[^<]+?>', '', item)
            rumor = t1rumor.find('div', attrs={'class': 'inline rumorContent'}).renderContents().replace('\r','')
            irc.reply(ircutils.bold(item) + " :: " + rumor)

    nbarumors = wrap(nbarumors)

    def nbatrans(self, irc, msg, args, optdate):
        """[YYYYmmDD]
        Display all NBA transactions. Will only display today's. Use date in format: 20120912
        """

        url = self._b64decode('aHR0cDovL20uZXNwbi5nby5jb20vbmJhL3RyYW5zYWN0aW9ucz93amI9')

        if optdate: 
            testdate = self._validate(optdate, '%Y%m%d')
            if not testdate:
                irc.reply("Invalid year. Must be YYYYmmdd.")
                return
        else:
            optdate = datetime.datetime.now().strftime("%Y%m%d")
            
        url += '&date=%s' % optdate

        try:
            req = urllib2.Request(url)
            html = (urllib2.urlopen(req)).read()
        except:
            irc.reply("Something broke trying to read: %s" % url)
            return

        html = html.replace('class="ind alt', 'class="ind')

        soup = BeautifulSoup(html)
        t1 = soup.findAll('div', attrs={'class': 'ind'})

        out_array = []

        for trans in t1:
            if "<a href=" not in trans: # no links
                match1 = re.search(r'<b>(.*?)</b><br />(.*?)</div>', str(trans), re.I|re.S) #strip out team and transaction
                if match1:
                    team = match1.group(1) 
                    transaction = match1.group(2)
                    output = ircutils.mircColor(team, 'red') + " - " + ircutils.bold(transaction)
                    out_array.append(output)

        if len(out_array) > 0:
            for output in out_array:
                irc.reply(output)
        else:
            irc.reply("No transactions on %s" % optdate)
            return
    
    nbatrans = wrap(nbatrans, [optional('somethingWithoutSpaces')])

Class = NBA


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
