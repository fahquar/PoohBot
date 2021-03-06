###
# Copyright (c) 2012, resistivecorpse
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
import untangle
import lxml.html
from lxml import etree
import string
import urllib2
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class Stumble(callbacks.Plugin):
    """This plugin returns random wesite links using stumbleupon, imgur and wikipedia."""
    threaded = True

    def stumble(self, irc, msg, args):
        """takes no arguments
        returns a random link using stumbleupon.com
        """
        user_agent = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:15.0) Gecko/20100101 Firefox/15.0.1"
        url = "http://www.stumbleupon.com/s/"
        req = urllib2.Request(url, None, { 'User-Agent' : user_agent})
        f = urllib2.urlopen(req)
        source = f.geturl()
#        link = source[56:]
        linkalt = source.split('/')[6]
        irc.reply('http://%s' % (linkalt), prefixNick=True)
#        if link.startswith("/"):
#            irc.reply('http://%s' % (linkalt[1:]), prefixNick=True)
#        else:
#            irc.reply('http://%s' % (linkalt), prefixNick=True)

    stumble = wrap(stumble)

Class = Stumble


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
