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
#from supybot.i18n import PluginInternationalization, internationalizeDocstring

from bs4 import BeautifulSoup
#from urllib2 import Request, build_opener, HTTPError
import urllib2
import json
import re

#_ = PluginInternationalization('FuckingDinner')
#
#@internationalizeDocstring
class FuckingMovie(callbacks.Plugin):
    """Add the help for "@plugin help FuckingDinner" here
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

    def fuckingmovie(self, irc, msg, args):
        """
        
        What the fuck should I watch tonight? Pulls a random movie from http://whatthefuckshouldiwatchtonight.com/"""

        url = 'http://whatthefuckshouldiwatchtonight.com/get_movie.php'

        try:
            html = utils.web.getUrl(url)
        except utils.web.Error, e:
            irc.error(format('I couldn\'t reach the search page (%s).', e), Raise=True)
        
        soup = BeautifulSoup(html)
        results = soup.findAll('p')    
        link = soup.findAll('a')
        if not results:
            irc.error('I could not the proper formatting on the page. Could %s be broken?' % url)
        else:
            out = results[0].text + ' ' + "'" + link[0].text + "': "
            out = re.sub(r'fucking', ircutils.bold(ircutils.mircColor('FUCKING', '5')), out, re.I)
            out = re.sub(r'<[^>]*?>', '', out)
            out = re.sub(r'\n', '', out)
#            out = ircutils.bold(out)
            out += link[0]['href']
            irc.reply(out.encode('utf-8'), prefixNick=True)

    fuckingmovie = wrap(fuckingmovie)

Class = FuckingMovie



# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=179:
