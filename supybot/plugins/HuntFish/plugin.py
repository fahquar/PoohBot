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

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import supybot.conf as conf
import random as random
import re
import time
import string

class HuntFish(callbacks.Plugin):
    """Adds hunt and fish commands for a basic hunting and fishing game."""
    threaded = True

    def hunt(self,irc,msg,args):
        """
        performs a random hunt
        """
        if(self.registryValue('enable', msg.args[0])):
            animals = [' bear', ' gopher', ' rabbit', ' hunter', ' deer', ' fox', ' duck', ' moose', ' pokemon named Pikachu', ' park ranger', ' Yogi Bear', ' Boo Boo Bear', ' dog named Benji', ' cow', ' raccoon', ' koala bear', ' camper', ' channel lamer', ' your mom']
            places = ['in some bushes', 'in a hunting blind', 'in a hole', 'up in a tree', 'in a hiding place', 'out in the open', 'in the middle of a field', 'downtown', 'on a street corner', 'at the local mall']

            with open(conf.supybot.directories.data.dirize('hunttrophy.txt'), 'r') as file:
                data = file.readlines()
                highScore = data[2].rstrip('\n')
            currentWhat = random.choice(animals)
            currentWhere = random.choice(places)
            weight = random.randint(int(highScore)/2,int(highScore)+10)
            weightType = self.registryValue('weightType')
            nick = ircutils.bold(msg.nick)
            thisHunt = (msg.nick + " goes hunting " + currentWhere + " for a " + str(weight) + weightType +  currentWhat + ".")
            irc.reply(thisHunt, private=True)
            irc.reply("Aims....", private=True)
            irc.reply("Fires.....", private=True)
            time.sleep(7)#pauses the output between line 1 and 2 for 5 seconds
            huntChance = random.randint(1,100)
            successRate = self.registryValue('SuccessRate')

            if huntChance < successRate:
                win = ("Way to go, " + msg.nick + "! You killed the " + str(weight) + weightType + currentWhat + ". :)")
                irc.reply(win, private=True)
                with open(conf.supybot.directories.data.dirize('hunttrophy.txt'), 'r') as file:
                    data = file.readlines()
                    bigHunt = data[2].rstrip('\n')
                    if weight > int(bigHunt):
                        with open(conf.supybot.directories.data.dirize('hunttrophy.txt'), 'w') as file:
                            data[0] = msg.nick
                            data[1] = currentWhat 
                            data[2] = weight
                            file.writelines(str(data[0]))
                            file.writelines('\n')
                            file.writelines(str(data[1]))
                            file.writelines('\n')
                            file.writelines(str(data[2]))
                            irc.reply("You got a new highscore!", private=True)


            else:
                lose = ("Oops, you missed, " + msg.nick + ". :(")
                irc.reply(lose, private=True)


    def fish(self,irc,msg,args):
        """
        performs a random fishing trip
        """
        if(self.registryValue('enable', msg.args[0])):
            fishes = (' salmon', ' herring', ' yellowfin tuna', ' pink salmon', ' chub', ' barbel', ' perch', ' northern pike', ' brown trout', ' arctic char', ' roach', ' brayling', ' bleak', ' cat fish', ' sun fish', ' old tire', ' rusty tin can', ' genie lamp', ' love message in a bottle', ' old log', ' rubber boot' , ' dead body', ' Loch Ness Monster', ' old fishing lure', ' piece of the Titanic', ' chunk of Atlantis', ' squid', ' whale', ' dolphin',  ' porpoise' , ' stingray', ' submarine', ' seal', ' seahorse', ' jellyfish', ' starfish', ' electric eel', ' great white shark', ' scuba diver' , ' lag monster', ' virus', ' soggy pack of smokes', ' bag of weed', ' boat anchor', ' pair of floaties', ' mermaid', ' merman', ' halibut', ' tiddler', ' sock', ' trout', ' piece of poop', ' aborted fetus', ' discarded foreskin', ' used condom', ' severed head', " piece of Jimmy Hoffa's corpse")
            fishSpots = ('a stream', 'a lake', 'a river', 'a pond', 'an ocean', 'a bathtub', 'a kiddies swimming pool', 'a toilet', 'a pile of vomit', 'a pool of urine', 'a kitchen sink', 'a bathroom sink', 'a mud puddle', 'a pail of water', 'a bowl of Jell-O', 'a wash basin', 'a rain barrel', 'an aquarium', 'a snowbank', 'a waterfall', 'a cup of coffee', 'a glass of milk', ' a uterus')

            with open(conf.supybot.directories.data.dirize('fishtrophy.txt'), 'r') as file:
                data = file.readlines()
                highScore = data[2].rstrip('\n')
            currentWhat = random.choice(fishes)
            currentWhere = random.choice(fishSpots)
            weight = random.randint(int(highScore)/2,int(highScore)+10)
            weightType = self.registryValue('weightType')
            nick = ircutils.bold(msg.nick)
            thisFishing = (nick + " goes fishing in " + currentWhere + ".")
            irc.reply(thisFishing, private=True)
            irc.reply("Casts in....", private=True)
            irc.reply("A " + str(weight) + weightType + currentWhat + " is biting...", private=True)
            time.sleep(7)#pauses the output between line 1 and 2 for 5 seconds
            huntChance = random.randint(1,100)
            successRate = self.registryValue('SuccessRate')

            if huntChance < successRate:
                win = ("Way to go, " + msg.nick + "! You caught the " + str(weight) + weightType + currentWhat + ". :)")
                irc.reply(win, private=True)
                with open(conf.supybot.directories.data.dirize('fishtrophy.txt'), 'r') as file:
                    data = file.readlines()
                    bigFish = data[2].rstrip('\n')
                    if weight > int(bigFish):
                        with open(conf.supybot.directories.data.dirize('fishtrophy.txt'), 'w') as file:
                            data[0] = msg.nick
                            data[1] = currentWhat 
                            data[2] = weight
                            file.writelines(str(data[0]))
                            file.writelines('\n')
                            file.writelines(str(data[1]))
                            file.writelines('\n')
                            file.writelines(str(data[2]))
                            irc.reply("You got a new highscore!", private=True)


            else:
                lose = ("Oops, it got away, " + msg.nick + ". :(")
                irc.reply(lose, private=True)

    def trophy(self,irc,msg,args):
        """
        Checks the current highscores for hunting and fishing.
        """
        if(self.registryValue('enable', msg.args[0])):
            weightType = self.registryValue('weightType')
            with open(conf.supybot.directories.data.dirize('hunttrophy.txt'), 'r') as file1:
                data1 = file1.readlines()
                hunter = data1[0].rstrip('\n')
                hunted = data1[1].rstrip('\n')
                score = data1[2].rstrip('\n')
                irc.reply("Hunting hiscore held by: " + hunter + " with a " + score + weightType + hunted + ".")
            with open(conf.supybot.directories.data.dirize('fishtrophy.txt'), 'r') as file2:
                data2 = file2.readlines()
                fisherman = data2[0].rstrip('\n')
                catch = data2[1].rstrip('\n')
                size = data2[2].rstrip('\n')
                irc.reply("Fishing hiscore held by: " + fisherman + " with a " + size + weightType + catch + ".")



Class = HuntFish


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
