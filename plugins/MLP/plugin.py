#################################
# Copyright (c) 2012, PoohBear  #
# All rights reserved.          #
#                               #
#                               #
#################################

import json
import urllib2
import socket
import re
import string
import urllib
import lxml.html
from BeautifulSoup import BeautifulSoup
from lxml import etree
import untangle
from urllib import urlencode
from urllib import urlopen
import base64
import os
import pycurl
import cStringIO

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

def filter_non_printable(str):
    return ''.join([c for c in str if ord(c) > 31 or ord(c) == 9])

class MLP(callbacks.Plugin):
    """A collection of various pony related plugins"""
    
    threaded = True
    def imgurupload(self, image):
        response = cStringIO.StringIO()
        c = pycurl.Curl()
        image = str(image)
        values = [
                  ("key", "c284f01adf471326611029a2ce4c2c19"),
                  ("image", image)]
        
        c.setopt(c.URL, "http://api.imgur.com/2/upload.xml")
        c.setopt(c.HTTPPOST, values)
        c.setopt(c.WRITEFUNCTION, response.write)
        c.perform()
        c.close()
        
        o = untangle.parse(response.getvalue())
        try:
            imageURL = o.upload.links.original.cdata
            return imageURL
        except:
            imageURL = image
            return imageURL
            
    def pmb(self, irc, msg, args):
        """
        Returns a random image from ponymindbleach.com
        """

        jsonurl = 'http://ponymindbleach.com/beta/functions/api.php?request={"command":"getJSON"}'

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
            irc.reply("Failed in loading JSON data for http://ponymindbleach.com")
            return

        if len(jsondata) < 1:
            irc.reply("I found no JSON Data for http://ponymindbleach.com")
            return
        title = jsondata.get('title')
        title = title + ':'
        title = ircutils.bold(title)
        image = jsondata.get('fullimageurl')
        pageurl = jsondata.get('permalink')
        imgururl = self.imgurupload(image)
    
        irc.reply('%s %s' % (title, imgururl))
        irc.reply(ircutils.bold('Page link: ') + '%s' % (pageurl))
    
    pmb = wrap(pmb)

    def mlfw(self, irc, msg, args, text):
        """<tag>
            
        Finds an image from mylittlefacewhen.com based on tags, or gives a random image.
        """
        # Some logic to determine if input is a user, a hostname, or IP address.
        # All code here is from the generous Hoaas who uses it within his Patdown Supybot plugin.
        if text is None:
            jsonurl = 'http://mylittlefacewhen.com/api/v2/face/?order_by=random&limit=1&format=json'
            title = "Random MLFW image:"
            self.log.info(jsonurl)
        else:
            originaltext = text
            text = text.replace(" ", "%20")
            jsonurl = 'http://mylittlefacewhen.com/api/v2/face/?search=["%s"]&order_by=random&limit=1&format=json' % text
            title = format("MLFW image for '%s': ", originaltext)
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
            irc.reply("Failed in loading JSON data for http://mylittlefacewhen.com")
            return
    
        if len(jsondata) < 1:
            irc.reply("I found no JSON Data for http://mylittlefacewhen.com")
            return
        title = ircutils.bold(title)
        objects = jsondata.get('objects')
        ids = [item['id'] for item in jsondata[u'objects']]
        for id in ids:
            id = id
        imagelink = None
        images = [item['image'] for item in jsondata[u'objects']]
        for image in images:
            imagelink = image
        if imagelink is None:
            self.mlfw(irc, msg, args,text=None)
        else:
            baseurl = 'http://scranton.mylittlefacewhen.com'
            baseurl += imagelink
            imgururl = self.imgurupload(baseurl)
            irc.reply('%s %s' % (title, imgururl))
    
    mlfw = wrap(mlfw,[additional('text')])

    def wikia(self, irc, msg, args, search):
        """<search term>
            
        Returns a short description from the MLP wiki"""
        addr = 'http://mlp.wikia.com/wiki/Special:Search?search=%s' % urllib.quote_plus(search)
        try:
            article = utils.web.getUrl(addr)
        except:
            irc.reply('Hmm, something went wrong fetching the page.  I\'m highlighting PoohBear so he can take a look.', prefixNick=True)
            return
        tree = lxml.html.document_fromstring(article)
        didyoumean = tree.xpath('//div[@class="searchdidyoumean"]/a[@title="Special:Search"]')
        if didyoumean:
            redirect = didyoumean[0].text_content().strip()
            redirect = redirect.encode('utf-8')
            irc.reply('I didn\'t find anything for "%s". Did you mean "%s"?' % (search, redirect), prefixNick=True)
            addr = 'http://en.wikipedia.org%s' % didyoumean[0].get('href')
            article = utils.web.getUrl(addr)
            tree = lxml.html.document_fromstring(article)
            search = filter_non_printable(redirect)
        searchresults = tree.xpath('//div[@class="mw-search-result-heading"]/a[1]')
        if searchresults:
            redirect = searchresults[0].text_content().strip()
            redirect = redirect.encode('utf-8')
            irc.reply('I didn\'t find anything for "%s", but here\'s the result for "%s":' % (search, redirect), prefixNick=False)
            addr = 'http://en.wikipedia.org%s' % searchresults[0].get('href')
            article = utils.web.getUrl(addr)
            tree = lxml.html.document_fromstring(article)
            search = redirect
        else:
            redirect = re.search('\(Redirected from <a href=[^>]*>([^<]*)</a>\)', article)
            if redirect:
                redirect = tree.xpath('//div[@id="contentSub"]/a')[0].text_content().strip()
                redirect = redirect.encode('utf-8')
                title = tree.xpath('//*[@class="firstHeading"]')
                title = title[0].text_content().strip()
                title = title.encode('utf-8')
                irc.reply('"%s" (Redirect from "%s"):' % (ircutils.bold(title), ircutils.bold(redirect)))
        addr = re.search('Retrieved from "<a href="([^"]*)">', article)
        addr = addr.group(1)
        disambig = tree.xpath('//table[@id="disambigbox"]')
        if disambig:
            disambig = tree.xpath('//*[@id="mw-content-text"]/ul/li/a')
            disambig = disambig[:5]
            disambig = [item.text_content() for item in disambig]
            r = utils.str.commaAndify(disambig)
            irc.reply('%s is a disambiguation page.  Possible results are: %s' % (addr, ircutils.bold(r)), prefixNick=False)
        elif re.search('This article is about the year [\d]*\.  For the [a-zA-Z ]* [\d]*, see', article):
            irc.reply('"%s" is a page full of events that happened in that year.  If you were looking for information about the number itself, try searching for "%s_(number)", but don\'t expect anything useful...' % (ircutils.bold(search), ircutils.bold(search)), prefixNick=False)
        else:
            p = tree.xpath("//meta[@property='og:description']")[0]
            p = p.get("content")
            p = p.strip()
            p = re.sub('\[\d+\]', '', p)
            p = p.encode('utf-8')
            title = tree.xpath("//meta[@property='og:title']")[0]
            title = title.get("content")
            title = title.encode('utf-8')
            newurl = tree.xpath("//meta[@property='og:url']")[0]
            newurl = newurl.get("content")
            imageurl = tree.xpath("//meta[@property='og:image']")[0]
            imageurl = imageurl.get("content")
            addr = re.sub('&amp;', '&', addr)
            imgururl = self.imgurupload(imageurl)
            irc.reply(newurl, prefixNick=False)
            irc.reply(ircutils.bold(title) + ': ' + p + ' ' + imgururl)
    
    wikia = wrap(wikia, ['text'])

Class = MLP


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=250:
