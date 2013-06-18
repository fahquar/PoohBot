###
# Copyright (c) 2008, Olivier Le Thanh Duong
# All rights reserved.
#
#
###

import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
import re

import random
import redtube

class Redtube(callbacks.Plugin):
    """Add the help for "@plugin help Redtube" here
    This should describe *how* to use this plugin."""
    threaded = True


    def redtube(self, irc, msg, args):
        """none

        return a redube video from Redtube recent page"""

        cli = redtube.RedTubeClient()
        videoEntry = random.choice(cli.get_videos())
        videoEntry.description = re.sub("\t\t\t\t\t", "", videoEntry.description)
        videoEntry.description = re.sub("\r\n\t", "", videoEntry.description)
        videoEntry.id = re.sub("'", "", videoEntry.id)
        nsfw = ircutils.bold(ircutils.mircColor("NSFW","4"))
        irc.reply("%s %s: http://www.redtube.com/%s" % (nsfw, ircutils.bold(videoEntry.description), videoEntry.id))


Class = Redtube


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
