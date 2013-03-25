###
# Copyright (c) 2012, Pooh Bear
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
import random

from random import randint
import re
import time

class Triggers(callbacks.PluginRegexp):
    """Add the help for "@plugin help Triggers" here
    This should describe *how* to use this plugin."""
    threaded = True
    regexps = ['whatislove', 'penis', 'nohomo', 'smile', 'fuckyeah', 'thrust', 'birthday', 'hugs', 'kisses','licks', 'crumpets', 'gross']

    def _color(self, c, fg=None):
        if c == ' ':
            return c
        if fg is None:
            fg = str(random.randint(2, 15)).zfill(2)
        return '\x03%s%s' % (fg, c)

    def hugs(self,irc,msg,match):
        r'ACTION(.+)?[Hh]ugs(.+)?'
        if re.search(r'[Pp]oohbot', msg.args[1], re.I):
        	irc.reply("""hugs %s back""" % msg.nick,prefixNick=False, action=True)
        else:
    		return
    
    def licks(self,irc,msg,match):
        r'ACTION(.+)?[Ll]icks(.+)?'
        if re.search(r'[Pp]oohbot', msg.args[1], re.I):
        	irc.reply("""o_O""",prefixNick=False)
        	irc.reply("""O_o""",prefixNick=False)
        else:
    		return
        
    def kisses(self,irc,msg,match):
        r'ACTION(.+)?[Kk]isses(.+)?'
        if re.search(r'[Pp]oohbot', msg.args[1], re.I):
        	irc.reply("""blushes""",prefixNick=False, action=True)
        else:
    		return
    

    def whatislove(self,irc,msg,match):
        r'[Ww]hat is love?'
        
        irc.reply("""Baby don't hurt me""",prefixNick=False)
        
        irc.reply("""Don't hurt me""",prefixNick=False)
        
        irc.reply("""No more""",prefixNick=False)
    
    def penis(self,irc,msg,match):
        r'B===D'
        
        u = unichr(0xCA0) + "_-"
        
        irc.reply(u, prefixNick=False)
        
    def birthday(self,irc,msg,match):
        r'(.+)?[Hh]appy(.+)?[Bb]irthday(.*)\!'
        channel = msg.args[0]
        if not irc.isChannel(channel):
            return
        if callbacks.addressed(irc.nick, msg):
            return
        
        text1 = "HAPPY BIRTHDAY!!!!!!"
        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
        L = [self._color(c, fg=colors.next()) for c in text1]
        irc.reply(''.join(L) + '\x03')

    def nohomo(self,irc,msg,match):
        r'(.+)?[Nn]o [Hh]omo(.+)?'
    
        irc.reply("""Come on, man. You don't have to hide it from us.""",prefixNick=True)

    def smile(self,irc,msg,match):
        r'[Ss]mile!'
        
        irc.reply("""http://youtu.be/mNrXMOSkBas""",prefixNick=False)

    
    def fuckyeah(self,irc,msg,match):
        r'(.+)?[Ff]uck [Yy]eah(.*)\!'
        
        irc.reply("""\o/""",prefixNick=False)

    def thrust(self,irc,msg,match):
        r'(.+)?ACTION(.+)?[Tt]hrusts(.+)?'
        
        irc.reply("""http://i.imgur.com/oz4RF.gif""")
#        irc.reply("""http://i.imgur.com/vOokp.gif""",prefixNick=False)
        
    def crumpets(self,irc,msg,match):
        r'(.+)?[Cc]rumpets(.+)?'
        
        irc.reply("""Crumpets? What is this sorcery?""",prefixNick=False)

#    def derp(self,irc,msg,match):
#        r'[Dd]erp'
#        
#        irc.reply("""herp""",prefixNick=False)

#    def herp(self,irc,msg,match):
#        r'[Hh]erp'
#        
#        irc.reply("""derp""",prefixNick=False)
    
    def gross(self, irc, msg, match):
        r'(.+)?[Gg]ross(.*)\!'
        
        irc.reply("""http://i.imgur.com/fmY1CvZ.jpg""",prefixNick=False)
             
Class = Triggers

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
