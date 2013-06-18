###
# Copyright (c) 2012, .
# All rights reserved.
#
#
###

import supybot.conf as conf
import supybot.registry as registry


def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('TopNews', True)


TopNews = conf.registerPlugin('TopNews')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(TopNews, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerChannelValue(TopNews, 'newsOrderByDate', registry.Boolean(False,"""Display news entries in order instead of by newest first"""))
conf.registerChannelValue(TopNews, 'headlineCharacters', registry.Integer(80, """Number of characters to display in a headline before truncation [...]"""))
conf.registerChannelValue(TopNews, 'defaultNumberEntries', registry.Integer(7, """Default number of news articles and entries to display. Be wise. It can flood."""))
conf.registerChannelValue(TopNews, 'displaySource', registry.Boolean(False, """Display source of article or entry next to the topic"""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=179:
