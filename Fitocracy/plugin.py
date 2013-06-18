###
# Copyright (c) 2012, spline
# All rights reserved.
#
#
###

import json
import urllib2
import socket

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
#from supybot.i18n import PluginInternationalization, internationalizeDocstring
#
#_ = PluginInternationalization('GeoIPJSON')
#
#@internationalizeDocstring
class Fitocracy(callbacks.Plugin):
    """Add the help for "@plugin help GeoIPJSON" here
    This should describe *how* to use this plugin."""
    threaded = True

#    @internationalizeDocstring
    def fitocracy(self, irc, msg, args, user):
        """<ip.address>
        Use a GeoIP API to lookup the location of an IP.
        """
        irc.reply(user)
        jsonurl = 'http://fitocracy-unofficial-api.herokuapp.com/user/%' % (user)

        self.log.info(jsonurl)

        try:
            request = urllib2.Request(jsonurl)
            response = urllib2.urlopen(request)
            response_data = response.read()
        except urllib2.HTTPError as err:
            if err.code == 404:
                irc.reply("Error 404")
                self.log.warning("Error 404 on: %s" % (jsonurl))
            elif err.code == 403:
                irc.reply("Error 403. Try waiting 60 minutes.")
                self.log.warning("Error 403 on: %s" %s (jsonurl))
            else:
                irc.reply("Error. Check the logs.")
            return

        try:
            jsondata = json.loads(response_data)
        except:
            irc.reply("Failed in loading JSON data for Fitocracy.")
            return

        if len(jsondata) < 1:
            irc.reply("I found no Fitocracy Data.")
            return
        name = jsondata.get('name') or 'N/A'
        progress = jsondata.get('progress_text') or 'N/A'
        level = jsondata.get('level', None)


#        if user != None and city != None and region_code != None:
        output = ircutils.bold(ircutils.underline(user))
        output += " " + name + ", " + progress + " " + level


        irc.reply(output)
    
    fitocracy = wrap(fitocracy, [('somethingWithoutSpaces')])

Class = Fitocracy


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
