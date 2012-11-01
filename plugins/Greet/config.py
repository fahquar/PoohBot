###
# Copyright (c) 2004, Jeremiah Fincher
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

import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    # This will be called by supybot to configure this module.  advanced is
    # a bool that specifies whether the user identified himself as an advanced
    # user or not.  You should effect your configuration by manipulating the
    # registry as appropriate.
    from supybot.questions import expect, anything, something, yn
    conf.registerPlugin('Greet', True)


Greet = conf.registerPlugin('Greet')
conf.registerChannelValue(Greet, 'greeting',
    registry.Boolean(True, """Determines whether messages will be sent to the
    channel when a recognized user joins; basically enables or disables the
    plugin."""))
conf.registerGlobalValue(Greet, 'requireCapability',
    registry.String('', """Determines what capability (if any) is required to
    add/change/remove the herald of another user."""))
conf.registerChannelValue(Greet, 'throttle',
    registry.PositiveInteger(1, """Determines the minimum number of seconds
    between greets."""))
conf.registerChannelValue(Greet.throttle, 'afterPart',
    registry.NonNegativeInteger(0, """Determines the minimum number of seconds
    after parting that the bot will not greet the person when he or she
    rejoins."""))
conf.registerChannelValue(Greet.throttle, 'afterSplit',
    registry.NonNegativeInteger(0, """Determines the minimum number of seconds
    after a netsplit that the bot will not greet the users that split."""))
conf.registerChannelValue(Greet, 'default',
    registry.String('', """Sets the default greet to use.  If a user has a
    personal greet specified, that will be used instead.  If set to the empty
    string, the default greet will be disabled."""))
conf.registerChannelValue(Greet.default, 'notice',
    registry.Boolean(True, """Determines whether the default greet will be
    sent as a NOTICE instead of a PRIVMSG."""))
conf.registerChannelValue(Greet.default, 'public',
    registry.Boolean(True, """Determines whether the default greet will be
    sent publicly."""))

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
