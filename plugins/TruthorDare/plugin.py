
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice
import random

class TruthorDare(callbacks.Plugin):
  """Add the help for "@plugin help Question" here
  This should describe *how* to use this plugin."""
  threaded = True
  dares = """
Take over my role for the next five minutes. Your job is to think of the questions.
Change your nick to WHINER and give it your best shot for 5 minutes.
Your dare is to add sex to every sentence. Example: How are you sex today?
Your dare is to pick three people from the room out and tell them what you really think about them.
Pretend you are your keyboard.. Tell the channel about your owners antics.
Describe yourself as if you were up for auction.
Sell yourself in an auction, take 15 minutes to describe all your finer points and why you're a prize for the highest bidder. You are the merchandise, the auctioneer and the one who has to close the deal.
Pick someone in the user list and perform a one sided scene with them of your choice. Make it good.
You are on the catwalk... ENTERTAIN US!: http://www.youtube.com/watch?v=39YUXIKrOFk 
You are now channel greeter for the next 30 minutes.. Make EVERYONE feel welcome.
You have to go to another room and recruit at least two more people for Truth or Dare. You have 10 minutes.
Lick the toes of the next five people to enter the room.
Use an entire paragraph to describe in detail how you're rubbing your own ankles.
Seduce the bot in the room, be very sexy.
Awww you have a cute pet spider named Earl, don't squash him, show people and tell them how much you love and care for him. Example (Earl is so cute all his warm eyes like watching everything)
Finish this Poem four times: Roses are Red, Violets are blue...
Three examples of "My Mom Told Me Not To".
Lick the feet of the person above you on the list. If no one is above you, lick PoohBot's feet.
Make out with someone in the room of the same gender.
Make out with someone in the room of the opposite gender.
Make out with someone in the room of the same gender.
Make out with someone in the room whose nick starts with the same first letter as yours.
Kiss the person below you on the list, and say you love them and you think they're sexy. If you are the last person on the list, PoohBot.
Tell someone (any gender) they're sexy.
Go into #reddit and scream out "someone shot me!", then do "/me dies" and leave.
Ask someone you don't know in chat for their phone number or Skype name.
Ask a random person in the chat if they want to make out. If they say yes, make out with them. 
Swap nicknames with someone else for 5 minutes.
Make someone ask someone out in the game, if they say yes you have to be their internet girlfriend/boyfriend for a least two weeks (or until that other person wants to break up). 
Call your crush on Skype and say they are sexy and or hot.
Call a random person on Skype from this room and say they're sexy and or hot.
Go up to someone in the chatroom and ask them out (does not matter the gender).
Hug the next five people who enter the chatroom.
Change your nick to "nicklebackfan", then go into #reddit and tell everyone that you are a born again Christian Republican, and that Twilight is your favorite book.
Change your nick to a "Zombie" version of your regular nick, and then go around the network biting people and yelling "BRRRRAAAAIIIINNNSSS" for the next hour.
Change your nick to iloverunfromnowhere, go into #mingle, and tell everyone how much you love runfromnowhere, how you want to have his children, etc.
You must listen to this for the entire 15 minute duration: http://goo.gl/JmLEj
		  """

  truths = """
Who is the one person you know that you would want to be in a serious relationship with?
Who is your one object of desire, and what would you do to them if you had the chance?
What is the strangest thing you have ever done to get a person's attention, and did it work?
If you were guaranteed an honest answer to any question from any person in the world, who and what would you ask, and why?
Did you ever get so drunk you did something that you regretted later? What did you do, exactly?
If you had the power to cancel three TV-shows, what shows would they be and why?
If you won an all expenses paid holiday to any three cities on this planet, what 3 cities would you like to visit and why?
If you found a wallet with 1000 dollars on the street and you knew it belonged to a rich person, would you return it to its owner? 
Have you ever gotten emotionally attached to someone you met online?
I want you to tell the room what you consider to be the best thing about being a man?
I want you to tell the room what you consider to be the best thing about being a woman?
If you were stranded on a desert island, who would you want to be stranded with and why?
If you were to have dinner with any four people you wanted, even people who are dead, what four people would you love to meet and have dinner with?
If someone asked you to become a stripper in an old folks home for $250 a night, would you do it?
What is the morally worst thing you have ever done in your life?
What would you really want to do but are afraid of doing it?
If you could do your life 'all over', what would you do different this time?
If you were to spend the next 3 months on a deserted island, what 5 items would you bring along?? (No real people)
If an 82 year old, extremely rich person asked you to marry him/her, knowing that all his/her millions of dollars would be yours in a few years, would you marry that person??
If you could ask the president of the U.S.A. a question, what would that question be?
If you could travel back in time, what (historic) event would you like to see witness "live" and why?? (E.g. the signing of the declaration of independence or a day at the circus of Rome)
Which cartoon-character looks the most like the "real" you?? And why is that??
Name one of your bad habits, and one of your good qualities,
What 3 body parts are you satisfied with?
If someone would ask you to host/produce your own TV-show, what kind of TV-show would you like to host or produce??
What is the oldest man/woman you have dated?
If you could write a letter to yourself and send it back in time to yourself what would it say and how old would you be?
If you could go back in history, and meet anyone at all, who would it be and why?
What is it that turns you on most about a certain race?
What color underwear do you have on right now?
Have you ever faked an orgasm?
Have you ever had a threesome or would you?
Would you ever date someone you met online?
Are you a member of the mile-high club?
Have you ever been skinny dipping?
Toe sucking is (1) disgusting, (2) all right occasionally depending on who it is, or (3) cant gets enough of it and it sends me through the roof.
If you could change your name, what would you change it to and why? 
If you could use any type of food in your sexual experience, what would it be and why? 
If you could be anywhere in the world right now, where would it be and why? 
If you could be any animal, what would you be and why? 
If you could be in any cartoon, which one would you be in?
If you had a half hour to live, what would you do? 
If you were on the menu, please describe yourself as a meal. 
Describe yourself as if you were writing a lonely hearts advert about yourself.
If you were given $100,000,000 to give up sex would you? (Including masturbation) 
What is the most taboo thing you have ever done that you swore you would never do? 
If you could win the lottery what's the first thing you would do?
Name three people in this room you would like have something more than a friendship with?
If you had one moment to relive, what would it be, and what would you do differently?
If you were a porn star, what would your name be?
Have you ever allowed yourself to be photographed nude? Tell us about it.
What is the most taboo thing you have ever done that you swore you would never do?
Choose different people from the channel to be the following: your husband/wife, your lover, your housekeeper, your best friend, and your boss. Who would you choose and why?
If you could describe yourself as a weather event, what would it be and why?
Would you ever date someone the same sex?
If you had to have ONE limb amputated, which one would you choose?
Who is the first person you think about in the morning?
Where would you want to be when you die?
What scares you the most?
What's the meanest (or nicest) thing anyone has done to (or for) you?
Have you ever gone a whole day without wearing underwear?
Which to you like better: no underwear or underwear?
If you could choose the gender you'd be before birth, what would you be (guy or girl)?
If you only had a couple of hours to live, what'd you do?
Who's the oldest person that you've seen naked?
What's the most embarrassing moment in your life?
Have you ever skinny-dipped? Would you ever?
What's the stupidest thing you've bought?
What's the strangest dream you've ever had?
What's your favorite thing about the opposite sex?
Would you rather have perfect: hair, face, legs, butt, abs, or thighs?
If you could kill anyone and get away with it, who would you kill and how would you do it?
If you and another person were the last people on earth, who would you want it to be?
What's one of your guilty pleasures?
What did you look like in 5th grade?
What was the worst thing you ever cooked/baked? What'd it taste like?
If someone made a movie about your life, what'd they call it?
What's the biggest lie you've ever told? Who was it to?
If you were stranded on an island with your crush, boyfriend, best guy friend, an ex, and you had a chance to get off the island alone, would you leave or stay?
What'd you buy if you could buy anything in the world for free?
What color is your underwear?
Have you ever bought anything at Victoria's Secret?
Pick three guys to be stuck on an island with.
What's your worst fear?
If you got a tattoo, where'd it be? What would the picture be?
Have you ever skinny-dipped? Would you ever?
What get's you first attracted to a person?
Do you prefer Boxers or Briefs or Nothing?
Pick one person you wouldn't mind chatting in private with?
What is the most embarrassing moment online?
Have you had phone sex with any of the people in this room? Tell us how many people, how long was the phone call?
Has anyone online made you cry or close to it? Who was the nick? 
If you had to be a member of the opposite sex, who in the room would you be?
Have you ever dreamed about someone on this server? Do they know?
What is the one thing you are still afraid of?
Which animal most resembles your personality?
Do you have a crush on someone in this room, right now?
Have you ever cross-dressed or worn undergarments of the opposite sex?
What's your idea about romance and dating?
If you were locked up in a room with some other person from this room, whom would you choose and why?
What attracts you most in a person of the opposite sex?
What is your idea about romance?
Have you ever had, or given thought, to the idea of a threesome?
Have you ever kissed someone of the same sex? Who?
Have you ever embarrassed yourself in front of someone you were interested in and what happened?
What is the stupidest thing you've done because someone dared you to?
If you could be a person that you know [of the opposite sex] for one day, who would you be and what would you do as them?
If you had 2 wishes that would expire after 24 hours what would they be?
Describe your worst experience online.
What's the "naughtiest" thing you've ever done or thought about?
What is your most embarrassing nickname? Explain how you got it if you got one or just give us a few of your pet names.
What is the biggest turn off a person can have?
What is abnormal about you? 
What would you say are your best physical and emotional attributes?
If you were invisible what is the first thing you would do?
What is the craziest thing you've done naked?
Out of all the people in this room how many have you dreamt of?
Describe how you like to kiss.
What kind of "toy" have you always wanted to have used but haven't? 
If you were on the menu, please describe yourself as a meal.
If you could pick anyone in the chatroom to date, who would it be?
If you could pick anyone in the chatroom to have a beer with, who would it be?
If you could pick anyone in the chatroom to travel to Mars with, who would it be?
If you could pick anyone in the chatroom to go on an adventure with, who would it be?
  		   """

  def truth(self, irc, msg, args, victim):
    """[<target>]
      
    Asks a random truth from a list.
    """
    label = ircutils.bold(ircutils.mircColor('Truth! ', '12'))
    plist = [x for x in TruthorDare.truths.split("\n") if len(x.strip())]
    p = choice(plist)
    if not victim:
    	victim=msg.nick
    	irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
    else:
      	irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
  truth = wrap(truth, [additional('text')])
  
  def dare(self, irc, msg, args, victim):
    """[<target>]
      
    Asks a random dare from a list.
    """
    label = ircutils.bold(ircutils.mircColor('Dare! ', '4'))
    plist = [x for x in TruthorDare.dares.split("\n") if len(x.strip())]
    p = choice(plist)
    if not victim:
    	victim=msg.nick
    	irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
    else:
    	irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
  dare = wrap(dare, [additional('text')])
  
  def truthordare(self, irc, msg, args, victim):
    """[<target>]
      
    Asks a random dare or truth from a list.
    """
    args = args
    msg = msg
    num = random.randint(0, 1)
    if num is 0:
    	label = ircutils.bold(ircutils.mircColor('Dare! ', '4'))
    	plist = [x for x in TruthorDare.dares.split("\n") if len(x.strip())]
    	p = choice(plist)
    	if not victim:
    		victim=msg.nick
      		irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
    	else:
      		irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
    elif num is 1:
    	label = ircutils.bold(ircutils.mircColor('Truth! ', '12'))
    	plist = [x for x in TruthorDare.truths.split("\n") if len(x.strip())]
    	p = choice(plist)
    	if not victim:
    		victim=msg.nick
      		irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
    	else:
      		irc.reply(format('%s%s: %s ', label, victim, p.strip()), prefixNick=False)
  truthordare = wrap(truthordare, [additional('text')])

Class = TruthorDare

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
