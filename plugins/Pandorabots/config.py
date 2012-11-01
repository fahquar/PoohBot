###
# Copyright (c) 2010, Jiang Yio
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
    conf.registerPlugin('Pandorabots', True)


Pandorabots = conf.registerPlugin('Pandorabots')
conf.registerGlobalValue(Pandorabots,'bot',registry.String('None',"""bot ID"""))
conf.registerGlobalValue(Pandorabots,'name',registry.String('God',"""bot name"""))
conf.registerChannelValue(Pandorabots,'react',registry.Boolean(True,"""Determine whether the bot should respond to errors."""))
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(Pandorabots, 'someConfigVariableName',
#     registry.Boolean(False, """Help for someConfigVariableName."""))


# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
