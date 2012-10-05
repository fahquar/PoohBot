
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
            sex-rex.tumblr.com
            dicksforgirls.tumblr.com
            sexcstatic.tumblr.com
            porn4ladies.tumblr.com
            goodfuckingsex.tumblr.com
            eatpussylivehappy.tumblr.com
            thingsaboutboyfriends.tumblr.com
            thingsaboutgirlfriends.tumblr.com
            sensualitea.tumblr.com
            crayonsandcancerbreaks.tumblr.com
            thisglitterfuck.tumblr.com
            thepleasures-unknown.tumblr.com
            keepcalmandgetwet.tumblr.com
            reluctanthedonist.tumblr.com
            g-uys.tumblr.com
            intimacyandclass.tumblr.com
            givemehardlove.tumblr.com
            coitusparty.tumblr.com
            xogogo.tumblr.com
            thehottestinhere.tumblr.com
            hotgirls4ever.tumblr.com
            s-e-x-d-a-y.tumblr.com
            fuck-yeahpickuplines.tumblr.com
            dodirtythingstome.tumblr.com
            edbphbr4you.tumblr.com
            carrie-so-very.tumblr.com
            sextsycrafts.tumblr.com
            sexy-yetclassy.tumblr.com
            thingsthatturnyouon.tumblr.com
            fuckthesex.tumblr.com
            girlslovesextoo.tumblr.com
            vvetdreams.tumblr.com
            iamsexuallyfrustrated.tumblr.com
            tumblrafter-dark.tumblr.com
            love-penetrate.tumblr.com
            drunk-on-sex.tumblr.com
            fuckhardlovelater.tumblr.com
            teach-you-how-to-fuck.tumblr.com
            justherguy.tumblr.com
            artofloveandsex.tumblr.com
            sexual-feelings.tumblr.com
            bendmeover.tumblr.com
            man-stuff.tumblr.com
            closetexhibitionist.tumblr.com
            deviantfemme.tumblr.com
            sexographies.tumblr.com
            thrushbone.tumblr.com
            moontang.tumblr.com
            vaginabubbles.tumblr.com
            hipandnaked.tumblr.com
            creditwhereitsdue.tumblr.com
            forhereyesonly.tumblr.com
            bonershock.tumblr.com
            i-will-call-you-sir.tumblr.com
            ourspacebetween.tumblr.com
            theladycheeky.tumblr.com
            thatscrazysexy.tumblr.com
            ladieslovesexx.tumblr.com
            hisandhrs.tumblr.com
            graffuck.tumblr.com
            fuckthegifs.tumblr.com
            theinfiniteache.tumblr.com
            younghornyandsexy.tumblr.com
            wordoyster.tumblr.com
            splicepicturesx.tumblr.com
            """

    def nsfw(self, irc, msg, args):
        """
        A list of classy erotic tumblrs compiled by Lee in #togetheralone.
        """
        plist = [x for x in NSFW.links.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply("NSFW " + p.strip(), prefixNick=True)

Class = NSFW

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
