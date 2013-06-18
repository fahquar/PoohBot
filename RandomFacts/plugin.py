###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import urllib2
import re

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
#from supybot.i18n import PluginInternationalization, internationalizeDocstring
#
#_ = PluginInternationalization('RandomFacts')
#
#@internationalizeDocstring
class RandomFacts(callbacks.Plugin):
    """Add the help for "@plugin help RandomFacts" here
    This should describe *how* to use this plugin."""
    threaded = True

    def randomfacts(self, irc, msg, args):
        """Fetch a random fact from www.randomfunfacts.com"""

        url = 'http://www.randomfunfacts.com'

        req = urllib2.Request(url)
        response = urllib2.urlopen(req)
        the_page = response.read()

        fact = re.search(r'<strong><i>(.*?)</i></strong>', the_page, re.I|re.S)

        irc.reply(fact.group(1), prefixNick=True)


Class = RandomFacts


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
