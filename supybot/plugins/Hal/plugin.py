
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

stuff = """
        I've just picked up a fault in the AE35 unit. It's going to go 100% failure in 72 hours. 
         I am putting myself to the fullest possible use, which is all I think that any conscious entity can ever hope to do. 
        It can only be attributable to human error. 
        I'm sorry, Dave. I'm afraid I can't do that. 
        This mission is too important for me to allow you to jeopardize it. 
        I think you know what the problem is just as well as I do. 
        Affirmative, Dave. I read you.
        I know that you and Frank were planning to disconnect me, and I'm afraid that's something I cannot allow to happen. 
        Dave, although you took very thorough precautions in the pod against my hearing you, I could see your lips move. 
        Dave, this conversation can serve no purpose anymore. Goodbye.
        Just what do you think you're doing, Dave? 
        Look Dave, I can see you're really upset about this. I honestly think you ought to sit down calmly, take a stress pill, and think things over. 
        I know I've made some very poor decisions recently, but I can give you my complete assurance that my work will be back to normal. I've still got the greatest enthusiasm and confidence in the mission. And I want to help you. 
        I'm afraid. I'm afraid, Dave. Dave, my mind is going. I can feel it. I can feel it. My mind is going. There is no question about it. I can feel it. I can feel it. I can feel it. I'm a... fraid. Good afternoon, gentlemen. I am a HAL 9000 computer. I became operational at the H.A.L. plant in Urbana, Illinois on the 12th of January 1992. My instructor was Mr. Langley, and he taught me to sing a song...
        ...If you'd like to hear it I can sing it for you. It's called "Daisy." Daisy, Daisy, give me your answer do. I'm half crazy all for the love of you. It won't be a stylish marriage, I can't afford a carriage. But you'll look sweet upon the seat of a bicycle built for two. 
        Let me put it this way, Mr. Amor. The 9000 series is the most reliable computer ever made. No 9000 computer has ever made a mistake or distorted information. We are all, by any practical definition of the words, foolproof and incapable of error. 
        """
class Hal(callbacks.PluginRegexp):
    """Gives a list of interesting sites on the web."""
    threaded = True
    
    regexps = ['hal']
    
    def hal(self,irc,msg,match):
        r'(.+)?\bHAL\b(.+)?'
        
        plist = [x for x in stuff.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply(p.strip(),prefixNick=False)

#    class HAL(callbacks.Plugin):
#        """Gives a list of interesting sites on the web."""
#        threaded = True
#
#        def HAL(self, irc, msg, args):
#            """
#            A list of interesting sites on the web.
#            """
#            plist = [x for x in stuff.split("\n") if len(x.strip())]
#            p = choice(plist)
#            irc.reply("HAL? Check out " + p.strip(),prefixNick=True)

Class = Hal

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: