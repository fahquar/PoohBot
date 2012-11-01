###
# Copyright (c) 2011, Valentin Lorentz
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

import random

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
#from supybot.i18n import PluginInternationalization, internationalizeDocstring
#
#_ = PluginInternationalization('Wish')

def unserialize(string):
    list = string.replace('||', '|').split(' | ')
    if '' in list:
        list.remove('')
    return list

def serialize(list):
    if '' in list:
        list.remove('')
    return ' | '.join([x.replace('|', '||') for x in list])

#@internationalizeDocstring
class Wish(callbacks.Plugin):
    """Add the help for "@plugin help Wish" here
    This should describe *how* to use this plugin."""

#    @internationalizeDocstring
    def wish(self, irc, msg, args, channel, thing):
        """[<channel>] <thing>

        Tell the bot you want the <thing>. <channel> is only needed if you
        don't send the message on the channel itself."""
        wishlist = unserialize(self.registryValue('wishlist', channel))
        if thing in wishlist:
            irc.error('This thing is already wanted.')
            return
        wishlist.append(thing)
        self.setRegistryValue('wishlist', serialize(wishlist), channel)
        irc.replySuccess()
    wish = wrap(wish, ['channel', 'something'])

#    @internationalizeDocstring
    def list(self, irc, msg, args, channel):
        """[<channel>]

        Returns the list of wanted things for the <channel>. <channel> defaults
        to the current channel."""
        wishlist = unserialize(self.registryValue('wishlist', channel))
        if list(wishlist) == 0:
            irc.error('No wish for the moment.')
            return
        indexes = range(1, len(wishlist) + 1)
        wishlist_with_index = zip(indexes, wishlist)
        formatted_wishlist = ['#%i: %s' % x for x in wishlist_with_index]
        irc.reply(utils.str.format('%L', formatted_wishlist))
    list = wrap(list, ['channel'])

#    @internationalizeDocstring
    def get(self, irc, msg, args, channel, id):
        """[<channel>] <id>

        Tell you the thing number <id>. <channel> is only needed if you
        don't send the message on the channel itself."""
        wishlist = unserialize(self.registryValue('wishlist', channel))
        if len(wishlist) < id:
            irc.error('No thing has this id.')
            return
        irc.reply('Wish #%i is %s.' % (id, wishlist[id - 1]))
    get = wrap(get, ['channel', 'id'])

#    @internationalizeDocstring
    def random(self, irc, msg, args, channel):
        """[<channel>]

        Tell you a random thing. <channel> is only needed if you
        don't send the message on the channel itself."""
        wishlist = unserialize(self.registryValue('wishlist', channel))
        if list(wishlist) == 0:
            irc.error('No wish for the moment.')
            return
        indexes = range(1, len(wishlist) + 1)
        wishlist_with_index = zip(indexes, wishlist)
        wishes = random.sample(wishlist_with_index, 1)[0]
        irc.reply('Wish #%i is %s.' % wishes)
    random = wrap(random, ['channel'])


Class = Wish


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
