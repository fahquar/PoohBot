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
    
    def movie(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Streams: ") + "http://www.livestream.com/tafilms || http://www.livestream.com/chickenstewgaming", msg.nick, private=True, notice=True)
    movie = wrap(movie)
    
    def dexter(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Stream: ") + "http://misclivestream.blogspot.co.uk/p/dexter.html", msg.nick, private=True, notice=True)
    dexter = wrap(dexter)
    
    def minecraft(self, irc, msg, args):
        
        irc.reply(ircutils.bold("Server Info: ") + "http://bit.ly/Qihbt7")
    minecraft = wrap(minecraft)

    def camchat(self, irc, msg, args):
        
        irc.reply("GET IN HERE: http://www.icanhazchat.com/nerdcraft")
    camchat=wrap(camchat)

    def nerdcraft(self, irc, msg, args):
        
        irc.reply("GET IN HERE: http://www.icanhazchat.com/nerdcraft")
    nerdcraft = wrap(nerdcraft)
                  
    def zombies(self, irc, msg, args):
                  
        irc.reply("""Plants vs. Zombies! Free! Go to http://www.stopzombiemouth.com and enter the code PEAH8R. Valid from October 30 to November 10, 2012.""")
    zombies = wrap(zombies)
                  
    def tksync(self, irc, msg, args):
                  
        irc.reply("""Come join!: http://tksync.com/""")
    tksync = wrap(tksync)
                
Class = TA

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
