###
# Copyright (c) 2010, Christopher Slowe
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
import json as simplejson
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import re, os
from reddit import RedditSession
import urllib
from local import BeautifulSoup
import supybot.conf as conf
import time
import datetime
import supybot.ircmsgs as ircmsgs
import supybot.conf as conf

try:
    feedparser = utils.python.universalImport('feedparser', 'local.feedparser')
except ImportError:
    raise callbacks.Error, \
        'You need the feedparser module installed to use this plugin.  ' \
        'Download the module at <http://www.feedparser.org/>.'

simplejson = None

try:
    import json as simplejson
except ImportError:
    pass

try:
    # The 3rd party simplejson module was included in Python 2.6 and renamed to
    # json.  Unfortunately, this conflicts with the 3rd party json module.
    # Luckily, the 3rd party json module has a different interface so we test
    # to make sure we aren't using it.
    if simplejson is None or hasattr(simplejson, 'read'):
        simplejson = utils.python.universalImport('simplejson',
                                                  'local.simplejson')
except ImportError:
    raise callbacks.Error, \
        'You need Python2.6 or the simplejson module installed to use ' \
        'this plugin.  Download the module at ' \
        '<http://undefined.org/python/#simplejson>.'

reddit = RedditSession()

reddit_re = re.compile(r"(http://([^/]*\.)?reddit.com/\S+)")
redditsub_re = re.compile(r"(http://([^/]*\.)?reddit.com/(r/[^/]+/)?comments/(?P<id>[^/]+))")
reddituser_re = re.compile(r"(http://([^/]*\.)?reddit.com/user/(?P<username>[^/]+))")

def present_listing_first(res, original_link=False, color_score=False):
	try:
		d = res.get("data", {}).get("children", [{}])[0].get("data",{})
		if d:
			if not original_link:
				d["url"] = "http://www.reddit.com/r/%(subreddit)s/comments/%(id)s/" % d
            
			if color_score:
				score_part = "(%s|%s)[%s]" % (ircutils.bold(ircutils.mircColor("%(ups)s", "orange")),
                                              ircutils.bold(ircutils.mircColor("%(downs)s", "12")),
                                              ircutils.bold(ircutils.mircColor("%(num_comments)s", "dark grey")))
			else:
				score_part = "(%(score)s)"
			title_part = "%(title)s"
			url_part = ircutils.underline("%(url)s")
			nsfw_part = "NSFW"*d['over_18'] or ''
			nsfw_part =ircutils.bold(ircutils.mircColor(nsfw_part, 'red'))
			template = "%s %s %s %s" % (nsfw_part, score_part, title_part, url_part)
			template = (template % d)
			template = template.replace('\n', ' ')
			template = template.replace('&amp;','&')
		
			if d["created_utc"] < time.time() - 2678400:
				return False
			return template
			
    
	except IndexError:
		return None

def present_user(res):
    d = res.get("data")
    made_utc = d["created_utc"]
    age = int((time.time() - made_utc)/86400)
    name_part = d["name"]
    name_part = ircutils.bold(name_part)
    if d:
        return ("%s" % name_part + " has %(link_karma)s link karma, %(comment_karma)s comment karma," % d + " and has been a redditor for %s days." % age)

def _present_links(text, color=False):
    links = utils.web.urlRe.findall(text)
    for link in links:
        reddit_m = reddit_re.match(link)
        if reddit_m:
            user_m = reddituser_re.match(link)
            sub_m = redditsub_re.match(link)
            if user_m:
                res = reddit.API_GET("/user/%s/about.json" % urllib.quote(user_m.group("username")))
                yield present_user(res)
            
            elif sub_m:
                res = reddit.API_GET("/by_id/t3_%s.json" % urllib.quote(sub_m.group("id")))
                yield present_listing_first(res, original_link=True, color_score=color)
            
        else:
            res = reddit.API_GET("/api/info.json?limit=1&url=%s" % urllib.quote(link))
            yield present_listing_first(res, color_score=color)

def present_links(text, *args, **kwargs):
    return filter(None, _present_links(text, *args, **kwargs))

class RedditLinks(callbacks.Plugin):
    """Add the help for "@plugin help RedditLinks" here
    This should describe *how* to use this plugin."""
        
    def doPrivmsg(self, irc, msg):
        if ircmsgs.isCtcp(msg) and not ircmsgs.isAction(msg):
            return
        channel = msg.args[0]
        if callbacks.addressed(irc.nick, msg):
            return
        if self.registryValue('titleSnarfer', channel):
            if irc.isChannel(channel):
                if ircmsgs.isAction(msg):
                    text = ircmsgs.unAction(msg)
                else:
                    text = msg.args[1]
                for info in present_links(text, color=True):
                    irc.reply(info, prefixNick=False, private=False, notice=False)
                    
    def reddituser(self, irc, msg, args, username):
        """[<username>]

        Displays the reddit profile information of a given user.
        """
        res = reddit.API_GET("/user/%s/about.json" % username)
        userurl = "http://www.reddit.com/user/%s" % username
        userinfo = present_user(res)
        irc.reply(userinfo + " " + userurl, prefixNick=False, private=False, notice=False)
    reddituser = wrap(reddituser, ['text'])

Class = RedditLinks


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
