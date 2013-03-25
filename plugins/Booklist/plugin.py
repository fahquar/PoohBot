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


class Booklist(callbacks.Plugin):
    def booklist(self, irc, msg, args):
            headline = ircutils.bold('Recommended Reading List or #togetheralone: ')
            headline = ircutils.bold(headline)
            book1 = ircutils.bold('How to Win Friends and Influence People, by Dale Carnegie:') + """ https://dl.dropbox.com/u/21084567/How_to_Win_Friends_and_Influence_People.pdf"""
            book2 = ircutils.bold('The Six Pillars of Self-Esteem, by Dr. Nathaniel Branden:') + """ https://dl.dropbox.com/u/21084567/The_Six_Pillars_of_Self-Esteem.pdf"""
            book3 = ircutils.bold('Feeling Good - The New Mood Therapy, by David D. Burns:') + """ https://dl.dropbox.com/u/21084567/Feeling_Good_The_New_Mood_Therapy.pdf"""
            book4 = ircutils.bold('Get Anyone to do Anything, by David J. Lieberman:') + """ https://dl.dropbox.com/u/21084567/Get_Anyone_to_do_Anything.pdf"""
            irc.reply(headline, private=True, notice=True)
            irc.reply(book1, private=True, notice=True)
            irc.reply(book2, private=True, notice=True)
            irc.reply(book3, private=True, notice=True)
            irc.reply(book4, private=True, notice=True)
    booklist = wrap(booklist)

    threaded = True

Class = Booklist


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
