###
# Copyright (c) 2012, .
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import re
import urllib
import urllib2
import json
import feedparser

#libraries for time_created_at
import time
from datetime import tzinfo, datetime, timedelta

class TopNews(callbacks.Plugin):
    """Add the help for "@plugin help TopNews" here
    This should describe *how* to use this plugin."""
    threaded = True

    def _time_created_at(self, s):
        """
        returns relative time string from now.	
        """

        plural = lambda n: n > 1 and "s" or ""

        try:
            ddate = time.strptime(s, "%a, %d %b %Y %H:%M:%S GMT")[:-2]
        except ValueError:
            return "", ""

        created_at = datetime(*ddate, tzinfo=None)
        d = datetime.utcnow() - created_at

        if d.days:
            rel_time = "%s days ago" % d.days
        elif d.seconds > 3600:
            hours = d.seconds / 3600
            rel_time = "%s hour%s ago" % (hours, plural(hours))
        elif 60 <= d.seconds < 3600:
            minutes = d.seconds / 60
            rel_time = "%s minute%s ago" % (minutes, plural(minutes))
        elif 30 < d.seconds < 60:
            rel_time = "less than a minute ago"
        else:
            rel_time = "less than %s second%s ago" % (d.seconds, plural(d.seconds))
        return rel_time

    # smart_truncate from http://stackoverflow.com/questions/250357/smart-truncate-in-python
    def _smart_truncate(self, text, length, suffix='...'):
        """Truncates `text`, on a word boundary, as close to
        the target length it can come.
        """

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

        # if google news is up, safe to assume this is also up?
        data = json.dumps(data)
        request = urllib2.Request(posturi,data,headers)
        response = urllib2.urlopen(request)
        response_data = response.read()
        shorturi = json.loads(response_data)['id']
        return shorturi

    def topnews(self, irc, msg, args, options, topic):
        """[--num number] <topic>
        Returns the latest Google News entries (max 5). 
        Shows stories from Top News if <topic> is not specified.
        """
        # arguments are kinda described on here:
        # https://developers.google.com/news-search/v1/jsondevguide

        url = 'http://news.google.com/news?ned=us'

        num,geo = False,False
        # process options
        if options:
            for (type, arg) in options:
                if type == 'num':
                    num = arg
                if type == 'geo':
                    geo = arg
        
        # number of entries. 1-7 is valid. 5 otherwise.
        if num and (0 < num <= 7):
            url += '&num=%s' % num
        else:
            defaultNumberEntries = self.registryValue('defaultNumberEntries', msg.args[0])
            url += '&num=%s' % defaultNumberEntries

        # You cannot use topic in conjunction with either the query or the geo argument. If you specify either of these with topic, the searcher ignores it.
        if geo:
            url += '&geo=%s' % urllib.quote(geo)
        else:
            if topic:
                url += '&q=' + urllib.quote(topic)
            else:
                url += '&topic=n'

        url += '&output=rss'

        # ned=location
        # hl=lang # http://bit.ly/Ko0WFP

        try:
            self.log.info(url)
            feeds = feedparser.parse(url)
        except:
            irc.reply("Failed to parse google news feed.")
        
        if len(feeds.entries) == 0:
            self.log.warning("Failed to find any Google News entries")
            irc.reply("Failed to find any Google News entries.")
        else:

            # https://github.com/ProgVal/Supybot-plugins/blob/master/Debian/plugin.py
            # sort by newest since Google News RSS does not give you the newest in order.
            # function from: ctb@github http://bit.ly/K5E0Ni
            newsOrderByDate = self.registryValue('newsOrderByDate', msg.args[0])
            if newsOrderByDate:
                date_format = "%a, %d %b %Y %H:%M:%S GMT"
                extract_date = lambda entry: datetime.strptime(entry.published, date_format)
                entries = sorted(feeds.entries, key=extract_date, reverse=True)
            else:
                entries = feeds.entries

            headlineCharacters = self.registryValue('headlineCharacters', msg.args[0])
            displaySource = self.registryValue('displaySource', msg.args[0])

            for data in entries:
                # format published date with relative time and color
                published = data.published
                published = self._time_created_at(published)
                published = ircutils.mircColor(published, 'light gray')

                # Article Title Formatting
                #title = data["title"].encode('utf-8')
                title = data["title"]
                if not displaySource:
                    title = re.sub(r'\s-\s.*?$','',title)
                    title = self._smart_truncate(title,headlineCharacters)
                else:
                    # split the title by the -. truncate and color
                    titlesplit = re.search(r'^(.*?)\s-\s(.*?)$', title)
                    title = titlesplit.group(1)
                    title = self._smart_truncate(title,headlineCharacters)
                    title += " - " + ircutils.mircColor(titlesplit.group(2), 'orange')

                # shorten link and make it blue
                link = self._shortenUrl(data["link"])
                link = ircutils.mircColor(link, 'blue')

                #topnews_entries.append({'title': title, 'link': link, 'published': published})

                irc.reply(title + " " + link + " " + "[" + published + "]")

    topnews = wrap(topnews, [getopts({'num': 'int', 'geo': 'text'}), optional('text')])

Class = TopNews


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=300:
