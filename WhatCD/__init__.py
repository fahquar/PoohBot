"""
Includes various web-related commands.
"""

import supybot
import supybot.world as world

__version__ = "%%VERSION%%"


# This is a dictionary mapping supybot.Author instances to lists of
# contributions.
__contributors__ = {}

import config
import plugin
reload(plugin) # In case we're being reloaded.
# Add more reloads here if you add third-party modules and want them to be
# reloaded when this plugin is reloaded.  Don't forget to import them as well!

Class = plugin.Class
configure = config.configure


# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
