# -*- coding: UTF-8 -*-
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


class TA(callbacks.Plugin):
    
    threaded = True
    
    def _color(self, c, fg=None):
        if c == ' ':
            return c
        if fg is None:
            fg = str(random.randint(2, 15)).zfill(2)
    	return '\x03%s%s' % (fg, c)
    
    def movie(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Stream: ") + "http://www.livestream.com/tafilms")
    movie = wrap(movie)
    
    def dexter(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Stream: ") + "http://misclivestream.blogspot.co.uk/p/dexter.html", msg.nick, private=True, notice=True)
    dexter = wrap(dexter)
    
    def minecraft(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Server Info: ") + "http://bit.ly/Qihbt7")
    minecraft = wrap(minecraft)

    def camchat(self, irc, msg, args):
    	if msg.args[0] == "#togetheralone":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True) 
        if msg.args[0] == "#r4r":
        	title = "WaNt tO Go WiLd~*~* Try out the camchat! ---> "
        	title = ircutils.bold(ircutils.mircColor(title,'pink', '12'))
        	irc.reply(title + """http://www.icanhazchat.com/redditorforredditor""", prefixNick=True)
    camchat=wrap(camchat)

    def nerdcraft(self, irc, msg, args):
        
        irc.reply(ircutils.bold("""ICHC Room: """) +  "http://www.icanhazchat.com/nerdcraft")
    nerdcraft = wrap(nerdcraft)
    
    def nerdbang(self, irc, msg, args):
        
        irc.reply(ircutils.bold("""18+ ICHC Room: """) + "http://www.icanhazchat.com/nerdbang")
    nerdbang = wrap(nerdbang)
                  
    def tksync(self, irc, msg, args):
                  
        irc.reply("""Come join!: http://tksync.com/""")
    tksync = wrap(tksync)
    
    def radio(self, irc, msg, args):
                  
        irc.reply("""Click this: http://98.202.200.208:8002/listen.m3u""", prefixNick=True)
        irc.reply("""If you have any requests, feel free to bug PoohBear :)""", prefixNick=True)
    radio = wrap(radio)
    
    def rooms(self, irc, msg, args):
        irc.reply("""If you are interested in other social rooms on Freenode, check out #r.trees #reddit-mlp (/r/mylittlepony) #reddit-depression #reddit-twoxchromosomes #teaandcrumpets (general UK chat) #introverts #defocus (general chat) ##socialites (general social room) #okchat (/r/okcupid) ##loseit #r4r #r4r30plus #togetheralone and #makenewfriendshere""", prefixNick=True)
    rooms = wrap(rooms)
    
    def mods(self, irc, msg, args):
        irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, voidboi, and actualgirl.""", prefixNick=True)
    mods = wrap(mods)
    
    def gaybar(self, irc, msg, args):
        irc.reply("""http://youtu.be/HTN6Du3MCgI""", prefixNick=True)
    gaybar = wrap(gaybar)
    
    def pics(self, irc, msg, args):
        irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/14yv6n/new_picture_thread/""")
    pics = wrap(pics)
    
    def birthdays(self, irc, msg, args):
        irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/Lz5MP""")
    birthdays = wrap(birthdays)
    
    def birthdayform(self, irc, msg, args):
        irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/9UlyC""")
    birthdayform = wrap(birthdayform)
    
    def tinychat(self, irc, msg, args):
        irc.reply(ircutils.bold("""Tinychat Room: """) + "http://tinychat.com/chilijam")
    tinychat = wrap(tinychat)
    
    def chilijam(self, irc, msg, args):
        irc.reply(ircutils.bold("""Tinychat Room: """) + "http://tinychat.com/chilijam")
    chilijam = wrap(chilijam)

    def friday(self, irc, msg, args):
        irc.reply("http://youtu.be/kfVsfOSbJY0", prefixNick=True)
    friday = wrap(friday)
    
    def languages(self, irc, msg, args):
    	irc.reply("""http://goo.gl/DBImS""", prefixNick=True)
    languages = wrap(languages)
    
    def adventuretime(self, irc, msg, args):
    	irc.reply("http://www.justin.tv/cujoe50", prefixNick=True)
    adventuretime = wrap(adventuretime)
    	
    
    def hangout(self, irc, msg, args, victim):
    	text1 = "COME JOIN!!! ---> "
#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
#        L = [self._color(c, fg=colors.next()) for c in text1]
#        text2 = ''.join(L) + '\x03'
        text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
        text2 = text1 + """http://goo.gl/oms8X"""
        if not victim:
            irc.reply(text2, prefixNick=True)
        else:
            irc.reply(format('%s: %s ', victim, text2),
                      prefixNick=False)
    hangout = wrap(hangout, [additional('text')])
        
    def rules(self, irc, msg, args):
    	if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#tamods":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""") 
        if msg.args[0] == "#r4r":
            irc.reply(ircutils.bold("""Rules for #r4r: """) + """http://pastebin.com/8aFkb48r""")
        if msg.args[0] == "#newjersey":
            irc.reply(ircutils.bold("""Rules for #newjersey: """) + """http://pastebin.com/AgRarwqu""")            
        else:
            return None
    rules = wrap(rules)
    
    def games(self, irc, msg, args):
    	irc.reply("For game rooms on Freenode, check out ##poker ##uno ##apples2 #wolfgame ##trivia and #botsagainsthumanity", prefixNick=True)
    games = wrap(games)
    	
    def banlist(self, irc, msg, args):
    	irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    banlist = wrap(banlist)
    
    def map(self, irc, msg, args):
    	irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    map = wrap(map)
    
    def butts(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/6uR360O.gif", prefixNick=True)
    butts = wrap(butts)
    
    def simpsons(self, irc, msg, args):
    	irc.reply("http://tgun.tv/embed/simps.php", prefixNick=True)
    simpsons = wrap(simpsons)
    
    def belair(self, irc, msg, args):
    	irc.reply("http://youtu.be/aZZULi9r6mY", prefixNick=True)
    belair = wrap(belair)
    
    def yay(self, irc, msg, args):
    	irc.reply("http://flutteryay.com/", prefixNick=True)
    yay = wrap(yay)
    
    def dew(self, irc, msg, args):
    	irc.reply("http://dewextended.ytmnd.com", prefixNick=True)
    dew = wrap(dew)
        
    def no(self, irc, msg, args, victim):
    	lod = """ಠ_ಠ"""
    	if victim is None:
    		return None
        irc.reply(format('%s: %s', victim, lod))
    no = wrap(no,[additional('text')])

Class = TA

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
