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


class Chathelp(callbacks.Plugin):
    def chathelp(self, irc, msg, args):
            chathelp0 = """Hello, and welcome to the IRC room for http://www.reddit.com/r/togetheralone! We try to be a positive, welcoming, and inclusive community for people looking to make friends, so feel free to make yourself at home. :D""" 
            chathelp1 = """PLEASE READ: If you are feeling seriously depressed, you should visit http://www.crisischat.org/chat/, or http://carecrisischat.org/chat_now.php, where people will be ready to comfort you and help you get through it. If you are feeling suicidal, PLEASE call 1-800-273-8255 (or your local suicide hotline outside of the US), or visit http://suicidepreventionlifeline.org/GetHelp/LifelineChat.aspx immediately."""
            chathelp2 = """General Rules: 1. Don't be an asshole. This goes for sexist generalizations, racist and homophobic slurs/remarks, ad hominems, being obnoxious, etc. In general, respect people's boundaries and be civil. If you feel that someone is being rude to you, please speak up and/or notify a mod as soon as possible."""
            chathelp3 = """2. If someone finds your humor or choice of topic offensive, please respect that. If you are being an asshat and getting on other people's nerves, you are a cancer on the chatroom, and will be dealt accordingly. As with Rule 1, if you find a particular topic offensive, don't hesitate to speak up and/or notify a moderator."""
            chathelp4 = """3. On IRC, please take people's age into consideration. Not everyone is 18+."""
            chathelp5 = """4. For links containing gore/nudity, please tag them NSFW when they are posted."""
            chathelp6 = """5. For regular violations of the rules, warn/kick/ban will typically be enforced. Blatant trolling, extreme creepy behavior, or making serious personal threats will typically be met with an immediate ban. However, since not every situation is the same, OPs reserve the right to warn/kick/ban as they see fit."""
            chathelp7 = """6. Nothing said in here is private. However, don't post people's personal information without their consent (i.e., real names, Facebook profiles, etc.) This also includes scraping information from the chat and/or posting personal information from the chat publicly on the internet."""
            chathelp8 = """7. If you are a chat regular, try to be friendly and welcoming to new people who are coming in. Also, if someone comes to the chat to discuss something serious, please don't blow them off, spam the bots, or make insensitive comments. We were all new at some point, and it can often be hard for newcomers to fit in with the group at first, so please take that into consideration. :-)"""
            chathelp9 = """Instakick rules: 8. DON'T SPAM THE BOTS! The bots exist to add to the chat, not to clog it up and prevent conversation from happening. Please take this into consideration, and don't abuse the bots to the point where it becomes an irritation for others. Also, if you want to play around with a bot's functions, you can always send commands to the bot through PM."""
            chathelp10 = """9. Making sleazy comments towards people in the chat room, such as "I can help with that", asking for pics, highlighting the prescence or absence of women in the chatroom, arguing about the definition of "forever alone". It's obnoxious, and if you are regularly acting like this, then you probably deserve to be alone. Harmless joking is fine, of course, but use common sense. Example: http://xkcd.com/322/"""
            chathelp11 = """Instaban rules: 10. Random PMs hitting on people ("A/S/L", etc.), or creepy PMs will not be tolerated. If you want to PM someone, please make sure they are comfortable with that first. If you are receiving unwanted PMs like those described, please let a mod know immediately."""
            chathelp12 = """11. Due to several past incidents, promoting PUA (Pick Up Artist) and/or /r/seduction material is strictly forbidden and will be dealt with harshly."""
            chathelp13 = """ 12. Blatant spamming/trolling. If you are coming into the chat under a different nick to troll, then every other nick you try to use will be banned as well."""
            chathelp14 = """Bots: The channel bot is PoohBot. For a list of plugins, type .list. For a list of commands within a plugin, type .list <plugin>. Please keep in mind the that PoohBot has a throttle, and too many commands in a row might lead to PoohBot ignoring you."""
            chathelp15 = """Issues: If you have any issues with people in chat or anything at all you want to talk about feel free to message any one of the mods who are in the room. They are: absw/orion, PoohBear, kittenhands, Stereo, Ray, ptard, friday, madsy, danilo_d, Elderthedog, wolfc86, citra, FlagranteDelicto, summerinthecity, fahquar, and kinematic1."""

            irc.reply(chathelp0, msg.nick, private=True, notice=True)
            irc.reply(chathelp1, msg.nick, private=True, notice=True)
            irc.reply(chathelp2, msg.nick, private=True, notice=True)
            irc.reply(chathelp3, msg.nick, private=True, notice=True)
            irc.reply(chathelp4, msg.nick, private=True, notice=True)
            irc.reply(chathelp5, msg.nick, private=True, notice=True)
            irc.reply(chathelp6, msg.nick, private=True, notice=True)
            irc.reply(chathelp7, msg.nick, private=True, notice=True)
            irc.reply(chathelp8, msg.nick, private=True, notice=True)
            irc.reply(chathelp9, msg.nick, private=True, notice=True)
            irc.reply(chathelp10, msg.nick, private=True, notice=True)
            irc.reply(chathelp11, msg.nick, private=True, notice=True)
            irc.reply(chathelp12, msg.nick, private=True, notice=True)
            irc.reply(chathelp13, msg.nick, private=True, notice=True)
            irc.reply(chathelp14, msg.nick, private=True, notice=True)
            irc.reply(chathelp15, msg.nick, private=True, notice=True)
    chathelp = wrap(chathelp)
    threaded = True

Class = Chathelp


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
