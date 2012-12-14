
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

stuff = """
		100,000 Stars: http://workshop.chromeexperiments.com/stars/?%3Ffsrc%3Dscn%2F=tw%2Fdc
        Winning Solitaire: http://www.winningsolitaire.com
        Aphorisms and Paradoxes by Brian Jay Stanley: http://www.brianjaystanley.com 
        Websites from Hell: http://websitesfromhell.net
        World Wonders: http://www.google.com/culturalinstitute/worldwonders/
        Endangered Sounds: http://savethesounds.info/
        Harmony: http://mrdoob.com/projects/harmony/
        Time Cube: http://www.timecube.com/
        You Are Not So Smart: http://youarenotsosmart.com/
        Music-Map: http://www.music-map.com/
        The Scale of the Universe: http://htwins.net/scale2/
        Free eBooks by Project Gutenberg: http://www.gutenberg.org/
        iDaft: http://www.najle.com/idaft/
        Type Like a TV Hacker: http://www.hackertyper.com/
        The Fucking Weather: http://thefuckingweather.com/
        What does the internet think?: http://whatdoestheinternetthink.net/
        Stamen Maps: http://maps.stamen.com/
        Orsinal: http://www.ferryhalim.com/orisinal/
        Devastating Explosions: http://www.devastatingexplosions.com/
        Top Documentary Films: http://topdocumentaryfilms.com/
        Bored: http://bored.overnow.com/
        This is Sand: http://thisissand.com/
        Making Music with Coke: http://www.makingmusicwithcoke.com/
        8tracks: http://8tracks.com/
        Instead of TV, you should watch... http://unplugthetv.com/
        SLC Punk!: http://www.youtube.com/watch?v=mqduWjRuRW4
        You Offend Me You Offend My Family: http://youoffendmeyouoffendmyfamily.com/
        LIFE: http://life.time.com/
        Lifehacker: http://lifehacker.com/
        Observatory: http://observatory.designobserver.com/
        Pooh's Corner: http://poohbear120mm.tumblr.com/
        Laughing Squid: http://laughingsquid.com/
        I love charts: http://ilovecharts.tumblr.com/
        Neatorama: http://www.neatorama.com
        Twaggies: http://twaggies.com/
        INCREDIBOX: http://www.incredibox.fr/en/#/application
        Abobo's Big Adventure: http://www.abobosbigadventure.com/fullgame.php
        NetHack: http://www.nethack.org/
        WTF Mate?: http://www.endofworld.net
        superwhite: http://www.superwhite.cc/
        Moving Pictures: http://cinemagram.tumblr.com/
        Woah Dude: http://www.reddit.com/r/woahdude/
        Sistine Chapel Panorama: http://www.vatican.va/various/cappelle/sistina_vr/index.html
        Corporation Inc.: http://armorgames.com/play/7348/corporation-inc
        Attack of the Cute: http://attackofthecute.com/
        Pinterest: http://pinterest.com/
        The Kingdom of Loathing: http://www.kingdomofloathing.com/
        Hippo Coworker: http://hippocoworker.tumblr.com/
        I Waste So Much TIme: http://iwastesomuchtime.com/
        Super Mario Crossover: http://www.explodingrabbit.com/games/super-mario-bros-crossover
        Retro Junk: http://www.retrojunk.com
        Wonder How To: http://www.wonderhowto.com/
        E-Mails From an Asshole: http://dontevenreply.com/
        Hyperbole and a Half: http://hyperboleandahalf.blogspot.com/
        Axe Cop: http://axecop.com/
        Fuck Yeah Weird (NSFW): http://fuckyeahweird.tumblr.com/
        Red Meat: http://www.redmeat.com/redmeat/current/index.html
        How-To Videos: http://www.howcast.com/
        My Damn Channel: http://www.mydamnchannel.com/
        Dear Photograph: http://dearphotograph.com/
        1000 Awesome Things: http://1000awesomethings.com/
        Grantland: http://www.grantland.com/
        Big Think: http://bigthink.com/
        The Escapist: http://www.escapistmagazine.com/
        Retrocade: http://www.retrocade.net/
        Khan Academy: http://www.khanacademy.org/
        Mega Mash: http://www.nitrome.com/games/megamash/
        Endeavor: http://www.newgrounds.com/portal/view/555072
        Robot Unicorn Attack: http://games.adultswim.com/robot-unicorn-attack-twitchy-online-game.html
        Instructables: http://www.instructables.com/
        Ultimate Flash Sonic: http://www.mad4flash.com/classics/sonic-the-hedgehog.html
        Khan Academy: http://www.khanacademy.org/
        TED: http://www.ted.com/
        Unplug the TV: http://www.unplugthetv.com/
        Fucking Homepage: http://www.fuckinghomepage.com/
        If Everyone Knew: https://www.ifeveryoneknew.com/
        Free Rice: http://www.freerice.com/
        Lizard Point: http://www.lizardpoint.com/
        Math Run: http://www.mathrun.net/
        Open Culture: http://www.openculture.com/
        No Excuse List: http://www.noexcuselist.com/
        Sci Show: http://www.youtube.com/user/scishow/videos
        Crash Course: http://www.youtube.com/user/crashcourse/videos
        Minute Physics: http://www.youtube.com/user/minutephysics/videos
        Toonami Aftermath: http://www.toonamiaftermath.com/
        Pointer Pointer: http://www.pointerpointer.com/
		HexGL: http://hexgl.bkcore.com
		TV Without Context: http://neave.com/television/
		Super Mario 63: http://www.newgrounds.com/portal/view/498969
        """
#class Bored(callbacks.PluginRegexp):
#    """Gives a list of interesting sites on the web."""
#    threaded = True
#    
#    regexps = ['bored']
#    
#    def bored(self,irc,msg,match):
#        r'(.+)?([Ii]\'m|[Ii] am|[Ss]o|[Ii]m)(.+)?[Bb]ored(.+)?'
#        
#        plist = [x for x in stuff.split("\n") if len(x.strip())]
#        p = choice(plist)
#        irc.reply("Bored? Check out " + p.strip(),prefixNick=True)

class Bored(callbacks.Plugin):
    """Gives a list of interesting sites on the web."""
    threaded = True

    def bored(self, irc, msg, args):
        """
        A list of interesting sites on the web.
        """
        plist = [x for x in stuff.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply("Bored? Check out " + p.strip(),prefixNick=True)

Class = Bored

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79: