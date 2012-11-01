###
# Copyright (c) 2012, mameman
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
from urllib2 import HTTPError
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from BeautifulSoup import BeautifulSoup
import random
import urllib2


class Metacritic(callbacks.Plugin):
    """Add the help for "@plugin help Fun" here
    This should describe *how* to use this plugin."""
    def metacritic(self, irc, msg, args):
        '.mc [all|movie|tv|album|x360|ps3|pc|ds|3ds|wii|psv] <title> -- gets rating for'\
        ' <title> from metacritic on the specified medium'
        
        # if the results suck, it's metacritic's fault
        
        args = args[1].strip()
        irc.reply(args)
        
        game_platforms = ('x360', 'ps3', 'pc', 'ds', 'wii', '3ds', 'gba', 'psv')
        all_platforms = game_platforms + ('all', 'movie', 'tv', 'album')
        
        try:
            plat, title = args.split(' ', 1)
            if plat not in all_platforms:
                # raise the ValueError so that the except block catches it
                # in this case, or in the case of the .split above raising the
                # ValueError, we want the same thing to happen
                raise ValueError
        except ValueError:
            plat = 'all'
            title = args
        
        cat = 'game' if plat in game_platforms else plat
        
    #        title_safe = http.quote_plus(title)
        
        url = 'http://www.metacritic.com/search/%s/%s/results' % (cat, title)
        
        try:
            doc = urllib2.urlopen(url)
        except HTTPError:
            return 'error fetching results'
        
        ''' result format:
            -- game result, with score
            -- subsequent results are the same structure, without first_result class
            <li class="result first_result">
            <div class="result_type">
            <strong>Game</strong>
            <span class="platform">WII</span>
            </div>
            <div class="result_wrap">
            <div class="basic_stats has_score">
            <div class="main_stats">
            <h3 class="product_title basic_stat">...</h3>
            <div class="std_score">
            <div class="score_wrap">
            <span class="label">Metascore: </span>
            <span class="data metascore score_favorable">87</span>
            </div>
            </div>
            </div>
            <div class="more_stats extended_stats">...</div>
            </div>
            </div>
            </li>
            
            -- other platforms are the same basic layout
            -- if it doesn't have a score, there is no div.basic_score
            -- the <div class="result_type"> changes content for non-games:
            <div class="result_type"><strong>Movie</strong></div>
            '''
        
        # get the proper result element we want to pull data from
        
        result = None
        
        if not doc.find_class('query_results'):
            return 'no results found'
        
        # if they specified an invalid search term, the input box will be empty
        if doc.get_element_by_id('search_term').value == '':
            return 'invalid search term'
        
        if plat not in game_platforms:
            # for [all] results, or non-game platforms, get the first result
            result = doc.find_class('result first_result')[0]
            
            # find the platform, if it exists
            result_type = result.find_class('result_type')
            if result_type:
                
                # if the result_type div has a platform div, get that one
                platform_div = result_type[0].find_class('platform')
                if platform_div:
                    plat = platform_div[0].text_content().strip()
                else:
                    # otherwise, use the result_type text_content
                    plat = result_type[0].text_content().strip()
        
        else:
            # for games, we want to pull the first result with the correct
            # platform
            results = doc.find_class('result')
            for res in results:
                result_plat = res.find_class('platform')[0].text_content().strip()
                if result_plat == plat.upper():
                    result = res
                    break
        
        if not result:
            return 'no results found'
        
        # get the name, release date, and score from the result
        product_title = result.find_class('product_title')[0]
        name = product_title.text_content()
        link = 'http://metacritic.com' + product_title.find('a').attrib['href']
        
        try:
            release = result.find_class('release_date')[0].\
                find_class('data')[0].text_content()
            
            # strip extra spaces out of the release date
            release = re.sub(r'\s{2,}', ' ', release)
        except IndexError:
            release = None
        
        try:
            score = result.find_class('metascore')[0].text_content()
        except IndexError:
            score = None
        
        return '[%s] %s - %s, %s -- %s' % (plat.upper(), name,
                                           score or 'no score',
                                           'release: %s' % release if release else 'unreleased',
                                           link)

Class = Metacritic


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
