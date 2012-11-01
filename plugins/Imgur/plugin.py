###
# Copyright (c) 2012, PoohBear (mostly)
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions, and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright notice,
#     this list of conditions, and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of the author of this software nor the name of
#     contributors to this software may be used to endorse or promote products
#     derived from this software without specific prior written consent.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.

###
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

class Imgur(callbacks.Plugin):
    """This plugin returns random wesite links using stumbleupon, imgur and wikipedia."""
    threaded = True
    
    def imgurupload(self, image):
        response = cStringIO.StringIO()
        c = pycurl.Curl()
        image = str(image)
        values = [
                  ("key", "Put API key here"),
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


    def imgur(self, irc, msg, args, url):
        """<image url>
            
            Uploads an image onto imgur. Useful for bypassing web filters.
            """
        
        title = ircutils.bold("Here's your imgur link --> ")
        imgururl = self.imgurupload(url)
        irc.reply("%s %s" % (title, imgururl), prefixNick=True)

    imgur = wrap(imgur, ['text'])

    def randomimgur(self, irc, msg, args):
        """takes no arguments
        returns a random gallery from imgur.com
        """
        url = "http://imgur.com/gallery/random.json"
        try:
            req = urllib2.Request(url)
            f = urllib2.urlopen(req)
            f_data=f.read()
        except:
            irc.reply("Unable to return info. Maybe imgur is down?")
            return
        jsondata = json.loads(f_data)
        data = jsondata.get('data')[1]
        type = data[u'ext']
        hash = data[u'hash']
        image = "http://i.imgur.com/%s%s"% (hash, type)
        title = data[u'title']
#        title = title + ":"
        title = ircutils.bold(title)
        irc.reply("%s %s" % (title, image))

    randomimgur = wrap(randomimgur)

Class = Imgur


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
