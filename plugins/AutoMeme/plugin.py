###
# Copyright (c) 2012, spline
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

import json
import urllib2

#_ = PluginInternationalization('AutoMeme')
#
#@internationalizeDocstring
class AutoMeme(callbacks.Plugin):
    """Add the help for "@plugin help AutoMeme" here
    This should describe *how* to use this plugin."""
    threaded = True

    def automeme(self, irc, msg, args, number):
        """
        Display a meme from http://www.automeme.net
        Specify a number after the command [1-7] for more than one.
        """

        if number and (0 < number <= 7):
            number = number
        else:
            number = 1


        jsonurl = 'http://api.automeme.net/text.json?lines=%s' % number
        request = urllib2.Request(jsonurl)
        response = urllib2.urlopen(request)
        response_data = response.read()
        jsondata = json.loads(response_data)

        for meme in jsondata:
            irc.reply(ircutils.bold(meme), prefixNick=True)
        
    automeme = wrap(automeme, [optional("int")])

Class = AutoMeme


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=200:
