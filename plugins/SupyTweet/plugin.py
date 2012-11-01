###
# Copyright (c) 2010, Kenji Eva
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

import re
import csv
import time
from oauthtwitter import OAuthApi

import supybot.utils as utils
from supybot.commands import *
import supybot.conf as conf
import supybot.ircdb as ircdb
import supybot.plugins as plugins
import supybot.ircmsgs as ircmsgs
import supybot.ircutils as ircutils
import supybot.schedule as schedule
import supybot.callbacks as callbacks

# Supytweet identifiers
# Do not change, these identify this as "SupyTweet" to the Twitter API
consumer_key = "hXmgIkQTELAUglEBekwRLg"
consumer_secret = "wUdexMbIzxUfOC7w32roze0q5rU1EPez7Jg4DV7ec"


class SupyTweet(callbacks.Plugin):
    """Plugin for interacting with Twitter. For first use
    'supytweet getauth' will give you the authorization URI,
    after which you should privately send supybot supytweet PIN
    <pin> to authorise and login. IRC: #supytweet on Freenode
    Twitter: @supytweet"""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(SupyTweet, self)
        self.__parent.__init__(irc)
        #OAuth
        self.access_token = dict()
        self.authfile = conf.supybot.directories.data.dirize('SupyTweet.auth')
        self._openAuth()
        self.have_temp = False
        self.oauthpin = None
        #Schedulers
        self.events = {}
        self.events['mentions'] = 0
        self.events['DM'] = 0
        self.events['timeline'] = 0
        self.lastMention = -1
        self.lastDM = -1
        self.lastTimeline = -1
        #Start up
        self.twitLogin(irc)
        # Read all coTag config values once, so they stay stored, else unused ones get lost
        for u in ircdb.users.itervalues():
            tag = self.userValue('coTag', u.name)
            self.log.debug(format("Cotag for %s: %s", u.name, tag))

    # Read stored access token for session restore
    def _openAuth(self):
        self.log.debug("Attempting to open access token file")
        try:
            fd = file(self.authfile)
            reader = csv.reader(fd)
            for (key, value) in reader:
                self.access_token[key] = value
            self.log.debug("Finished reading access token file")
            fd.close()
        except EnvironmentError, e:
            self.log.warning('Couldn\'t open %s: %s', self.authfile, e)

    # Save a working access token
    def _flushAuth(self):
        self.log.debug("Writing access token file")
        fd = utils.file.AtomicFile(self.authfile)
        writer = csv.writer(fd)
        for (key, value) in self.access_token.iteritems():
            writer.writerow([key, value])
        fd.close()

    # Attempt to log in to Twitter
    # If log in info isn't available, create a temporary token for PIN login
    # Takes a boolean, if true will send error responses back to irc
    def twitLogin(self, irc, output=False):
        if len(self.access_token):
            if 'oauth_token' in self.access_token:
                self.log.debug("Have stored access token")
                self.log.debug("Make twitter connection")
                self.twitter = OAuthApi(consumer_key, consumer_secret, self.access_token['oauth_token'], self.access_token['oauth_token_secret'])
                try:
                    self.user_self = self.twitter.ApiCall("account/verify_credentials")
                    self.log.info("Twitter authorized")
                    self.not_auth = False
                    self._flushAuth()
                    self._initSched(irc)
                except Exception, e:
                    self.log.warning(format("%s", e))
                    self.log.info("Possible bad stored Twitter auth token; removing")
                    self.not_auth = True
                    self.access_token = dict()
                    self._flushAuth()
            else:
                self.log.info("Malformed stored Twitter auth token")
                if output:
                    irc.error("Error: OAuth token was bad")
                return
        else:
            self.not_auth = True
            if not self.have_temp:
                self.log.debug("Getting temp credentials")
                self.twitter = OAuthApi(consumer_key, consumer_secret)
                self.temp_credentials = self.twitter.getRequestToken()
                self.have_temp = True
            self.oauth_verifier = self.oauthpin
            if self.oauth_verifier:
                self.log.debug("Have a PIN, get an access token")
                self.access_token = self.twitter.getAccessToken(self.temp_credentials, self.oauth_verifier)
                if len(self.access_token):
                    self.twitLogin(irc)
                else:
                    self.log.info("Bad Twitter auth token")
                    if output:
                        irc.reply("Have temporary login, awaiting correct PIN")
            else:
                self.log.debug("No PIN")
                if output:
                    irc.reply("Have temporary login, awaiting correct PIN, use 'supytweet getauth' to get one")

    # Reply with url for the PIN to authorize with Twitter
    def get_auth(self, irc, msg, args):
        if self.not_auth:
            self.twitLogin(irc)
            self.log.debug("Get Auth URL")
            auth_url = self.twitter.getAuthorizationURL(self.temp_credentials)
            irc.reply(format("Browse to %s and use 'supytweet pin <pin>' in private", auth_url))
        else:
            irc.reply("Already authorized")
    getauth = wrap(get_auth)

    # Takes a PIN and attempts to connect using it and the temp token
    def pin(self, irc, msg, args, newpin):
        """<PIN>

        Use PIN as an oauth verifier and attempt to authorise. This command
        must be sent privately.
        """
        if self.not_auth:
            if newpin and irc.isChannel(msg.args[0]):
                raise callbacks.Error, conf.supybot.replies.requiresPrivacy()
            self.oauthpin = newpin
            self.twitLogin(irc, True)
            if not self.not_auth:
                irc.replySuccess()
        else:
            irc.reply("Already authorized")
    pin = wrap(pin, ["text"])
    
    # Old login sequence, from PIN config value
    # may still be useful if the above 'pin' timeouts
    def login(self, irc, msg, args):
        """<no arguements>

        Attempts to authorize to the twitter API.
        """
        if self.not_auth:
            self.oauth_verifier = self.oauthpin
            if self.oauth_verifier:
                self.twitLogin(irc, True)
                if not self.not_auth:
                    irc.replySuccess()
            else:
                self.log.debug("No PIN")
                irc.reply("No PIN set, cannot login")
        else:
            irc.reply("Already authorized")
    login = wrap(login)

    # Takes a user id and returns json user details
    def _userLookup(self, id):
        self.log.debug("Looking up user id")
        ret = self.twitter.ApiCall("users/lookup", parameters={'user_id': id})
        return ret

    # Update the rate limit counts
    def _getRateLimit(self):
        self.log.debug("Get rate_limit_status")
        self.rate_limit = self.twitter.ApiCall("account/rate_limit_status")

    # Get and display rate limits
    def ratelimit(self, irc, msg, args):
        """<no arguements>

        Returns information on the API limits.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            self._getRateLimit()
            hourlylimit = self.rate_limit['hourly_limit']
            remaininglimit = self.rate_limit['remaining_hits']
            resettime = time.mktime(time.gmtime(self.rate_limit['reset_time_in_seconds']))
            now = time.mktime(time.gmtime())
            when = utils.timeElapsed(resettime - now)
            irc.reply(format("Rate Limit: %s/%s (Remaining/Limit) - Reset in %s", remaininglimit, hourlylimit, when))
    ratelimit = wrap(ratelimit)

    # Get list of people who an id follows
    # id is optinal, default is return auth'd user
    def _getFriends(self, id=None):
        self.log.debug("Get statuses/friends")
        if id:
            self.friends = self.twitter.GetFriends({'id': id})
        else:
            self.friends = self.twitter.GetFriends()

    # Get and display list of users followed
    def following(self, irc, msg, args, id=None):
        """[<user>]

        Returns the users being followed. If <user> is given
        returns users being followed for <user>. <user> can
        be an id or screen name.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            self._getFriends(id)
            ret = []
            for i in range(0,len(self.friends)):
                screen_name = self.friends[i]['screen_name']
                ret.append(screen_name)
            prefix = format("Following (%s): ", len(self.friends))
            irc.replies(ret, prefixer=prefix)
    following = wrap(following, [optional(first('id', 'text'))])

    # Get list of users who follow an id
    # id is optinal, default is return auth'd user
    def _getFollowers(self, id=None):
        self.log.debug("Get statuses/followers")
        if id:
            self.myfollowers = self.twitter.GetFollowers({'id': id})
        else:
            self.myfollowers = self.twitter.GetFollowers()

    # Get and display users who follow
    def followers(self, irc, msg, args, id=None):
        """[<user>]

        Returns to users who are following. If <user> is given
        returns users who follow <user>. <user> can be an id or
        screen name.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            self._getFollowers(id)
            ret = []
            for i in range(0,len(self.myfollowers)):
                screen_name = self.myfollowers[i]['screen_name']
                ret.append(screen_name)
            prefix = format("Followers (%s): ",len(self.myfollowers))
            irc.replies(ret, prefixer=prefix)
    followers = wrap(followers, [optional(first('id', 'text'))])

    # Wrapper for sending a tweet, with optinal reply to id
    # returns resulting json
    def _postUpdateStatus(self, status, reply=None):
        if reply:
            self.log.debug(format("Post reply to %s", reply))
            result = self.twitter.UpdateStatus(status, {'in_reply_to_status_id': reply})
            #result = ({"request": "/1/statuses/update.json", "error": "Client must provide a 'status' parameter with a value."})
        else:
            self.log.debug("Post update")
            result = self.twitter.UpdateStatus(status)
            #result = ({"request": "/1/statuses/update.json", "error": "Client must provide a 'status' parameter with a value."})
        return result

    # Makes a plain tweet, checks for multiuser tagging and length
    def tweet(self, irc, msg, args, text):
        """<text>

        Tweets <text> to twitter. If in multiuser, appends your CoTag.
        Fails if total length is longer than 140 characters.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            if self.registryValue('useCoTags'):
                cotag = self.userValue('coTag', msg.prefix)
                if cotag:
                    self.log.debug("Multiuser has a cotag set")
                    status = text + " " + cotag
                else:
                    irc.error("You have no CoTag set, use 'supytweet cotag' to set")
                    return
            else:
                status = text
            self.log.debug(format("Message is %s long", len(status)))
            if len(status) <= 140:
                self.log.debug(format("Sending: '%s' to twitter", status))
                result = self._postUpdateStatus(status)
                if result:
                    if 'error' in result:
                        irc.error(result['error'])
                else:
                    irc.replySuccess()
            else:
                irc.error(format("Text is too long (%s) for a tweet", len(status)))
    tweet = wrap(tweet, ["text"])

    # Makes a reply tweet, checks for multiuser tagging and length
    def reply(self, irc, msg, args, id, text):
        """<id> <text>

        Tweets <text> to twitter in reply to <id>. If in multiuser
        , appends your CoTag. Fails if total length is longer than
        140 characters.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            if id:
                if self.registryValue('useCoTags'):
                    cotag = self.userValue('coTag', msg.prefix)
                    if cotag:
                        self.log.debug("Multiuser has a cotag set")
                        status = text + " " + cotag
                    else:
                        irc.error("You have no CoTag set, use 'supytweet cotag' to set")
                        return
                else:
                    status = text
                self.log.debug(format("Message is %s long", len(status)))
                if len(status) <= 140:
                    self.log.debug(format("Sending reply to %s: '%s' to twitter", id, status))
                    result = self._postUpdateStatus(status, id)
                    if result:
                        if 'error' in result:
                            irc.error(result['error'])
                    else:
                        irc.replySuccess()
                else:
                    irc.error(format("Text is too long (%s) for a tweet", len(status)))
            else:
                irc.error("No id given to reply to")
    reply = wrap(reply, ["id", "text"])

    # API retweet an id 
    def retweet (self, irc, msg, args, id):
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            if id:
                self.log.debug(format("Retweeting id %s", id))
                rt = "statuses/retweet/" + str(id)
                result = self.twitter.ApiCall(rt, "POST")
                if 'error' in result:
                    irc.error(result['error'])
                else:
                    irc.replySuccess()
            else:
                irc.error("No id given to reply to")
    retweet = wrap(retweet, ["id"])

    # Wrapper for displaying tweets
    # Takes a list of tweets as given by the API
    # returns a list of formatted text, with id, API and time info
    # TODO: (optionally) hide protected tweets from being included
    # TODO: toggle bold usernames/coloured #hash and @users
    def _tweetFormatter(self, items):
        ret = []
        for i in range(0,len(items)):
            bold = True
            self.log.debug(format("Building Tweet string %s", i))
            
            #Init optionals
            reply = ""
            reply_name = ""
            by = ""
            at = ""
            retweet = ""
            contributors = ""
            protected = False
            
            # retweet
            if "retweeted_status" in items[i]:
                id = items[i]['id']
                screen_name = items[i]['retweeted_status']['user']['screen_name']
                text = items[i]['retweeted_status']['text']
                reply_name = items[i]['retweeted_status']['in_reply_to_screen_name']
                via = items[i]['retweeted_status']['source']
                contributors = items[i]['retweeted_status']['contributors']
                if items[i]['retweeted_status']['place']:
                    at = " from " + items[i]['retweeted_status']['place']['name'] + ', ' + items[i]['retweeted_status']['place']['country_code']
                retweet_name = items[i]['user']['screen_name']
                # Check retweeter protection, then check retweeted protection
                if self.registryValue('hideProtected'):
                    protected = items[i]['user']['protected']
                    if not protected:
                        protected = items[i]['retweeted_status']['user']['protected']
            # direct message
            elif "sender" in items[i]:
                id = items[i]['id']
                screen_name = items[i]['sender']['screen_name']
                text = items[i]['text']
                via = "Direct Message"
                retweet_name = False
                if self.registryValue('hideProtectedDM'):
                    protected = items[i]['sender']['protected']
            # normal tweet
            else:
                id = items[i]['id']
                screen_name = items[i]['user']['screen_name']
                text = items[i]['text']
                reply_name = items[i]['in_reply_to_screen_name']
                via = items[i]['source']
                contributors = items[i]['contributors']
                if items[i]['place']:
                    at = " from " + items[i]['place']['name'] + ', ' + items[i]['place']['country_code']
                retweet_name = False
                if self.registryValue('hideProtected'):
                    protected = items[i]['user']['protected']

            # Stop that, it's silly (Date strings)
            created = items[i]['created_at']
            created = format("%s UTC", created)
            created_secs = time.mktime(time.strptime(created, "%a %b %d %H:%M:%S +0000 %Y %Z"))
            now = time.mktime(time.gmtime())
            try:
                ago = utils.timeElapsed(now - created_secs, years=True,
                    weeks=True, days=True, hours=True, minutes=False, seconds=False)
                self.log.debug("Over an hour")
                ago = "about " + ago + " ago"
            except ValueError, e:
                try:
                    ago = utils.timeElapsed(now - created_secs, years=False,
                        weeks=False, days=False, hours=True, minutes=True, seconds=False)
                    self.log.debug("Less than hour")
                    ago = ago + ' ago'
                except ValueError, e:
                    ago = utils.timeElapsed(now - created_secs, years=False,
                        weeks=False, days=False, hours=True, minutes=True, seconds=True)
                    self.log.debug("Less than minute")
                    ago = ago + ' ago'

            text = text.replace("&lt;", "<")
            text = text.replace("&gt;", ">")
            text = text.replace("&amp;", "&")
            # Cleanup API access link
            if via.startswith("<a "):
                begin = via.find(">") + 1
                end = via.find("</a>")
                via = via[begin:end]

            if reply_name:
                reply = " in reply to " + reply_name
            if contributors:
                cont_list = []
                for cont_id in contributors:
                    cont = self._userLookup(cont_id)
                    cont_list.append(cont[0]['screen_name'])
                by = " by " + utils.str.commaAndify(cont_list)
            if retweet_name:
                retweet = " Retweeted by " + retweet_name

            # Unicode sure takes some messing about
            screen_name = screen_name.encode("utf-8")
            text = text.encode("utf-8")
            text = text.replace("\xe2\x80\x9c", '"')
            text = text.replace("\xe2\x80\x9d", '"')
            text = text.replace("\xe2\x96\xb8", ">")
            text = text.replace("\xe2\x80\x99", "`")
            text = text.replace("\'", "`")
            reply = reply.encode("utf-8")
            ago = ago.encode("utf-8")
            via = via.encode("utf-8")
            by = by.encode("utf-8")
            at = at.encode("utf-8")
            retweet = retweet.encode("utf-8")

#            if bold:
#                screen_name = ircutils.bold(screen_name)

            if protected:
                out = "*Protected Tweet*"
            else:
                out = format("%s: %s%s, %s via %s%s%s.%s (%s)", screen_name, text, reply, ago, via, by, at, retweet, id)
            ret.append(out)
        if len(ret) is 0:
            ret.append("No tweets to display")
        return ret

    # Update the hometime line
    def _getTimeLine(self):
        self.log.debug("Get Home TimeLine")
        self.hometimeline = self.twitter.GetHomeTimeline()
        self.log.debug(format("Got %s Tweets", len(self.hometimeline)))

    # Get, format and display the main timeline
    def timeline (self, irc, msg, args):
        """<no arguements>

        Returns latest tweets on the timeline.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            self._getTimeLine()
            if 'error' in self.hometimeline:
                irc.error(self.hometimeline['error'])
            else:
                tweets = self._tweetFormatter(self.hometimeline)
                sep = '||'
                sep = ' ' + sep + ' '
                irc.replies(tweets, joiner=sep)
    timeline = wrap(timeline)
    
    # Update mentions
    def _getMentions(self):
        self.log.debug("Get Mentions")
        self.mymentions = self.twitter.ApiCall("statuses/mentions")
        self.log.debug(format("Got %s Tweets", len(self.mymentions)))

    # Get and display mentions
    def mentions (self, irc, msg, args):
        """<no arguements>

        Returns latest mentions (tweets containing @username).
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            self._getMentions()
            if 'error' in self.mymentions:
                irc.error(self.mymentions['error'])
            else:
                tweets = self._tweetFormatter(self.mymentions)
                sep = '||'
                sep = ' ' + sep + ' '
                irc.replies(tweets, joiner=sep)
    mentions = wrap(mentions)
    
    # Update DMs
    def _getDirectMess(self):
        self.log.debug("Get Direct Messages")
        self.direct_mess = self.twitter.ApiCall("direct_messages")
        self.log.debug(format("Got %s Tweets", len(self.direct_mess)))

    # Get and display DMs
    # Only works in query
    def dm (self, irc, msg, args):
        """<no arguements>

        Returns latest direct messages. This command must be sent privately.
        """
        if self.not_auth:
            irc.reply("Not authorized to twitter")
        else:
            if irc.isChannel(msg.args[0]):
                raise callbacks.Error, conf.supybot.replies.requiresPrivacy()
            else:
                self._getDirectMess()
                if 'error' in self.direct_mess:
                    irc.error(self.direct_mess['error'])
                else:
                    tweets = self._tweetFormatter(self.direct_mess)
                    sep = '||'
                    sep = ' ' + sep + ' '
                    irc.replies(tweets, joiner=sep)
    dm = wrap(dm)

    # Check if connected, and display basic user info for auth'd user
    def status (self, irc, msg, args):
        if self.not_auth:
            irc.reply("Not authorized to Twitter")
        else:
            self.user_self = self.twitter.ApiCall("account/verify_credentials")
            name = self.user_self["screen_name"].encode("utf-8")
            fullname = self.user_self["name"].encode("utf-8")
            location = self.user_self["location"]
            if location:
                location.encode("utf-8")
                location = format(" - %s", location)
            bio = self.user_self["description"]
            if bio:
                bio.encode("utf-8")
                bio = format(" | %s", bio)
            url = self.user_self["url"]
            if url:
                url.encode("utf-8")
                url = format(" | %s", url)
            followers = self.user_self["followers_count"]
            following = self.user_self["friends_count"]
            tweets = self.user_self["statuses_count"]

            irc.reply(format("Authorized to Twitter: %s (@%s)%s%s%s || Followers: %s || Following: %s || Tweets: %s", fullname, name, location, bio, url, followers, following, tweets))
    status = wrap(status)

    # Display or set a users CoTag
    # Takes a string in the ^XY format, where XY can be any upper case alphanumeric
    def cotag (self, irc, msg, args, tag):
        """[<tag>]

        Returns your cotag for twitter posts. If <tag> is
        given, sets your cotag to <tag>. Tags must take the
        form ^XY
        """
        cotag = self.userValue('coTag', msg.prefix)
        if tag:
            cocheck = re.compile('^\^[A-Z0-9][A-Z0-9]$')
            if not cocheck.match(tag):
                irc.reply('Tags must take the form: ^XY')
                return
            else:
                self.setUserValue('cotag', msg.prefix, tag)
                irc.replySuccess()
                return
        if not cotag:
            irc.reply('No CoTag set')
        else:
            irc.reply(cotag)
    cotag = wrap(cotag, [additional('text')])

    # Lists current users with CoTags set
    def cotags (self, irc, msg, args):
        """<no arguements>

        Lists known supytweet users, and their CoTags.
        """
        
        out = []
        for u in ircdb.users.itervalues():
            tag = self.userValue('coTag', u.name)
            if tag:
                out.append(format("%s: %s", u.name, tag))
        irc.reply(utils.str.commaAndify(out))
    cotags = wrap(cotags)

    # Command for restarting failed updates
    def updaterestart(self, irc, msg, args):
        """<no arguements>
        
        Restarts scheduled updates
        """
        if self.not_auth:
            irc.reply("Not authorized to Twitter")
        else:
            self._initSched(irc)
            irc.replySuccess()
    updaterestart = wrap(updaterestart)
    
    # Wrapper for checking if an event isn't scheduled, and to schedule it
    def _initSched(self, irc):
        if self.registryValue('mentions'):
            if not self.events['mentions']:
                self._scheduleMention(irc)
        
        if self.registryValue('DM'):
            if not self.events['DM']:
                self._scheduleDM(irc)
        
        if self.registryValue('timeline'):
            if not self.events['timeline']:
                self._scheduleTimeline(irc)

    # Schedule a mentions update
    def _scheduleMention(self, irc):
        if self.registryValue('mentions'):
            def announceMentionsCaller():
                self._announceMentions(irc)
        
            channel = self.registryValue('mentions.channel')
            waitPeriod = self.registryValue('mentions.waitPeriod')
            if channel:
                if self.lastMention is -1:
                    self._getMentions()
                    if len(self.mymentions) is not 0:
                        self.lastMention = self.mymentions[0]['id']
                    else:
                        self.lastMention = 0
                    self.log.debug('Starting with last mention id %s', self.lastMention)
                id = schedule.addEvent(announceMentionsCaller, time.time() + waitPeriod)
                self.events['mentions'] = id
                self.log.debug('Scheduling mention announce in %ss to %s', waitPeriod, channel)
            else:
                self.log.warning("Not scheduling mention announces since no announce channel has been configured.")
            
    # Called when the scheduled mention check occurs, looks for new mentions and displays
    def _announceMentions(self, irc):
        self.events['mentions'] = 0
        if self.not_auth:
            self.log.info("Unable to check mentions: Not authorized to twitter")
        else:
            if not self.registryValue('mentions'):
                self.log.debug("Mention checking turned off between checks")
                return
            self._scheduleMention(irc)
            self._getMentions()
            if 'error' in self.mymentions:
                self.log.warning(self.mymentions['error'])
            else:
                if len(self.mymentions) is 0:
                    self.log.debug('No mentions in timeline')
                    return
                ret = []
                for i in range(0, len(self.mymentions)):
                    if(self.mymentions[i]['id'] > self.lastMention):
                        ret.append(self.mymentions[i])
                        
                self.lastMention = self.mymentions[0]['id']
                self.log.debug('%s New Mentions!', len(ret))
                if len(ret) > 0:
                    tweets = self._tweetFormatter(ret)
                    channel = self.registryValue('mentions.channel')
                    sep = ' ' + '||' + ' '
                    out = format("%s New Mention(s)! %s", len(tweets), sep.join(tweets))
                    for target in channel:
                        irc.queueMsg(ircmsgs.privmsg(target, out))
                        
    # Schedule a DM update
    def _scheduleDM(self, irc):
        if self.registryValue('DM'):
            def announceDMCaller():
                self._announceDM(irc)
        
            channel = self.registryValue('DM.channel')
            waitPeriod = self.registryValue('DM.waitPeriod')
            if channel:
                if self.lastDM is -1:
                    self._getDirectMess()
                    if len(self.direct_mess) is not 0:
                        self.lastDM = self.direct_mess[0]['id']
                    else:
                        self.lastDM = 0
                    self.log.debug('Starting with last DM id %s', self.lastDM)
                id = schedule.addEvent(announceDMCaller, time.time() + waitPeriod)
                self.events['DM'] = id
                self.log.debug('Scheduling DM announce in %ss to %s', waitPeriod, channel)
            else:
                self.log.warning("Not scheduling DM announces since no announce channel has been configured.")
            
    # Called when the scheduled DM check occurs, looks for new DMs and displays
    def _announceDM(self, irc):
        self.events['DM'] = 0
        if self.not_auth:
            self.log.info("Unable to check DMs: Not authorized to twitter")
        else:
            if not self.registryValue('DM'):
                self.log.debug("DM checking turned off between checks")
                return
            self._scheduleDM(irc)
            self._getDirectMess()
            if 'error' in self.direct_mess:
                self.log.warning(self.direct_mess['error'])
            else:
                if len(self.direct_mess) is 0:
                    self.log.debug('No DMs in timeline')
                    return
                ret = []
                for i in range(0, len(self.direct_mess)):
                    if(self.direct_mess[i]['id'] > self.lastDM):
                        ret.append(self.direct_mess[i])
                        
                self.lastDM = self.direct_mess[0]['id']
                self.log.debug('%s New DMs!', len(ret))
                if len(ret) > 0:
                    tweets = self._tweetFormatter(ret)
                    channel = self.registryValue('DM.channel')
                    sep = ' ' + '||' + ' '
                    out = format("%s New DM(s)! %s", len(tweets), sep.join(tweets))
                    for target in channel:
                        irc.queueMsg(ircmsgs.privmsg(target, out))
                        
    # Schedule a timeline update
    def _scheduleTimeline(self, irc):
        if self.registryValue('timeline'):
            def announceTimelineCaller():
                self._announceTimeline(irc)
        
            channel = self.registryValue('timeline.channel')
            waitPeriod = self.registryValue('timeline.waitPeriod')
            if channel:
                if self.lastTimeline is -1:
                    self._getTimeLine()
                    if len(self.hometimeline) is not 0:
                        self.lastTimeline = self.hometimeline[0]['id']
                    else:
                        self.lastTimeline = 0
                    self.log.debug('Starting with last Timeline id %s', self.lastTimeline)
                id = schedule.addEvent(announceTimelineCaller, time.time() + waitPeriod)
                self.events['timeline'] = id
                self.log.debug('Scheduling Timeline announce in %ss to %s', waitPeriod, channel)
            else:
                self.log.warning("Not scheduling Timeline announces since no announce channel has been configured.")
            
    # Called when the scheduled timeline check occurs, looks for new tweets and displays
    def _announceTimeline(self, irc):
        self.events['timeline'] = 0
        if self.not_auth:
            self.log.info("Unable to check Timeline: Not authorized to twitter")
        else:
            if not self.registryValue('timeline'):
                self.log.debug("Timeline checking turned off between checks")
                return
            self._scheduleTimeline(irc)
            self._getTimeLine()
            if 'error' in self.hometimeline:
                self.log.warning(self.hometimeline['error'])
            else:
                if len(self.hometimeline) is 0:
                    self.log.debug('No tweets in home timeline')
                    return
                ret = []
                for i in range(0, len(self.hometimeline)):
                    if(self.hometimeline[i]['id'] > self.lastTimeline):
                        ret.append(self.hometimeline[i])
                        
                self.lastTimeline = self.hometimeline[0]['id']
                self.log.debug('%s New Tweets!', len(ret))
                if len(ret) > 0:
                    tweets = self._tweetFormatter(ret)
                    channel = self.registryValue('timeline.channel')
                    sep = ' ' + '||' + ' '
                    out = format("%s New Tweet(s)! %s", len(tweets), sep.join(tweets))
                    for target in channel:
                        irc.queueMsg(ircmsgs.privmsg(target, out))

Class = SupyTweet


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
