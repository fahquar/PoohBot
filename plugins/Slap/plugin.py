###
# Copyright (c) 2005, Kyle McFarland
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

import supybot

import string, random

import supybot.conf as conf
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.ircmsgs as ircmsgs
import supybot.registry as registry
import supybot.callbacks as callbacks


class Slap(callbacks.Plugin):
    """Add the help for "@plugin help Slap" here
    This should describe *how* to use this plugin."""
    def slap(self, irc, msg, args, channel, victim, number):
        """[<channel>] [<nick>] [<times>]

        Act optionally directed at a random string, person,
        object, etc.
        <times> can be used to slap more than one times
        """
        MaxSlaps = self.registryValue("MaxSlaps")
        #self.log.debug("slap: "+channel)
        if not victim: # no victim given
            victim = msg.nick
        if not channel: # no channel given
            channel = msg.args[0]
            if irc.nick == channel: #private chat
                channel = msg.nick
        if not number:
            number = 1
        if number > MaxSlaps:
            if MaxSlaps != 0:
                number = MaxSlaps
        for i in range(number):
            text = string.replace(self._buildSlap(), "$nick", victim)
            irc.queueMsg(ircmsgs.action(channel, text))
    slap = wrap(slap, [optional('channel'), optional('nick'), optional('int')])

    def _buildSlap(self):
        """
        slaps are formed: "slaps $nick around with a <adjectives> <noun>"
        """
        self.log.debug('slap choosing from %i nouns and %i adjectives ...' %
                (len(self.nouns), len(self.adjectives)))
        rnd = 0
        adj_pool = []
        adj_prob = self.registryValue('adjectiveProbability')
        while rnd < adj_prob:
            rnd = random.random()
            adj_pool += [random.choice(self.adjectives)]
        adj = ', '.join(adj_pool)
        is_exception = False
        if adj == "used":
            is_exception = True
        noun = random.choice(self.nouns)
        if not adj[0] in 'aeiou':
            an = 'a'
        else:
            if is_exception == True:
                an = 'a'
            else:
                an = 'an'
        if random.random() < adj_prob:
            an = 'the'
        if random.random() < 0.93:
            around = 'around'
        else:
            around = ''
        return 'slaps $nick %s with %s %s %s' % (
            around, an, adj, noun)
    nouns = ['space ship','Orlando Bloom','pi','apple pie',
        'rad scorpion','rock band','metal band','Lord of the Rings',
        'One','board','tv','floppy 5.25"','dschinn','dice','shadowrunner',
        'gmail account','ebay auction','root account','joke','w6','w20','w4',
        'undead','orang utan','Wolverine','Cpt. Picard','USS Enterprise',
        'super sheep','worm','Gimp','sidekick','statue','statue of liberty',
        'chat log','bot','staff','shotgun','rocket launcher','globus','w100',
        'coffee cup','flip chart','cow','fret','comic book','laptop',
        'bash script','daemon','BSD Devil','quiz','pirate','notebook','w10',
        'towel','fish','salmon','herring','foot','tea pot','toilet','w3','w8',
        'stunt actor','skeleton','dummy','Mr Johnson','counter','w12',
        'robot','C64','copyright','EULA','licence key','crack',
        'kombo','trailer','anime','Nemo','country singer','psychiatrist',
        'author','wardrobe','red bull(tm) energy drink','linux distribution',
        'role playing game','shisha','tomahawk','missile','councelor',
        'IE Version 5.5','registration form','Windows CD','sheep','pet',
        'Encyclopaedia Britannica','shelf of books','cover girl',
        'walrus','python script','PRIVMSG','thermonuclear weapon',
        'Nessie - the Loch Ness monster','hitch hikers guide to the galaxy',
        'Schnappi (a crocodile)','clown fish','goblin','fairy',
        'tuna (Still in the can)','dragon','pillow','hobgoblin',
        'gremlin','golem','CD RW','mouse pad','character','wiki',
        'gauntlet','plasma gun','rail gun','lighting gun','BFG',
        'flak cannon','redeemer','sword of haste','bastard sword +3',
        'dagger +6','sword of speed','axe of the heavens',
        'sword +2','iPod','mac mini','Neuros','BMW Z4',
        'wizard of the coast','decker','exile','bug','alien',
        'smoke ring','thesis','glimps of his eye','snap of his finger',
        'movie','DVD','magazine','laser cannon','pac man','Lara Craft',
        'IP address','werewolf','news paper','asteroid','powerbook',
        'wand of the elements','door','magnetic field','strength',
        'misery','space marine','zergling','zealot','magician',
        'journal','cookie','machine','super hero','orc','trading card',
        'elven','finger','smile','rune','symbol','spell','VISA card',
        'Steve Jobs','stone','dictionary','CVS','channel operator',
        'coconut','perl one liner','DnD source book','brain',
        'scroll of wisdom','scroll of identify','magic missile',
        'tooth fairy','elephant','Tux','ninja','kungfu master',
        'Frostmourne','Doombringer','discipline','endurance',
        'rogue','fighter/wizard/thief','powergamer','munchkin',
        'Merlin','donkey','Tie Fighter','X-Wing','Y-Wing',
        'Millenium Falcon','light saber','stick','Jedi Knight',
        'tissue','flower','half-orc','troll','slashdotter',
        'monkey king','usurpator','prince','trolley',
        'assassin','scroll of town portal','bit','video game',
        'sword','Amulet of Yendor','Silmarillion','console',
        'script', 'hammer','fork','carrot','smile','power','cheque',
        'tricorder','Scotty','Harry','kamikaze pilot','agent',
        'Keanu Reeves','network card','USB stick','hat','pipe',
        'file system','piano','jet','perl','penguin','whistle',
        'core dump','rfc','bottle','avatar','barkeeper','horn',
        'Albus Dumbledore','Nazghul','ring','wand of fire',
        'wand of blindness','wand of death','wand of destruction',
        'club (with a nail in it)','Queen of England','taxi','monitor',
        'marshmallow','girl scout','book by Stephen King','fist']
    adjectives = ['large','small','foul','steam-powered','empty',
        'stinkin','wild','rotten','big','huge','tiny','red',
        'iron','glowin','rolling','random','well known','open sourced',
        'fleeing','flying','book reading','gigantic','invisible',
        'hitch hiking','spiky','heavy','rusty','haunted',
        'chinese','fluffy','sweet','cushioned','used','summoned',
        'magic','trusted','fuzzy','unnatural','sharp',
        'chaotic, good','chaotic, evil','awesome',
        'surreal','alien','shipped','serialized','unnoticed',
        'dark','polished','dead','emerald','shiny','new','old',
        'nifty','talking','burning','frozen','mechanic',
        'gas-powered','golden','silver','spicy','unholy',
        'mindless','boring','lost','ancient','unworthy',
        'precious','expensive','eerie','damaged','rugged',
        'xenophobic','feared','casted','cursed',
        'uncursed','blessed','speaking','chatting','idling',
        'teeny-weeny','romantic','undead','blinking','built',
        'resurrected','german','american','english',
        'ascended','dumb','dull','russian','korean','nick named',
        'bug-free','buggy','symbolic','real','unrealistic',
        'unreal','twisted','returning','remote controlled',
        'evil','dangerous','armoured','bad','good','enourmous',
        'murderous','vicious','mysterous','forgotten','found',
        'semi-functional','non-functional','fatal','self-made',
        'morbid','crying','powerful','stolen','hidden',
        'blue','yellow','pink','white','black','green','painted',
        'colorful','holy','meaningful','monstrous',
        'virtual','private','public','smellin','vile']


Class = Slap


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
