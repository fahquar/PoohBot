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

    regexps = ['whatislove', 'penis', 'flutteryay', 'dance', 'nohomo', 'smile', 'camchat', 'minecraft', 'fuckyeah', 'thrust', 'nerdcraft', 'tksync', 'zombies', 'birthday', 'hugs']

    
#    def party(self,irc,msg,match):
#        r'(.+)?[P|p]arty(.*)\!'
#        
#        irc.reply("""(>'')>""",prefixNick=False)
#        
# 
#        irc.reply("""<(''<)""",prefixNick=False)
#        
#        
#        irc.reply("""^( '' )^""",prefixNick=False)
#        
#  
#        irc.reply("""v( '' )v""",prefixNick=False)
    
    
    
    
    def _color(self, c, fg=None):
        if c == ' ':
            return c
        if fg is None:
            fg = str(random.randint(2, 15)).zfill(2)
        return '\x03%s%s' % (fg, c)
    def hugs(self,irc,msg,match):
        r'/^(.+) (?:PoohBot)hugs'
        irc.reply('derp')
        irc.reply("""Baby don't hurt me""",prefixNick=False)

    def whatislove(self,irc,msg,match):
        r'(.+)?[Ww]hat is love(.+)?'
        
        irc.reply("""Baby don't hurt me""",prefixNick=False)
        
        irc.reply("""Don't hurt me""",prefixNick=False)
        
        irc.reply("""No more""",prefixNick=False)
    
    def penis(self,irc,msg,match):
        r'B===D'
        
        u = unichr(0xCA0) + "_-"
        
        irc.reply(u, prefixNick=False)
    
    def flutteryay(self,irc,msg,match):
        r'[Ff]lutteryay'

        irc.reply("""http://flutteryay.com/""",prefixNick=False)

    def dance(self,irc,msg,match):
        r'[Dd]ance!'
        
        right = ircutils.mircColor("(>", '13') + "''" + ircutils.mircColor(")>", '13')
        left = ircutils.mircColor("<(", '13') + "''" + ircutils.mircColor("<)", '13')
        up = ircutils.mircColor("^(", '13') + " '' " + ircutils.mircColor(")^", '13')
        down = ircutils.mircColor("v(", '13') + " '' " + ircutils.mircColor(")v", '13')
        
        
        irc.reply(right,prefixNick=False)
        
        
        irc.reply(left,prefixNick=False)
        
        
        irc.reply(up,prefixNick=False)
        
        
        irc.reply(down,prefixNick=False)
        
    def birthday(self,irc,msg,match):
        r'(.+)?[H\h]appy(.+)?[B|b]irthday(.*)\!'
        
        text1 = "HAPPY BIRTHDAY!!!!!!"
        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
        L = [self._color(c, fg=colors.next()) for c in text1]
        irc.reply(''.join(L) + '\x03')
        
#        right = ircutils.mircColor("(>", '13') + "''" + ircutils.mircColor(")>", '13')
#        left = ircutils.mircColor("<(", '13') + "''" + ircutils.mircColor("<)", '13')
#        up = ircutils.mircColor("^(", '13') + " '' " + ircutils.mircColor(")^", '13')
#        down = ircutils.mircColor("v(", '13') + " '' " + ircutils.mircColor(")v", '13')
#        
#        
#        irc.reply(right,prefixNick=False)
#        
#        
#        irc.reply(left,prefixNick=False)
#        
#        
#        irc.reply(up,prefixNick=False)
#        
#        
#        irc.reply(down,prefixNick=False)
#    
#        text2 = "WOOHOOOO!!!!!!!!!!!!!!!!!!!!!!!!"
#        L = [self._color(c) for c in text2]
#        irc.reply('%s%s' % (''.join(L), '\x03'))

    def nohomo(self,irc,msg,match):
        r'(.+)?[Nn]o [Hh]omo(.+)?'
    
        irc.reply("""Come on, man. You don't have to hide it from us.""",prefixNick=True)

    def smile(self,irc,msg,match):
        r'[Ss]mile!'
        
        irc.reply("""http://youtu.be/mNrXMOSkBas""",prefixNick=False)

    def camchat(self,irc,msg,match):
        r'[Cc]amchat!'
        
        irc.reply("""GET IN HERE: http://www.icanhazchat.com/nerdcraft""",prefixNick=False)

#    def nerdbang(self,irc,msg,match):
#        r'[Nn]erdbang!'
#        
#        irc.reply("""GET IN HERE (NSFW): http://www.icanhazchat.com/nerdbang""",prefixNick=False)
	
    def nerdcraft(self,irc,msg,match):
        r'[Nn]erdcraft!'
	irc.reply("""GET IN HERE: http://www.icanhazchat.com/nerdcraft""",prefixNick=False)
	
    def minecraft(self,irc,msg,match):
        r'[Mm]inecraft!'
        
        irc.reply("""Minecraft Info: http://bit.ly/Qihbt7""",prefixNick=False)
        #	irc.reply("""TeamSpeak: 209.239.114.150:10387""",prefixNick=False)
    #	irc.reply("""Server Map: http://69.175.57.41:8129""",prefixNick=False)

    def zombies(self,irc,msg,match):
        r'(.+)?[Zz]ombies(.*)\!'
    
        irc.reply("""Plants vs. Zombies! Free! Go to http://www.stopzombiemouth.com and enter the code PEAH8R. Valid from October 30 to November 10, 2012.""",prefixNick=False)
    
    def fuckyeah(self,irc,msg,match):
        r'(.+)?[Ff]uck [Yy]eah(.*)\!'
        
        irc.reply("""\o/""",prefixNick=False)

    def thrust(self,irc,msg,match):
        r'[Tt]hrusts'
        
        irc.reply("""http://i.imgur.com/vOokp.gif""",prefixNick=False)

    def tksync(self,irc,msg,match):
        r'[Tt]ksync!'
        
        irc.reply("""Come join!: http://tksync.com/""",prefixNick=False)


Class = Triggers

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
