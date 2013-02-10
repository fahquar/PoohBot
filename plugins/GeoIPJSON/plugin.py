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
class GeoIPJSON(callbacks.Plugin):
    """Add the help for "@plugin help GeoIPJSON" here
    This should describe *how* to use this plugin."""
    threaded = True

#    @internationalizeDocstring
    def geoip(self, irc, msg, args, user):
        """<ip.address>
        Use a GeoIP API to lookup the location of an IP.
        """

        # Some logic to determine if input is a user, a hostname, or IP address.
        # All code here is from the generous Hoaas who uses it within his Patdown Supybot plugin.

        try:
            socket.inet_aton(user)
            ip = user
            input = None
            user = None

        except socket.error:
            # If it is a nick in the channel
#            if ( irc.isNick(user) or user in irc.state.channels[msg.args[0]].users ):
            try:
                hostname = irc.state.nickToHostmask(user)
                hostname = hostname.replace("gateway/web/freenode/ip.", "")
                hostname = hostname[hostname.find("@")+1:]
            except:
                irc.reply("User not found.")
                return
            # Possibly an hostname?
#            else:
#                hostname = user
#                user = None
            try:
                __, __, ip = socket.gethostbyname_ex(hostname)
            except socket.herror:
                irc.reply("ALERT! ERROR! No srsly, not sure what this is.")
                return
            except socket.gaierror:
                irc.reply("No IP found. (it was a hostname, right?)")
                return

            ip = ip[0]


        jsonurl = 'http://freegeoip.net/json/%s' % (ip)

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
            irc.reply("Failed in loading JSON data for GeoIP.")
            return

        if len(jsondata) < 1:
            irc.reply("I found no JSON Data forGeoIP.")
            return
        country = jsondata.get('country_name') or 'N/A'
        city = jsondata.get('city') or 'N/A'
        region_code = jsondata.get('region_code', None)
        region_name = jsondata.get('region_name') or 'N/A'
        zipcode = jsondata.get('zipcode') or ''
        longitude = jsondata.get('longitude', None)
        latitude = jsondata.get('latitude', None)
        ip = jsondata.get('ip', None)

        if ip != None and city != None and region_code != None:
            output = ircutils.bold(ircutils.underline(ip))
            output += " " + city + ", " + region_name + " " + zipcode + " - " + country
            output += " (" + str(longitude) + ", " + str(latitude) + ") " 


        irc.reply(output)
    
    geoip = wrap(geoip, [('somethingWithoutSpaces')])

Class = GeoIPJSON


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
