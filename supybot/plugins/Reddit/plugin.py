###
# Copyright (c) 2012, Chris Dusovic
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
import requests
import json


class Reddit(callbacks.Plugin):
    """Add the help for "@plugin help Reddit" here
    This should describe *how* to use this plugin."""
    pass
    
    def __init__(self, irc):
        self.__parent = super(Reddit, self)
        self.__parent.__init__(irc)
        self.sessions = {}
        self.headers = {'user-agent': '/r/progcollab IRC Reddit Plugin(supybot)'}
    def login(self, irc, msg, args):
        """
        login <user> <pass>
        Logs you in (PM only)
        """
        if msg.args[0][0] == '#':
            irc.reply("This command is PM only!")
        else:
            self.sessions[msg.user] = requests.session()
            logininfo = {'user': args[0], 'passwd': args[1], 'api_type': 'json'}
            r = self.sessions[msg.user].post(r'http://www.reddit.com/api/login', data=logininfo, headers=self.headers)
            j = json.loads(r.text)
            self.sessions[msg.user].modhash = j['json']['data']['modhash']
            irc.reply("Logged in!")
    def logout(self, irc, msg, args):
        """
        logout
        Logs you out.
        """
        self.sessions.pop(msg.user)
        irc.reply("Logged out!")
    def post(self, irc, msg, args):
        """
        post <link | self> <subreddit> <title> <content>
        Posts to a subreddit. (Use double quotes for multiple words)
        """
        if args[0] == 'link':
            type = 'url'
        if args[0] == 'self':
            type = 'text'
        postinfo = {'uh': self.sessions[msg.user].modhash, 'kind': args[0], 'sr': args[1], 'r': args[1], 'title': args[2], type: args[3]}
        post = self.sessions[msg.user].post('http://www.reddit.com/api/submit', postinfo, headers=self.headers)
        l = json.loads(post.text)

        #ugly code is ugly
        if (args[0] == 'self'):
            if ("http://www.reddit.com/r/"+args[1] in post.text):
                irc.reply(l['jquery'][10][3][0])
            elif(".error.USER_REQUIRED" in post.text):
                irc.reply("You need to log in by doing \"login username password\" by PM to the bot.")    
            elif(".error.RATELIMIT.field-ratelimit" in post.text):
                irc.reply(l['jquery'][14][3][0])
            elif(".error.QUOTA_FILLED" in post.text):
                irc.reply("Looks like you're either a brand new user or your posts have not been doing well recently. You may have to wait a bit to post again.")
            elif(".error.BAD_CAPTCHA.field-captcha" in post.text):
                irc.reply("Your post could not be posted due to reddit requiring a CAPTCHA.")
            elif(".error.ALREADY_SUB.field-url" in post.text):
                irc.reply("This post was already posted to the subreddit, it might be stuck in the spam filter. Message the subreddit mods to find out more.")
            else:
                irc.reply("Uncaught error: " + post.text)
        else: #link post
            if ("http://www.reddit.com/r/"+args[1] in post.text):
                irc.reply("Comments page: " + l['jquery'][16][3][0]) # + " Points to: " + l['jquery'][12][4][1]) out of range, cant figure it out.
            elif(".error.USER_REQUIRED" in post.text):
                irc.reply("You need to log in by doing \".login username password\" by PM to the bot.")    
            elif(".error.RATELIMIT.field-ratelimit" in post.text):
                irc.reply(l['jquery'][20][3][0])#this one might not work sometimes
            elif(".error.QUOTA_FILLED" in post.text):
                irc.reply("Looks like you're either a brand new user or your posts have not been doing well recently. You may have to wait a bit to post again.")
            elif(".error.BAD_CAPTCHA.field-captcha" in post.text):
                irc.reply("Your post could not be posted due to reddit requiring a CAPTCHA.")
            elif(".error.ALREADY_SUB.field-url" in post.text):
                irc.reply("This post was already posted to the subreddit, it might be stuck in the spam filter. Message the subreddit mods to find out more.")
            else:
                irc.reply("Uncaught error: " + post.text)
            # errors to add: 
                
        
Class = Reddit


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
