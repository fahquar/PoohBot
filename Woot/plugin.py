###
# Copyright (c) 2012, woot
# All rights reserved.
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

import urllib2
import urllib
import json
import xml.dom.minidom

class Woot(callbacks.Plugin):
    """Add the help for "@plugin help Woot" here
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

    def woot(self, irc, msg, args):	
        """ Display daily woot.com deal."""

        url = "http://www.woot.com/salerss.aspx"
        
        dom = xml.dom.minidom.parse(urllib2.urlopen(url))
      
        product = dom.getElementsByTagName("woot:product")[0].childNodes[0].data
        price = dom.getElementsByTagName("woot:price")[0].childNodes[0].data
        purchaseurl = dom.getElementsByTagName("woot:purchaseurl")[0].childNodes[0].data
        soldout = dom.getElementsByTagName("woot:soldout")[0].childNodes[0].data # false
        shipping = dom.getElementsByTagName("woot:shipping")[0].childNodes[0].data

        if soldout == 'false':
            output = ircutils.mircColor("IN STOCK ", "green")
        else:
            output = ircutils.mircColor("SOLDOUT ", "red")

        output += ircutils.underline(ircutils.bold("ITEM:")) + " " + product + " "
        output += ircutils.underline(ircutils.bold("PRICE:")) + " " + price + " (Shipping:" + shipping + ") "
        output += ircutils.underline(ircutils.bold("URL:")) + " " + self._shortenUrl(purchaseurl) + " "

        irc.reply(output, prefixNick=True)
	
    woot = wrap(woot)

    def wootshirt(self, irc, msg, args):	
        """ Display daily woot.com deal."""
    
        url = "http://shirt.woot.com/salerss.aspx"
    
        dom = xml.dom.minidom.parse(urllib2.urlopen(url))
    
        product = dom.getElementsByTagName("woot:product")[0].childNodes[0].data
        price = dom.getElementsByTagName("woot:price")[0].childNodes[0].data
        purchaseurl = dom.getElementsByTagName("woot:purchaseurl")[0].childNodes[0].data
        soldout = dom.getElementsByTagName("woot:soldout")[0].childNodes[0].data # false
        shipping = dom.getElementsByTagName("woot:shipping")[0].childNodes[0].data
    
        if soldout == 'false':
            output = ircutils.mircColor("IN STOCK ", "green")
        else:
            output = ircutils.mircColor("SOLDOUT ", "red")
    
        output += ircutils.underline(ircutils.bold("ITEM:")) + " " + product + " "
        output += ircutils.underline(ircutils.bold("PRICE:")) + " " + price + " (Shipping:" + shipping + ") "
        output += ircutils.underline(ircutils.bold("URL:")) + " " + self._shortenUrl(purchaseurl) + " "
    
        irc.reply(output, prefixNick=True)
        
    wootshirt = wrap(wootshirt)


Class = Woot

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=280:
