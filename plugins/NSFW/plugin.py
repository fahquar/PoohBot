
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

class NSFW(callbacks.Plugin):
    """Add the help for "@plugin help Zen" here
    This should describe *how* to use this plugin."""
    threaded = True

    links = """
    	http://nubia.tumblr.com
    	http://nakedebony.tumblr.com/
    	http://nopornhere.tumblr.com
    	http://thepureskin.tumblr.com
        http://sex-rex.tumblr.com
 		http://walletinspector.tumblr.com/
		http://iloveass.tumblr.com/
		http://gentlemanexhibitionist.tumblr.com/
		http://sexy-dirty-love.tumblr.com/
		http://fluffyporn.tumblr.com/
		http://fuckyeahvlines.tumblr.com/
		http://dicksforgirls.tumblr.com/
		http://sexcstatic.tumblr.com/
		http://porn4ladies.tumblr.com/
		http://thingsaboutboyfriends.tumblr.com/
		http://sensualitea.tumblr.com/
		http://reluctanthedonist.tumblr.com/
		http://g-uys.tumblr.com/
		http://raw-sensual-passion.tumblr.com/
		http://xogogo.tumblr.com/
		http://fuck-yeahpickuplines.tumblr.com/
		http://dodirtythingstome.tumblr.com/
		http://edbphbr4you.tumblr.com/
		http://fuckthesex.tumblr.com/
		http://girlslovesextoo.tumblr.com/
		http://vvetdreams.tumblr.com/
		http://iamsexuallyfrustrated.tumblr.com/
		http://tumblrafter-dark.tumblr.com/
		http://love-penetrate.tumblr.com/
		http://drunk-on-sex.tumblr.com/
		http://teach-you-how-to-fuck.tumblr.com/
		http://justherguy.tumblr.com/
		http://artofloveandsex.tumblr.com/
		http://sexual-feelings.tumblr.com/
		http://bendmeover.net/
		http://man-stuff.tumblr.com/
		http://closetexhibitionist.tumblr.com/
		http://sexographies.tumblr.com/
		http://thrushbone.tumblr.com/
		http://moontang.tumblr.com/
		http://vaginabubbles.tumblr.com/
		http://hipandnaked.tumblr.com/
		http://creditwhereitsdue.tumblr.com/
		http://forhereyesonly.tumblr.com/
		http://bonershock.tumblr.com/
		http://i-will-call-you-sir.tumblr.com/
		http://ourspacebetween.tumblr.com/
		http://www.ladycheeky.com/
		http://thatscrazysexy.tumblr.com/
		http://hisandhrs.tumblr.com/
		http://graffuck.com/
		http://fuckthegifs.tumblr.com/
		http://theinfiniteache.tumblr.com/
		http://younghornyandsexy.tumblr.com/
		http://www.wordoyster.com/
		http://splicepicturesx.tumblr.com/
		http://thrushbone.tumblr.com/
		http://dirtyhappypills.tumblr.com/
		http://bnjubnjab.tumblr.com/
		http://wisegaymen.tumblr.com/
		http://bonvivanski.tumblr.com/
		http://masturbationdestination.tumblr.com/
		http://sexysexnsuch.tumblr.com/
		http://behindthatgreendoor.tumblr.com/
		http://sexual-passion.tumblr.com/
		http://twistedfyre.tumblr.com/
		http://say-sex.tumblr.com/
		http://sexographies.tumblr.com/
            """

    def nsfw(self, irc, msg, args):
        """
        A list of classy erotic tumblrs compiled by Lee in #togetheralone.
        """
        plist = [x for x in NSFW.links.split("\n") if len(x.strip())]
        p = choice(plist)
        nsfw = ircutils.bold(ircutils.mircColor("NSFW ","4"))
        irc.reply(nsfw + p.strip())

Class = NSFW

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
