###
# Copyright (c) 2009, James Scott
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
import gdata.youtube
import gdata.youtube.service
from urlparse import *

class Youtube(callbacks.Plugin):
    """Add the help for "@plugin help Youtube" here
    This should describe *how* to use this plugin."""
    threaded = True

    def __init__(self, irc):
        self.__parent = super(Youtube, self)
        self.__parent.__init__(irc)
        self.service = gdata.youtube.service.YouTubeService()
        self.service.developer_key = self.registryValue('developer_key')
        self.service.client_id = self.registryValue('client_id')

    def _video_id(self,value):
        """
        Examples:
        - http://youtu.be/SA2iWivDJiE
        - http://www.youtube.com/watch?v=_oPAwA_Udwc&feature=feedu
        - http://www.youtube.com/embed/SA2iWivDJiE
        - http://www.youtube.com/v/SA2iWivDJiE?version=3&amp;hl=en_US
        """
        #print value
        query = urlparse(value)
        if query.hostname == 'youtu.be':
            return query.path[1:]
        if query.hostname in ('www.youtube.com', 'youtube.com'):
            if query.path == '/watch':
                p = parse_qs(query.query)
                return p['v'][0]
            if query.path[:7] == '/embed/':
                return query.path.split('/')[2]
            if query.path[:3] == '/v/':
                return query.path.split('/')[2]
        # fail?
        return None

#    def _lookUpYouTube(self, irc, msg):
#        (recipients, text) = msg.args
#        yt_service = self.service
#        try:
#            if "https" in text:
#                url = text.split("https://")[1]
#            else:
#                url = text.split("http://")[1]
#            url = url.split(" ")[0]
#        except:
#            url = text
#        vid_id = self._video_id("http://"+url)
#        entry = yt_service.GetYouTubeVideoEntry(video_id=vid_id)
#        title = ""
#        rating = ""
#        views = 0
#        try:
#            title = ircutils.bold(entry.media.title.text)
#        except:
#            pass
#        try:
#            views = ircutils.bold(entry.statistics.view_count)
#        except:
#            views = ircutils.bold('0')
#        try:  
#            rating = ircutils.bold('{:.2%}'.format((float(entry.rating.average)/5)))
#        except:
#            rating = ircutils.bold("n/a")
#        try:
#            likes = ircutils.bold(entry.rating.numLikes
#        except:
#            likes = ircutils.bold('0')
#        try:
#            dislikes = ircutils.bold(entry.rating.numDisikes)
#        except:
#            dislikes = ircutils.bold('0')
#        irc.reply('Title: %s  Views: %s  Rating: %s Likes: %s Dislikes: %s ' % (title, views, rating, likes, dislikes),prefixNick=False)
#    
#    
#    def doPrivmsg(self, irc, msg):
#        (recipients, text) = msg.args
#        #print text.find("youtube.com/watch?v=")
#        if "youtube.com" in text:
#            self._lookUpYouTube(irc, msg)
#        elif "youtu.be" in text:
#            self._lookUpYouTube(irc, msg)
#        else:
#            pass
    
    def youtube(self, irc, msg, args):
        (recipients, text) = msg.args
        text = text.replace(".youtube ", "")
        yt_service = self.service
        query = gdata.youtube.service.YouTubeVideoQuery()
        query.vq = text
        query.orderby = 'relevance'
        query.racy = 'include'
        query.max_results = 3
        feed = yt_service.YouTubeQuery(query)
        logo1 = 'You'
        logo2 = 'Tube'
        logo1 = ircutils.bold(ircutils.mircColor(logo1, '1', '0'))
        logo2 = ircutils.bold(ircutils.mircColor(logo2, '0', '4'))
        i=1
        irc.reply("Top %s%s results for '%s':" % (logo1, logo2, text))
        for entry in feed.entry:
            irc.reply(format(ircutils.bold(ircutils.mircColor(i, '12')) + ircutils.bold(ircutils.mircColor(". ", '12')) + '%s <%s>', ircutils.bold(entry.media.title.text),entry.media.player.url),notice=False,prefixNick=False,private=False)
            i=1+i


Class = Youtube


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
