###
# Copyright (c) 2011, Mikael Emilsson
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

import urllib2
import re
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks

class UrbanDictionary(callbacks.Plugin):
    threaded = True
    def ud(self, irc, msg, args, text):
        """ - search for definitions on UrbanDictionary """
        user_agent = "Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.2.2) Gecko/20100316 Firefox/3.6.2 (.NET CLR 3.5.30729)"
        term = text
        term = term.replace(' ', '%20')
        url = "http://www.urbandictionary.com/define.php?term="+term
        irc.reply(url)
        req = urllib2.Request(url, None, { 'User-Agent' : user_agent})
        file = urllib2.urlopen(req)
        source = file.read()
        re_defines = re.compile(r'.*class="definition"\>(.*)\<\/div\>\<di')
        defines = re.findall(re_defines, source)
        defs = ""
        for lol in defines:
            lol = lol.replace('&quot;','"')
            lol = lol.replace('\r', ' ')
            lol = lol.replace('&lt;', '<')
            lol = lol.replace('&gt;', '>')
            lol = lol.replace('&amp;', '&')
            lol_list = list(lol)
            i = 0
            while i < len(lol_list):
                if lol_list[i] == '<':
                    while lol_list[i] != '>':
                        lol_list.pop(i)
                    lol_list.pop(i)
                else:
                    i=i+1
            defs = defs + "'" + ''.join(lol_list) + "' "
        if defs:
            irc.reply(ircutils.bold(text) + ': ' + defs)
        else:
            irc.reply("Tomt")
    ud = wrap(ud,['text'])
Class = UrbanDictionary


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
