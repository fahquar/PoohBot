##
# coding=utf-8
#
# Copyright (c) 2012, nyuszika7h <nyuszika7h@cadoth.net>
#
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0
# Unported License <https://creativecommons.org/licenses/by-nc-sa/3.0/>.
##

# Standard library imports
import json
import urllib2

# Supybot imports
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from supybot.i18n import PluginInternationalization, internationalizeDocstring

_ = PluginInternationalization('MCStatus')

@internationalizeDocstring
class MCStatus(callbacks.Plugin):
    """This plugin provides a command to show the status of the Mojang servers.
    The output format is customizable via configuration variables."""

    def __init__(self, irc):
        self.__parent = super(MCStatus, self)
        self.__parent.__init__(irc)

    def mcstatus(self, irc, msg, args):
        """takes no arguments

        Shows the status of the Mojang servers.
        """
        prefix = self.registryValue('prefix')
        suffix = self.registryValue('suffix')

        separator = self.registryValue('separator')

        svprefix = self.registryValue('service.prefix')
        svsuffix = self.registryValue('service.suffix')

        stonline = self.registryValue('status.online')
        stoffline = self.registryValue('status.offline')


        json_data = urllib2.urlopen(self.registryValue('statusURL')).read()
        data = json.loads(json_data)
        services = []

        for pair in data:
            service, status = pair.keys()[0], pair.values()[0]
            services.append('%s%s%s%s' % (svprefix, service, svsuffix,
                                          stonline if status == 'green' else \
                                          stoffline))

        irc.reply('%s%s%s' % (prefix, separator.join(services), suffix))
    mcstatus = wrap(mcstatus)

Class = MCStatus

# vim: set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
