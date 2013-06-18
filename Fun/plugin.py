###
# Copyright (c) 2012, mameman
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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from BeautifulSoup import BeautifulSoup
import random
import urllib


class Fun(callbacks.Plugin):
    """Add the help for "@plugin help Fun" here
    This should describe *how* to use this plugin."""
    pass
    def fun(self, irc, msg, args):
		s = ''
		if not args:
			s+= 'PoohBot'
		else:
			for st in args:
				s += st + ' '
		
                sites = ['http://www.sloganizer.net/en/outbound.php?slogan=', 'http://www.sloganmaker.com/hate/sloganmaker.php?user=', 'http://parsers.faux-bot.com/slogan/']
                num = random.randint(0, 2)
                
                if num is 0:
                        irc.reply(str(urllib.urlopen(sites[0]+s.strip()).read()).split('>')[1].split('<')[0], prefixNick=False)
                elif num is 1:
                        site = BeautifulSoup(urllib.urlopen(sites[1]+s.strip()).read())
                        #irc.reply(str(site.find('p')).split('<p>')[1].split('</p>')[0], prefixNick=False)
                        irc.reply(str(site.body.div.p).split('<p>')[1].split('</p>')[0], prefixNick=False)
                elif num is 2:
                        irc.reply(str(urllib.urlopen(sites[2]+s.strip()).read()).split('Response: ')[1].split('\nEnd')[0], prefixNick=False)
Class = Fun


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
