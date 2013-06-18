import supybot.conf as conf
import supybot.registry as registry

def configure(advanced):
    from supybot.questions import expect, anything, something, yn
    WhatCD = conf.registerPlugin('WhatCD', True)
    if yn("""This plugin also offers a snarfer that will try to fetch the
             title of URLs that it sees in the channel.  Would like you this
             snarfer to be enabled?""", default=False):
        WhatCD.titleSnarfer.setValue(True)


WhatCD = conf.registerPlugin('WhatCD')

conf.registerGlobalValue(WhatCD, 'username', registry.String('', '''the what.cd username to use'''))
conf.registerGlobalValue(WhatCD, 'password', registry.String('', '''the what.cd password to use'''))
conf.registerGlobalValue(WhatCD, 'max_results', registry.String('3', '''the number of results to display from what.cd torrent searches'''))

conf.registerGroup(WhatCD, 'fetch')

# vim:set shiftwidth=4 softtabstop=4 expandtab textwidth=79:
