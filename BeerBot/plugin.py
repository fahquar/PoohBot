###
# Copyright (c) 2012, Brandon Betances
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
#
# Local Imports
import re
import urllib

#
# Supybot Imports
import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

#
# Classes
class BeerBot(callbacks.Plugin):
    """The BeerBot plugin provides some fuctionality to interact with
    the various craft beer related websites."""
    threaded = True

    _baUrl = 'http://www.beeradvocate.com' # beeradvocate base URL
    _baSearch = '/search?q=' # beeradvocate search string
    _baBeerRegex = '/beer/profile/\d+/\d+' # regex to find beer profiles
    
    #
    # Functions

    def ba(self, irc, msg, args, search):
        """<search>

        searches BeerAdvocate for <search>, and returns the first URL."""
        if search:
            queryString = self._baUrl + self._baSearch + search
            getUrl = urllib.urlopen(queryString)
            data = getUrl.read()
            m = re.search(self._baBeerRegex, data) # matches BeerAdvocate beer profile.
            if m:
                result = m.group(0)
                getBeer = urllib.urlopen(self._baUrl + result)
                dataBeer = getBeer.read()
                brewedBy = re.search('<b>Brewed by:</b>.*?<b>(.*?)</b></a>',dataBeer, re.M|re.S)
                brewedBy2 = brewedBy.group(1)
                irc.reply(brewedBy2 + " - " + self._baUrl + result, prefixNick=True)

                #style = re.search('<b>Style |(.*?)</b>.*?<b>(.*?)</b></a>.*?%nbsp;(.*?)<a href', dataBeer, re.M|re.S)
                #style2 = style.group(1) + style.group(2) + style.group(3)
                #irc.reply(style2)

            else:
                irc.reply("no results found.")
        else:
            irc.reply("please supply a search term.") # this doesn't work either.

    ba = wrap(ba, ['text'])

Class = BeerBot


# <b>Brewed by:</b>
#<br>
#<a href="/beer/profile/96"><b>Magic Hat Brewing Company</b></a>&nbsp;
#<a href="http://www.magichat.net"><img src="/im/i_website.gif" width="16" height="12" border="0" alt="visit their website" style="vertical-align: middle;"></a>
#<br><a href="/beerfly/directory/9/US/VT">Vermont</a>, <a href="/beerfly/directory/9/US">United States</a><br><br>
#<b>Style | ABV</b>
#<br>
#<a href="/beer/style/9"><b>Fruit / Vegetable Beer</b></a> | &nbsp;5.10% <a href="/articles/518">ABV</a>
#<br><br>
