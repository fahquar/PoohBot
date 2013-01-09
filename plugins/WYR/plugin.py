
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

class WYR(callbacks.Plugin):
    """Add the help for "@plugin help Question" here
    This should describe *how* to use this plugin."""
    threaded = True

    wyrs = """
Be one meter taller, or one meter shorter?
Sleep with Cameron Diaz with no legs, or sleep with Liv Tyler with no eyes?
Have a pencil for a penis, or have a rather large butternut squash for a penis?
Have a blonde, fit, dumb wife, or have a ginger, ugly, highly intelligent wife?
Talk like Yoda, or breathe like Darth Vader for the rest of your life?
Be the giver, or be the taker?
Win $500 for yourself, or win $5,000 for charity?
Your mom didn't shave her legs, or your father shaved his?
Have the ability to fly, or have the ability to be invisible?
Be a Scouser, or be a Geordie?
Die drowning, or die in a fire?
Cheat on your partner, or find out your partner cheated on you?
Find out that your wife was actually your cousin, or find out your parents were cousins?
Live in Wank, a German ski resort, or Live in Spunkie, a small village near Glasgow?
Get drunk, or get stoned?
Have both your arms severed in an accident, or have your genitalia severed in an accident?
Find out that your girlfriend was actually male, or find out that your boyfriend was actually female?
Be bald, or be ginger?
Have reversed knee joints, or have reversed elbow joints?
Have a foot long nose, or have a foot long tongue?
Weigh 500 lbs, or weigh 50 lbs?
Eat a block of butter, or eat a block of salt?
Live forever, or die tomorrow?
Have sneakers that are in style with holes in them and all dirty, or have not in style shoes that are perfectly clean and new?
Get really drunk, screw Pamela Anderson and forget, or get really stoned, screw Michael Jackson and remember it?
Catch your mother masturbating, or have your mother catch you masturbating?
Eat a human arm, or eat a cows brain?
Watch a movie with a picture and no sound, or watch a movie with sound and no picture?
Get kicked in the face by a horse, or get punched in the groin by a baby?
Spend 4 years in jail for something you never did, or spend 10 years in jail for something you did do?
Be a famous sports star, or be a famous actor?
Be color blind, or have no taste buds?
Jump off a cliff, or have a huge rock dropped on top of you?
Have loved and lost, or have never loved at all?
Be ginger, or be dead?
Sleep with Gary Busey, or sleep with Gary Coleman?
Live with wild animals till you die, or live with a serial killer and not even know it?
Have a foot long goatee, or have foot long eyebrows?
Have to say the phrase 'stone the crows' every ten minutes, or say the phrase 'heavens to betsy' every ten minutes?
Blow snot all over your date, or fart loudly while on the date?
Walk in on your parents having sex, or have your parents walk in on you having sex?
Be in a chamber of 100 giant mosquitoes for a week, or wear a poison ivy suit for a month?
File your teeth down to the gums, or file your fingertips down to the bone?
Lose all your money, or lose the person you love most?
Be blind and deaf, or live with a second head on your body?
Have one really close best friend, or have lots of casual friends?
Change your name to Axewound or Pissflap?
Have your eyes and nipples change places, or have your nose and your perineum change places (look it up)?
Be Christina Hendricks' wonderbra, or be Jennifer Lopez's bike seat?
Be a high tech pair of long handled pruning shears, or be an old fashioned garden rake?
Be keen ,eager, and fucking useless, or be talented but unmotivated?
Have glow sticks as fingers, or pom-poms as hands?
Be half women, half man, or be a midget?
Watch a porn movie with your parents, or watch a porn movie starring your parents?
Shave your head, or lose your pinky fingernail for life?
Every time you entered a room, Darth Vader's theme song is played from your crotch, or have genitals that glow like E.T.'s heart whenever you are attracted to someone?
Never be able to taste, or never be able to smell?
Have one testicle the size of a football, or 30 testicles the size of peas?
Have to chew every mouthful for 15 minutes, or never be able to chew at all?
Have 3 tiny eyes, or have one massive eye?
Have your body covered with scales, or have your body covered with fur?
Have too much skin, or not have enough skin?
Be permanently cold, or be permanently hot?
Be sick (puking) for the rest of your life, or never brush your teeth again for the rest of your life?
Fall out the ugly tree, or be hit with the ugly spade?
Fire your boss, or have your boss fire you?
Not be anatomically correct (think barbie and ken), or have no face?
Die a fast, but really painful death, or live a long boring life?
Have no eyebrows, or have no fingernails?
Fart while having sex with your dream person, or have your dream person fart while having sex?
Read a WYR so sick that you cry, or read a WYR so sick that you actually puke?
Have hands as big as tables, or feet as big as tables?
Be a significant nobody, or be an insignificant somebody?
Be dumped by his/her best friend, or be dumped by text message?
Have sex with your unexperienced boyfriend/girlfriend, or with his/her experienced best friend?
Be on top, or be on the bottom?
Never have sex again, or have sex with a walrus once?
Eat a peanut butter and jelly sandwich, or eat a ham sandwich?
Always have to sneeze, or always have to poop?
Never brush your teeth, or never wash your face?
Marry an extremely attractive poor person, or a very obese, unclean, unattractive wealthy person?
Be a ninja, or be a pirate?
Be a heavyweight boxer, or be a formula one driver?
Dress like The Darkness, or dress like MC Hammer?
Look like Macy Gray, or Sing like Macy Gray?
Die a virgin at age 70, or die at age 30 doing it twice a day?
Freeze to death, or die in the desert?
Have 3 average sized female boobs, or have your butt in front and your crotch in the back?
Date Britney Spears, or date Christina Aguilera?
Have sex in the bathroom, or have sex in front of your parents?
Dance if I asked you to dance, or cry if I asked you to cry?
Freeze to death, or burn to death?
Your nose constantly bled, or ears constantly bled?
Be an average football player, or be the world's best Yo-Yoer?
Be Peter Beardsley, or be a beard?
Be John Barnes, or be John Noakes?
Marry Britney Spears for 55 hours, or never get married at all?
Sleep forever, or never sleep again?
Have Breakfast at Tiffany's, or be Livin' on a Prayer?
Eat broken glass, or gargle sulphuric acid?
Send a mouse into space, or save starving people?
Feel it in your fingers, or feel it in your toes?
Have love all around you, or be on the highway to hell?
Fight a shark, or fight a bear?
Smell like shit, or smell like rotting flesh?
Be Hugh Grant, or be Hugh Jass?
Be John Barnes, or be John Craven?
Be chased by a bear you have seen, or run away from a bear you have not seen?
Be covered in treacle and stung to death by bees, or be covered in honey and eaten by bears?
Wear unfashionable clothes, or have a terrible haircut?
Be raised by wolves, or reared by apes?
Be J-Lo's personal nipple tweaker, or Halle Berry's bikini-line waxer?
Run with the fox, or hunt with the hounds?
Have a third nipple, or have an extra toe?
Have no teeth, or have an extra finger?
Float like a butterfly, or Sting like a bee?
Know when you will die, or know how you will die?
Have pies for eyes, or chips for lips?
Always take a cold shower, or sleep an hour less than you need to be fully rested?
Always get first dibs, or the last laugh?
Give up your computer forever, or Tv forever?
Always have to say everything on your mind, or never speak again?
Always lose, or never play?
Always wear earmuffs, or a nose plug?
Always win pie-eating contests, or always win wheelbarrow races?
Be 3 feet tall, or 8 feet tall?
Be 3 feet taller, or 3 feet shorter?
Be a deep sea diver, or an astronaut?
Be a dog named Killer, or a cat named Fluffy?
Be a giant hamster, or a tiny rhino?
Be a tree, or live in a tree?
Be able to hear any conversation, or take back anything you say?
Be able to read everyone's mind all the time, or always know their future?
Be able to stop time or fly?
Be an unknown minor league basketball player, or a famous professional badminton star?
Be born with an elephant trunk, or a giraffe neck?
Be forced to tell your best friend a lie, or tell your parents the truth?
Be forgotten, or hatefully remembered?
Be go about your normal day naked, or fall asleep for a year?
Be gossiped about, or never talked about at all?
Be hairy all over, or completely bald?
Be happy for 8hrs/day and poor, or sad for 8hr/day and rich?
Be invisible, or be able to read minds?
Be rich and ugly, or poor and good looking?
Be stranded on an island alone, or with someone you hate?
Be the most popular, or the smartest person you know?
Be the sand castle, or the wave?
Eat a bar of soap, or drink a bottle of dishwashing liquid?
Eat a handful of hair, or lick three public telephones?
Eat a stick of butter, or a gallon of ice cream?
Eat a stick of margarine, or five tablespoons of hot pepper sauce?
Eat poison ivy, or a handful of bumblebees?
End hunger, or hatred?
Find true love, or 10 million dollars?
Forget who you were, or who everyone else was?
Get caught singing in the mirror, or spying on your crush?
Get even, or get over it?
Give bad advice, or take bad advice?
Give up your computer, or your pet?
Go to an amusement park, or to a family reunion?
Go without television, or junk food for the rest of your life?
Have a beautiful house and ugly car, or an ugly house and beautiful car?
Have a kangaroo, or koala as your pet?
Have a missing finger, or have an extra toe?
Have one wish granted today, or three wishes granted in 10 years?
Have x-ray vision, or bionic hearing?
Invent a cure for cancer, or a cure for AIDS?
Kiss a jellyfish, or step on a crab?
Know it all, or have it all?
Live without music, or live without T.V.?
Love and not be loved back, or be loved but never love?
Make headlines for saving somebody's life, or winning a nobel prize?
Meet an alien visitor, or travel to outer space?
Never use the internet again, or never watch TV again?
Not be able to use your phone, or your e-mail?
Only be able to whisper, or only be able to shout?
Own a ski lodge, or a surf camp?
Publish your diary, or make a movie on your most embarrassing moment?
Spend the day surfing the internet, or the ocean?
Sweat moderately but constantly 24 hours a day all over your body, or have a metal pin in your jaw that constantly picks up talk radio stations?
Sit next to someone on a bus, who looks at you then moves seat, or have someone in a car look at you, then turn around and lock their door?
Spend your last night alive going out to dinner with your closest friends, or have it with your favorite movie star?
Have to spend the next year repeating the fourth grade (at your current age), or spend a month in jail for a crime you did not commit?
Have a third leg, or a third arm?
Live as a dog, or live as a cat?
Live as a lion, or live as a tiger?
Watch a horror movie with 10 friends, or try and survive a horror film with your 3 closest friends?
Be a child forever, or an adult?
Be smart, or pretty for the rest of your life?
Live in Monopoly City, or a Ghetto City?
Be cheated on, or cheat on somebody?
Would you rather accidentally slam your hand down on a telephone message spike, or get the tips of your fingers caught in a paper shredder?
Chew the beak off of a chicken, or bite the legs off half a dozen mice?
Drink a gallon of dirty denture water, or lick a NY cab driver's seat in July?
Choose to see your future (without being able to change it), or know everyone else's future and not be able to tell them?
Have your nipple ring yanked out, or have to lift 20 lbs with your nose ring?
Always feel like you have to pee but you don't really have to, or never know when you have to go?
Wake up after sleepwalking to find yourself standing in the middle of a freeway, or on a window ledge 40 stories up?
Have a sex change, or change sexual preference?
Wake up and find every person you've ever known gone from Earth, or wake up and be 85 years old?
Be a woman trapped inside a man's body, or a man trapped inside a woman's body?
Get caught by your boss masturbating in your favorite superhero outfit, or screwing his/her spouse?
Be fed feet first into a wood chipper, or run over feet first by a steam roller?
Have your breath smell like a bad fart, or have your laugh sound like a fart?
Not try to save someone in an accident in which the person dies, or save him/her and be a hero, but lose a hand in the process?
Have a plugged nose, or perpetually plugged ears?
Pick your nose in public and eat it, or pick someone else's nose in public?
Have ten seconds to get as far away as you can (or find shelter) from a bomb made of 100 sticks of dynamite, or have ten minutes to get as far away as possible (or find shelter) from an atomic bomb?
Wake up nude and unharmed on a park bench and have no idea how you got there, or expecting a costume party, dress as a giant banana for a black tie affair and have to stay the whole night?
Take a full swing of a baseball bat to the kneecap, or forcefully run a razorblade along both your top and bottom gum lines?
While looking up have a bird poop in your mouth, or your eye?
Have both your new bf/gf hear your parents having screaming sex, or have your parents hear you and your partner having screaming sex?
Be known as the dumber identical twin, or the uglier one?
Be buried alive, or eaten alive?
After flirting with the cute store clerk, realize you had a slight string of snot stretching from your nose to your ear, or a tiny spot of poop on your cheek from playing with your dog earlier?
Have science empirically confirm the existence of God, or find the cure for cancer?
Live the rest of your life as the opposite sex, or start over as a little kid?
Take a nasty steamer at your date's house on the first date only to find that the toilet won't flush, or throw up in your date's new car on the first date?
Be directly responsible for the death of a beloved celebrity and have everyone know it, or be responsible for the death of a carload of people and have nobody find out?
If your life (and your competitor's) depended on victory, have to run a 100 yard race against a 6th grader, or against your own 11 year old dog?
Have to spend an entire pro basketball game with your face sticking right above the rim, or an entire hockey game with your face sticking out into the middle of the goal net?
As a woman, have enormous hands and feet, or a big rear end?
Eat 15 feet of aluminum foil, or swallow six steel guitar strings?
Be left at the alter, or have your spouse leave a month after the wedding?
Be thought of as a bumbling, incompetent fool by everyone you work with, or as sexually inadequate by everyone you've slept with?
Have a firecracker blow up in your mouth, or drill a small hole in your own forehead?
Lock your keys in the car for an hour with the motor running, while it sits in an intersection blocking traffic near your home (WHY is it in the middle of the intersection??), or have it reported in the local newspaper that you ere injured from falling off the toilet?
Lick up someone else's vomit, or let someone urinate in your mouth (and swallow it)?
Live in a world where nobody cleans up after his dog, or everybody, including you, has to do it bare-handed?
As a man, lose one testicle permanently, or grow another set of them?
Have a lisp, or a wandering eye?
Eat chewed food out of a randomly chosen stranger's mouth, or drink the remainder of ten randomly selected bottles you find in an inner city block?
Have kids who are very smart but don't do well socially, or who are popular and engaging but are C and D students?
Be married to someone who immediately balloons up 100 lbs within the first year, or to someone who develops an extraordinary amount of intestinal gas, but refuses to go to the doctor for the condition?
As a woman, breastfeed a seventy-year-old man, or breastfeed a chimp?
Spend a week at school in nothing but your underwear, or attend two classes completely nude?
Drink the water from the hot tub after a fraternity party, or drink Mexican tap water?
As a man, crap a softball, or pee a marble?
Get caught masturbating by your mother, or catching your mother masturbating?
Cheat on your spouse and have nobody know, or not cheat and have everything think that you did?
Be cleaning your gun and accidentally very slightly wound your ten-year-old child, or be cleaning your gun and killing that child's dog that he/she has had since birth?
As a firefighter, not be able to save anyone in a burning house, or in attempting to save an entire family, be forced to make the decision to leave behind the youngest child?
Wake up hungover in bed and roll over and see your boss, or roll over and see someone you don't recognize?
Have to use a toilet that is unbelievably filthy and gross, or use one that's clean but has six small jumping fish in it?
Have fantastic meals but vomit after each one, or always have to eat food you hate?
Lose the ability to taste food, or lose the ability to feel sexual pleasure?
Have the fingers of your left hand cut off one by one with a cigar slicer, or have your left eye scooped out with a spoon?
Be the top scientist in your feild, or get mad cow disease?
    """

    def wyr(self, irc, msg, args, victim):
        """[<target>]
            
        Asks a random "would you rather" from a list.
        """
        plist = [x for x in WYR.wyrs.split("\n") if len(x.strip())]
        p = choice(plist)
        if not victim:
            irc.reply("Would you rather... " + p.strip(), prefixNick=True)
        else:
            irc.reply(format('%s: Would you rather... %s ', victim, p.strip()),
                      prefixNick=False)
    wyr = wrap(wyr, [additional('text')])

Class = WYR

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
