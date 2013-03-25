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
from random import choice

class TA(callbacks.Plugin):

    threaded = True
    wordbutts = """http://i.imgur.com/2FhYOYj.gif
http://i.imgur.com/44meRoE.gif
http://i.imgur.com/Yn3Ziai.gif
	"""
    sexybutts = """http://i.imgur.com/o2f4BgA.gif
http://i.imgur.com/5berE6P.gif
http://i.imgur.com/qzspW6C.gif
http://i.imgur.com/F2FYrBZ.gif
http://i.imgur.com/RW0erPq.gif
http://i.imgur.com/Ydqt9vu.gif
http://i.imgur.com/kk6Giqv.gif
http://i.imgur.com/KobLlIY.gif
http://i.imgur.com/A6H3HJp.gif
http://i.imgur.com/4QW5RLK.gif
http://i.imgur.com/uQZm4wQ.gif
http://i.imgur.com/nThuXaq.gif
http://i.imgur.com/jUquNlN.gif
http://i.imgur.com/H801wMW.gif
http://i.imgur.com/iKTO09R.gif
http://i.imgur.com/VIpc1Cx.gif
http://i.imgur.com/5IL5mIy.gif
http://i.imgur.com/eDs1vk7.gif
http://i.imgur.com/sZuzG9e.gif
http://i.imgur.com/EZxCwh9.gif
http://i.imgur.com/xTSr0M5.gif
http://i.imgur.com/zIXWa81.gif
http://i.imgur.com/qRyNv8l.gif
http://i.imgur.com/MJpQTeY.gif
http://i.imgur.com/pAe7HUg.gif
http://i.imgur.com/SzVZjgu.gif
http://i.imgur.com/08w6YLb.gif
http://i.imgur.com/knsuCYD.gif
http://i.imgur.com/5wkeM0u.gif
http://i.imgur.com/WEWf2Ym.gif
http://i.imgur.com/3sn23fp.gif
http://i.imgur.com/tsuAwoi.gif
http://i.imgur.com/FABU9lM.gif
http://i.imgur.com/eH0oav1.gif
http://i.imgur.com/vIjfkFA.gif
http://i.imgur.com/SQXUJZ5.gif
http://i.imgur.com/JRcATG1.gif
http://i.imgur.com/36xf970.gif
http://i.imgur.com/BvwVMQJ.gif
http://i.imgur.com/FY5rbc4.gif
http://i.imgur.com/4LSV94x.gif
http://i.imgur.com/J87lZwT.gif
http://i.imgur.com/JFfszV7.gif
http://i.imgur.com/p4qj4Vb.gif
http://i.imgur.com/dxHksGk.gif
http://i.imgur.com/zZblTI2.gif
http://i.imgur.com/jHSP7Yg.gif
http://i.imgur.com/Bm2t527.gif
http://i.imgur.com/qrLIsdS.gif
http://i.imgur.com/OYIBIfc.gif
http://i.imgur.com/nff4X48.gif
	"""
    sexyguys = """http://i.imgur.com/CzMHq.gif
http://i.imgur.com/RvnHuqZ.gif
http://i.imgur.com/ZH8KfJE.gif
http://i.imgur.com/0rcDucX.gif
http://i.imgur.com/ADUZI9L.gif
http://i.imgur.com/LB3BAST.gif
http://i.imgur.com/Fl86jNY.gif
http://i.imgur.com/vT5EwHU.gif
http://i.imgur.com/IDTwSag.gif
http://i.imgur.com/L2IAw2k.gif
http://i.imgur.com/KBpPRzI.gif
http://i.imgur.com/6nVpdXc.gif
http://i.imgur.com/u2h1Ubs.gif
http://i.imgur.com/0TSq0sK.gif
http://i.imgur.com/jBRZk8x.gif
http://i.imgur.com/8qpberS.gif
http://i.imgur.com/6e2W9Ur.gif
http://i.imgur.com/d6bA51t.gif
http://i.imgur.com/X0xoFPj.gif
http://i.imgur.com/gT6DgSO.gif
http://i.imgur.com/BjKiZJo.gif
http://i.imgur.com/tlqeLLx.gif
http://i.imgur.com/5yDz098.gif
	"""
	
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
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""ICHC Room  ---> """) +  "http://www.icanhazchat.com/nerdcraft", prefixNick=True)
        if msg.args[0] == "#tamods":
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
        irc.reply("""If you are interested in other social rooms on Freenode, check out #r.trees #reddit-mlp (/r/mylittlepony) #reddit-depression #reddit-twoxchromosomes #teaandcrumpets (general UK chat) #introverts #defocus (general chat) ##socialites (general social room) #okchat (/r/okcupid) ##loseit #r4r #r4r30plus #togetheralone #makenewfriendshere and #gaygeeks""", prefixNick=True)
    rooms = wrap(rooms)
    
    def mods(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, voidboi, and actualgirl.""", prefixNick=True)
    	if msg.args[0] == "#ta-support":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, voidboi, and actualgirl.""", prefixNick=True)
    	if msg.args[0] == "#ta-lounge":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, voidboi, and actualgirl.""", prefixNick=True)
        if msg.args[0] == "#tamods":
        	irc.reply("""The #togetheralone mods are Alpha`/orion`, PoohBear, kittenhands, Stereo`, Ray`, ptard, friday, Madsy, danilo_d, Elderthedog, citra, fahquar, kinematic1, remedy, Zekk, CeruleanSky, BurritoEclair, Rahas, Ham, voidboi, and actualgirl.""", prefixNick=True)
        else:
			return
    mods = wrap(mods)
    
    def gaybar(self, irc, msg, args):
        irc.reply("""http://youtu.be/HTN6Du3MCgI""", prefixNick=True)
    gaybar = wrap(gaybar)
    
    def pics(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/14yv6n/new_picture_thread/""")
        if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/14yv6n/new_picture_thread/""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/14yv6n/new_picture_thread/""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Picture thread for /r/togetheralone: """) + """http://www.reddit.com/r/togetheralone/comments/14yv6n/new_picture_thread/""")
        else:
			return
    pics = wrap(pics)
    
    def bdaylist(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Birthday list for /r/togetheralone: """) + """http://goo.gl/qZ6lx""")
        else:
			return
    bdaylist = wrap(bdaylist)
    
    def bdayform(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
    	if msg.args[0] == "#ta-support":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
    	if msg.args[0] == "#ta-lounge":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
        if msg.args[0] == "#tamods":
        	irc.reply(ircutils.bold("""Birthday form for /r/togetheralone: """) + """http://goo.gl/L31rf""")
        else:
			return
    bdayform = wrap(bdayform)
    
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
    
    def womp(self, irc, msg, args):
    	irc.reply("http://youtu.be/yJxCdh1Ps48", prefixNick=True)
    womp = wrap(womp)
    
    def nph(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/hSU3tmQ.jpg",prefixNick=True)  
    nph = wrap(nph)  
    def hangout(self, irc, msg, args, victim):
        if msg.args[0] == "#togetheralone":
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
    	if msg.args[0] == "#ta-support":
    		text1 = "COME JOIN!!! ---> "
	#        colors = utils.iter.cycle([4, 7, 8, 3, 2, 12, 6])
	#        L = [self._color(c, fg=colors.next()) for c in text1]
	#        text2 = ''.join(L) + '\x03'
        	text1 = ircutils.bold(ircutils.mircColor(text1,'9', '2'))
        	text2 = text1 + """http://goo.gl/oms8X"""
        	if not victim:
        		irc.reply(text2, prefixNick=True)
        	else:
        		irc.reply(format('%s: %s ', victim, text2),prefixNick=False)
    	if msg.args[0] == "#ta-lounge":
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
        if msg.args[0] == "#tamods":
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
    	else:
    		return
    hangout = wrap(hangout, [additional('text')])
        
    def rules(self, irc, msg, args):
    	if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#ta-support":
            irc.reply(ircutils.bold("""Rules for #togetheralone: """) + """http://rules.together-alone.org""")
        if msg.args[0] == "#ta-lounge":
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
        if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	if msg.args[0] == "#ta-support":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	if msg.args[0] == "#ta-lounge":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
        if msg.args[0] == "#tamods":
    		irc.reply(ircutils.bold("""Public banlist for #togetheralone: """) + "http://goo.gl/WZAby")
    	else:
    		return
    banlist = wrap(banlist)
    
    def map(self, irc, msg, args):
        if msg.args[0] == "#togetheralone":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	if msg.args[0] == "#ta-support":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	if msg.args[0] == "#ta-lounge":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
        if msg.args[0] == "#tamods":
    		irc.reply(ircutils.bold("""Map for /r/togetheralone: """) + "https://www.zeemaps.com/map?group=489050#")
    	else:
    		return
    map = wrap(map)
    
    def butts(self, irc, msg, args):
        if msg.args[0] == "#ta-lounge":
    		plist = [x for x in TA.sexybutts.split("\n") if len(x.strip())]
    	else:
    		plist = [x for x in TA.wordbutts.split("\n") if len(x.strip())]
    	p = choice(plist)
    	irc.reply(p.strip(), prefixNick=True)
    butts = wrap(butts)
    
    def guys(self, irc, msg, args):
        if msg.args[0] == "#ta-lounge":
    		plist = [x for x in TA.sexyguys.split("\n") if len(x.strip())]
    		p = choice(plist)
    		irc.reply(p.strip(), prefixNick=True)
    	else:
    		irc.reply("That command is too sexy for this room. Come on over to #ta-lounge and try it there.", prefixNick=True)
    guys = wrap(guys)
    
    def simpsons(self, irc, msg, args):
    	irc.reply("http://www.justin.tv/arconai_214", prefixNick=True)
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
    
    def peen(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/iYehgzT.gif", prefixNick=True)
    peen = wrap(peen)
    
    def taco(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/xupXop2.gif", prefixNick=True)
    taco = wrap(taco)
    
    def dituni(self, irc, msg, args):
    	irc.reply("http://i.imgur.com/ywToWF0.png", prefixNick=True)
    dituni = wrap(dituni)

    def dance(self,irc,msg,args):
        right = ircutils.mircColor("(>", '13') + "'.'" + ircutils.mircColor(")>", '13')
        left = ircutils.mircColor("<(", '13') + "'.'" + ircutils.mircColor("<)", '13')
        up = ircutils.mircColor("^(", '13') + " '.' " + ircutils.mircColor(")^", '13')
        down = ircutils.mircColor("v(", '13') + " '.' " + ircutils.mircColor(")v", '13')
        
        irc.reply(right,prefixNick=False)
        irc.reply(up,prefixNick=False)
        irc.reply(left,prefixNick=False)
        irc.reply(down,prefixNick=False)
    dance = wrap(dance)

    def no(self, irc, msg, args, victim):
    	lod = """ಠ_ಠ"""
    	if victim is None:
    		return None
        irc.reply(format('%s: %s', victim, lod))
    no = wrap(no,[additional('text')])
    
    def kanye(self, irc, msg, args, words):
        """[<nick(optional)/person/(is|was|had|has)/thing(plural)>]
        
        Turns a group of words into a quote from Kanye West. Example: "kanye Derpy/Carl Sagan/is/atheists" will return 
        "Yo Derpy. I'm really happy for you, and I'm gonna let you finish, but Carl Sagan is one of the best atheists OF ALL TIME." 
        If no nick is specified, the caller's nick is used instead.
        """
        wordlist = words.split('/')
        if len(wordlist) == 3:
        	irc.reply(format("""Yo %s, I'm really happy for you, and I'm gonna let you finish, but %s %s one of the best %s OF ALL TIME.""", msg.nick, wordlist[0], wordlist[1], wordlist[2]))
        elif len(wordlist) == 4:
        	irc.reply(format("""Yo %s, I'm really happy for you, I'mma let you finish, but %s %s one of the best %s OF ALL TIME.""", wordlist[0], wordlist[1], wordlist[2], wordlist[3]))
        else:
        	return None
    kanye = wrap(kanye,[('text')])
Class = TA

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
