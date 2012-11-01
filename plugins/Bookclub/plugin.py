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


class Bookclub(callbacks.Plugin):
    def booklist(self, irc, msg, args):
            book = ircutils.bold('The Picture of Dorian Gray: ')
            ebook = 'Ebook Download' + """: http://www.gutenberg.org/ebooks/4078"""
            audiobook = 'Audiobook Download' + """: http://freeclassicaudiobooks.com/audiobooks/Dorian/mp3/"""
            irc.reply('The ##bookclub book for this month is ' + book + 'http://en.wikipedia.org/wiki/The_Picture_of_Dorian_Gray', msg.nick, private=True, notice=True)
            irc.reply('GoodReads Discussion Group: http://www.goodreads.com/group/show/75673-snoonet-bookclub', msg.nick, private=True, notice=True)
            irc.reply(ebook, msg.nick, private=True, notice=True)
            irc.reply('Uncensored Edition Download: http://goo.gl/iPLLT', msg.nick, private=True, notice=True)
            irc.reply(audiobook, msg.nick, private=True, notice=True)
    booklist = wrap(booklist)

    threaded = True

Class = Bookclub


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
