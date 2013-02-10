
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice
import random

class Question(callbacks.Plugin):
    """Add the help for "@plugin help Question" here
    This should describe *how* to use this plugin."""
    threaded = True

    questions = """
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
What do you do to deliberately impress others?
What will you never do?
Excluding romantic relationships, who do you love?
What is your earliest childhood memory?
What book has had the greatest influence on your life?
What three questions do you wish you knew the answers to?
What is the greatest peer pressure you've ever felt?
What's the biggest lie you once believed was true?
In your lifetime, what have you done that hurt someone else?
What's the best part of growing older?
What's been on your mind most lately?
What do you think is worth waiting for?
What chances do you wish you had taken?
Where else would you like to live?  Why?
What motivates you to go to work each day?
What do you wish you had done differently?
What is your greatest strength and your greatest weakness?
When was the last time you lied?  What did you lie about?
What made you smile this week?
What do you do with the majority of your money?
What motivates you to be your best?
When was the last time you lost your temper?  About what?
What will you never give up on?
When you look into the past, what do you miss the most?
How would you describe the past year of your life in one sentence?
What is the most spontaneous thing you've ever done?
What makes you uncomfortable?
If you had to move 3000 miles away, what one thing would you miss the most?
What worries you about the future?
What one 'need' and one 'want' will you strive to achieve in the next twelve months?
What life lessons did you have to experience firsthand before you fully understood them?
Do you like the city or town you live in?  Why or why not?
What's the best part of being you?
When you look back over the past month, what single moment stands out?
What do you do to relieve stress?
What is your happiest memory?
What is your saddest memory?
What would you like to change?
How many people do you love?
What's the best decision you've ever made?
What's your favorite true story that you enjoy sharing with others?
Right now, at this moment, what do you want most?
What are you waiting for?  How are you writing your life's story?
What makes love last?
What good comes from suffering?
What's the most important lesson you've learned in the last year?
Based on your current daily actions and routines, where would you expect to be in five years?
What was your last major accomplishment?
Through all of life's twists and turns who has been there for you?
What or who has been distracting you?
What are you looking forward to in the upcoming week?
Who is your mentor and what have you learned from them?
What are you uncertain about?
What do you think about when you lie awake in bed?
What's something most people don't know about you?
When you have a random hour of free time, what do you usually do?
What makes you weird?
If you could relive yesterday what would you do differently?
What do you do over and over again that you hate doing?
Would you rather your child be less attractive and extremely intelligent or extremely attractive and less intelligent?
What white lies do you often tell?
What is the biggest change you have made in your life in the last year?
What do you understand today about your life that you did not understand a year ago?
Whose life have you had the greatest impact on?
What did life teach you yesterday?
Who impresses you?
What have you done that you are not proud of?
When should you reveal a secret that you promised you wouldn't reveal?
How would you spend your ideal day?
What is the one primary quality you look for in a significant other?
What do you admire most about your mother and father?
What is the best advice you have ever received?
If you could live forever, would you want to?  Why?
If you had to be someone else for one day, who would you be and why?
What positive changes have you made in your life recently?
Who makes you feel good about yourself?
What is your biggest regret?
Which one of your responsibilities do you wish you could get rid of?
What's something you don't like to do that you are still really good at?
What type of person angers you the most?
What is missing in your life?
What is your most striking physical attribute?
What has fear of failure stopped you from doing?
Who would you like to please the most?
If you could go back in time and change things, what would you change about the week that just passed?
When you meet someone for the very first time what do you want them to think about you?
Who would you like to forgive?
At what point during the last five years have you felt lost and alone?
What is one opportunity you believe you missed out on when you were younger?
What do you want more of in your life?
What do you want less of in your life?
Who depends on you?
Who has had the greatest impact on your life?
Are you happy with where you are in your life?  Why?
In one year from today, how do you think your life will be different?
How have you sabotaged yourself in the past five years?
Other than money, what else have you gained from your current job?
Whom do you secretly envy?  Why?
In twenty years, what do you want to remember?
What are you most excited about in your life right now, today?
What experience from this past year do you appreciate the most?
What is the most enjoyable thing your family has done together in the last three years?
Why are my testicles covered in Cheez-Whiz?
How many hours of television do you watch in a week?  A month?  A year?
What is the biggest obstacle that stands in your way right now?
What do you sometimes pretend you understand that you really don't?
What do you like most about your job?  What do you dislike most about your job?
What's something new you recently learned about yourself?
In one sentence, how would you describe your relationship with your mother?
What was the most defining moment in your life during this past year?
What's the number one change you need to make in your life in the next twelve months?
What makes you feel secure?
What is your favorite sound?
This isn't a question, but I just wanted to tell you that citra has a massively huge penis.
Why isn't there a special name for the tops of your feet?
Why isn't there mouse-flavored cat food?
Can fat people go skinny-dipping?
If you throw a cat out of the car window, does it become kitty litter?
If you choke a Smurf, what color does it turn?
Can you cry under water?
How important does a person have to be before they are considered assassinated instead of just murdered?
Why do you have to "put your two cents in". but it's only a "penny for your thoughts"? Where's that extra penny going to?
Why does a round pizza come in a square box?
What disease did cured ham actually have?
How is it that we put man on the moon before we figured out it would be a good idea to put wheels on luggage?
Why is it that people say they "slept like a baby" when babies wake up like every two hours?
If a deaf person has to go to court, is it still called a hearing?
Why are you IN a movie, but you're ON TV?
Why do people pay to go up tall buildings and then put money in binoculars to look at things on the ground?
Why do doctors leave the room while you change? They're going to see you naked anyway.
Why is "bra" singular and "panties" plural?
Can a hearse carrying a corpse drive in the carpool lane?
Why does Goofy stand erect while Pluto remains on all fours? They're both dogs!
If Wyle E. Coyote had enough money to buy all that ACME crap, why didn't he just buy dinner?
Why do they call it an asteroid when it's outside the hemisphere, but call it a hemorrhoid when it's in your butt?
Ever wonder what the speed of lightning would be if it didn't zigzag?
How much deeper would the ocean be if sponges didn't live there?
I thought about how my mother fed me with a tiny spoon and fork, so I wonder what Chinese mothers use? Toothpicks?
If a person with multiple personalities threatens suicide, is that considered a hostage situation?
If a cow laughed, would milk come out of it's nose?
So what's the speed of dark?
After eating, do amphibians need to wait an hour before getting OUT of the water?
If you're sending someone some Styrofoam, what do you pack it in?
Whose cruel idea was it for the word "lisp" to have an "s" in it?
How come abbreviated is such a long word?
A bus station is where a bus stops. A train station is where a train stops. On my desk, I have a work station.
Is it OK to use the AM radio after noon?
What do chickens think we taste like?
What do people in China call their good plates?
What do you call a male ladybug?
What hair color do they put on the driver's license of a bald man?
When dog food is new and improved tasting, who tests it?
Why do they sterilize the needle for lethal injections?
Why do they call it a pair of pants, but only one bra?
Why do you need a driver's license to buy liquor when you can't drink and drive?
Why isn't phonetic spelled the way it sounds?
Why are there Interstates in Hawaii?
Why are there flotation devices in the seats of planes instead of parachutes?
Why are cigarettes sold at gas stations where smoking is prohibited?
Have you ever imagined a world without hypothetical situations?
How does the guy who drives the snowplow get to work?
If the 7-11 is open 24 hours a day, 365 days a year, why does it have locks on the door?
You know that indestructible black box that is used on airplanes? Why don't they make the whole plane out of that stuff?
If a firefighter fights fire and a crime fighter fights crime, what does a freedom fighter fight?
If they squeeze olives to get olive oil, how do they get baby oil?
If a cow laughs, does milk come out of her nose?
If you are driving at the speed of light and you turn your headlights on, what happens?
Why do they put Braille dots on the keypad of a drive-up ATM?
Why don't sheep shrink when it rains?
What would Geronimo say if he jumped out of an airplane?
Why are they called apartments when they are all stuck together?
If con is the opposite of pro, is Congress the opposite of progress?
If flying is so safe, why do they call the airport the terminal?
Why do toasters always have a setting that burns the toast to a horrible crisp which no decent human being would eat?
Why is there a light in the fridge and not in the freezer?
If Jimmy cracks corn and no one cares, why is there a song about him?
If the professor on Gilligan's Island can make a radio out of coconut, why can't he fix a hole in a boat?
Why does goofy stand erect while Pluto remains on all fours? They're both dogs!
What do you call male ballerinas?
Why ARE Trix only for kids?
If Wile E. Coyote had enough money to buy all that Acme crap, why didn't he just buy dinner?
Why is a person that handles your money called a 'Broker'?
If corn oil is made from corn, and vegetable oil is made from vegetables, then what is baby oil made from?
If a man is talking in the forest, and no woman is there to hear him, is he still wrong?
If electricity comes from electrons, does morality come from morons?
Is Disney World the only people trap operated by a mouse?
Why do the Alphabet song and Twinkle, Twinkle Little Star have the same tune?
Do illiterate people get the full effect of Alphabet Soup?
What is an occasional table the rest of the time?
If you get a beer belly by drinking beer, do you get a pot belly by smoking pot?
Why is Friday 13th considered unlucky, considering that the Last Supper was on Thursday?
If you can enjoy yourself, why can't you enjoy anyone else?
What would a burger of ham be called?
If dawn breaks, does dusk come together?
Why does 'dyslexia' have to be so hard to spell?
If you think you're a hypochondriac, then are you one or not?
If you try to fail, and succeed, which have you done?
How are children supposed to take medicine if it's meant to be kept out of their reach?
Why do people talk about 'girlie' things but never 'boyie' things?
If you sneezed on a computer, would it get a virus?
Can you dream of having a dream?
Why do we close doors and windows to reduce noise, considering that sound travels better through solids?
If Pinocchio said, "My nose is about to grow", what would happen?
What did the designer of the drawing board go back to when his/her original design was a failure?
What sort of a vehicle did those huge 300 kg tires that are used in the World's Strongest Man contests come off?
Why do we hang our clothes on a washing line and not a drying line?
Why do 'a fat chance' and 'a slim chance' mean the same thing?
Why does your nose run and your feet smell?
Why is 'abbreviation' such a long word?
Why are there seeds in seeded grapes, but no bones in a boned fillet?
When people go mental, why do they get physically violent?
Why do we never hear of people coming from 'left west' or 'right east'?
Who copyrighted the copyright symbol?
Why are the numbers on a calculator and a phone reversed?
Do fish ever get thirsty?
Can you get cornered in a round room?
What does OK actually mean?
Why do birds not fall out of trees when they sleep?
What came first, the fruit or the color orange?
What should one call a male ladybird?
If a person suffered from amnesia and then was cured would they remember that they forgot?
Can you blow a balloon up under water?
Why doesn't McDonald's sell hotdogs? 
At a movie theater which arm rest is yours? 
What is Satan's last name? 
Why do doctors leave the room when you change? They're going to see you naked anyway. 
Where does the toe-tag go on a dead person if they don't have toes? 
If your driving a federal owned car, and you run a stop sign, is it considered a felony? 
Why is there a disclaimer on the Allstate Auto Insurance commercials that says "Not available in all states"? 
If you dug a hole through the center of the earth,and jumped in, would you stay at the center because of gravity? 
If a person dies and then springs back to life, do they get their money back for the coffin? 
If you are asked to tell the truth, the whole truth and nothing but the truth and your the main witness, what if you say "no"? 
Do they bury people with their braces on? 
How far east can you go before you're heading west? 
How does a Real Estate company sell its office without causing confusion? 
Do dentists go to other dentists or do they just do it themselves? 
If, in a baseball game, the batter hits a ball splitting it right down the center with half the ball flying out of the park and the other half being caught, what is the final ruling? 
If you were to get drunk in a country where the drinking limit is under 21, and went to the states and were still over the limit, could they arrest you for underage drinking even though you did not do the drinking in the states. 
Why do people think that swaying their arm back and forth would change the direction of a bowling ball? 
If girls with large breasts work at Hooters, then do girls with one leg work at IHOP? 
Why is it that everyone driving faster than you is considered an idiot and everyone driving slower than you is a moron? 
If pro and con are opposites, wouldn't the opposite of progress be congress? 
Why does grape flavor smell the way it is when actual grapes don't taste or smell anything like it. 
If a kid refuses to sleep during nap time, are they guilty of resisting a rest? 
Is it rude for a deaf person to talk (sign) with their mouth full of food? 
If its 11:30 PM Dec 31 in Texas and 12:30 AM Jan 1st in New York and you have a New York driver's license that expires Jan 2007, does that mean your license has expired? 
What's the difference between normal ketchup and fancy ketchup? 
Why is the Lone Ranger called 'Lone' if he always has his Indian friend Tonto with him? 
When does it stop being partly cloudy and start being partly sunny?
Are eyebrows considered facial hair?
If a baby's leg pops out at 11:59PM but his head doesn't come out until 12:01, which day was he born on?
In the song Yankee Doodle, is he calling the horse or the feather "macaroni"? 
Is there a time limit on fortune cookie predictions? 
Since bread is square, then why is sandwich meat round? 
Do they have the word "dictionary" in the dictionary?
Can you daydream at night?
Why is it that on a phone or calculator the number five has a little dot on it? 
Can crop circles be square?
If ghosts can walk through walls and glide down stairs, why don't they fall through the floor? 
Is it legal to travel down a road in reverse, as long as your following the direction of the traffic?
When Atheists go to court, do they have to swear on the bible?
Why is vanilla ice cream white when vanilla extract is brown?
Can animals commit suicide? 
What do you do when you see an endangered animal that is eating an endangered plant?
If a doctor suddenly had a heart attack while doing surgery, would the other doctors work on the doctor or the patient?
How can something be "new" and "improved"? if it's new, what was it improving on?
Why aren't drapes double sided so it looks nice on the inside and outside of your home?
Why is it that when we "skate on thin ice", we can "get in hot water"?
Why do people say beans beans the magical fruit when beans are vegetables?
If laughter is the best medicine, who's the idiot who said they 'died laughing'? 
If money doesn't grow on trees then why do banks have branches? 
Why are the little styrofoam pieces called peanuts?
Why does the Easter bunny carry eggs? Rabbits don't lay eggs.
Do siamese twins pay for one ticket or two tickets when they go to movies and concerts?
Why are they called 'Jolly Ranchers'? Who said that the ranchers were jolly?
Why does caregiver and caretaker mean the same thing?
Can a short person "talk down" to a taller person? 
If a bald person works as a chef at a restaurant, do they have to wear a hairnet?
If milk goes bad if not refrigerated, does it go bad if the cow isn't refrigerated? 
How fast do hotcakes sell?
Do prison buses have emergency exits?
Do astronauts change their clocks when they move over different time zones in space?
Can a black person join the KKK?
When lightning strikes the ocean why don't all the fish die?
When there's two men who get married, do they both go to the same bachelor party?
If a guy that was about to die in the electric chair had a heart attack should they save him?
Why are there interstate highways in Hawaii?
Do Jewish vampires avoid crosses or Stars of David?
If London Bridge is standing why is there a song about it falling down?
Why is it that before 9/11 they always showed the emergency broadcast system test, and on 9/11 they never used it?
If a nursing mother had her nipples pierced would the milk come out of all three holes?
Who was Sadie Hawkins?
If a stripper gets breast implants can she write it off on her taxes as a business expense?
Why do we sing "Rock a bye baby" to lull a baby to sleep when the song is about putting your baby in a tree and letting the wind crash the cradle on the ground?
If parents say, "Never take candy from strangers" then why do we celebrate Halloween?
Do the minutes on the movie boxes include the previews, credits, and special features, or just the movie itself?
Is there ever a day that mattresses are not on sale?
What does PU stand for (as in "PU, that stinks!")?
Why do we put suits in a garment bag and put garments in a suitcase?
Can cannibals be arrested for being under the influence of alcohol (e.g. drunk-driving) if they have eaten someone who was drunk?
What is the stage of a reptile when it has eggs in it but they haven't been laid. Are they pregnant?
If Mars had earthquakes would they be called marsquakes?
Why do people never say "it's only a game" when they're winning?
If an ambulance is on its way to save someone, and it runs someone over, does it stop to help them?
Why is it called a funny bone, when if you hit it, it's not funny at all?
Do you yawn in your sleep?
Why do dogs like the smell of other dogs butts?
If a cannibal was on death row could he ask for the last guy that was electrocuted for his last meal?
Do Chinese people get English sayings tattooed on their bodies?
Do glow-in-the-dark objects stop glowing when somebody turns the lights on?
If you died with braces on would they take them off?
If someone has their nose pierced, have a cold, and take their nose ring out. Does snot come out of the piercing hole?
How come lemon washing up liquid contains real lemons, but lemon juice contains artificial flavorings.
Do you wake up or open your eyes first?
Did Noah have woodpeckers on the ark? If he did, where did he keep them?
Why are builders afraid to have a 13th floor but book publishers aren't afraid to have a Chapter 11?
How do you handcuff a one-armed man?
If the FBI breaks your door down do they have to pay for it?
In some books, why do they have blank pages at the very end?
Why can't donuts be square? 
Why put a towel in the dirty clothes basket if when you get out of the shower you are clean?
What happens to an irrisistable force when it hits an immovable object?
If there's a speed of sound and a speed of light is there a speed of smell?
Why do overalls have bel loops, since they are held up at the top by the straps?
Do people in prison celebrate halloween.... if so how? 
Do the security guards at airports have to go through airport security when they get to work?
Why are all of the Harry Potter spells in Latin if they're English?
What do Greeks say when they don't understand something? 
What happens if a queen gives birth to a pair of siamese twins? Who gets to be king?
Do all-boys schools have girls bathrooms? Conversely, do all-girls schools have boys bathrooms? 
Are children who act in rated 'R' movies allowed to see them?
How come cats butts go up when you pet them?
What would happen to the sea's water level if every boat in the World was taken out of the water at the same time?
How come you never see a billboard being put up by the highway? 
Do the English people eat English muffins, or are they just called muffins? 
How much deeper would the ocean be if sponges didn't grow in it?
Why do they call it the Department of Interior when they are in charge of everything outdoors?
Why does Jello have a smell when you add the powder in the water, but when it "gels" the smell is gone?
Why are dogs noses always wet? 
If a bee is allergic to pollen would it get the hives?
Why do people say "heads up" when you should duck?
Why is it OK for dudes to slap other dudes' asses in football, but not in any other situation? 
Why does triangularly cut bread taste better than square bread?
If one man says, "it was an uphill battle," and another says, "it went downhill from there," how could they both be having troubles?
Why does a round pizza come in a square box?
At what point in man's evolution did he start wiping his ass?
Do bald people get Dandruff?
Why is it that no matter what color bubble bath you use the bubbles are always white?
Why do superheroes wear their underwear on the outside of their clothes?
If you get cheated by the Better Business Bureau, who do you complain to?
When sign makers go on strike, is anything written on their signs? 
Why does someone believe you when you say there are four billion stars, but check when you say the paint is wet?
Can you cry under water? 
Why Does Pluto Live in a dog house, eat dog food, etc. but Goofy, who is also a dog, lives in a condo and drives a car?
If you blew a bubble in space would it pop?
Are children who use sign language allowed to talk with their mouth full?
How come all of the planets are spherical?
How did the first women ever to shave their legs know that the skin wouldn't just peel right off?
when a pregnant lady has twins, is there 1 or 2 umbilical cords?
Why doesn't Winnie the Pooh ever get stung by the bees he messes with?
Why do they put holes in crackers?
Can you still say "Put it where the sun don't shine " on a nude beach?
What do people in China call their good plates?
How come toy hippos are always blue, or purple, when real hippos are brown? 
Why don't woodpeckers get headaches when they slam their head on a tree all day?
If someone owns a piece of land, do they own it all the way to the center of the earth?
If an escalator breaks down, does it become stairs?
Why do they call him Donkey Kong if he is not a donkey?
Why do they say a football team is the 'world champion' when they don't play anybody outside the US? 
Do stuttering people stutter when they're thinking to themselves?
If you put a chameleon in a room full of mirrors, what color would it turn?
What are the handles for corn on the cob called?
Why do British people never sound British when they sing?
Why do we press the start button to turn off the computer?
Do your eyes change color when you die?
Were Mary and Joseph's surname Christ before Jesus was born?
If a bunch of cats jump on top of each other, is it still called a dog pile?
Do sheep get static cling when they rub against one another?
In libraries, do they put the bible in the fiction or non-fiction section?
How old are you before it can be said you died of old age?
If K.F.C Stands for Kentucky Fried Chicken, Why do they play sweet home Alabama on the commercials?
If people with one arm go to get their nails done, do they pay half price?
What type of animal is Snuffaluffagus?
If you had a three story house and were in the second floor, isn't it possible that you can be upstairs and downstairs at the same time?
Can a hearse carrying a corpse drive in the carpool lane?
If a king is gay and marries another guy what is that guy to the royal family?
Why do they call it "getting your dog fixed" if afterwards it doesn't work anymore?
Does a 'Marks-A-Lot' marker, mark any more than a regular marker?
If you really could dig a hole to China, and you did, and you fell in, would you stop in the middle because of gravity?
If the funeral procession is at night, do folks drive with their headlights off?
What happens when you put a lightsaber in water?
On Gilligan's Island, how did Ginger have so many different outfits when they were only going on a 3 hour tour? 
If I had my legs amputated, would I have to change my height and weight on my driver's license?
If nobody buys a ticket to a movie do they still show it?
How do you tell when you run out of invisible ink? 
Do movie producers still say lights, camera, and action when it is a dark scene?
What do you call male ballerinas? 
How does Freddy Kruger wipe his butt? 
Why people are so scared of mice,which are much smaller than us, when no one seems to be scared of Micky Mouse, who is bigger than us?
Why are the numbers on a calculator and a phone reversed?
Why are plastic bears the only animal you can get honey from? Why can't you get honey from a plastic bee? 
Can bald men get lice?
When your photo is taken for your driver's license, why do they tell you to smile? If you are stopped by the police and asked for your license, are you going to be smiling?
Do butterflies remember life as a caterpillar?
If you undergo chemotherapy do you lose your pubic hairs?
Why do people constantly return to the refrigerator with hopes that something new to eat will have materialized?
Does the postman deliver his own mail?
Why does toilet bowl cleaner only come in the color blue?
What happens when you put hand sanitizer on a place other then your hand?
Why are women and men's shoe sizes different?
Can you "stare off into space" when you're in space?
Where do people in Hell tell other people to go?
Is "vice-versa" to a dyslexic just plain redundant?
How come you can kill a deer and put it up on your wall. but it's illegal to keep one as a pet?
Why do we say we're head over heels when we're happy? Isn't that the way we normally are?
If prunes are dehydrated plums, where does prune juice come from? 
Is it appropriate to say "good mourning" at a funeral?
If there's an exception to every rule, is there an exception to that rule?
When you're caught "between a rock and a hard place", is the rock not hard?
Was Jesus a virgin when he died?
Why is there a light in the fridge and not in the freezer? 
Doesn't a lightning rod on top of church show a lack of faith?
Who coined the phrase, 'coined the phrase?'
If there were a thousand seagulls in an airplane while its flying, each weighing two pounds a piece, but they were all flying in the airplane, would the airplane weigh 2000 pounds more?
If you soak a raisin in water, does it turn back into a grape?
How important does a person have to be before they are considered assassinated instead of just murdered? 
Why do they call steam rollers, steam rollers? They don't produce, get rid of, or have anything to do with steam. 
What is another word for "thesaurus"?
What are the most intellectually stimulating websites you know of?
What's your secret that could literally ruin your life if it came out?
Could you destroy the entire Roman Empire during the reign of Augustus if I traveled back in time with a modern U.S. Marine infantry battalion or MEU?
What's a little-known site you think everyone should know about?
What is a "mind trick" you know of?
What little easter eggs on websites do you love?
Most embarrassing situation you've been in?
What's the most shocking thing you've ever caught a family member doing?
Would you support a regulated prostitution industry?
What is the most mundane thing/situation that always makes you horny for unknown reasons?
How old would you be if you didn't know how old you are?
Which is worse, failing, or never trying?
If life is so short, why do we do so many things we don't like and like so many things we don't do?
When it's all said and done, will you have said more than you've done?
What is the one thing you'd most like to change about the world?
If happiness was the national currency, what kind of work would make you rich?
Are you doing what you believe in, or are you settling for what you are doing?
If the average human life span was 40 years, how would you live your life differently?
To what degree have you actually controlled the course your life has taken?
Are you more worried about doing things right, or doing the right things?
You're having lunch with three people you respect and admire.  They all start criticizing a close friend of yours, not knowing she is your friend.  The criticism is distasteful and unjustified.  What do you do?
If you could offer a newborn child only one piece of advice, what would it be?
Would you break the law to save a loved one?
Have you ever seen insanity where you later saw creativity?
What's something you know you do differently than most people?
How come the things that make you happy don't make everyone happy?
What one thing have you not done that you really want to do?  What's holding you back?
Are you holding onto something you need to let go of?
If you had to move to a state or country besides the one you currently live in, where would you move and why?
Do you push the elevator button more than once?  Do you really believe it makes the elevator faster?
Would you rather be a worried genius or a joyful simpleton?
Why are you, you?
Have you been the kind of friend you want as a friend?
Which is worse, when a good friend moves away, or losing touch with a good friend who lives right near you?
What are you most grateful for?
Would you rather lose all of your old memories, or never be able to make new ones?
Is it possible to know the truth without challenging it first?
Has your greatest fear ever come true?
Do you remember that time 5 years ago when you were extremely upset?  Does it really matter now?
What is your happiest childhood memory?  What makes it so special?
At what time in your recent past have you felt most passionate and alive?
If not now, then when?
If you haven't achieved it yet, what do you have to lose?
Have you ever been with someone, said nothing, and walked away feeling like you just had the best conversation ever?
Why do religions that support love cause so many wars?
Is it possible to know, without a doubt, what is good and what is evil?
If you just won a million dollars, would you quit your job?
Would you rather have less work to do, or more work you actually enjoy doing?
Do you feel like you've lived this day a hundred times before?
When was the last time you marched into the dark with only the soft glow of an idea you strongly believed in?
If you knew that everyone you know was going to die tomorrow, who would you visit today?
Would you be willing to reduce your life expectancy by 10 years to become extremely attractive or famous?
What is the difference between being alive and truly living?
When is it time to stop calculating risk and rewards, and just go ahead and do what you know is right?
If we learn from our mistakes, why are we always so afraid to make a mistake?
What would you do differently if you knew nobody would judge you?
When was the last time you noticed the sound of your own breathing?
What do you love?  Have any of your recent actions openly expressed this love?
In 5 years from now, will you remember what you did yesterday?  What about the day before that?  Or the day before that?
Decisions are being made right now.  The question is:  Are you making them for yourself, or are you letting others make them for you?
Has anyone really been far even as decided to use even go want to do look more like?
How would you describe your future in three words?
What simple fact do you wish more people understood?
If you could do it all over again, would you change anything?
What's one downside of the modern day world?
What do you usually think about on your drive home from work?
What can someone do to grab your attention?
What is the most insensitive thing a person can do?
When did you first realize that life is short?
When was the last time you felt lucky?
When in your life have you been a victim of stereotyping?
What makes someone a hero?
Where do you spend most of your time while you're awake?
Now that it's behind you, what did you do last week that was memorable?
What stresses you out?
What could society do without?
What is the number one solution to healing the world?
What job would you never do no matter how much it paid?
What was the last thing you furiously argued about with someone?
What makes life easier?
What have you lost interest in recently?
What's a quick decision you once made that changed your life?
What do you know well enough to teach to others?
How do you deal with isolation and loneliness?
What is the closest you have ever come to fearing for your life?
What's something you wish you had done earlier in life?
Who or what is the greatest enemy of mankind?
What artistic medium do you use to express yourself?
Where or who do you turn to when you need good advice?
What is your favorite fictional story?  (novel, movie, fairytale, etc.)
What is your favorite quote?
When did you not speak up when you should have?
In what way are you your own worst enemy?
What confuses you?
What is the most recent dream you remember having while sleeping?
What is something you have always wanted since you were a kid?
What is your favorite time of the year?
What things in life should always be free?
How would an extra $1000 a month change your life?
What are you an expert at?
What questions do you often ask yourself?
What do you love to practice?
What is your favorite place on Earth?
What bad habits do you want to break?
What is the number one quality that makes someone a good leader?
Are you more like your mom or your dad?  In what way?
What specific character trait do you want to be known for?
What do you love to do?
How many hours a week do you spend online?
When was your first impression of someone totally wrong?
How much money per month is enough for you to live comfortably?
How many friends do you have in real life that you talk to regularly?
What are some recent compliments you've received?
What is your biggest phobia?
Who was the last person you said "I love you" to?
What is your biggest pet peeve?
What was the last thing that made you laugh out loud?
If I gave you $1000 and told you that you had to spend it today, what would you buy?
What music do you listen to to lift your spirits when you're feeling down?
What is the number one motivator in your life right now?
What celebrities do you admire?  Why?
In one word, how would you describe your childhood?
What recent memory makes you smile the most?
What is your favorite smell?
What simple gesture have you recently witnessed that renewed your hope in humanity?
What are the top three qualities you look for in a friend?
When was the last time you tried something new?
Who do you sometimes compare yourself to?
What's the most sensible thing you've ever heard someone say?
What gets you excited about life?
What life lesson did you learn the hard way?
What do you wish you spent more time doing five years ago?
Do you ask enough questions or do you settle for what you know?
Who do you love and what are you doing about it?
What's a belief that you hold with which many people disagree?
What can you do today that you were not capable of a year ago?
Do you think crying is a sign of weakness or strength?
What would you do differently if you knew nobody would judge you?
Do you celebrate the things you do have?
What is the difference between living and existing?
If not now, then when?
Have you done anything lately worth remembering?
What does your joy look like today?
Is it possible to lie without saying a word?
If you had a friend who spoke to you in the same way that you sometimes speak to yourself, how long would you allow this person to be your friend?
Which activities make you lose track of time?
If you had to teach something, what would you teach?
What would you regret not fully doing, being or having in your life?
Are you holding onto something that you need to let go of?
When you are 80-years-old, what will matter to you the most?
When is it time to stop calculating risk and rewards and just do what you know is right?
How old would you be if you didn't know how old you are?
Would you break the law to save a loved one?
What makes you smile?
When it's all said and done, will you have said more than you've done?
If you had the opportunity to get a message across to a large group of people, what would your message be?
If the average human lifespan was 40 years, how would you live your life differently?
What do we all have in common besides our genes that makes us human?
If you could choose one book as a mandatory read for all high school students, which book would you choose?
Would you rather have less work or more work you actually enjoy doing?
What is important enough to go to war over?
Which is worse, failing or never trying?
When was the last time you listened to the sound of your own breathing?
What's something you know you do differently than most people?
What does 'The American Dream' mean to you?
Would you rather be a worried genius or a joyful simpleton?
If you could instill one piece of advice in a newborn baby's mind, what advice would you give?
What is the most desirable trait another person can possess?
What are you most grateful for?
Is stealing to feed a starving child wrong?
What do you want most?
Are you more worried about doing things right, or doing the right things?
What has life taught you recently?
What is the one thing you would most like to change about the world?
Where do you find inspiration?
Can you describe your life in a six word sentence?
If we learn from our mistakes, why are we always so afraid to make a mistake?
What impact do you want to leave on the world?
What is the most defining moment of your life thus far?
In the haste of your daily life, what are you not seeing?
If life is so short, why do we do so many things we don't like and like so many things we don't do?
What lifts your spirits when life gets you down?
Have you ever regretted something you did not say or do?
Has your greatest fear ever come true?
Why do we think of others the most when they're gone?
What is your most beloved childhood memory?
Is it more important to love or be loved?
If it all came back around to you, would it help you or hurt you?
If you had the chance to go back in time and change one thing would you do it?
If a doctor gave you five years to live, what would you try to accomplish?
What is the difference between falling in love and being in love?
Who do you think stands between you and happiness?
What is the difference between innocence and ignorance?
What is the simplest truth you can express in words?
What gives your life meaning?
Can there be happiness without sadness?  Pleasure without pain?  Peace without war?
What's the one thing you'd like others to remember about you at the end of your life?
Is there such a thing as perfect?
To what degree have you actually controlled the course your life has taken?
What does it mean to be human?
If you looked into the heart of your enemy, what do you think you would find that is different from what is in your own heart?
What do you love most about yourself?
Where would you most like to go and why?
Is it more important to do what you love or to love what you are doing?
What do you imagine yourself doing ten years from now?
What small act of kindness were you once shown that you will never forget?
What is your happiest childhood memory?  What makes it so special?
Do you own your things or do your things own you?
Would you rather lose all of your old memories or never be able to make new ones?
How do you deal with someone in a position of power who wants you to fail?
What do you have that you cannot live without?
When you close your eyes what do you see?
What sustains you on a daily basis?
What are your top five personal values?
Why must you love someone enough to let them go?
Do you ever celebrate the green lights?
What personal prisons have you built out of fears?
What one thing have you not done that you really want to do?
Why are you, you?
If you haven't achieved it yet what do you have to lose?
What three words would you use to describe the last three months of your life?
Is it ever right to do the wrong thing?  Is it ever wrong to do the right thing?
How would you describe 'freedom' in your own words?
What is the most important thing you could do right now in your personal life?
If you could ask one person, alive or dead, only one question, who would you ask and what would you ask?
If happiness was the national currency, what kind of work would make you rich?
What is your number one goal for the next six months?
Would you ever give up your life to save someone else?
Are you happy with yourself?
What is the meaning of 'peace' to you?
What are three moral rules you will never break?
What does it mean to allow another person to truly love you?
Who or what do you think of when you think of love?
If your life was a novel, what would be the title and how would your story end?
What would you not give up for $1,000,000 in cash?
When do you feel most like yourself?
When you help someone do you ever think, "What's in it for me?"
What is your greatest challenge?
How do you know when it's time to continue holding on or time to let go?
How do you define success?
If someone could tell you the exact day and time you are going to die, would you want them to tell you?
If I could grant you one wish what would you wish for?
What have you read online recently that inspired you?
Why do religions that advocate unity divide the human race?
If you could live one day of your life over again, what day would you choose?
What can money not buy?
If you left this life tomorrow, how would you be remembered?
Beyond the titles that others have given you, who are you?
If you could live the next 24 hours and then erase it and start over just once, what would you do?
Is it possible to know the truth without challenging it first?
What word best describes the way you've spent the last month of your life?
What makes everyone smile?
What do you owe yourself?
What would your 'priceless' Mastercard-style commercial be?
Can you think of a time when impossible became possible?
What matter to you most in your life?
How have you changed in the last five years?
What are you sure of in your life?
When you think of 'home,' what, specifically, do you think of?
What's the difference between settling for things and accepting the way things are?
How many of your friends would you trust with your life?
What's your definition of heaven?
What is your most prized possession?
How would you describe yourself in one sentence?
What stands between you and happiness?
What makes a person beautiful?
Is there ever a time when giving up makes sense?
What makes you proud?
How do you find the strength to do what you know in your heart is right?
Where do you find peace?
When have you worked hard and loved every minute of it?
How short would your life have to be before you would start living differently today?
Is it better to have loved and lost or to have never loved at all?
What would you do if you made a mistake and somebody died?
Who do you trust and why?
If you were forced to eliminate every physical possession from your life with the exception of what could fit into a single backpack, what would you put in it?
When does silence convey more meaning than words?
How do you spend the majority of your free time?
Who do you think of first when you think of 'success?'
What did you want to be when you grew up?
How will today matter in five years from now?
How have you helped someone else recently?
What is your greatest skill?
Do you see to believe or believe to see?
How are you pursuing your dreams right now?
What's the next big step you need to take?
If today was the last day of your life, would you want to do what you are about to do today?
If today was the last day of your life, who would you call and what would you tell them?
Who do you dream about?
What do you have trouble seeing clearly in your mind?
What are you looking forward to?
What is the number one thing you want to accomplish before you die?
When is love a weakness?
What has been the most terrifying moment of your life thus far?
Who is the strongest person you know?
If you could take a single photograph of your life, what would it look like?
Is the reward worth the risk?
For you personally, what makes today worth living?
What have you done in the last year that makes you proud?
What did you learn recently that changed the way you live?
What is your fondest memory from the past three years?
What are the primary components of a happy life?
How would the world be different if you were never born?
What is your favorite song and why?
With the resources you have right now, what can you do to bring yourself closer to your goal?
What are your top three priorities?
Why do we idolize sports players?
What is the nicest thing someone has ever done for you?
What do you see when you look into the future?
What makes you angry?  Why?
What is the most valuable life lesson you learned from your parents?
What does love feel like?
What are your favorite simple pleasures?
If you could go back in time and tell a younger version of yourself one thing, what would you tell?
    """
        
    def question(self, irc, msg, args, victim):
        """[<target>]
            
        Asks a random question from a list.
        """
        colors = ("2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13")
        plist = [x for x in Question.questions.split("\n") if len(x.strip())]
        p = choice(plist)
        color = choice(colors)
        label = ircutils.bold(ircutils.mircColor('Question! ', color))
        if not victim:
        	victim = msg.nick
        irc.reply(format('%s%s: %s ', label, victim, p.strip()))
    question = wrap(question, [additional('text')])

Class = Question

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
