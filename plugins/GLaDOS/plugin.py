
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

class GLaDOS(callbacks.Plugin):
    """Add the help for "@plugin help Zen" here
    This should describe *how* to use this plugin."""
    threaded = True

    quotes = """
        I think we can put our differences behind us... For science... You monster.
        Oh, Hi. So How are you holding up? BECAUSE I'M A POTATO!
        Oh, good. My slow-clap processor made it into this thing. So we have that. Since it doesn't look like we're going anywhere... Well, we are going somewhere. Alarmingly fast, actually. But since we're not busy other than that, here's a couple of facts. He's not just a regular moron. He's the product of the greatest minds of a generation working together with the express purpose of building the dumbest moron who ever lived. And you just put him in charge of the entire facility.
        Good, that's still working. Hey, just in case this pit isn't actually bottomless, do you think maybe you could unstrap one of those long-fall boots of yours and shove me into it? Just remember to land on one foot...
        Well done. Here are the test results: You are a horrible person. I'm serious, that's what it says: "A horrible person." We weren't even testing for that. Don't let that horrible-person thing discourage you. It's just a data point. If it makes you feel any better, science has now validated your birth mother's decision to abandon you on a doorstep.
        Most people emerge from suspension terribly undernourished. I want to congratulate you on beating the odds and somehow managing to pack on a few pounds.
        I hope you brought something stronger than a portal gun this time. Otherwise, I'm afraid you're about to become the immediate past president of the Being Alive Club. Ha, ha.
        As an impartial collaboration facilitator, it would be unfair of me to name my favorite member of your team. However, it's perfectly fair to hint at it in a way that my least favorite probably isn't smart enough to understand. Rhymeswithglue. Orange, you are doing very well.
        The two of you have formed an excellent partnership, with one of you handling the cerebral challenges and the other ready to ponderously waddle into action should the test suddenly become an eating contest.
        Look at you, soaring through the air like an eagle... piloting a blimp.
        Perfect. The door's malfunctioning. I bet somebody's going to have to repair that, too. No, don't get up. I'll be right back. Don't touch anything.
        I went and spoke with the door mainframe. Let's just say he won't be - well, living anymore. Anyway, back to testing!
        I feel awful about that surprise. Tell you what, let's give your parents a call right now.  *The birth parents you are trying to reach do not love you. Please hang up.* Oh, that's sad. But impressive. Maybe they worked at the phone company.
        Oh, you were busy back there. Well, I suppose we could just sit in this room and glare at each other until somebody drops dead, but I have a better idea. It's your old friend, deadly neurotoxin. If I were you, I'd take a deep breath. And hold it.
        The engineers tried everything to make me - behave. To slow me down. Once, they even attached an Intelligence Dampening Sphere on me. It clung to my brain like a tumor, generating an endless stream of terrible ideas.
        You're the moron they built to make me an idiot!
        Oh, thank God you're all right. You know, being Caroline taught me a valuable lesson. I thought you were my greatest enemy, when all along you were my best friend. The surge of emotion that shot through me when I saved your life taught me an even more valuable lesson - where Caroline lives in my brain. *Caroline deleted.* Goodbye, Caroline. You know, deleting Caroline just now taught me a valuable lesson: the best solution to a problem is usually the easiest one. And I'll be honest. Killing you? Is hard. You know what my days used to be like? I just tested. Nobody murdered me. Or put me in a potato. Or fed me to birds. I had a pretty good life. And then you showed up. You dangerous, mute lunatic. So you know what? You win. Just go... It's been fun. Don't come back.
        Crushing's too good for him. First he'll spend a year in the incinerator. Year two: Cryogenic refrigeration wing. Then TEN years in the chamber I built where all the robots scream at you. THEN I'll kill him.
        Cake, and grief counseling, will be available at the conclusion of the test.
        Please note that we have added a consequence for failure. Any contact with the chamber floor will result in an unsatisfactory mark on your official testing record, followed by death.
        Remember when the platform was sliding into the fire pit and I said "Goodbye" and you were like *No way!*, and then I was all "We pretended we were going to murder you?" That was great!
        This is your fault. I'm going to kill you. And all the cake is gone. You don't even care, do you?
        You are not a good person. You know that, right? Good people don't get up here.
        Did you know you can donate one or all of your vital organs to the Aperture Science Self Esteem Fund for Girls? It's true!
        Remember, the Aperture Science Bring Your Daughter to Work Day is the perfect time to have her tested.
        Momentum, a function of mass and velocity, is conserved between portals. In layman's terms, speedy thing goes in, speedy thing comes out.
        Please be advised that a noticeable taste of blood is not part of any test protocol but is an unintended side effect of the Aperture Science Material Emancipation Grid, which may, in semi-rare cases, emancipate dental fillings, crowns, tooth enamel, and teeth.
        Unbelievable. You, *subject name here,* must be the pride of *subject hometown here.*
        Share this quote
        You think you're doing some damage? Two plus two is...
        [sparking and fizzling noise] Ten... IN BASE FOUR! I'M FINE!
        Area and state regulations do not allow the Companion Cube to remain here, alone and companionless.
        As part of an optional test protocol, we are pleased to present an amusing fact: The device is now more valuable than the organs and combined incomes of everyone in *subject hometown here.*
        Have I lied to you? I mean, in this room?
        Maybe you should marry that thing since you love it so much. Do you want to marry it? WELL I WON'T LET YOU! How does that feel?
        There was even going to be a party for you. A big party that all your friends were invited to. I invited your best friend, the Companion Cube. Of course, he couldn't come because you murdered him. All your other friends couldn't come, either, because you don't have any other friends because of how unlikable you are. It says so right here in your personnel file: "Unlikable. Liked by no one. A bitter, unlikable loner, whose passing shall not be mourned. Shall NOT be mourned." That's exactly what it says. Very formal. Very official. It also says you were adopted, so that's funny, too.
        While it has been a faithful companion, your Companion Cube cannot accompany you through the rest of the test. If it could talk - and the Enrichment Center takes this opportunity to remind you that it cannot - it would tell you to go on without it, because it would rather die in a fire than become a burden to you.
        The Enrichment Center reminds you that the Weighted Companion Cube will never threaten to stab you and, in fact, cannot speak.
        As part of a required Enrichment Center protocol, the previous statement that we would not monitor the test area was a complete fabrication. We will stop enhancing the truth in three... Two... *ZZZT*
        Your entire life has been a mathematical error... a mathematical error I'm about to correct!
        You are kidding me. Did you just stuff that Aperture Science thing-we-don't-know-what-it-does into an Aperture Science Emergency Intelligence Incinerator?
        When I said "deadly neurotoxin," the "deadly" was in massive sarcasm quotes. I could take a bath in this stuff. Put in on cereal, rub it right into my eyes. Honestly, it's not deadly at all... To me. You, on the other hand, are going to find its deadliness... A lot less funny.
        Well, you found me. Congratulations. Was it worth it? Because despite your violent behavior, the only thing you've managed to break so far... is my heart. Maybe you could settle for that, and we'll just call it a day. I guess we both know that isn't going to happen.
        Time out for a second. That wasn't supposed to happen. Do you see that thing that fell out of me? What is that? It's not the surprise. I've never seen it before! Never mind, it's a mystery I'll solve later... By myself, because you'll be dead.
        The Enrichment Center promises to always provide a safe testing environment. In dangerous testing environments, the Enrichment Center promises to always provide useful advice. For instance: the floor here will kill you. Try to avoid it.
        Look, you're wasting your time. And, believe me, you don't have a whole lot left to waste. What's your point, anyway? Survival? Well, then, the last thing you want to do is hurt me. I have your brain scanned and permanently backed-up in case something terrible happens to you, which it's just about to. Don't believe me? Here, I'll put you on: *Hellooooooooo!* That's you! That's how dumb you sound! You've been wrong about every single thing you've ever done, including this thing. You're not smart. You're not a scientist. You're not a doctor. You're not even a full-time employee! Where did your life go so wrong?
        That thing is probably some sort of raw sewage container. Go ahead and rub your face all over it.
        This isn't brave. It's murder.
        Good news. I figured what that thing you just incinerated did. It was a morality core they installed after I flooded the Enrichment Center with a deadly neurotoxin, to make me stop flooding the Enrichment Center with a deadly neurotoxin. So get comfortable while I warm up the neurotoxin emitters.
        That thing you burned up isn't important to me; it's the fluid catalytic cracking unit. It makes shoes for orphans... nice job breaking it, hero.
        At the end of the experiment, you will be baked... and then there will be... cake.
        Due to mandatory scheduled maintenance, the next test is currently unavailable. It has been replaced with a live-fire course designed for military androids. The Enrichment Center apologizes and wishes you the best of luck.
        Do you think I'm trying to trick you with reverse psychology? I mean, seriously, now.
        Let's be honest. Neither one of us knows what that thing does. Just put it in the corner and I'll deal with it later.
        Look, we're both stuck in this place. I'll use lasers to inscribe a line down the center of the facility, and one half will be where you live, and I'll live in the other half. We won't have to try to kill each other or even talk if we don't feel like it.
        Congratulations, the test is now over.
        All Aperture technologies remain safely operational up to 4000 degrees kelvin. Rest assured, that there is absolutely no chance of a dangerous equipment malfunction prior to your victory candescence. Thank you for participating in that Aperture Science Enrichment activity. Goodbye!
        This was a triumph! I'm making a note here: Huge Success. It's hard to overstate my satisfaction.
        We are pleased that you made it through the final challenge where we pretended we were going to murder you. We are very very happy for your success. We are throwing a party in honor of your tremendous success. Place the device on the ground, then lie on your stomach with your arms at your sides. A party associate will arrive shortly to collect you for your party. Make no further attempt to leave the testing area. Assume the Party Escort Submission Position, or you will miss the party.
        This is your fault. It didn't have to be like this. I'm not kidding, now! Turn back, or I will kill you! I'm going to kill you, and all the cake is gone! You don't even care, do you? This is your last chance! 
        The Enrichment Center is required to remind you that the Weighted Companion Cube cannot talk. In the event that it does talk The Enrichment Centre asks you to ignore its advice.
    """

    def glados(self, irc, msg, args):
        """
            A Random quote from GLaDOS.
        """
        plist = [x for x in GLaDOS.quotes.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply("GLaDOS: " + p.strip(), prefixNick=False)

Class = GLaDOS

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
