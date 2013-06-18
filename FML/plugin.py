###
# Copyright (c) 2012, Aha2Y
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
import urllib2
import lxml.html

def sortByTag(data):
    D = {}
    for entry in data:
        L = entry.split(':')
        key = L[0].lower()
        contents = L[1][1:]
        D[key] = contents
    return D
 
class Fml:
    def __init__(self):
        api = urllib2.urlopen("http://rscript.org/lookup.php?type=fml")
        data = lxml.html.parse(api)
        api.close()
       
        contents = data.xpath("//pre/text()")[0].split('\n')
        contents.sort()
        # lets remove the trash that will fuck the dict up
        del contents[0]
        del contents[0]
        contents.remove("START")
        contents.remove("END")
       
        data = sortByTag(contents)
       
        # lets sort it into something BEAUTIFUL :D
        self.id = data['id']
        self.cate = data['cate']
        self.text = data['text']
        self.agree = data['agree']
        self.deserved = data['deserved']
        self.comments = data['comments']
        
       

class FML(callbacks.Plugin):
    """Add the help for "@plugin help Fml" here
    This should describe *how* to use this plugin."""
    threaded = True

    def fml(self, irc, msg, args):
        if irc.nested: return
        fml = Fml()
        id = fml.id
        id = "#" + id
        id = ircutils.bold(ircutils.mircColor(id, '12'))
        cate = "["+fml.cate+"]"
        cate = ircutils.bold(ircutils.mircColor(cate, '14'))
        url = "http://www.fmylife.com/%s/%s" % (fml.cate, fml.id)
        comments = "("+fml.comments+")"
        comments = ircutils.mircColor(comments, '14')
        agree = "("+fml.agree+")"
        agree = ircutils.mircColor(agree, '14')
        deserved = "("+fml.deserved+")"
        deserved = ircutils.mircColor(deserved, '14')
        agree2 = ircutils.bold(ircutils.mircColor('agree', '12'))
        deserved2 = ircutils.bold(ircutils.mircColor('deserved', '12'))
        irc.reply(url)
        irc.reply("%s %s %s %s | %s %s - %s %s" % (cate, fml.text, id, comments, agree2, agree, deserved2, deserved), prefixNick=False)
    fml = wrap(fml)

Class = FML


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
