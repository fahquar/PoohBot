import json
import urllib
import urllib2
import re


import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class HackerNews(callbacks.Plugin):
    """Add the help for "@plugin help HackerNews" here
    This should describe *how* to use this plugin."""
    threaded = True

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


    def hackernews(self, irc, msg, args, optlist):
        """[--newest|--latest|--best|--ask] type of headlines to display.
        
        Display top hackernews.com headlines.
        """

        hnposts = "latest"

        #for (key, value) in optlist:
        #    if key == 'newest':
        #        hnposts = "newest"
        #    if key == 'latest':
        #        hnposts = "latest"
        #    if key == 'best':
        #        hnposts = "best"
        #    if key == 'ask':
        #        hnposts = "ask"

        api_url = "http://hackernews-frontend.appspot.com/%s/format/json/limit/5" % hnposts
        self.log.info(api_url)
        response = urllib2.urlopen(api_url)
        data = response.read().decode('latin-1')
        jsondata = json.loads(data)

        #self.log.info(json.dumps(jsondata, indent=2))

        items = jsondata['items']

        #entries = sorted(items, key=items['comments'], reverse=True)

        for item in items:
            title = item['title']
            url = self._shortenUrl(item['url'])
            score = item['score']
            user = item['user']
            comments = item['comments']
            time = item['time']
            item_id = item['item_id']
            irc.reply(title + " " + url)

    hackernews = wrap(hackernews, [getopts({'newest': '','latest': '','best': '','ask': ''})])

Class = HackerNews


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=200:
