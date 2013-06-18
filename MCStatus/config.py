##
# coding=utf8
#
# Copyright (c) 2012, nyuszika7h <nyuszika7h@cadoth.net>
#
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0
# Unported License <https://creativecommons.org/licenses/by-nc-sa/3.0/>.
##

import supybot.conf as conf
import supybot.registry as registry
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('MCStatus')

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('MCStatus', True)


MCStatus = conf.registerPlugin('MCStatus')
# This is where your configuration variables (if any) should go.  For example:
# conf.registerGlobalValue(MCStatus, 'someConfigVariableName',
#     registry.Boolean(False, _("""Help for someConfigVariableName.""")))
conf.registerGlobalValue(MCStatus, 'statusURL',
        registry.String('http://status.mojang.com/check', _("""This is the URL
        that is queried for JSON data. You shouldn't change this unless you
        know what you are doing.""")))
conf.registerChannelValue(MCStatus, 'prefix',
        registry.String('', _("""This text is prepended to the mcstatus
        command's output.""")))
conf.registerChannelValue(MCStatus, 'suffix',
        registry.String('', _("""This text is appended to the mcstatus
        command's output.""")))
conf.registerChannelValue(MCStatus, 'separator',
        registry.StringSurroundedBySpaces('|', _("""This text is inserted between service-status
        pairs.""")))
conf.registerGroup(MCStatus, 'service')
conf.registerChannelValue(MCStatus.service, 'prefix',
        registry.String('', _("""This text is prepended to each service's
        name.""")))
conf.registerChannelValue(MCStatus.service, 'suffix',
        registry.StringWithSpaceOnRight(':', _("""This text is appended to each service's
        name.""")))
conf.registerGroup(MCStatus, 'status')
conf.registerChannelValue(MCStatus.status, 'online',
        registry.NormalizedString('\x0309ONLINE\x03', _("""This text is displayed when a
        service is online (green).""")))
conf.registerChannelValue(MCStatus.status, 'offline',
        registry.NormalizedString('\x0304OFFLINE\x03', _("""This text is displayed when a
        service is offline (red).""")))

# vim: set shiftwidth=4 tabstop=4 expandtab textwidth=79:
