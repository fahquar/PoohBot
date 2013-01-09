##
# coding=utf-8
#
# Copyright (c) 2012, nyuszika7h <nyuszika7h@cadoth.net>
#
# Licensed under the Creative Commons Attribution-NonCommercial-ShareAlike 3.0
# Unported License <https://creativecommons.org/licenses/by-nc-sa/3.0/>.
##

"""
This plugin provides a command to show the status of the Mojang servers.
The output format is customizable via configuration variables.
"""

import supybot
import supybot.world as world

# Use this for the version of this plugin.  You may wish to put a CVS keyword
# in here if you're keeping the plugin in CVS or some similar system.
__version__ = '1.0.2'

# XXX Replace this with an appropriate author or supybot.Author instance.
__author__ = supybot.Author('nyuszika7h', 'nyuszika7h',
                            'nyuszika7h@cadoth.net')

# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

# This is a URL where the most recent plugin package can be downloaded.
__url__ = ''

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

if world.testing:
    import test

Class = plugin.Class
configure = config.configure

# vim: set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
