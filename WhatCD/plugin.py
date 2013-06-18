import re
import urllib, urllib2, httplib, cookielib
import HTMLParser
import htmlentitydefs
import sys, os
import simplejson as json


import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks


class Title(HTMLParser.HTMLParser):
    entitydefs = htmlentitydefs.entitydefs.copy()
    entitydefs['nbsp'] = ' '
    entitydefs['apos'] = '\''
    def __init__(self):
        self.inTitle = False
        self.title = ''
        HTMLParser.HTMLParser.__init__(self)

    def handle_starttag(self, tag, attrs):
        if tag == 'title':
            self.inTitle = True

    def handle_endtag(self, tag):
        if tag == 'title':
            self.inTitle = False

    def handle_data(self, data):
        if self.inTitle:
            self.title += data

    def handle_entityref(self, name):
        if self.inTitle:
            if name in self.entitydefs:
                self.title += self.entitydefs[name]

class WhatCD(callbacks.PluginRegexp):
    """Add the help for "@help WhatCD" here."""
    threaded = True
    regexps = ['titleSnarfer']
    username = ''
    password = ''
    searchKeys = ['artist', 'song', 'album']
    _whois = {}

    def __init__(self, irc):
        self.__parent = super(WhatCD, self)
        self.__parent.__init__(irc)
        self.username = self.registryValue('username')
        self.password = self.registryValue('password')
        self.maxResults = int(self.registryValue('max_results'))

    def do311(self, irc, msg):
        nick = ircutils.toLower(msg.args[1])
        if (irc, nick) not in self._whois:
            return
        else:
            self._whois[(irc, nick)][-1][msg.command] = msg


    def do318(self, irc, msg):
        nick = msg.args[1]
        loweredNick = ircutils.toLower(nick)
        if (irc, loweredNick) not in self._whois:
            replyIrc.reply("%s doesn't seem to be online" % nick)
            del self._whois[(irc, loweredNick)]
            return

        (replyIrc, replyMsg, d) = self._whois[(irc, loweredNick)]

        userId = d['311'].args[2]
        if not re.match('^\d+$', userId):
            replyIrc.reply("%s isn't identified with DRONE" % nick)
            del self._whois[(irc, loweredNick)]
            return

        hostmask = '@'.join(d['311'].args[2:4])
        user = d['311'].args[-1]
        replyIrc.reply("https://what.cd/user.php?id=%s" % userId)
        del self._whois[(irc, loweredNick)]


    def callCommand(self, command, irc, msg, *args, **kwargs):
        try:
            super(WhatCD, self).callCommand(command, irc, msg, *args, **kwargs)
        except utils.web.Error, e:
            irc.reply(str(e))

    def outFilter(self, irc, msg):
        if msg.command == 'PRIVMSG':
            nick = msg.args[0]
            msgstr = msg.args[1]
            self.log.debug("outFilter nick: %s msg: %s" %(nick, msgstr))

            pattern = "You're now playing: (.*) - (.*)\."
            matches = re.search("%s"%pattern, "%s"%msg)

            if matches:
                artist = "%s" % matches.group(1)
                song = "%s" % matches.group(2)

                jstr = self.whatSearch(dict({'filelist': song, 'artistname': artist}))
                jobj = json.loads(jstr)
                results = jobj['response']['results']
                if len(results) > 0:
                    html = HTMLParser.HTMLParser()
                    rg = results[0]
                    url = "https://what.cd/torrents.php?id=%s" % rg['groupId']
                    msgstr = "You're now playing %s by %s on %s (%d) | %s" % (song, artist, html.unescape(rg['groupName']), rg['groupYear'], url)

                msg = ircmsgs.privmsg(msg.args[0], msgstr, msg=msg)
        return msg

    def parseChunk(self, chunk):
        if len(str(chunk)):
            chunk = chunk.strip()
            splits = re.split('\s', chunk)
            self.log.debug("splits: %s" % splits)
            searchKey = splits.pop(0)
            if not re.match('^(%s)$' % '|'.join(self.searchKeys), searchKey):
                self.log.error('%s is not a valid key' % searchKey)
                return None

            self.log.debug("translating key %s" % searchKey)
            if searchKey == 'artist':
                keyOut = 'artistname'
            elif searchKey == 'song':
                keyOut = 'filelist'
            elif searchKey == 'album':
                keyOut = 'groupname'
            else:
                return None
            
            return dict({'key': keyOut, 'val': ' '.join(splits)})


    def search(self, irc, msg, args, text):
        searchKeys = dict()
        if re.search('\|', text):
            for chunk in re.split('\|', text):
                parsed = self.parseChunk(chunk)
                if parsed == None:
                    continue
                searchKeys[parsed['key']] = parsed['val']
        elif re.match('^(%s)\s' % '|'.join(self.searchKeys), text):
            parsed = self.parseChunk(text)
            searchKeys[parsed['key']] = parsed['val']
        else:
            searchKeys['searchstr'] = text

        jstr = self.whatSearch(searchKeys)
        if len(jstr)== 0:
            return False
        jobj = json.loads(jstr)
        results = jobj['response']['results']
        maxResults = self.maxResults
        totalResults = len(results)
        self.log.warning("total/max %s/%s" %(totalResults, maxResults))
        if totalResults < maxResults:
            maxResults = totalResults
        self.log.warning("total/max %s/%s" %(totalResults, maxResults))
        current = 0
        irc.reply('Showing %d of %d Search Results:' % (maxResults, totalResults))
        for rg in results:
            html = HTMLParser.HTMLParser()
            url = "https://what.cd/torrents.php?id=%s" % rg['groupId']
            irc.reply('%s - %s (%d) | %s' % (html.unescape(rg['artist']), html.unescape(rg['groupName']), rg['groupYear'], url))
            current += 1
            if current >= maxResults:
                break
    whatsearch = wrap(search, [optional('text')])

    def whatSearch(self, searchDict):
        html = HTMLParser.HTMLParser()
        searchStrings = list()
        for (key, val) in searchDict.items():
            searchStrings.append('%s=%s' % (key, urllib.quote(val)))
        return self.whatGet('https://what.cd/ajax.php?action=browse&%s' % '&'.join(searchStrings))

    def whatGet(self, url):
        self.log.debug("URL: %s"%url)
        if len(self.username) < 1 or len(self.password) < 1:
            self.log.error("you need to set a username and password before what snarfing will work")
            self.log.debug("Username: %s Password: %s" %(self.username, self.password))
            return ''

        try:
            cj = cookielib.LWPCookieJar(conf.supybot.directories.data.dirize('what.cookies'))
            try:
                cj.load(ignore_discard=True, ignore_expires=True)
            except IOError, e:
                print e
                
            cookieprocessor = urllib2.HTTPCookieProcessor(cj)
            opener = urllib2.build_opener(cookieprocessor)
            urllib2.install_opener(opener)
                
            response =urllib2.urlopen(url)
                
            if re.search('/login.php$', response.url):
                httpdict = {'username' : self.username, 'password' : self.password, 'keeplogged' : '1' }
                http_args = urllib.urlencode(httpdict)
                req = urllib2.Request(response.url, http_args)
                response = urllib2.urlopen(req)
                cj.save(ignore_discard=True, ignore_expires=True)
            return response.read()                    
        except IOError:
            return ''

    def titleSnarfer(self, irc, msg, match):
        r"https?://(ssl\.)?what\.cd[^\])>\s]+"
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        if callbacks.addressed(irc.nick, msg):
            return

        url = match.group(0)
        text = self.whatGet(url)

        parser = Title()
        try:
            parser.feed(text)
        except HTMLParser.HTMLParseError:
            self.log.debug('Encountered a problem parsing %u.  Title may '
                           'already be set, though', url)
        if parser.title:
            domain = utils.web.getDomain(url)
            title = utils.web.htmlToText(parser.title.strip())
            s = format('Title: %s (at %s)', title, domain)
            irc.reply(s, prefixNick=False)
    titleSnarfer = urlSnarfer(titleSnarfer)

    def whatNick(self, irc, msg, args, otherIrc, nick):
        """[<network>] <nick>
        """
        # The double nick here is necessary because single-nick WHOIS only works
        # if the nick is on the same server (*not* the same network) as the user
        # giving the command.  Yeah, it made me say wtf too.
        nick = ircutils.toLower(nick)
        otherIrc.queueMsg(ircmsgs.whois(nick, nick))
        self._whois[(otherIrc, nick)] = (irc, msg, {})
    whatnick = wrap(whatNick, ['networkIrc', 'nick'])


Class = WhatCD

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
