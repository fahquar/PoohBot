
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

class Simpsons(callbacks.Plugin):
    """Add the help for "@plugin help Zen" here
    This should describe *how* to use this plugin."""
    threaded = True

    quotes = """
Rev. Lovejoy: Thanks a lot, Marge. That was our only burlesque house.
Rev. Lovejoy: We're happier then Adam and Eve before Eve munched us all to hell.
Rev. Lovejoy: Today's Christian doesn't think he needs God. He's got his Hi-Fi, his boob tube, and his instant pizza pie...
Rev. Lovejoy: Get a divorce. Helen Lovejoy: Mmm-hmm. Marge: But isn't that a sin? Rev. Lovejoy: Marge, just about everything is a sin. (Holds up a Bible) You ever sat down and read this thing? Technically, we're not allowed to go to the bathroom.
Rev. Lovejoy: Eventually I stopped caring, but that was the 80's so nobody noticed.
Rev. Lovejoy: Oh, come on, Lisa. You're here for a reason. (Whispering) Is your father stealing bread? Lisa: Maybe. I don't watch him every minute.
Rev. Lovejoy: Ned, there's an oil stain in the parking lot that looks like St. Barnibus.
Rev. Lovejoy: C'mon boy, this is the spot, right here. That's a good boy, do your dirty, sinful business. Ned Flanders: Well, howdy, Reverend Lovejoy. Nice to see you there... on my lawn... with your dog.
Rev. Lovejoy: Wait a minute, this sounds like rock and or roll.
Rev. Lovejoy: ...and so in summary, there are only two real commandments and the other eight are just filler.
Rev. Lovejoy: It's all over, people! We don't have a prayer!
Rev. Lovejoy: Ned, have you thought about one of the other major religions? They're all pretty much the same.
Rev. Lovejoy: While I have no opinion for or against your sinful lifestyles, I cannot marry two people of the same sex no more than I can put a hamburger on a hotdog bun. Now, go back to working behind the scenes at every facet of entertainment!
Rev. Lovejoy: Once something has been approved by the Government, It's no longer immoral.
Rev. Lovejoy: Judgment Day is upon us. I warned you the Lord wouldn't stand for your minidresses and Beatle boots. But it's not too late to repent your sins and be embraced by the Almighty!
Rev. Lovejoy: ...And as we pass the collection plate, please give as if the person next to you was watching.
Rev. Lovejoy: We have some new pamphlets available in our church news rack including 'Bible Bafflers,' 'Satan's Boners' and 'Good Grief, More Satan's Boners' and for you teens, 'It isn't cool to fry in Hell.'
Rev. Lovejoy: I remember another gentle visitor from the heavens, he came in peace and then died, only to come back to life, and his name was *E.T. the Extra Terrestrial*. I loved that little guy.
Rev. Lovejoy: This so called new religion is nothing but a pack of weird rituals and chants designed to take away the money of fools. Let us say the Lord's prayer 40 times, but first let's pass the collection plate.
Rev. Lovejoy: Alright Hans, time to go. Hans Moleman: But he ate my last meal! Rev. Lovejoy: If that's the worst thing that happens to you today consider yourself lucky.
Rev. Lovejoy: Damn Flanders.
Superintendent Chalmers: Skinner! I warned you about interacting with students. I don't want to have to yell at you! Principal Skinner: You yell at me about everything. Superintendent Chalmers: Well I can't yell at anyone else. Teachers have a union. Student have parents. Principal Skinner: What about Willie? Superintendent Chalmers: I like Willie!
Superintendent Chalmers: I've had it with this school, Skinner. Low test scores, class after class of ugly, ugly children...
Superintendent Chalmers: Rest assured Mrs. Simpson we have a zero tolerance policy for this sort of thing when it occurs in front of witnesses.
Superintendent Chalmers: Why is it when I heard the word 'school' and the word 'exploded,' I immediately thought of the word 'SKINNER?'
Superintendent Chalmers: Steamed hams? Principal Skinner: It's an upstate New York term. Superintendent Chalmers: Well I'm from Utica, I've never heard of them. Principal Skinner: It's more of an Albany term.
Principal Skinner: So, what's the word down at one School Board Plaza? Superintendent Chalmers: We're dropping the geography requirement. The children weren't testing well. It's proving to be an embarrassment. Principal Skinner: Very good. Back to the three R's. Superintendent Chalmers: Two R's, come October.
Superintendent Chalmers: You have got to end this thing, Seymour. Principal Skinner: We're not coming down until our jobs are reinstated and you acknowledge and celebrate our love. Superintendent Chalmers: Seymour, no one would like to celebrate your love more than I, but I'm a public servant. I'm not permitted to use my own judgment in any way. Mrs. Krabappel: (Taking phone) Then let us take our case directly to the townspeople. Superintendent Chalmers: Oh, yeah, that'll be real productive. Who do you want to talk to first? The guy with a bumblebee suit, or the one with a bone through his hair? Sideshow Mel: (Indignant) My opinions are as valid as the next man's!
Superintendent Chalmers: Religion has no place in public schools the way facts have no place in organized religion.
Superintendent Chalmers: (After Principal Skinner said he was a virgin) Well, it's clear you've been falsely accused. Because no one... anywhere, ever... would pretend to be a 44 year-old virgin.
Homer: No offense Apu, but when they're handing out religions you must be out taking a whiz. Apu: Mr. Simpson, pay for your purchases and get out... and come again.
Apu: Thank you for coming. I'll see you in Hell.
Apu: Oh, what a surprise, Joe Jesus Jr. is going to set us all straight.
Apu: That's the thing with your religion, it's a real bummer. Ned Flanders: Even the sing-alongs? Apu: No, the sing-alongs are ok.
Apu: By the seven arms of Vishnu, I swear it. I am not a Hindu.
Apu: He slept, he stole, he was rude to the customers. Still, there goes the best damned employee a convenience store ever had.
Apu: I won't lie to you. On this job, you will be shot at. Each of these bullet wounds is a badge of honor... Here's a pointer, try to take it in the shoulder.
Apu: I have been shot eight times this year, and as a result, I almost missed work.
Apu: This is how you talk when you learn English from porno movies.
Apu: Apu Nahasapeemapetilon. Nigel: Hmm. Never fit on a marquee, love. From now on, your name is Apu de Beaumarchais. Apu: That is a great dishonor to my ancestors and my God, but okay!
Apu: Serving the customer is merriment enough for me. Thank you, come again. See? Most enjoyable.
Apu: Mr. Simpson, a *Twizzler* is not a sprinkle... a *Mounds* is not a sprinkle... a *Jolly Rancher* is NOT a sprinkle!
Apu: Yes! I am a citizen! Now, which way to the welfare office? I'm kidding, I'm kidding, I work, I work.
Apu: Yes, yes, I know the procedure for armed robbery. I do work in a convenience store, you know.
Apu: Clean up in... all the aisles.
Apu: Spit the grapes back in with the others.
Apu: When your woman is all peace and content, that means all hell is about to break loose.
Apu: You can apologize in Hell. Marge: I guess I could...
Apu: Please do not offer my God a peanut.
Apu: Please take the babies home. The porn customers are too nervous to make their move. (Camera shows Moe and a few other men in an aisle waiting) Moe: Come on!
Homer: Thanks. Are you sure you don't want to come? In a *Civil War* re-enactment we need lots of Indians to shoot. Apu: I don't know what part of that sentence to correct first, but I cannot come.
Apu: Poor Mr. Homer! Could it be that my snack treats are responsible for his wretched health? (A customer enters) Customer: Gimme some jerky. Apu: Would you like some vodka with that? Customer: What the hell, sure!
Apu: (Apu gets shot) Ahhhh! The searing kiss of hot lead... How I missed you! I mean, I think I'm dying.
Apu: Ooh, they used nylon rope this time. It feels so smooth against my skin. Almost sensuous.
Apu: Homer, you are asleep at your post! Now go change the expiration dates on the dairy products!
Lisa: Wow, a secret staircase. But what do you do if someone wants a non-alcoholic beer? Apu: You know, it's never come up.
Apu: Oooo, a head bag. These are chock full of... heady goodness.
Apu: This passport is a cheap forgery! A cheap $2,000 forgery!
Apu: Ok, you are banned from my store. You'll have to shop at the Kwik-E-Mart across the street from me. You know the much nicer, much newer one. Good day to you!
Apu: All Kwik-E-Mart employees must be skilled in the deadly arts.
Apu: You have made a very powerless enemy.
Apu: Thank you for knocking over my inventory. Please come again.
Apu: Hello? I am not interested in buying your house, but I would like to use your rest room, flip through your magazines, rearrange your carefully shelved items and handle your food products in an unsanitary manner. Ha! Now you know how it feels! (Runs off)
Homer: What's this again? Apu: A napkin, sir.
Apu: Be careful when we capture him! We cannot claim the reward unless we have 51% of the carcass.
Apu: Hey, hey, this is not a lending library. If you're not going to buy that thing put it down or I'll blow your heads off!
Apu: Silly customer, you cannot hurt a *Twinkie*!
Proctor: : All right, here's your last question. What was the cause of the Civil War? Apu: Actually, there were numerous causes. Aside from the obvious schism between the abolitionists and the anti-abolitionists, there were economic factors, both domestic and inter... Proctor: :Wait, wait... just say slavery. Apu: Slavery it is, sir.
Apu: I've just enrolled in a screenwriting class. I yearn to tell the story of an idealistic young Hindu, pushed too far by convenience store bandits. I call it 'Hands Off My Jerky, Turkey.'
Apu: Nickel off on expired baby food.
Selma: We own you like Siegfried owns Roy.
Patty: Lisa, this is going to slow for me, and I work at the D.M.V.
Patty: Hey, chunky with a pants of meat balls.
Homer: Patty! Selma! What a pleasant surprise! Patty: (Grunts) Whaddya know, he's wearing pants. Selma: I owe you a lunch.
Selma: I can't believe Homer ruined another family picnic. Homer: Hey, everybody pees in the pool. Patty: Not from the diving board!
Patty: We thought we'd stop by unexpectedly for dinner. Selma: Now bring us some extra chairs like a good blubber-in-law. Homer: Time to fertilize the lawn; a couple of 500 pound bags should do it!
Homer: It's a place I've never been before. Selma: The shower? Homer: Hey!
Patty: When are you going to wake up and smell your husband, Marge? Selma: Granted, you got some kids out of him. But when the seeds have been planted, you throw away the envelope!
Selma: (To Homer) Your neck looks like a sideways ass!
Selma: You tried to kill me. I want a separation.
Patty: (Showing slides) They say everyone can float in the dead sea. Selma sank straight to the bottom.
Patty: It's like he disappeared into FAT air. Homer: Hey, shut up!
Mr. Burns: Just sign this form, and the money will be yours. Muhahahahaha... Ahem. Sorry, I was just um, eh, um, thinking of something funny Smithers did today. Smithers: I didn't do anything funny today. Mr. Burns: Shut! up!
Mr. Burns: Are you acquainted with our state's stringent usury laws? Homer: Usury? Mr. Burns: Oh, silly me! I must've just made up a word that doesn't exist.
Mr. Burns: No, just give the great unwashed a pair of oversized breasts and a happy ending, and they'll oink for more every time.
Mr. Burns: This is a thousand monkeys working at a thousand typewriters. Soon, they'll have written the greatest novel known to mankind. (Reads one of the papers) 'It was the best of times, it was the blurst of times?' You stupid monkey! (The monkey screeches) Oh, shut up.
Mr. Burns: Who is that bookworm, Smithers? Smithers: Homer Simpson, sir. Mr. Burns: Simpson, eh? How very strange. His job description clearly specifies an illiterate!
Mr. Burns: Take a note! From now on, I'm only going to be good and kind to everyone. Smithers: I'm sorry sir, I don't have a pencil. Mr. Burns: Ehh, don't worry, I'm sure I'll remember it.
Mr. Burns: You know, Smithers, I think I'll donate a million dollars to the local orphanage... when pigs fly! (Pig sails across the sky) Smithers: Will you be donating that million dollars now, Sir? Mr. Burns: Nooo, I'd still prefer not.
Mr. Burns: Oh, General Kao, you're a bloodthirsty foe, but your chicken is delectable.
Smithers: Here are several fine young men who I'm sure are gonna go far. Ladies and gentlemen, *The Ramones*! Mr. Burns: Ah. These minstrels will sooth my jangled nerves. Joey Ramone: I'd just like to say this gig sucks! Johnny Ramone: Hey, up yours, Springfield! The Ramones: ONE-TWO-THREE-FOUR! (Music starts) Happy Birthday to you, Happy Birthday to you, Happy Birthday, Burnsie, Happy Birthday to you! C.J. Ramone: Go to Hell, you old bastard! (Mr. Burns is shaking with anger at his table) Marky Ramone: (After the curtain closes) Hey, I think they liked us! Mr. Burns: Have the *Rolling Stones* killed. Smithers: Sir, those aren't... Mr. Burns: Do as I say!
Mr. Burns: Ah, Smithers. You're the sober yin to my incorrigible yang.
Mr. Burns: Now that I'm Springfield's oldest man, I'm starting to realize I'm not a young man anymore.
Smithers: Look at all the wonderful things you have. Mr. Burns: *King Arthur's Excalibur*, the only existing nude photo of *Mark Twain*, and that rare first draft of *The Constitution* with the word 'suckers' in it. Mr. Burns: Yes, yes, yes. So what! Smithers: You want your bear, Bobo, don't you? Mr. Burns: Liar! I'll give you the thrashing of a lifetime! (Flails his arms in weak attempt to hit Smithers) Resistance is futile!
Barney: Hey, aren't you that guy everybody hates? Mr. Burns: Oh, my, no! I'm Monty Burns.
Mr. Burns: Ahoy-hoy...
Mr. Burns: Mmmm... that's a bingo.
Mr. Burns: Sure you can have a health plan, or two donuts a day.
Mr. Burns: What do you think, Smithers? Smithers: I think women and sea men don't mix. Mr. Burns: We know what you think.
Mr. Burns: Ex-cellent.
Mr. Burns: Wait! I'm shooting AT Nazis? That's not how I remember it.
Mr. Burns: (To duck wearing a hardhat) Get back to work, Stuart!
Mr. Burns: (Checking his stocks) Ah, right where I left off September, 1929 ...oh... oh no... Smithers, why didn't you tell me about this market crash? Smithers: Um, well... sir, it happened twenty-five years before I was born. Mr. Burns: Oh, that's your excuse for everything!
Mr. Burns: Hmmm... Eternal happiness for one dollar? I'd think I'd be happier with the dollar.
Mr. Burns: I'm at war with a little girl! And I'm losing!
Lisa: You haven't changed at all! You're still evil and when you try to be good, you're even more evil! Mr. Burns: I don't understand. Pigs need food, engines need coolant, dynamiters need dynamite. I'm supplying it to them at a tiny profit... and not a single sea creature was wasted. (Very creepy) You inspired it all... Li'l Lisa.
Mr. Burns: We don't have to be adversaries, Homer. We both want a fair union contract. Homer: (Thinking to himself) Why is Mr. Burns being so nice to me? Mr. Burns: ...and if you scratch my back, I'll scratch yours. Homer: (Thinking to himself) Wait a minute. Is he coming onto me? Mr. Burns: I mean, if I should slip something into your pocket, what's the harm? Homer: (Thinking to himself) My God! He is coming onto me! Mr. Burns: After all, negotiations make strange bedfellows. (Laughs and winks) Homer: (Screams on the inside) Sorry, Mr. Burns, but I don't go in for these back door shenanigans. Sure, I'm flattered, maybe even a little curious, but the answer is no!
Mr. Burns: Non-violence never solved anything!
Mr. Burns: Smithers! Massage my brain!
Smithers: It feels good to help some one doesn't it sir? Mr. Burns: No, it feels weird.
Lisa: Mr. Burns, does your plant have a recycling program? Mr. Burns: Re-sy-hling?
Mr. Burns: (Addressing Homer at the Simpsons' front door) Sir, we've never met before, but my name is Mr. Burns and I want your daughter to help make me rich again. Homer: You mean Maggie? (Maggie stares at Mr. Burns and gestures her hand like a gun aimed at him) Mr. Burns: Ahh, the baby who shot me. No, I was referring to your other daughter.
Mr. Burns: The whole plant is environmentally sound. It's powered by old newspapers, machinery is made entirely of used cans, and the windows are from the old liquor bottles we collected. (To Barney) Hey! I thought I told you to stop licking my windows! Barney: I know you told me. And when I woke up this morning, I said, 'Barney, you're not gonna lick that...'
Mr. Burns: You've just won the, uh, First Annual Montgomery Burns Award for, uh, Outstanding Achievement in the Field of... uh, Excellence...
Mr. Burns: Darling, my kneecaps are filling with fluid even as I speak, so I'll get right to the point.
Mr. Burns: I'm warning you, you're making a very powerful temporary enemy...
Mr. Burns: Yes, yes, we've heard quite enough about Blizblaz and Himham, get to the bloody point!
Mr. Burns: (To Homer) You're so much more fun than Smithers. Why, he doesn't even know the meaning of the word 'gay.'
Mr. Burns: Now let's enjoy the Miami of Canada, Chicago!
Mr. Burns: I dub the king of the morons, also known as supervisor for sector 7-G.
Smithers: Sir, bad news from accounting, the economy's hit us pretty hard. Mr. Burns: Tough times, huh? I've lived through twelve recessions, eight panics, and five years of *McKinleynomics*. I'll survive this.
Mr. Burns: You there! Fill this up with petroleum distillate. And revulcanize my tires, post haste!
Mr. Burns: This will be like stealing candy from a baby... say, that sounds like a lark.
Mr. Burns: Simpson, eh! New man? Smithers: He thwarted your campaign for governor, you ran over his son, he saved the plant from meltdown, his wife painted you in the nude... Mr. Burns: Doesn't ring a bell...
Mr. Burns: Hello, my name is Mr. ...Snurb, yes, that will do.
Mr. Burns: No kind of love can come from one man paying another...
Mr. Burns: So ironic. After all my years of shock-jobbing, gun running, attempted murder, successful murder, and tom peepery, they get me on a petty multi-million dollar art theft.
Mr. Burns: Take me home, Smithers. We'll destroy something tasteful.
Mr. Burns: Goodbye insufficiently cruel world...
Homer: Thanks for giving me my job back, Mr. Burns. Mr. Burns: I'm afraid it's not that simple. As punishment for your desertion, it's company policy to give you the plague. Smithers: Uh, sir, that's the plaque. Mr. Burns: Ah, yes, the special de-motivational plaque to break what's left of your spirit. For you see, you're here... forever.
Mr. Burns: Now, what was I laughing about? Oh, yes, that crippled Irishman. (Starts laughing again)
Mr. Burns: Release the League of Evil. (Wall opens to reveal a table with skeletons at it) What happened to my league? Smithers: Even monsters need air, sir.
Mr. Burns: Smithers, I've designed a new airplane. I call it the 'Spruce Moose,' and it will carry two hundred passengers from New York's *Idyllwild Airport* to the Belgian Congo in seventeen minutes! Smithers: That's quite a nice model, sir. Mr. Burns: Model?
Mr. Burns: This house has quite a long and colorful history. It was built on an ancient Indian burial ground, and was the setting of Satanic rituals, witch-burnings, and five *John Denver* Christmas specials.
Mr. Burns: I see you have your running shoes on. That's a good thing...
Mr. Burns: Welcome, to the American dream. A billionaire using public funds to construct a private playground for the rich and powerful.
Homer: Mr. Burns, I insist that we cheat! Mr. Burns: Ex-cellent.
Bart: So, Mr. Burns, you're saying my dad has gone insane, and thinks he's a God, and broken off all contact with the outside world? Smithers: I told you Simpson was a poor choice, sir. Mr. Burns: You know, Smithers, 'I told you so,' has a brother. His name is, 'Shut the hell up!'
Mr. Burns: (Mr. Burns is trying to make Homer lose weight through sit ups. Homer is lying on the ground, never managing to get more than a few inches up) One... One!... ONE! BAH! I'll just pay for the blasted liposuction! Homer: WOO-HOO!
Mr. Burns: The telephone is so impersonal. I much prefer the hands-on touch you can only get with hired goons.
Mr. Burns: Who's that goat-legged fellow? I like the cut of his jib. Smithers: That's the Prince of Darkness, sir. He's your eleven o'clock. Mr. Burns: Ex-cellent.
Mr. Burns: I wonder if this Homer Simpson is related to *Richard Nixon*. Smithers: Probably not sir, as they spell and pronounce their names differently.
Doctor: We call it, '*Three Stooges* syndrome.' Mr. Burns: So, what you're telling me is... I'm indestructible. Doctor: Oh, no no. Even a slight breeze could... Mr. Burns: Indestructible.
Kid: ...but then we'll go too far and get corrupt and shiftless, and the Japanese will eat us alive! Mr. Burns: The Japanese? Those sandal-wearing goldfish tenders? Mr. Burns: (To Smithers, in the present) If only we'd listened to that boy, instead of walling him up in the abandoned coke oven.
Smithers: Our research shows that people see you as something of an ogre. Mr. Burns: Why, I ought to club them and eat their bones!
Lawyer: Your Honor, my client has instructed me to remind the court how rich and important he is, and that he is not like other men. Mr. Burns: I should be able to run over as many kids as I want!
Mr. Burns: Quick Smithers, bring the mind eraser device! Smithers: You mean the revolver, sir? Mr. Burns: Precisely.
Mr. Burns: Oh, meltdown. It's one of those annoying buzzwords. We prefer to call it an unrequested fission surplus.
Mr. Burns: I don't like being outdoors Smithers, for one thing, there's too many fat children.
Mr. Burns: Well, that's odd... I've just robbed a man of his livelihood, and yet I feel strangely empty. Tell you what, Smithers, have him beaten to a pulp.
Mr. Burns: I could crush him like an ant. But it would be too easy. No, revenge is a dish best served cold. I'll bide my time until... Oh, what the hell. I'll just crush him like an ant.
Mr. Burns: What good is money if it can't inspire terror in your fellow man?
Mr. Burns: What are you doing man, that's Carl!
Mr. Burns: Stroke! Stroke! Stroke! Apu: I'm rowing as fast as I can, sir! Mr. Burns: No! I'm having one!
Mr. Burns: Well, for once, the rich white man is in control.
Mr. Burns: What's a good time for a mass evacuation of the plant? Smithers: 45 seconds. Mr. Burns: And what's our time so far? Smithers: I don't know, sir, this stopwatch only goes up to 15 minutes.
Mr. Burns: (Turning on a lamp) Ah! 60 watts? What do you think this is? A tanning salon?
Mr. Burns: Donuts? I told you, I don't like ethnic food.
Mr. Burns: You're fired. Marge: You can't fire me just because I'm married. I'm gonna sue the pants off of you. Mr. Burns: You don't have to sue me to get my pants off.
Mr. Burns: Smithers, for attempting to kill me, I'm giving you a five percent pay cut!
Mr. Burns: I'm looking for something in an attack dog. One who likes the sweet gamey tang of human flesh. Hmmm, why here's the fellow... Wiry, fast, firm, proud buttocks. Reminds me of me.
Mr. Burns: So, Smithers, what are you doing this weekend. Something gay, I expect? Smithers: What? Mr. Burns: You know, light and fancy free! Mothers, lock up your daughters! Smithers is on the town! Smithers: Oh! Of course.
Mr. Burns: Ooh, the Germans are mad at me. I'm so scared! Oooh, the Germans!
Smithers: Sir, we're those real bullets? Mr. Burns: Yes, was that a real gorilla? Smithers: No. Mr. Burns: I see.
Mr. Burns: F-U-N? Is that how it's pronounced? I've only seen it written.
Mr. Burns: Smithers, take my hands and clap them sarcastically. (While Smithers is clapping his hands) More sarcastic!
Mr. Burns: ...who tragically died from complications due to union organizing.
Mr. Burns: Is it a crime to want nice things, and then to steal them from a public museum where any gum chewing monkey in a Tuffs University jacket can gawk at them? I think not.
Mr. Burns: Smithers! Sound the alarm. Summon the Shirelive! Wake the beagle!
Mr. Burns: How odd. His money seems to have bought him happiness.
Mr. Burns: That's it man, pave and tar the way God intended.
Mr. Burns: Yes, by cutting off cable TV and the beer supply, I can ensure an honest winter's work out of those low-lifes. Smithers: Sir, did you ever stop to think that maybe it was doing this that caused the previous caretakers to go insane and murder their families? Mr. Burns: Hmm... perhaps. Tell you what, we come back and everyone's slaughtered, I owe you a *Coke*.
Mr. Burns: Bad corpse! Stop... scaring... Smithers!
Mr. Burns: A lifetime of working with nuclear power has left me with a healthy green glow... and left me as impotent as a Nevada boxing commissioner.
Mr. Burns: Look at that pig. Stuffing his face with donuts on my time! That's right, keep eating... Little do you know you're drawing ever closer to the poison donut! (Heckles evilly, then stops abruptly) There is a poison one, isn't there Smithers? Smithers: Err...no, sir. I discussed this with our lawyers and they consider it murder. Mr. Burns: Damn their oily hides!
Mr. Burns: Look at them, Smithers. Goldbrickers... layabouts... slug-a-beds! Little do they realize their days of suckling at my teat are numbered.
Mr. Burns: This anonymous clan of slack-jawed troglodytes has cost me the election, and yet if I were to have them killed, I would be the one to go to jail. That's democracy for you. Smithers: You are noble and poetic in defeat, sir.
Mr. Burns: Nonsense! Dogs are idiots! Think about it, Smithers. If I came into your house and started sniffing at your crotch and slobbering all over you, what would you say? Smithers: If you did it, sir?
Mr. Burns: (Stone flies through Mr. Burns' office window) Look Smithers, a bird has become petrified and lost its sense of direction.
Mr. Burns: Do my worst, eh? Smithers, release the robotic *Richard Simmons*.
Mr. Burns: Ah, Monday morning. Time to pay for your two days of debauchery, you hung-over drones.
Mr. Burns: Family, religion, friends... these are the three demons you must slay if you wish to succeed in business.
Mr. Burns: One more thing, you must find the Jade Monkey before the next full moon! Smithers: Actually sir, we found the jade monkey. It was in your glove compartment. Mr. Burns: And the road maps, and the driving gloves? Smithers: Yes, sir. Mr. Burns: Ex-cellent, its all falling into place!
Mr. Burns: Oh, so mother nature needs a favor? Well, maybe she should have thought of that when she was besetting us with droughts and floods and poison monkeys.
Mr. Burns: Mankind has always dreamed of destroying the sun.
Chief Wiggum: Lemmie tell you what I tell everyone who comes in here, the police are powerless to help you.
Milhouse: I can't go to juvie! They use guys like me as currency! Chief Wiggum: Yeah, they'll pass you around like... like currency, like you said.
Lou: Hey, Chief, can I hold my gun sideways? It looks so cool. Chief Wiggum: Sure, whatever you want, birthday boy.
Chief Wiggum: Nine-one-one, this better be good. Marge: I cut off my husband's thumb! Chief Wiggum: Attempted murder? You'll burn for this... burn in jail!
Chief Wiggum: Mrs. Simpson, I believe your husband is D.O.A.... Marge: HE'S DEAD? Chief Wiggum: Oh, no, that's D.W.I. I always get these police terms mixed up. Woman: Hi, you said my husband was D.W.I... Chief Wiggum: Why don't you talk to that officer over there. I'm going out to lunch...
Chief Wiggum: See ya in court, Simpson. Oh, and bring that evidence with ya, otherwise, I got no case and you'll go scot-free.
Chief Wiggum: All right, you scrawny beanpoles, becoming a cop is not something that happens overnight. It takes one solid weekend of training to get that badge.
Chief Wiggum: No jury in the world is going to convict a baby... maybe Texas.
Chief Wiggum: Oh, now who could blame you. Your sports team lost.
Chief Wiggum: You're all that rare combination, prying, but not purvey.
Chief Wiggum: How fast we're they going Lou? Lou: I don't know Chief. We can't afford a radar gun. We're just using a thermos on top of a hose head.
Chief Wiggum: Do you ever stop breathing when you're asleep. Homer: Yeah, the say it's because I'm overweight.
Chief Wiggum: Oh, that was a tire iron poking me in the back. That clears up allot.
Lou: There's two guys fighting at the Aquarium Chief. Chief Wiggum: Do they still sell those frozen bananas? Lou: I think so. Chief Wiggum: Let's roll!
Chief Wiggum: Oh, sure. We'd all love some real friends, Marge. But what are the odds of that happening?
Chief Wiggum: Things on the ground are out of my jurisdiction.
Chief Wiggum: (Shooting into the portal) Take that, ya lousy dimension!
Chief Wiggum: I hope this has taught you kids a lesson... kids never learn.
Chief Wiggum: That's the end of your Looney Tune, Drugs Bunny.
Chief Wiggum: I'll probably be asleep in front of the fridge when you get home.
Chief Wiggum: (Radar gun reads 110 miles per hour) Let him go Lou, someone going that fast has no time for a ticket.
Chief Wiggum: You think this would fit little Ralphie? Lou: Chief, that's evidence. Chief Wiggum: I know, but after it's evidence it's a shirt again, isn't it?
Chief Wiggum: Homer Simpson, you're under arrest for attempted murder. Homer: D'oh! Chief Wiggum: Yeah, that's what they all say. They all say 'D'oh.'
Chief Wiggum: Sideshow Bob has no decency. He called me Chief Piggum! (Everyone in the courtroom laughs) Chief Wiggum: Heh, now I get it! That's good.
Chief Wiggum: Fat Tony is a cancer on this fair city! He is the cancer and I am the... uh... what cures cancer?
Chief Wiggum: Oh, Simpson, what are you doin' up here? Homer: My wife's having a girl's night out! Chief Wiggum: Ah, just get one of those inflatable women. But make sure it's a woman, though, 'cuz one time I... (Chuckles sheepishly)
Chief Wiggum: Can't you people take the law into your own hands? I mean, we can't be policing the entire city!
Chief Wiggum: Ok, we'll put the tired over here, the poor over there, and the huddled masses yearning to breathe free over there.
Chief Wiggum: Ralphie is so incredible, the special schools are all over him.
Homer: You know, if you let us go, there's a diamond necklace in it for you. Chief Wiggum: I hope you're not suggesting that I would take that necklace as a bribe. Think again, dirt bag, cause I can swipe it later from the evidence locker.
Chief Wiggum: I'd like to help you ma'am, but, heh heh, I'm afraid there's no law against mailing threatening letters. Marge: I'm pretty sure there is. Chief Wiggum: Hah! The day I take cop lessons from Ma Kettle... Lou: Hey, she's right Chief. (Shows him 'Springfield Law') Chief Wiggum: Well, shut my month. It's also illegal to put squirrels down your pants for the purposes of gambling... Boys, knock it off!
Chief Wiggum: Cuff him, boys. We're putting this dirt bag away. Snake: I'll be back on the street in 24 hours. Chief Wiggum: We'll try to make it 12.
Chief Wiggum: Let him go. I have a feeling we'll meet again. Each and every week.
Dr. Hibbert: Homer, this is your physician, Dr. Julius Hibbert. Can you tell us what it's like in there? Homer: Uh, it's like, uh... Did anybody see the movie *Tron*? Dr. Hibbert: No. Lisa: No. Chief Wiggum: No. Marge: No. Bart: No. Patty: No. Chief Wiggum: No. Ned Flanders: No. Selma: No. Professor Frink: No. Rev. Lovejoy: No. Chief Wiggum: Yes. I mean, uh, I mean, no.
Bart: (Pointing to Sideshow Bob) Take him away, boys. Chief Wiggum: Hey, I'm the Chief here! Bake him away, toys. Lou: Uh, what'd you say, Chief? Chief Wiggum: ...Just do what the kid says.
Homer: (Chief Wiggum pulls Homer over) Is there a problem, officer? Chief Wiggum: Yep. Got a tail-light out. Homer: Where? Chief Wiggum: (Smashing a tail-light) Right there. Homer: You know, one day, honest citizens are gonna stand up to you crooked cops! Chief Wiggum: They are? Oh no! Have they set a date?
Chief Wiggum: No, you got the wrong number. This is 91... 2.
Chief Wiggum: I don't want to censor myself. That's how creativity dies.
Chief Wiggum: Homer Simpson, you always know the perfect thing to say.
Chief Wiggum: Do you every worry that the sun is not going to come back after it goes down at night?
Lisa: Chief Wiggum, how did you get these tickets? Chief Wiggum: Krusty knows how to play ball. (Flashback: Krusty sits in a porno theater, Chief Wiggum enters behind him) Chief Wiggum: Ahhh... nothin' beats a good porno movie! Krusty: (Startled) Chief Wiggum! Is this a bust? Chief Wiggum: Uh, yeah. That's what it is, a bust. (Back to reality...) Lisa: That story isn't appropriate for children! Chief Wiggum: Really? I keep my pants on in this version.
Chief Wiggum: Bye, Lisa! If anything goes wrong, just dial 911! Uh, unless it's an emergency! Lisa: G'bye, Chief! Enjoy *Bob Saget*! Chief Wiggum: Heh, it's *Bob Seger*! (He looks at the tickets and frowns) Aw, crap!
Chief Wiggum: Oh, man, what a day. It's no cakewalk being a single parent, juggling a career and family like so many juggling balls... two, I suppose.
Chief Wiggum: She didn't reckon with the awesome power of the Chief of Police! Now where did I put my badge?... Hey, that duck's got it! (Chasing after the duck) Awww c'mon! Give it back!
Chief Wiggum: This is Papa Bear. Put out an A.P.B. for a male suspect, driving a... car of some sort, heading in the direction of, uh, you know, that place that sells chili. Suspect is hatless. I repeat, hatless.
Chief Wiggum: Time for another hot beef injection.
Chief Wiggum: Awww, isn't that cute? A baby driving a car. And look! There's a dog driving a bus!
Chief Wiggum: Well, I I'd like to thank you both for cooperating with... DID YA DO IT? Marge: Chief Wiggum, Homer and I are innocent. Chief Wiggum: I'm sorry I can't believe I tried to trick you with such an underhanded guess... DID YA DO IT? Marge: NO! Homer: Now if you'll excuse us, we'll be on our... DOES THAT EVER WORK? Chief Wiggum: Nah, nah it never does. Homer: Book him, Lou. Chief Wiggum: Yeah sure, go ahead. I'll be back on the streets by dinner time! You'll see.
Chief Wiggum: My position? Ah, jeez. I'm on a road. There's some trees and shrubs. I'm directly under the Earth's sun... NOW!
Chief Wiggum: Disperse! We are ready to use force!... What's that? We're not? Uh oh. Somebody call the police. Lou: Oh, they never come.
Chief Wiggum: All right, smart guy, where's the fire? Homer: Over there. Chief Wiggum: Okay, you just bought yourself a 317, pointing out police stupidity. Oh wait, is that a 314? No, 314 is a dog, uh, in, no, is that a 315? Eh, you're in trouble, pal.
Marge: Please, you have to protect my husband. Chief Wiggum: Where on my badge does it say anything about protecting people? Lou: Uh, second word, Chief. Chief Wiggum: Thanks a lot, Princeton Pete.
Lou: Another case of *Monopoly* related violence, chief. Chief Wiggum: How do those *Parker Brothers* sleep at night?
Chief Wiggum: Would an innocent person flee?... No really... I'm asking. I honestly don't know. Lou: Ah, no Chief. Ralph: Even I knew that. Chief Wiggum: Yeah, yeah. I'm no good.
Chief Wiggum: Take a good hard look at the innocent love in your son's eyes because when he gets out of prison It'll be gone forever. He will have a great bod though, and a couple of those teardrop tattoos. Those are cool!
Chief Wiggum: Um, what does it say on my badge? Cash bribes only! Lets go.
Chief Wiggum: Ok folks, back away nothin' to see here... Oh my God, a horrible plane wreck! Hey everybody crowd around, come on don't be shy crowd around.
Chief Wiggum: What is your fascination with my forbidden closet of mysteries?
Chief Wiggum: You know, fingerprints are just like snowflakes. They're both very pretty.
Lisa: All the years I've lobbied to be treated like an adult have blown up in my face.
Lisa: Dad, I broke my last saxophone reed, and I need you to get me a new one. Homer: Uh, isn't this the kind of thing your mother's better at? Lisa: I called her. She's not home. I also tried Mr. Flanders, Aunt Patty, Aunt Selma, Dr. Hibbert, Rev. Lovejoy, and that nice man who caught the snake in our basement.
Lisa: I'm too excited to sleep. Anyone up for the *Winifred Beecher Howe Memorial*?
Homer: Oh, where did I lose 'em? I'll never wiggle my bare butt in public again. Lisa: I'd like to believe that this time. I really would. Marge: Bart, run down to the store and get a bag of ice for your father. Bart: Yes'm. Dad, I know you're discouraged but please don't deny the world your fat can. Homer: Don't worry, boy. She'll be ready for your Aunt Selma's birthday. Lisa: I knew it.
Lisa: So what prize did you end up getting? Bart: Mustache comb, what did you get? Lisa: Fake mustache... wanna comb it?
Lisa: Homer and Ned Flanders friends? What's next, A's on Bart's report card? (Marge, Lisa, and Bart laugh, but Bart stops) Bart: (Realizes he's been insulted) Hey!
Lisa: Don't tell me that mom dresses you! Homer: I dunno. Either her or one of her friends.
Lisa: The city of Washington was built on a stagnant swamp some two hundred years ago and very little has changed; it stank then and it stinks now. Only today, it is the fetid stench of corruption that hangs in the air.
Lisa: A man who envies our family is a man who needs help.
Lisa: (At Homer's hastily-concocted award ceremony) This show is the biggest farce I ever saw! Bart: What about the Emmys? Lisa: I stand corrected.
Homer: D'oh! Lisa: A deer! Marge: A female deer!
Lisa: Dad! I think a hurricane's coming! Homer: Oh, Lisa! There's no record of a hurricane ever hitting Springfield. Lisa: Yes, but the records only go back to 1975, when the Hall of Records was mysteriously blown away!
Lisa: Bart's pain is funny, but mine isn't.
Crowd: (Pointing at Lisa) Gifted! Gifted! Lisa: I'm just advanced, you can catch up.
Lisa: Several? That's more then a few and almost a bunch.
Lisa: How is that fun? Fun is only fun if everyone is having fun.
Homer: Have you learned anything from watching Bart drive? Lisa: A little.
Lisa: But don't you know, people who don't go to college make three percent less then people who do?
Lisa: The man hates pants.
Lisa: Actually dad, as a supervising parent today, you'll get your share of the blame too.
Lisa: WOO-HOO! Test day! Now I can show off at the federal level.
Lisa: Ok, let's see. How many jazz musicians have lived long and happy lives?
Lisa: I never dreamed an American car, designed in Germany, assembled in Mexico, from parts made in Canada, could be so amazing.
Lisa: But mom, if you take our cartoons away, we'll grow up without a sense of humor and be robots.
Lisa: I'm no theologian. I don't know who or what God is. All I know is He's more powerful than mom and dad put together.
Lisa: (Checking the card catalog) Let's see... Football... Football... 'Homoeroticism in'... 'Oddball Canadian rules'... 'Phyllis George and'...
Lisa: (At the pound) Too fluffy... too scrawny... too needy... too arrogant... eye infection... (Stops) Clearly a skunk.
Lisa: It's so sad that Krusty is ashamed of his roots. (Homer walks into the living room with a plunger on his head) Homer: Marge, it happened again. Bart: What are you going to change your name to when you grow up? Lisa: *Lois Sandborne*. Bart: *Steve Bennett*.
Bart: See that fat lady with the mustache? That's you. Lisa: See the hippo rolling in dung? You're the dung.
Lisa's Brain: They're only using you for your pool, you know? Lisa: Shut up, brain. I've got friends now. I don't need you anymore!
Bart: Nothing you say can upset us. We're the *MTV* generation. Lisa: We feel neither highs or lows. Homer: Really? What's it like? Lisa: Eeh. (Shrugs).
Bart: *Wicca's* a Hollywood fad. Lisa: That's *Kabala*, you jerk.
Lisa: Where am I at? This neighborhood is starting to look a lot like *Sesame Street*.
Marge: Sweety, you could still go to *McGill*. The *Harvard* of Canada. Lisa: Anything that is the something of the something, isn't really the anything of anything.
Lisa: But I never make a final decision in the forest at night...
Lisa: First of all, it's never wise to use the word 'spew' in a love song.
Lisa: This goes against every feminist bone in my body, but dad, can't you control your woman? Homer: How can I control her? I have nothing to withhold.
Lisa: (To Bart) I'm sure you did nothing to discourage this, you scavenger of human misery.
Lisa: Oh no, the dead have risen and they're voting *Republican*.
Lisa: You're serving us gruel? Dolph: Not quite. This is Krusty-Brand Imitation Gruel. Nine out of ten orphans can't tell the difference.
Lisa: It's not our fault our generation has short attention spans, dad. We watch an appalling amount of T.V.
Lisa: Dad, is it all right to take things from people you don't like?
Bart: Lisa, I have this strong unpleasant feeling I've never had before. Lisa: It's called remorse, you vile burlesque of irrepressible youth.
Lisa: Science has already proven the dangers of smoking, alcohol, and Chinese food, but I can still ruin soft drinks for everyone!
Lisa: Perhaps there is no moral to this story.
Lisa: (To Bart) You made me love baseball. Not as a collection of numbers, but as an unpredictable passionate game, beaten in excitement by every other sport...
Lisa: Wow, this must be important dad. I've never seen you walk up an incline before.
Lisa: Oh no, you took to long to make an obvious decision.
Lisa: Another Springfield family moves to Detroit to find a better life. Marge: Now that it's empty who's going to buy their house? What if someone moves in with two Barts, or four teenage Barts?
Lisa: I'm impressed you were able to write so legibly on your own butt.
Lisa: I'm no theologian. I don't know who or what God is, exactly. All I know is he's a force more powerful than mom and dad put together, and you owe him big.
Principal Skinner: What comes to mind when you think of drama? Lisa: Well, according to Aristotle, drama contains six elements: plot, theme, character... Principal Skinner: Not the smarty-pants answer. What's the drama in your life? Lisa: Ok, but can I just finish the smarty pants answer? Principal Skinner: No, in you life! Lisa: My family, language, rhythm, and spectacle.
Lisa: I think Bart's stupid again, mom. Marge: Oh, well...
Lisa: Somethings wrong, dad would never miss an open bar with chicken wings.
Lisa: (To Homer) Is it really worth risking your lives for some sugar? Marge: Dessert's on! I steamed some limes! Lisa: God speed.
Lisa: You've become a product of our quick fix, one-hour photo, instant oatmeal society.
Lisa: If cartoons were meant for adults, they'd put them on in prime time.
Marge: I'm sure you'll make plenty of friends. All you have to do is be yourself. Lisa: Be myself? I've been myself for eight years and it hasn't worked.
Lisa: (Talking about Nelson) He's not like anybody I've ever met. He's like a riddle wrapped in an enigma wrapped in a vest.
Lisa: I am the Lizard Queen!
Lisa: When there's cruelty involved, Bart sure knows his history.
Lisa: I traded away my pearls. Without them I'm just a big Maggie.
Lisa: Hurray! I'm a brainy outcast again.
Lisa: While I know firsthand how fragile young talent is, I'd love to hear the particulars of how your gift was squashed.
Lisa: It always comes down to transubstantiation versus consubstantiation.
Colin: I'm Colin. Lisa: I haven't seen you at school. Colin: Just moved from Ireland. My dad's a musician. Lisa: Is he...? Colin: He's not *Bono*. Lisa: I just thought because you're Irish and you care about... Colin: He's NOT *Bono*.
Lisa: (After seeing a comic book of Angry Dad) Bart, this is just dad. Bart: It's a composite character: your dad, my dad, a little of Maggie's dad... Lisa: No, it's just dad. Bart: Well, maybe Angry Dad needs a sidekick: Know-It-All Sister! Lisa: (Gasps happily) Can she have a pony, and the last line in the scene? (Bart pauses for a moment, then nods with a smile, and Lisa giggles)
Bart: Lisa, if I ever stop loving violence, I want you to shoot me. Lisa: Can do!
Bart: You bought my soul back? Lisa: With the spare change in my piggy bank. Bart: You don't have any spare change in your piggy bank. Lisa: Not in any of the ones you know about.
Lisa: Solitude never hurt anyone. *Emily Dickinson* lived alone, and she wrote some of the most beautiful poetry the world has ever known... then went crazy as a loon.
Lisa: Relax? I can't relax! Nor can I yield, relent, or... Only two synonyms? Oh my God, I'm losing my perspicacity! Aaaaa!
Lisa: Milhouse, knock him down if he's in your way! Jimbo, Jimbo, go for the face! Ralph Wiggum lost his shin guard! Hack the bone! Hack the bone!
Lisa: Mom, romance is dead. It was acquired in a hostile takeover by *Hallmark* and *Disney*, homogenized, then sold off piece by piece.
Lisa: As intelligence goes up, happiness goes down. See, I made a graph. I make a lot of graphs.
Lisa: Prayer, the last refuge of a scoundrel.
Lisa: I'm sorry but the team all got food poisoning at the pre-rally egg salad sandwich party. Luckily, as equipment manager, I was not invited.
Lisa: This is our house. There is nothing buried here except hopes and dreams.
Lisa: I can't go home. Something happened this week that completely changed me. Marge: Oh, you didn't see a boy loose his swim trunks, did you? Lisa: No, I fell in love with theater, dance, and song.
Lisa: I'm proud of you, mom. You're like *Christopher Columbus*. You discovered something millions of people knew about before you.
Lisa: It would rather destroy itself than live with us. You can't help but feel a little rejected.
Lisa: This is ridiculous. Only babies and ex-junkies are afraid of needles. Stick me, chuckles. (Cries) Can I have a lollipop?
Lisa: You can't change anyone... except for that boy at the library.
Lisa: As usual, the playground has the facts right, but misses the point entirely.
Lisa: ...and now you can go back to just being you, instead of a one-dimensional character with a silly catch-phrase. Homer: (Breaking a lamp) D'oh! Bart: Ay, carumba! Marge: (Groans) Maggie: (Sucks her pacifier) Ned Flanders: Hi-dilly-ho! Barney: (Belches) Nelson: Ha, ha! Burns: Ex-cellent! (Long pause. Everyone looks expectantly at Lisa) Lisa: If anyone wants me, I'll be in my room. Homer: What kind of catch phrase is that?
Lisa: I'm gonna pump 'em so full of sap they're gonna wipe their nose with a pancake!
Miss Hoover: Now, take out your red crayons. Ralph: Miss Hoover? Miss Hoover: Yes Ralph? Ralph: I don't have a red crayon. Miss Hoover: Why not? Ralph: I ate it.
Ralph: Bart's my bestest boyfriend.
Bart: Got any threes? Ralph: Go fish! Bart: See, here's the problem Ralph, you have several threes Ralph: Go fish!
Ralph: I'm going to eat chocolate 'til I barf!
Ralph: My parents won't let me use scissors. (The rest of the class laughs) Miss Hoover: The children are right to laugh at you, Ralph. These things couldn't cut butter.
Ralph: Which one is one?
Ralph: I'm a furniture.
Ralph: Grandma had hair like that when she went to sleep in her forever box.
Ralph: Principal Skinner is an old man who lives at the school.
Ralph: Hey, I know you, my daddy took your beer.
Ralph: Help! She's touching my special area!
Jimbo: Mush nerds, mush! Ralph: I'm part of a team!
Ralph: This is my sandbox, I'm not allowed to go in the deep end.
Ralph: This snowflake tastes like fish sticks.
Ralph: Is this my house?
Ralph: I wet my arm pants.
Ralph: And I want a bike and a monkey and a friend for the monkey.
Ralph: At my house, we call them 'Uh-Oh's.'
Ralph: Why do people run away from me? (Wets his pants, then smiles)
Ralph: My daddy shoots people!
Ralph: Teacher, my shoes are making noise.
Ralph: I ate too much plastic candy.
Ralph: Everybody's hugging!
Ralph: Your God is wrong!
Ralph: When he grows up I want to be like me.
Ralph: What's lime disease? Does that mean you're crazy?
Ralph: Can you open my milk, mommy? Miss Hoover: I'm not mommy, Ralph. I'm Miss Hoover.
Ralph: Oh boy, sleep! That's where I'm a Viking!
Ralph: My cat's breath smells like cat food.
Ralph: Miss Hoover? I glued my head to my shoulder.
Ralph: I cheated wrong, I copied the Lisa name and used the Ralph answers.
Ralph: I'm learnding!
Ralph: Clouds are God's sneezes.
Ralph: Dying tickles!
Ralph: It says 'I Choo-choo-choose You,' and there's a picture of a train!
Ralph: What's a battle?
Ralph: Wheee! ...ow, I bit my tongue!
Ralph: I'm Idaho. Principal Skinner: Sure you are...
Ralph: What's a diorama?
Ralph: I beat the smart kids! I beat the smart kids!
Ralph: Um, Miss Hoover? There's a dog in the vent.
Ralph: Ow, my face is on fire!
Ralph: Was president *Lincoln* okay?
Ralph: Your toys are fun to touch. Mine are all sticky.
Ralph: My neck hurts and my ear hurts. I have two owwies.
Ralph: *Martin Luther King* had a dream. Dreams are where *Elmo* and *Toy Story* had a party, and I went there.
Ralph: I'm pedaling backwards!
Ralph: (Catching a baseball) I caught a white apple.
Ralph: I'm a *Star Wars*.
Ralph: My knob tastes funny.
Ralph: Do alligators alginate?
Ralph: Miss Hoover, what's our lesson today? Is it school?
Ralph: In fifty years the vacuum cleaner will be quiet and not scary.
Ralph: Maybe she drove to the moon.
Bart: Smell that? That's the smell of justice. Ralph: Smells like hot dogs.
Ralph: Bushes are nice 'cause they don't have prickers. Unless they do. This one does. Ouch!
Ralph: My worm went in my mouth and then I ate it.
Homer: There's your giraffe, little girl. Ralph: I'm a boy. Homer: That's the spirit. Never give up.
Ralph: My cat's name is Mittens.
Ralph: When I grow up, I want to be a principal or a caterpillar.
Ralph: When I grow up I'm going to Bovine University.
Ralph: Prinskipper Skippel... Primdable Skimpsker... I found something!
Ralph: Even my boogers are spicy!
Ralph: Uh... so... do you like... stuff?
Ralph: Principal Skinner, I got car sick in your office.
Ralph: Tastes like burning!
Ralph: A-B-C-D-E-F-G... (Long pause) How I wonder what you are.
Ralph: Hooray for different face.
Ralph: Me fail English? That's unpossible.
Ralph: Hi, *Super Nintendo* Chalmers!
Ralph: My not dead grandma sent it from Tokyo.
Ralph: Eww, daddy, this tastes like Grandma!
Ralph: Lisa's dancing makes my feet sad.
Ralph: Oww, I bent my *Wookie*.
Ralph: The doctor said I wouldn't have so many nose bleeds if I kept my finger outta there.
Ralph: Daddy, I'm scared. Too scared to even wet my pants. Chief Wiggum: Just relax and it'll come son.
Ralph: I heard your dad went into a restaurant and ate everything in the restaurant and they had to close the restaurant.
Ralph: ...and when the doctor said I didn't have worms any more, that was the happiest day of my life. Miss Hoover: Thank you Ralph, very graphic...
Ralph: I found a moon rock in my nose!
Ralph: That's where I saw the Leprechaun. He tells me to burn things!
Ralph: Mrs. Krabappel and Principal Skinner were in the closet making babies and I saw one of the babies and then the baby looked at me.
Ralph: Your eyes need diapers!
Principal Skinner: Oh terrible, just terrible. You know, they seem to get worse every year. (Comes out on stage) Wonderful! You know, I think this is the best pageant we've ever had. I really do!
Principal Skinner: They called me old-fashioned for teaching the duck-and-cover method, but who's laughing now!
Principal Skinner: They're just asserting their independence. If a child doesn't do it now it may never happen! Agnes: Seymour, do you want your vitamins in applesauce or are you gonna take it like a big boy? Principal Skinner: Applesauce.
Principal Skinner: (On P.A. system) Attention students, please make your way for an assembly at the Butthead Memorial Auditorium. (In his office) Damn it, I wish we hadn't let the children name that one.
Principal Skinner: I haven't seen such unfettered hurley-burley since the fall of *Saigon*.
Principal Skinner: Where do you think you're going? Bart: Aww get back to your knitting Seymour. Principal Skinner: I will, but it's because I want too.
Principal Skinner: Fire can be our servant, whether it's toasting s'mores, or raining down on Charlie.
Principal Skinner: Huhuhuh, oh I think Uter's around somewhere, children.. huhuhuh I think there's a little Uter.. in all of us! huhuhuh..in fact, maybe we just ATE Uter, and he's in our stomachs right now! ...Ahem, scratch that last part.
Principal Skinner: Attention, all honor students will be rewarded with a trip to an archaeological dig. Conversely, all detention students will be punished with a trip to an archaeological dig.
Principal Skinner: Oh, mercy.
Principal Skinner: Lisa, Lisa, go home, relax. Try to do some kid things. You know, with a ball or something...
Principal Skinner: Ralph you're not a kangaroo.
Principal Skinner: Buying those trophies from cash strapped schools really filled up the old case.
Principal Skinner: Niki No! I prefer a dead child to a lawsuit from your parents.
Principal Skinner: I'll grill your cheese yet boy. You weren't the first prankster to destroy the car I rent from mother, and you won't be the last. Bart: Rent? Principal Skinner: Rent to own. Just thirty-five more payments and it's half way-mine.
Principal Skinner: Lisa Simpson in detention? My horoscope said I would see something interesting today but, I thought it meant the horoscope itself.
Principal Skinner: Time for me to do what I have never done as Principle: something.
Principal Skinner: It will be a rewarding day of pencil sharpening and eyes on your own paper keeping.
Principal Skinner: Out of gas? But how? I put in a dollar this morning and we've only driven 90 cents.
Homer: Why are you dressed as *Catwoman*? Principal Skinner: They told me it was Catman!
Principal Skinner: The judge offered me a choice: jail, the army, or apologize to the judge and old lady. Of course, if I knew there was a war going on, I probably would have apologized.
Principal Skinner: Three large men? I don't remember any appointment with three large men.
Principal Skinner: That's two independent thought alarms in one day. Willie, the children are over-stimulated. Remove all the colored chalk from the classrooms.
Principal Skinner: You did it, Nibbles! Now... chew through my ball sack!
Principal Skinner: Bart, if there's one thing I'm good at, it's pretending things didn't happen. And I think this is one of those.
Principal Skinner: for privacy's sake let's call her... Lisa S. No, that's too obvious... uuuh, let's say L. Simpson...
Principal Skinner: Oh, Edna. We all know that these children HAVE no future... Prove me wrong children. Prove me wrong.
Principal Skinner: Up yours, children!
Principal Skinner: Edna, we can tolerate mild alcoholism, leaving melted cheese in the microwave, even selling A's for cigarettes. But, in laying a hand on a student, you have crossed a line.
Principal Skinner: Mother it's my birthday not our anniversary.
Principal Skinner: In order to save money the following presidents will no longer be taught: Buchanan, Fillmore, Pierce, Bush, Bush...
Principal Skinner: I'm sorry Bart, I can't just get rid of a teacher if he's doing a good job, or an adequate job, or just shows up and doesn't touch anyone.
Principal Skinner: Young man, I'm going to be on you like a numerator on a denominator.
Principal Skinner: Oh, things have changed. There will be no mockery of your name, Mr. Glasscock.
Principal Skinner: Say what you want about our cafeteria, I still think they're the best tater tots money can buy.
Principal Skinner: I hardly think the children's appearance is my fault!
Principal Skinner: ...And I'm a very patient man. I once waited an hour and a half for a haircut.
Principal Skinner: Edna, control your student. He has ruined more assemblies then the afternoon sun on the west window. Mrs. Krabappel: He's uncontrollable. Pumpkin stickers mean nothing to him. Principal Skinner: That's crazy talk.
Principal Skinner: Curse the man who discovered helium. Curse *Pierre Jules Cesar Janssen*.
Principal Skinner: Oh, you think this stolen 'H' is a laugh riot, don't you? Well, I'll tell you something that's not so funny. Right now Superintendent Chalmers is at home crying like a little girl! Well, I guess that is a little funny.
Principal Skinner: If you get me out of this there's a hall monitor position coming open in the Spring. Nelson: I spit on your monitors. Principal Skinner: I know. That's why the position's available.
Principal Skinner: I spent the next three years in a P.O.W. camp, forced to subsist on a thin stew made of fish, vegetables, prawns, coconut milk, and four kinds of rice. I came close to madness trying to find it here in the States, but they just can't get the spices right!
Principal Skinner: I'm going to enjoy devouring you, Bart Simpson. Yes... I believe I'll start, as you've so often suggested, by eating your shorts!
Principal Skinner: I have caught word that a child is using his imagination, and I've come to put a stop to it.
Principal Skinner: What's bothering you son? Bart: I don't want to talk about it. Principal Skinner: Thank God, I don't want to either.
Principal Skinner: Children, I couldn't help monitoring you conversation. There's no mystery about Willie. Why, he simply disappeared. Now, let's have no more curiosity about this bizarre cover-up.
Principal Skinner: There's no justice like angry-mob justice.
Principal Skinner: Yes, that involuntary preconscious reflex I made in utero was unforgivable.
Rev. Lovejoy: Your son has been working in a burlesque house. Helen Lovejoy: Principal Skinner saw him with his own eyes. Principal Skinner: (Appearing from behind Rev. Lovejoy) That's true, but I was only in there to get directions on how to get away from there.
Principal Skinner: Hello, Simpson. I'm riding the bus today because mother hid my car keys to punish me for talking to a woman on the phone. She was right to do it.
Principal Skinner: I've always admired car owners and I hope to be one myself as soon as I finish paying off mother. She insists I pay her retroactively for the food I ate as a child.
Principal Skinner: That's why I love elementary school, Edna. The children believe anything you tell them.
Principal Skinner: Do you kids want to be like the real U.N., or do you want to squabble and waste time?
Principal Skinner: Your son is a ravenous demon, relentlessly gnawing at all that's good and true.
Moe: Uh, how do I say this without being offensive? Marge there ain't enough booze in this place to make you look good.
Moe: Hey, I don't need no advice from a pinball machine. I'll have you know, I wrote the book on love.
Moe: If I didn't sell booze they probably wouldn't even come here.
Moe: Oh, why did I advertise my drink specials in *Scientific American*?
Moe: I was just doing what comes natural to me, being mean to animals.
Moe: Kid, you got a lot of shoddy money saving ideas. Like a major airline, but your here on time.
Moe: Hey clown, we've heard your standup now lets hear some shut up.
Moe: They love me for my bile, and I have a spleen full.
Moe: Hi, I'm Moe, or, as the ladies used to call me 'Hey you behind the bushes.'
Moe: You want to buy a round? I heard about it in bar tending school, but I've never seen it happen.
Moe: Just like my dad used to say: 'Sooner or later, everybody gets shot.'
Moe: I'm gonna drive a golden spike where your *Union* meets your *Central Pacific*!
Patty: Calm down, everybody. Here's a movie of us. (Crowd boos as Patty and Selma show their home movie) Moe: Wow, even I ain't hoping for porn.
Moe: Telegram for Heywood U. Cuddleme! Heywood U. Cuddleme? Big guy in the back, Heywood U. Cuddleme?
Moe: Okay, well I really enjoyed being you Dr. Hibbert. Oh, by the way, you're not welcome in the library no more. I'm sorry.
Moe: Bea O'Problem! Bea O'Problem! Come on, guys, do I have a Bea O'Problem here?
Moe: Uh, Hugh Jass? Oh, somebody check the men's room for a Hugh Jass!
Moe: Hey mister positive, shut the hell up.
Moe: Don't forget my cut. Homer: Your cut of what? Moe: I don't know. I just go around saying that and hope it will be applicable.
Moe: (To Lisa) Listen, I don't like you and you don't like me. But we both wanna stop Homer from shooting the turkey. Lisa: You don't like me? I like you. Moe: You do? Then I like you, too. Here, have a towelette.
Moe: Hey, is there a Butz here? Seymour Butz? Hey, everybody, I wanna Seymour Butz! Oh, wait a minute... Listen, you little scum-sucking pus-bucket! When I get my hands on you, I'm gonna put out your eyeballs with a corkscrew!
Moe: Uh, is I.P. Freely here? Hey, everybody, I.P. Freely! Wait a minute... Listen to me you lousy bum. When I get a hold of you, you're dead. I swear I'm gonna slice your heart in half!
Bart: Can I speak to Amanda Hugankiss? Moe: Amanda Hugankiss! I'm looking for Amanda Hugankiss. Oh, why can't I find Amanda Hugankiss? Barney: Maybe your standards are too high.
Bart: Can I speak to Ivana Tinkle? Moe: Ivana Tinkle! Come on everybody, put down your glasses, Ivana Tinkle!
Bart: Can I speak to Homer Sexual? Moe: Homer Sexual! Come on, one of you's gotta be Homer Sexual. Homer: Don't look at me...
Homer: Hello, I'd like to speak with a Mr. Snotball, first name Eura. Moe: Eura Snotball? Homer: What? How dare you! If I find out who this is, I'll staple a flag to your butt and mail you to Iran!
Moe: Oliver Clothesoff! Call for Oliver Clothesoff!
Moe: That's the best book I've ever seen! Homer: (Looking in his *World Records* book) Nope. The best book you've ever seen is '*Tom Clancy's Op-Center*.' Moe: That thing knows me better than I know myself.
Moe: Phone call for Al... Al Coholic... is there an Al Coholic here?... Listen, you little yellow-bellied rat jackass, if I ever find out who you are, I'm gonna kill you!
Moe: What's the matter, Homer? The depressing effects of alcohol usually don't kick in 'til closing time.
Barney: Is it okay to come out now, Mr. Gay Man? Sir? Moe: I'll do anything you say!... Anything!
Moe: Well, let's see now, uh, time was you sent a boy off to war. Shooting a man fixed 'em right up. But there's not even any wars no more, thank you very much, *Warren Christopher*!
Moe: Moe's Tavern, where the elite meet to drink. Bart: Uh, hello. Is Mike there? Last name, Rotch. Moe: Hold on, I'll check. Mike Rotch! Mike Rotch! Hey, has anybody seen Mike Rotch lately?... Listen, you little puke. One of these days, I'm going to catch you, and I'm going to carve my name on your back with an ice pick.
Moe: Moe's Tavern. Mr. Burns: I'm Looking for a Mr. Smithers. First name Wayland. Moe: OOOOhhh.. so you're looking for a Mr. Smithers eh! First name Wayland is it? Listen to me, you! When I catch you, I'm gonna pull out your eyes and shove 'em down your pants, so you can watch me kick the crap outta you! Okay! Then I'm gonna use your tongue to paint my boat!
Moe: The 'garage?' Hey fellas, the 'garage!' Well, ooh la di da, Mr. French Man. Homer: Well what do you call it? Moe: A car hole!
Homer: Moe, I need your advice. Moe: Yeah? Homer: See, I got this friend named... Joey Jo Jo... Junior... Shabadoo. Moe: That's the worst name I ever heard. (Man runs out of the bar crying) Barney: Hey! Joey Jo Jo!
Moe: Homer, lighten up! You're making Happy Hour bitterly ironic.
Moe: I moved here because the zip code on a calculator spells 'BOOBS.'
Moe: Ain't bein' conformable with something weird the best?
Moe: T.V.? That crap still on?
Moe: Even you let me down *Hitler*.
Patty: What a cheat date this is. Moe: I'm not cheap baby. I'm just embarrassed to be seen with you. Big difference...
Moe: I am so not British. Don't let this pasty face and bad teeth fool you.
Moe: Hey, Bob! How come you can't kill Bart? Killing a kid should be easy! Lenny: If it was me, I'd just slash him open while he's sleeping.
Moe: Well I'm better than dirt! Well, most kinds of dirt. I mean, not that fancy store-bought dirt. That stuff's loaded with nutrients. I can't compete with that stuff.
Moe: Geez, who'd a thought a whale would be so heavy?
Professor: Describe your tavern, in one word. Moe: Uh, is 'crap-hole' one word? Professor: Yes, if it's hyphenated. Moe: Then I'll stick with 'crap-hole.'
Moe: Let's have a minute of silent prayer for out good friend, Homer Simpson. (The barflies all bow their heads. After a short silence...) Barney: How long has it been? Moe: Six seconds. Barney: Do we have to start over? Moe: Hell, no!
Moe: Oh, great! And I just got all that gum out of my armpits!
Moe: There's a naked idiot on the field.
Moe: Oh, I'm sorry everyone. This is the most embarrassing thing I've ever had to say but... I ain't gay.
Moe: He may have come up with the recipe, but I came up with the idea of charging $6.95 for it.
Russian Model: After *Chernobyl*, my penis is falling off. Moe: And penis is Russian for...?
Moe: Not bad. Like Frisbee golf, I'm glad I tried it once.
Moe: I'll use your head as a bucket and paint my house with your brains.
Moe: Homer stole our rock performers! That fat, dumb, and bald guy sure plays some real hardball.
Moe: All right! I'm going to sit at home and ogle the ladies in the *Victoria's Secret* catalog.
Moe: They think they're so high and mighty, just because they never got caught driving without pants.
Moe: People today are healthier and drinking less. You know, if it wasn't for the junior high school next door, no one would even use the cigarette machine.
Moe: Say, Barn. Uh, remember when I said I'd have to send away to *N.A.S.A.* to calculate your bar tab? Barney: Oh ho, oh yeah. We all had a good laugh, Moe. Moe: The results came back today.
Moe: Man, you go through life, you try to be nice to people, you struggle to resist the urge to punch 'em in the face, and for what?
Moe: Call this an unfair generalization if you must, but old people are no good at everything.
Homer: I hope I win. Last year I was the first guy to barf. Moe: Barf? Please, in this business we refer to that as a 'Roman incident.' Homer: That does sound allot classier.
Homer: Lousy cheap country...
Homer: The bee bit my bottom! Now my bottom's big!
Homer: Your king needs these stilts! Jimbo: Jesus is our King! Homer: Not anymore!
Homer: Ooh, I love your magazine. My favorite section is 'How to increase your word power.' That thing is really, really.. really... good.
Homer: Wow! A shoe horn! Just like in the movies!
Carmen Electra: My face is up here, Homer. Homer: (Looking at Carmen's breasts) I've made my choice.
Homer: What could be greater then eating and drinking for hours in a drizzly parking lot? Lisa: Anything.
Homer: I used to rock and roll all night and party ev-er-y day. Then it was every other day. Now I'm lucky if I can find half an hour a week in which to get funky.
Bart: What are you gonna do, dad? Homer: Something I should've done a long time ago. (Pause) Marge: You don't know, do you? Homer: No, ma'am.
Homer: '...it was the most I ever threw up, and it changed my life forever.' Bart: You the man, Homer! Homer: Thanks, boy!
Homer: Hello, son. I wanna apologize. I just got so caught up trying to encourage you, I was blinded to your stinky performance. If you forgive me, I promise I'll never encourage you again.
Homer: Who would have guessed reading and writing would pay off?
Lisa: I hear noises coming form the kitchen. Homer: Uh oh, that's where the food sleeps.
Homer: Where there's an expo there's free Frisbees.
Lisa: Dad you're leading the way in clean energy. Homer: Yeap. I *Al Gored* it pretty good. Where's my *Grammy* for audio book narration?
Marge: Well, at least we got a free sample of Reading Digest. Homer: Marge, I never read a magazine in my life, and I'm not going to start now.
Marge: Ok Magie, we'll be back in three hours. Homer: ...or longer if something happens to us.
Marge: Our wedding china is ruined. Homer: Now we'll have to eat Thanksgiving dinner off regular plates like animals.
Homer: Who are these belts made for? French supermodels.
Marge: Homey, what's going on in there? Homer: I'm fighting the robber, you go get ice cream.
Lisa: Dad, Bart's throwing away his future! Homer: Oh no! Now who will sell oranges on the off-ramp?
Homer: I think Milhouse is El Barto.
Marge: Homey, slow down. Homer: Why should I? The city's broke. They can't afford to enforce their precious laws.
Homer: Look at this electrical bill! I'm not made of money. I'm made of man meet and a skeleton.
Homer: Stupid Grandpa. I try to end the cycle of neglect and he hits me with some super neglect.
Homer: And now you're going to visit your grandpa while I drive around the corner and take a nap.
Homer: Mom, you keep disappearing and reappearing and it's not funny. You're just like that show *Scrubs*.
Homer: Alright, time to dig in. I brought everything we need. Bart: It's just forks and plates. Didn't we bring any food? Homer: The food is all around us! Bart: You brought us here to beg? Homer: Up up up up, when you know the people you're begging from, it's mooching.
Homer: The real reason we Americans put up with sports is for this: Behold, the tailgate Party! The pinnacle of human achievement.
Homer: See that ball of fire? That's the sun. It goes by many names: Apollo's lantern, day moon, old blazy. The important thing is never to touch it. Marge: I know what the sun is. Homer: Yes, now you do.
Marge: You promised. You can't back out like when you volunteered for that military experiment to get out of dinner with my sisters. Military Officer: (In a flashback) Now Mr. Simpson, you do realize this medicine could cause hair loss, giddiness and loss of equilibrium. Homer: Yeah, yeah, yeah. Give me the serum. (Flashback ends) Heh heh heh... It was worth it. (Falls over and laughs hysterically)
Homer: WOO-HOO! Marital sex!
Homer: Everyone in that studio audience is dead now.
Homer: Life was so much easier when a machine told you when to laugh.
Homer: Lisa, mash the buttons until something good comes on.
Homer: Is my job creating power empowering? Lisa: No it's oddly dehumanizing.
Homer: (On the phone) Hello, Jerry? Homer Simpson. Remember last month when I paid back that loan? Well now I need YOU to do a favor for ME.
Homer: Mmmmm... 50 dollar pretzel.
Homer: Mmmmm... 64 slices of American cheese.
Homer: Mmmmm... apple.
Homer: Mmmmm... bacon.
Homer: Mmmmm... beer.
Homer: Mmmmm... beer nut.
Homer: Mmmmm... bowling alley fresh.
Homer: Mmmmm... burger.
Homer: Mmmmm... business deal.
Homer: Mmmmm... candy.
Homer: Mmmmm... caramel.
Homer: Mmmmm... caramel bologna.
Homer: Mmmmm... chocolate.
Homer: Mmmmm... convenient.
Homer: Mmmmm... crumbled-up cookie things.
Homer: Mmmmm... danish.
Homer: Mmmmm... elephant fresh.
Homer: Mmmmm... spaghetti.
Homer: Mmmmm... strained peas.
Homer: Mmmmm... tasty.
Homer: Mmmmm... urinal fresh.
Homer: Mmmmm... various eggs.
Homer: Mmmmm... waffle runoff.
Homer: Mmmmm... something.
Homer: Mmmmm... That's the next best thing to eating Lenny.
Homer: Mmmmm... Marge.
Homer: Mmmmm... doughnut.
Homer: Mmmmm... terrible.
Homer: Mmmmm... chicken.
Homer: Ooooohhhh, you're mad when you're angry.
Homer: I was standing in line to use the bathroom, but now my license is expired.
Homer: First I work, then I pay, then I have to eat fruit? Why was I ever born?
Homer: Masseuses... the half doctors, half hookers that solve everything.
Homer: Marge, it's the golden rule: Treat others the way they mess with you...
Homer: Typical eco-jerks, using words to talk.
Homer: (Picks up the phone) Hello boat store? I'd like to buy a boat. What do you mean dial tone?
Homer: If only I could be eaten by a giraffe. That would be fun.
Homer: Oh Lisa, I'm sorry. I tried my best. It's really hard to discover your dad's not perfect. Bart: Not perfect? You can say that again. Homer: I'm trying to be a sensitive father you unwanted moron!
Homer: Pack your coat, because we're going to Canada's warmest city.
Homer: Gee Lisa, it looks like tomorrow I'll be shoveling ten feet of global warming. Lisa: Global warming can cause weather at both extremes, both hot and cold. Homer: I see, so you're saying warming makes it colder? Well aren't you the queen of crazy land? Every thing's the opposite of everything.
Homer: Hello, I'd like to vote for President, Governor, and anything that will take away from our parks and libraries.
Homer: Go on boy, and pay attention, because if you do, one day you may achieve something that we Simpsons have dreamed about for generations, you may outsmart someone.
Lisa: Mom and dad can't do marriage counseling. If you listen closely, you can here them arguing now. (They then listen closely) Homer: (In the distance) I don't care what you say! A monkey CAN mow our lawn!
Homer: This is all Lisa's fault! Bart and I will take over your dad's business until he gets better. Michael: What do you know about being a mob boss? Homer: Everything! And I owe it all to the greatest gangster movie ever made: *Shark Tale*!
Bart: So, according to creationism, there were NO cavemen. Homer: Good riddance. Their drawings suck and they looked like hippies! Lisa: Dad, you're not really reconsidering evolution, are you? Homer: My mind is always open to new ideas... (Sees onions placed in his peas) ONIONS AND PEAS? WHAT THE HELL? (Throws plate at the wall behind him)
TV: Gabbo, Gabbo, GABBO! (Bart and Homer stare in awe at the T.V.) Bart: Did you see that? Homer: Yeah! Bart: Who's Gabbo? Homer: I figure it's some guy. (Pause) Some guy named Gabbo.
Homer: As *Tolstoy* said in *Quotable Notables*, 'Give me learning, sir, and you may keep your black bread.'
Homer: I had a feeling it was too good to be true. Every time you get a million dollars, something queers the deal. Lisa: I don't think real checks have exclamation points.
Lisa: Dad, that's the water softener. Homer: Well, I am missing the back of my head. I think you can cut me some slack.
Marge: Oh no! My baby's up there! Lisa: It's okay, mom! (Holds up rope) I have a safety line! Homer: (To Jesse) This is your fault, with your non-threatening *Bobby Sherman* style good looks! No girl could resist your charms! Jesse: This was her choice, Mr. Simpson. Homer: I'm sorry, I wasn't listening. I was lost in your eyes.
Homer: If this were a cartoon, the cliff would fall off now.
Homer: People in other countries make love? It's about time.
Homer: (After Marge got knocked out on the floor) Marge, speak to me! Marge: I think you've put on a little weight. Homer: Nag nag nag...
Homer: Well, the toaster's never been wrong before.
Homer: It's bad luck to eat an even number of cheese cubes.
Homer: I guess these days head-hunters can be anything.
Homer: Is that all this temporary job was to you, a gig?
Homer: I'm a yo-yo dieter. Yo, hot dog man! Yo, peanuts!
Homer: Look at me. I'm flying like *Superman's* dog.
Homer: Oh, I've seen that look before. That's the I ate the last piece of wedding cake she's been saving in the freezer ten years look. Marge: You what?
Homer: Can you help me out? I need change for a dollar. Oh, I also need a dollar.
Ned Flanders: Hey Homer! How was your Christmas? Homer: It was ok. I got *Seinfeld* season seven.
Homer: He who is tired of *Weird Al* is tired of life.
Homer: You left a hole in my heart that could never be filled. So, I filled it with food, but I'm never full.
Homer: I'm fine, it's my feelings that are mad.
Homer: Drunk and disorderly? That's a little redundant.
Homer: Son, coin collecting is a lot like life. It stopped being fun a long time ago.
Bart: Uh, dad, whenever I would hang out with grandma, she would ask me about you and I would say you suck, and she would say you didn't suck that bad. Homer: She said I didn't suck? Bart: That bad. Homer: That bad, wow. Bart: Yeah.
Homer: Oh, he's gone and he's never coming back. Wait! There he is! No, it's a horse...
Homer: I don't have to be careful. I got a gun.
Homer: Sooner or later everyone meets their Homer.
Homer: Just pick a dead end and chill out 'till you die.
Homer: ...and anything else my limited imagination can come up with...
Marge: The last time you ate there you spent three nights in the mall jail. Homer: That was last week and you're still bringing that up.
Bart: Dad, I've got some bad news. Homer: Your mother's not pregnant, is she?
Lisa: I thought we're doing this out of friendship. Homer: That doesn't sound like me.
Homer: I promise you kids lots of things. That's what makes me such a good father! Lisa: Actually, keeping promises would make you a good father. Homer: No, that would make me a great father.
Marge: Well, maybe our next anniversary will be more romantic. Aww, look, Homey, our wedding cake! Homer: You mean there's been cake in our freezer for eleven years? Why was I not informed?
Homer: Ah, Ethnictown. Where hard-working immigrants dream of becoming lazy, overfed Americans.
Marge: This should be a time... for communication. Homer: That's a good idea, dear. Bart, turn on the T.V.
Marge: Homer, the Lord only asks for an hour a week. Homer: Well in that case he should've made the week an hour longer. (Mumbles) Lousy God...
Homer: I hope you learned your lesson, Lisa. Never help anyone.
Homer; Sorry honey, I wasn't listening and I won't be listening now.
Marge: Dear Lord, please give my stubborn husband the wisdom to see that I am right, as usual. Homer: To late Marge. I already used a prayer block on your prayer. Homer: There's no such thing as prayer blocks. Homer: Yeah right.
Homer: You're a month behind on homework? Bart: I tried really hard to stop you from finding out. Does that help? Homer: A little!
Homer: Oh, Marge, I thought I had an appetite for destruction, but all I wanted was a club sandwich.
Smithers: Simpson, what are you doing here? Why aren't you at work? Homer: I made a bad mistake and Lenny sent me home to think about what I did. I don't remember what it was, so I'm watching T.V.
Homer: (After realizing that he has a problem with anger) Very well. I'm not gonna be Angry Dad for one day longer! I'm giving up anger forever! Marge: If you ask me, you should give up fatty foods. Homer: I said anger!
Bart: Hmmm... all I need is one classic character. (Sees Homer outside struggling with a lawn chair) Homer: Widat-wi-stupid lawn chair! Unfold you... (Chair snaps his tongue) OUCH! Bart: Perfect! (Begins drawing) Homer: This'll teach that stupid chair... AAAAAAAHHHH! I'm on fire! (Shows Homer running around on fire) Aaaaaah... I hope no ones drawing this! Aaaahh!
Homer: (Drunk) Did you ever see that *Blue Man Group*? Total rip-off of the *Smurfs*. And the *Smurfs*... they suck!
Lisa: Mom, dad, there's something I have to do. You're not gonna like it, but I really believe it's the right thing. (Leaves) Homer: Marge, she's gonna narc on our stash! Marge: We don't have a stash. Homer: (Shifty eyes) No, of... course not.
Homer: Now we just sit back and wait for an *NFL* franchise. Cardinals Representative: I couldn't help overhearing... I represent the *Arizona Cardinals*... Homer: Keep walking.
Al: Homer, did you polish your head in the Shine-O Ball-O? Homer: No sir. Al: Alright, then.
Lisa: Stop doing that. Homer: Do'h or WOO-HOO? Lisa: Both.
Homer: Oh son, I can't quit drinking anymore then I can quit being a man.
Homer: Oh, I don't know. There's something about this noose I just don't like.
Homer: No, stop! No *Star Wars* parodies.
Homer: Is it drinking and driving if you flying a blimp?
Homer: Oh, that's ridiculous. How can two people from the same family need therapy?
Homer: Yeah strangling. I mean it's not the only tool in my parenting tool box, but uh, it's the sharpest...
Marge: That's great. Then you won't mind me enrolling you in a fathering class. Homer: I'd like to see you sub through an extension school catalog and find one... Ahhh... Marge: Here's one right here. Homer: Please Marge, no. The other negligent dads will make fun of me. Their so clicky. Marge: You'll be fine. You always are. Homer: Oh, I miss my friends from drunk driving school.
Bart: Dad, are you hurt? Homer: Just... my bones... and organs.
Homer: Bart's never going to forgive me for humiliating him. Marge: And I wouldn't blame him. You destroyed our son's self esteem. Homer: Well it was your idea to give him self esteem in the first place.
Homer: Lousy dog. If you had your way I'd walk you every day.
Marge: Which is our room again? Homer: You know, it had that painting of that lady and that monster on the ceiling. Marge: That was a mirror.
Homer: WOO-HOO! Underpants dinner! Marge: No it's not!
Homer: Marge, unlike C.P.R., this is something I must know.
Homer: I liked the producing, the executive producing, and especially the co-producing, but the supervising producing was the best I've ever seen.
Homer: Stupid kid, thinks he's smarter then a computer.
Homer: Boys don't have feelings, they have muscles. Marge: Why do you say such ridiculous things? Homer: They sound good in my brain then my tongue makes not the words sound very good... formally.
Homer: You can't close. I'll have to go home and drink better beer, at half the price, in natural lighting!
Homer: Oh, man. Who would think the first day of Lent would be such a bummer?
Homer: Marge don't worry. It's like when we stopped paying the phone bill. They stopped calling us, in fact everyone did.
Homer: Oh, why would you bring me here? It's like bringing *Richard Nixon* to the *Watergate* or *Kevin Costner* to *Waterworld*.
Homer: I want him to know that if your life doesn't turn out the way you wanted. there's someone else to blame. Bart: I already knew that. I'm going to blame you. Homer: I respect your choice.
Homer: ...a simpler time when the only thing we worried about was total nuclear annihilation.
Homer: If losers like me know one thing, that deep down winners like him are miserable.
Homer: Marge, I'm going to a hardcore gay club and I won't be back 'till three in the morning. Marge: Have fun!
Homer as Joseph: A pregnant virgin? That's every man's worst nightmare!
Marge: Maybe you should get a plumber to help you with that. Homer: Eh, those guys are all crooks. They charge you for parts and labor. Pick one buddy. I can do this just fine by myself.
Homer: That place was for die hard sports fans. Not guys like me who are fans when their team makes the playoffs.
Homer: Uh oh, what kind of ventilating is that? Marge: Hyper.
Homer: Well God doesn't need his own special day. Bart: What about Sunday? Homer: Sunday's the Lord's day boy, not God's. Completely different guy.
Bart: Mom, you've always been cool to me. But, Homer is a lousy dad. Homer: My dad was lousy and I didn't sue him. I just dumped in the cheapest home I could find.
Homer: Whoo! Purple Rain! Little Richard: SHUT UP! Homer: Did you hear that? *Michael Jackson* told me to shut up.
Bart: Uh, yeah, I'd like to speak to a Mr. Tabooger, first name Ollie. Homer: (Excited) Ooh, Bart, my first prank call! What do I do? Bart: Just ask if anyone knows Ollie Tabooger. Homer: (Clueless) I don't get it. Bart: (Frustrated) Yell out 'I'll eat a booger!' Homer: (Clueless) What's the gag? Bart: Oh, forget it! (Hangs up)
Homer: Area code? But it's a local call! Marge: The phone company ran out of numbers, so they split the city into two area codes. Half the town keeps the old 636 area code, and our half gets 939. Homer: 939? WHAT THE HELL IS THAT? Oh, my life is ruined. Marge: Geez, you just have to remember three extra numbers. Homer: Oh, if only it were that easy Marge.
Bart: Somebody ought to ruin Gabbo's career the way he ruined Krusty's. Lisa: Two wrongs don't make a right, Bart. Bart: Yes, they do. Lisa: No, they don't. Bart: Yes, they do. Lisa: No, they don't. Bart: Yes, they do. Lisa: Dad! Homer: Two wrongs make a right, Lisa.
Moe: Cheer up, Homer. You still got that other kid, Lisa. We'll take her hunting and make her into a man. Homer: She'd never go. She's a vegetarian. Moe: Oh, jeez Homer, jeez! You and Marge ain't cousins, are you?
Lenny: How'd you get *R.E.M.* to play in your garage? Homer: I told them it was a benefit concert. They think we're saving the rain forest!
Barney: Today, you're gonna be a man, Bart. Bart: You guys going to teach me to drive? Moe: (To Barney) Oh yeah, let Twinkle Toes drive Betsy. Right. Homer: (Chuckling nervously) No, boy. You can't drive. You're only ten. You're going hunting. Moe: You ever been hunting before, there, Barty? Bart: Nope. Something about a bunch of guys alone together in the woods... seems kinda gay. (Awkward silence) Homer: That is a very immature attitude, young man.
Marge: Homer, do you remember your promise to the children? Homer: Sure do! When you're 18, you're out the door!
Homer: ...And like any prudent gambler I know when to walk away... Never!
Homer: Beneath this smile I'm in awful, awful pain...
Homer: Wow! Nobody gives better parenting advice then childless drunks!
Marge: I'm still mad at you for last night. Homer: Today is the first which means it was last month which means you're being ridiculous.
Homer: (To Patty and Selma) Go ugly someone else's house. You penis curling she devils.
John: Homer, what have you got against Gays? Homer: You know! It's not... usual. If there was a law, it'd be against it! Marge: Oh, Homer, please! You're embarrassing yourself. Homer: No, I'm not, Marge! They're embarrassing me. They're embarrassing America! They turned the *Navy* into a floating joke. They ruined all our best names like Bruce, and Lance, and Julian. Those were the toughest names we had! Now they're just, uh... John: Queer? Homer: Yeah, and that's another thing! I resent you people using that word. That's our word for making fun of you! We need it! Well, I'm taking back our word, and I'm taking back my son!
Homer: Marge, the boy was wearing a Hawaiian shirt. Marge: So? Homer: There's only two kinds of guys who wear those shirts: gay guys and big, fat party animals. And Bart doesn't look like a big, fat party animal to me... Marge: So, if you wore a Hawaiian shirt, it wouldn't be gay? Homer: Right. Thank you.
Marge: Homer, didn't John seem a little... festive to you? Homer: Couldn't agree more. Happy as a clam. Marge: He prefers the company of men! Homer: Who doesn't?
John: It's camp!... The tragically ludicrous? The ludicrously tragic? Homer: Oh, yeah... Like when a clown dies.
Homer: I guess it wouldn't do any good to run 'cause you're a mail-lady and you know my name and address and everything, huh? Postal Worker: That's right. Homer: Well.. I'm still going to run.
Marge: Homer, you don't do things like that to be rewarded. You do them because a fellow human being needs a helping hand. Homer: Marge, you're my wife, I love you very much, but you're living in a world of make-believe! With flowers and bells and leprechauns and magic frogs with funny little hats.
Marge: Have you been up all night eating cheese? Homer: I think I'm blind...
Homer: I've never been so relieved... relieved, and angry!
Homer: Drive my kids to school? Never!
Homer: Let me get the camera we use for precious moments and insurance claims.
TV Announcer: Next on *Fox*, *Carmen Electra* stars in 'Boobs,' about a class of remedial reading students and their teacher who wants to be taken seriously. Homer: (Disappointed) Awww, I thought it was about her boobs.
Homer: All right, pal. I've made a diagram of all the places on Marge you're not allowed to touch. (Shows diagram) Especially the hair! Charles: Oh, not to worry. I'm a bit of an elbow man myself. Bit different... bit weird... not sexual. Homer: You take forever to say nothing.
Homer: I am so stoked about Lenny's party, he said he's gonna make a surprise announcement. Marge: Oooh, maybe he's getting married. Homer: Cuph! Why the Hell would he wanna do that... (Marge is frowning) ...blessed sacrament, that has made my life so rich? I like your hat, sweetie. Marge: I'm not wearing a hat. Homer: I mean... the one at the house.
Homer as Joseph: Oh, this is the worst Christmas ever!
Homer: Homey, just tell them what they want to hear. Homer: I can't, latkas aren't as good as American pancakes.
Homer: Son, if I was interested in fun I would have run away the day you were born.
Waitress: What will you have? Homer: I'll have the smiley faced breakfast special, but could you add a bacon nose, bacon hair, bacon mustache, 5 o'clock shadow made of bacon bits and a bacon body.
Homer: (At the *Leaning Tower of Pisa*) I've seen this in pictures, but you have to actually be there to really experience it. (Camera pans out showing that they are at *McDonald's*) A *McDonald's* that actually serves booze!
Homer: Holy moly! I always thought you were, you know, out loud and proud. Sideshow Bob: Well, I experimented in college, as one does. Homer: Yeah, I never went to college. Sideshow Bob: (Not surprised) Stop the presses.
Homer: (Answering phone) 'Yello? Bart: (In raspy voice) This is the kidnapper. Do what I say and Bart won't get hurt! Homer: Oh yeah? Send a finger wrapped in today's paper to prove you have him! Marge: Homer!
Homer: Lousy American made dog!
Homer: Sorry Marge, the last time I stepped on a baseball field I got tazzed.
Homer: This is my favorite family tradition, ice cream after a botched recital.
Homer: I can't believe how easy it is in this country to get cigarettes. (Putting his gun in his jacket to reveal more guns)
Homer: I thought this might happen. So, I bought the best weapon to operate while drugged. A cross bow.
Homer: Son, while your mother, and little mother are out, I'm going to let you in on a deep dark family secret. Bart: You have a drinking problem? Homer: I said a secret.
Homer: The Internet wasn't created for mockery, it was supposed to help researchers at different universities share data sets. It was!
Marge: (Reading aloud) We have kidnapped your son... follow instructions and Bart will not be harmed! Homer: Follow instructions? He's doomed!
Homer: I can see you need your dad more than ever! Grandpa: And Homer, I can see you need me more than ever. Homer: Get back in the garage, old man! Grandpa: But, there's spiders in the boxes. Homer: Stay out of my boxes!
Homer: Please don't hurt me! I won't tell anyone about the skeleton. And I can bring you more victims, like Lenny! He'd go great with wild rice!
Bart: What happened to you, Homer? You used to be cool. Homer: I'm still cool! Bart: Nah. You've changed, man. Homer: Well I do have this robotic prostate, but you can't see it. (Homer looks down) Oh, you can.
Homer: Oh, what a bleak and horrible future we live in! Bart: Don't you mean present? Homer: Right, right. Present.
Marge: What are you doing? Homer: I'm writing a delicious send-up of Mr. Burns for his birthday party. Is 'poopoo' one word or two?
Homer: We'd like to dedicate this next number to a very special woman. She's a hundred years old, and she weighs over two hundred... tons. Man: This enormous woman will devour us all! Aah! (Jumps into the water) Homer: Er, I meant the statue...
Homer: Stand back and watch the pro. Lisa: Uhh, shouldn't you put on a batting helmet? Homer: Nah, it'll mess up my hair.
Homer: I know we don't call as often as we should and we aren't as well behaved as our goodie two-shoes brother Canada. Who by the way has never had a girlfriend... I'm just saying.
Homer: Oh Marge, I'm so sorry. I should have listened to whatever it was you were saying.
Homer: I'm the worst thing to happen to sports since *Fox*.
Homer: Calendar? Oh my God. I forgot to move Carl's 12:30 to 2:30. Oh, his astrologist will show up at the same time as his astronomer.
Homer: To the panic room! Marge: We don't have a panic room. Homer: To the panic room store!
Marge: My husband has forgot our last three Anniversaries, he made a badminton net out of my wedding dress, which he hardly ever uses, and last week, he called out his bowling balls' name during sex!
Homer: Maybe the Internet can help me out. It sure gave some good advice on wang enhancement. Okay, 'www.nuclearsecrets.com.' 'Are you a terrorist?' No. 'Would you like to meet someone new, but are tired of the bar scene?' No! I will never tire of the bar scene!
Homer: How hard can it be to build a nuclear reactor? Korea did it, and look at the quality of their animation. (Continues talking, and the animation of his mouth slips off his face)
Bart: Just watch the *Conan O'Brian* show. You'll see. Homer: Alright. But after *Leno*, I'm all laughed out, you know.
Homer: Ahh! Fire! Wait, the song! (Singing) When the fire starts to burn, there's a lesson you must learn. Something, something, then you'll see. You'll avoid catastrophe... D'oh!
Homer: This is some way to show your gratitude, no gold, no diamonds, no rubies, not even a lousy card! Wait a minute, there was a card... that's what got me so mad in the first place!
Homer: Hey little girl, what's your name? Little girl: Ooliooliookietelawanjay. Homer: Fine, I'll call you, Lisa Jr.
Homer: Oh, what's the big deal, Bart didn't like his presents? So what? It's not like he gives us such great gifts. Remember that maple leaf iron between the sheets of wax paper. What was that? That was crap!
Homer: I understand honey. I used to believe in things when I was a kid.
Marge: Why do you have to eat peanuts in the shower? Homer: Can't start the day without that fresh from the circus feeling.
Marge: Homer no! Revenge never solves anything! Homer: Then what is America doing in Iraq?
Apu: Sir, you look familiar. Are you on the television or something? Homer: Sorry, buddy. You've got me confused with *Fred Flintstone*.
Homer: We left plenty of food so you won't starve. Grandpa: Oh, thank you. Homer: I was talking to the cat.
Patty: Hey, saturated fats, I need a favor. Homer: Let me get my belt sander, maybe I can try to grind some of the ugly off your face! Patty: Ha ha ha, very funny. Homer: I wasn't joking! (Homer pulls out a belt sander, turns it on, and advances on Patty)
Wink: You may come down if you can answer one question about Japan. Homer: Is the answer Japan? Wink: Actually, it is. (Yells in Japanese to someone offstage, translation: You idiot! Who the hell gave the answer?)
Marge: Come on, Homer. Japan will be fun. You liked Rashomon. Homer: That's not how I remember it. Besides, if I wanted to see Japanese people I could have gone to the zoo. Marge: Homer! Homer: What? The man who washes the elephants is Japanese. His name is Takashi. He's in my book club.
Lisa: (The Simpson family visits a cyber cafe) Wow, Dad, you're surfing like a pro! Homer: Oh, yeah! I'm betting on *Jai-alai* in the Cayman Islands, I invested in something called '*News Corp*'... Lisa: Dad! That's *Fox*! Homer: AAHH! Undo! Undo!
Homer: Oh... but Marge, am I doomed to spend the rest of my life sweating like a pig? Bart: Yeah, not to mention looking like a pig, eating like a pig... Apu: Don't forget the smell. Homer: Will you get off my front lawn? Apu: Why don't you make me? Homer: Why! Oh, I give up.
Homer: Marge, I know you didn't believe me about the vending machines, that's why I had the firemen write me a note! Marge: (Reading) 'Mrs. Simpson, while we were out rescuing your husband, a lumber yard burned down. Homer: D'oh! (Ruefully) Lumber has a million uses.
Bart: I'd do anything to go to that show! Homer: I'd sell my first-born son! Bart: Hey! Homer: You'll do as you're told!
Insurance Troy McClure: Any valuables in the house? Homer: Well, there was the *Picasso*, my collection of classic cars... Insurance Troy McClure: Sorry. This policy only covers actual losses... Homer: (Miffed) Well that's just great!
Homer: Now, I'm not saying Mr. Burns is incontinent... Bart: Incontinent! (Laughs) Too rich! Lisa: Does either of you know what 'incontinent' means?
Homer: A woman is a lot like a refrigerator. Six feet tall, 300 pounds... it makes ice...
Marge: Are you really going to ignore Grandpa for the rest of your life? Homer: Of course not, just for the rest of his life.
Bart: You know, Grandpa kinda smells like that trunk in the garage where the bottom's all wet. Lisa: Nuh-uh, he smells more like a photo lab. Homer: Stop it, both of you! Grandpa smells like a regular old man, which is more like a hallway in a hospital.
Marge: We can't afford to buy a pony. Homer: Marge, with today's gasoline prices, we can't afford not to buy a pony.
Homer: Oh, every thing's cruel according to you. Keeping him chained up in the backyard is cruel. Pulling on his tail is cruel. Yelling in his ears is cruel. Everything is cruel. So excuse me if I'm cruel.
Apu: What's the matter, sir? Never have I seen you look so unhappy while purchasing such a large quantity of ice cream. Homer: The reason I look unhappy is that tonight I have to see a slide show starring my wife's sisters. Or as I call 'em, the Gruesome Twosome.
Lisa: Remember, Dad. The handle of the Big Dipper points to the North Star. Homer: That's nice, Lisa, but we're not in astronomy class. We're in the woods.
Lisa: (Reading) Come to Homer's BBBQ. The extra 'B' is for BYOBB. Bart: What's THAT extra 'B' for? Homer: That's a typo.
Lisa: Dad, someone stole my saxophone. Homer: WOO-HOO! Bart: Dad, someone stole our portable T.V. Homer: D'oh!
Rescue Worker: Homer, there's no easy way to put this, but we're going to have to saw your arms off. Homer: They'll grow back, right? Rescue Worker: Oh...yeah. Homer: Whew.
Rescue Worker: Homer, are you still holding onto the can? Homer: Your point being...? (Homer leaves the plant where everyone is laughing)
Worker 1: Excuse me, we wanted to see the geek who valued the happiness of his children more than money. Homer: Right here... Worker 2: Aw, You said his head was the size of a baseball. Homer: Ugh, My life can't get any worse... Smithers: (Over intercom) Homer Simpson, report for much worse duties. Homer: Do'h!
Marge: Lisa, watch out for poison ivy. Remember, leaves of three, let it be. Homer: Leaves of four, eat some more!
Homer: Son, a woman is like a beer. They look good, they smell good, you'd step over your own mother just to get one! But you can't stop at one. You wanna drink another woman!
Homer: Facts are meaningless. You could use facts to prove anything that's even remotely true. Facts, schmacts.
Homer: Why did this have to happen during prime-time, when T.V.'s brightest stars come out to shine?
Homer: Well, you're to blame for not being here. So in a way, this is all your fault. Well, this is your mess and I'll be damned if I'm having anything to do with it.
Homer: It seems that the cat has been caught by the very person who was trying to catch him.
Homer: BART! You can't weld with such a little flame! (Grumbling) Stupid kid...
Lisa: Ugh! I wish I'd never found those stupid bones! It's time to put an end to this. Bart, I'm borrowing your blue crowbar. Bart: Good ol' Blue-y. Marge: Hey, she's gonna smash the angel! Homer: Somebody stop her! Lisa: (Walks into garage, turns on the light) (Gasps) It's gone! Homer: (Weeping) Oh, no! This can't be happening! What the hell are we gonna do with 10,000 angel ashtrays? (Sobbing) Bart: I could take up smoking. Homer: You damn well better.
Homer: All my life I've had one dream, to achieve my many goals.
Homer: Oh, what do I do? Patty is going to kill me. Unless, I kill her first. I put the body in the car. I dump the car in the lake. I put a *James Taylor* C.D. in the stereo so they think it's a suicide...
Homer: I'll just keep cutting until I hit something solid.
Homer: (Crying) She just wanted to ride bikes through New England, but those seats hurt my ass.
Homer: You know, Marge, that Bart is a little miracle, his winning smile, his button nose, his fat little stomach, his face alight with wholesome mischief. He reminds me of me before the weight of the world crushed my spirit.
Marge: I know we didn't ask for this, Homer, but doesn't the Bible say, 'Whatsoever you do to the least of my brothers, that you do unto me?' Homer: Yes, but doesn't the Bible also say, 'Thou shalt not take moochers into thy hut?'
Marge: How was your day at work, dear? Homer: Oh, the usual. Stand in front of this, open that, pull down this, bend over, spread apart that, turn your head that way, cough...
Bart: You're absolutely right, Homer. We don't need a babysitter! Homer: (Suspicious) Wait a second... (Pulls a card from his pocket: 'Always do the opposite of what Bart says.') Homer: Hmm... you kids do need a babysitter! Bart: Blast that infernal card! (To Homer) Don't give that card to me. Homer: Here you g... (Pulls back) No!
Homer: All right, Herb. I'll give you the money. But first you have to forgive me and treat me like a brother. Herb: Nope. Homer: All right, then just give me the drinking bird.
Marge: I think the money should be spent on something the whole town can be proud of. Homer: Like a giant billboard that says 'No fat chicks!'? Marge: No.
Homer: Lisa! Never ever stop in the middle of a hoedown!
Marge: (After fire caused by birthday candle) This disaster was a real wake up call, we need to find a way to protect our irreplaceables. Firefighter: You could buy a fire-proof safe. Homer: Or we could just resolve to be more careful with our open flames. Firefighter: Sir, we've been here six times this month. Homer: Yeah but, uhm, one of those I dialed 911 by mistake but I was too embarrassed to admit it, so I set the house on fire. Feels good to tell the truth... no I'm lying again it feels bad.
Homer: (Singing) Oh, Margie... You came and you gave me a turkey... On my vacation away from working...
Homer: Son, one day you're going to be a great father. Bart: Aww, and someday you'll be one too. Homer: Thanks boy, heh heh heh!
Homer: Oh, there's so much I don't know about astrophysics. I wish I'd read that book by that wheelchair guy.
Homer: Who are you? Guardian Angel: Homer, I am your Guardian Angel, I have assumed the form of someone who you idolize and revere, *Sir Isaac Newton*. Homer: Sir Isa Who? Guardian Angel: Oh very well. (Homer's Guardian Angel changes shape and becomes Col. Klink, from Hogan's Heroes) Homer: *Col. Klink!* Did you ever get my letters? Guardian Angel: (In Klink's voice) Homer! I am not *Col. Klink*. I am just assuming his form. Homer: (Chuckles) Did you know that *Hogan* had tunnels all over your camp? Guardian Angel: (Quiver in voice) Homer!
Homer: (Snugly wrapped in bed) Ah, I'm just a big toasty cinnamon bun. I never wanna leave this bed! Uh-oh. Gotta take a whizz. Think, Homer, think. Think, think, think! Aw... I better get up. Homer: (In the bathroom) I'm whizzin' with the door open... and I love it!
Marge: We're just going to have to cut down on luxuries. Homer: Well, you know, we're always buying Maggie vaccinations for diseases she doesn't even have!
Lisa: Wait dad, I've got something for you. (Kisses him) Homer: Oh, I was hoping it'd be money.
Marge: That's illegal! Homer: That's for the courts to decide!
Homer: (Singing) I am so smart, I am so smart, s-m-r-t... I mean s-m-A-r-t.
Bart: And I'll take up smoking and give that up. Homer: Good for you, son. Giving up smoking is one of the hardest things you'll ever have to do. Have a dollar. Lisa: But he didn't do anything! Homer: (Wisely) Didn't he, Lisa? Didn't he? (Realizes) Hey, wait a minute... he didn't! (Snatches the dollar back)
Homer: Look at these low, low price on famous name-brand electronics! Bart: Don't be a sap, dad. These are just crappy knock-offs! Homer: Pfft! I know a genuine SORNY when I see one!
Homer: 'Dear Homer, I.O.U. one emergency donut. Signed, Homer.' Bastard! He's always one step ahead.
Homer: (Wearing *Henry Kissinger's* glasses) The sum of the square roots of any two sides of an isosceles triangle is equal to the square root of the remaining side. Man on Toilet: That's a right triangle, you idiot! Homer: D'oh!
Homer: I can't believe we spent $2,000 on this when right now rollers could be kneading my buttocks. Herb: Homer, will you stop thinking about your ass? Homer: I try, but I can't.
Homer: (Reading screen) 'To Start Press Any Key.' Where's the ANY key? I see Esk ('ESC'), Catarl ('CTRL'), and Pig-Up ('PGUP'). There doesn't seem to be any ANY key. Woo! All this computer hacking is making me thirsty. I think I'll order a *TAB*. (Presses TAB key)
Homer: For the last time, *Bush*, apologize for spanking my boy! George George HW Bush: Never! Tell him to apologize for destroying my memoirs! Homer: (To Bart) You didn't tell me you destroyed his memoirs. (To Bush) NEVER!
Homer: Isn't there a pound where you can pick up cheap ponies that ran away from home?
Marge: Homey, you've got to stop looking for the quick fix. If you keep spending time with Lisa, she'll forgive you. Homer: Marge, if I spend any more time doing these girl things, I'm going to, you know, go fruity.
Homer: Maybe I should just cut my losses, give up on Lisa, and make a fresh start with Maggie.
Homer: Look, I get enough admiration and respect at work! I don't need it here at home!
Homer: Who'd have thought a nuclear reactor would be so complicated?
Ned Flanders: Hi giggly, hey neighbor! Homer: OH MY GOD! THIS DUDE DOES THE BEST FLANDERS! You got the mustache, and the diddly. Ned Flanders: Heh heh heh...Homer it's me, Ned Flanders. Homer: Oh right, the God dude.
Homer: In America, first you get the sugar, then you get the power, then you get the women.
Homer: The slim lazy Homer you knew is dead. Now I'm a big fat dynamo! And where's that cake?
Homer: Could Jesus microwave a burrito so hot that he himself could not eat it?
Doctor: Mr. Simpson, after talking to your wife, we believe you're no threat to yourself or others. Homer: That's the most flattering thing anyone has ever said to me.
Homer: I gotta call my family. Oh, this is so embarrassing, calling them from a nuthouse. I mean, they think I'm a god!
Homer: Son, it's no different than the time I let you vote for me. Remember that absentee ballot?
Homer: Dear Lord: The gods have been good to me. For the first time in my life, everything is absolutely perfect just the way it is. So here's the deAl: You freeze everything the way it is, and I won't ask for anything more. If that is Ok, please give me absolutely no sign... Ok, deal. In gratitude, I present you this offering of cookies and milk. If you want me to eat them for you, give me no sign... Thy will be done.
Homer: Kids, kids. As far as daddy's concerned, you're both potential murderers.
Homer: I guess some people never change. Or, they quickly change and then quickly change back.
Homer: Print name? Oh...
Homer: Just because I'm wearing a pink shirt doesn't mean I'm some kind of pink doughnut eater... although it is tempting.
Homer: You know what you two need? A little comic strip called '*Love is*.' It's about two naked 8-year olds who are married.
Herb: Every word you say makes me want to punch you in the face! Homer: Well, while you're a guest in my home, could you just try to kick me in the butt? Herb: I'll try, but I'm not making any promises.
Homer: Aagh! Pink? Marge, I can't wear a pink shirt to work. Everybody wears white shirts. I'm not popular enough to be different...
Homer: Bart! Get out of the *Spirit of St. Louis*!
Homer: Well, if kids are so innocent, why is everything bad named after them? Acting childish, kidnapping, child abuse... Bart: What about adultery? Homer: Not until you're older, son.
Homer: Helllooo, my name is Mr. Burns. I believe you have a letter for me. Postal Clerk: Okay, Mr. Burns, uh, what's your first name? Homer: ...I don't know.
Homer: Marriage is like a coffin and each kid is like another nail.
Homer: (Singing) Spider Pig, Spider Pig, does what ever a Spider Pig does. Can he swing from a web? No he can't, he's a pig. Look out, he is the Spider Pig.
Homer: Do you want the job done right, or do you want it done fast?
Bart: This is the worst day of my life. Homer: The worst day of your life so far...
Homer: (Looking at map) North... south... aw, nuts to this! I'm going to take a shortcut. Marge: Homer, no, you're going to get lost. Homer: Trust me, Marge. With today's modern cars, you can't get lost, what with all the silicon chips and such.
Bart: Military school? You guys lied to me! Homer: Well, I'm sorry if you heard '*Disneyland*,' but I distinctly said, 'military school!'
Homer: I want to share something with you: The three little sentences that will get you through life. Number 1: Cover for me. Number 2: Oh, good idea, Boss! Number 3: It was like that when I got here.
Homer: Sometimes the only way you can feel good about yourself is by making someone else look bad. And I'm tired of making other people feel good about themselves.
Homer: I probably shouldn't have eaten that packet of powered gravy I found in the parking lot.
Homer: Marge, you being a cop makes you the man! Which makes me the woman, and I have no interest in that, besides occasionally wearing the underwear, which as we discussed, is strictly a comfort thing.
Homer: How could you? Haven't you learned anything from that guy who gives those sermons at church? Captain Whatshisname? We live in a society of laws! Why do you think I took you to all those *Police Academy* movies? For fun? Well, I didn't hear anybody laughing, did you? Except at that guy who made sound effects. Makes sound effects and laughs. Where was I? Oh yeah! Stay out of my booze!
Homer: (To Bart) You gave both dogs away? You know how I feel about giving!
Homer: Ooh, Mama! This is finally really happening. After years of disappointment with get-rich-quick schemes, I know I'm gonna get rich with this scheme... and quick!
Homer: Volunteering is for suckers. Did you know that so called volunteers don't even get paid?
Homer: A job's a job. I mean, take me. If my plant pollutes the water and poisons the town, by your logic, that would make me a criminal.
Homer: I think the saddest day of my life was when I realized I could beat my dad at most things, and Bart experienced that at the age of four.
Homer: This is the most exciting thing I've seen since *Halley's Comet* collided with the moon.
Homer: I'm awake. I'm awake. I'm a productive member of the team. You can't fire me, I quit! Please, I have a family.
Homer: Look at them. Watching my T.V. Sitting on my couch. You better not be in my ass groove!
Homer: I felt a surge of power, like God must feel, when he's holding a gun.
Homer: Marge, this ticket doesn't just get me a seat. It gives me the right... no, the DUTY to make a complete ass of myself!
Young Bart: Krusty funny. Homer: Well, duh...
Homer: (Singing) Call Mr. Plow, that's my name. That name again is Mr. Plow.
Homer: For the first time in my life, people weren't laughing at me, they were laughing towards me!
Homer: I must have the right... what's that stuff?
Homer: Who is Fonzy? Don't they teach you anything at school?
Lisa: To the reference desk! Homer: The library? Can you believe we're married to those nerds?
Homer: Bart, you're saying butt-kisser like it's a bad thing!
Homer: I won't sleep in the same bed with a woman who thinks I'm lazy! I'm going right downstairs, unfold the couch, unroll the sleeping ba... (Goes back to bed) uh, goodnight.
Homer: I've got two questions. One, where's the fife? And two, gimme the fife.
Homer: What is a wedding? *Webster's Dictionary* defines a wedding as 'The process of removing weeds from one's garden.' (Giving a lecture on marriage).
Homer: Marge, your paintings look like the things they look like.
Homer: Hey, can you take the wheel for a second, I have to scratch my self in two places at once.
Homer: Marge! Look at all this great stuff I found at the Marina. It was just sitting in some guy's boat!
Homer: We monorail conductors are a crazy breed.
Homer: Yeah, the Simpson family is a long line of horse thieves, dead beats, horse beats, dead thieves, and even a few ...alcoholics.
Lisa: I can't believe we're descendants of slave owners. Homer: Me nether, for once the Simpsons were in management. Marge: Homer!
Homer: The motto of the Simpsons is: 'Quit while you're ahead.'
Homer: I kicked a giant mouse in the butt! Do I have to draw you a picture?
Homer: You know those balls that they put on car antennas so you can find them in the parking lot? Those should be on EVERY car!
Homer: We're gonna get a new T.V. Twenty-one inch screen, realistic flesh tones, and a little cart so we can wheel it into the dining room on holidays.
Homer: Well, I'm tired of being a wannabe league bowler. I wanna be a league bowler!
Homer: Well you know boys, a nuclear reactor is a lot like women. You just have to read the manual and press the right button.
Homer: Oh look at me! I'm making people happy! I'm the magical man from happy land, with a gumdrop house on lollipop lane! Oh, by the way... I was being sarcastic.
Homer: First you don't want me to get the pony, then you want me to take it back. Make up your mind.
Marge: Homer, you cannot miss Lisa's big day. And you have to come sober! Homer: American sober or Irish sober? Marge: .08 sober! Homer: .15! Marge: .09! Homer: .10 with a stomach full of bread. My final offer. Marge: (Groans) Deal.
Homer: Meals on wheels... Eat up or I go to jail. Crazy Old Guy: Didn't these meals used to have a cobbler? Homer: Uh, they discontinued the cobbler. Crazy Old Guy: You smell like cobbler. Homer: Now, let's not get into who smells like what.
Homer: If they think I'm going to stop at that stop sign, they're sadly mistaken!
Bart: Dad, you were great! Lisa: And you contributed to our culture! Homer: (Worried) Well, I didn't mean to. Lisa: No, no, it's a good thing. Homer: Oh, good. This makes up for me showing up drunk to the father-daughter dance. Lisa: The dance isn't 'til next week. Homer: Sorry, Lisa. Can't change the future.
Homer: (Grabbing Marge) Yer gotta redda kid forrad yarrar! Marge: Homer, what is it? Slow down! Homer: (Slower) J'yer gedda ferda redderarrar. Marge: THINK before you say each word. Homer: You broke a promise to your child. Marge: What? Homer: You promised Lisa to help her with her costume. You made her cry. Then I cried. Then Maggie laughed... Oh, she's such a little trooper.
Homer: I may just quit my job at the plant to become a full-time stock market guy.
Homer: Oh, Lisa, you and your stories... Bart's a vampire, beer kills brain cells. Now let's go back to that... building... thingie... where our beds and T.V... is.
Homer: Damn it! I'm no supervising technician. I'm a technical supervisor. It's too late to teach this old dog new tricks.
Homer: Nobody snuggles with Max Power. You strap yourself in and feel the G's!
Bart: Dad, do I have to brush my teeth? Homer: Nah, but at least rinse your mouth out with soda.
Homer: This is the kind of car you see in commercials.
Homer: Aww... Don't give up boy. I believe in you, and not just because I have too.
Homer: I don't apologize. I am sorry Lisa, that's the way I am.
Homer: It's a good thing that beer wasn't shaken up any more, or I'd have looked quite the fool. An April fool, as it were.
Homer: Man, I got more trophies than *Wayne Gretzky* and *The Pope* combined.
Bart: Cool, a lie detector. (Bart puts on the lie detector and a results sheet prints out as he speaks) Bart: Lisa is a dork. Lisa is a dork.  Lisa: Dad, make him stop. (Homer looks at the results sheet) Homer: Hmm... According to this, he's telling the truth.
Homer: Vietnam veteran. Gatekeeper: Do you have a military ID? Homer: ID? Damn Charlie didn't ask for ID when I fought at La Choy, and Chun King. I saw my best friend's head explode at *Margaret Cho*. Marge: Homer, give him the fifty cents. Homer: Why should I? Did my country give me a parade? No, man, they spat at me and... Gatekeeper: Just go! (Waves him in) Homer: Thank you. This closes the saddest chapter in American history.
Homer: Good horse. Here's one taco. You'll get another one when you win.
Homer: Ohh... Why do my actions have consequences?
Homer: Mr. Hammock, say hello to Madame Ass!
Homer: I hate traffic, the band and the phenomenon.
Homer: Good drink... good meat... good God, let's eat!
Homer: Mmmmm... fattening.
Homer: Mmmmm... foot-long chili dog.
Homer: Mmmmm... forbidden donut.
Homer: Mmmmm... free goo.
Homer: Mmmmm... free wig.
Homer: Mmmmm... fresh batch of American balls.
Homer: Mmmmm... fuzzy.
Homer: Mmmmm... ginger bread house.
Homer: Mmmmm... grapefruit.
Homer: Mmmmm... gummy-bear.
Homer: Mmmmm... gum with a cracker center.
Homer: Mmmmm... ham.
Homer: Mmmmm... hamburgers.
Homer: Mmmmm... hippo.
Homer: Mmmmm... hog fat.
Homer: Mmmmm... hogan berry.
Homer: Mmmmm... honey-smoked bacon.
Homer: Mmmmm... horse doovers.
Homer: Mmmmm... hug.
Homer: Mmmmm... incapacitating.
Homer: Mmmmm... invisible cola.
Homer: Mmmmm... macadamia nuts.
Homer: Mmmmm... marshmallows.
Homer: Mmmmm... mediciny.
Homer: Mmmmm... memo.
Homer: Mmmmm... open-faced club sandwich.
Homer: Mmmmm... organized crime.
Homer: Mmmmm... pie.
Homer: Mmmmm... pistol whip.
Homer: Mmmmm... pointy.
Homer: Mmmmm... potato chips.
Homer: Mmmmm... purple.
Homer: Mmmmm... recirculated air.
Homer: Mmmmm... reprocessed pig fat.
Homer: Mmmmm... rich creamery butter.
Homer: Mmmmm... sacrilegious.
Homer: Mmmmm... salty.
Homer: Mmmmm... sandwich.
Homer: Mmmmm... shrimp.
Homer: Mmmmm... slanty.
Homer: (Watches Santa's Little Helper eating dog food) Hey, how come he gets meat and we don't? Marge: You wouldn't want what he's eating, it's mostly just snouts and entrails. Homer: Mmmmm... snouts.
Homer: Mmmmm... lamb.
Homer: Mmmmm... soylent green.
Lurleen: Oh, Homer, you're as smart as you are handsome. Homer: Hey! Oh, you meant that as a compliment...
Chief Wiggum: All right, show's over, folks. I'm afraid this horse is going to the dog food factory. Homer: Good luck getting a horse to eat dog food.
Mr. Burns: Now, let's get down to business. Homer: (Thinking to himself) Oh, man. I have to go to the bathroom. Why did I have all that beer and coffee and watermelon? Mr. Burns: Now Homer, I know what you're thinking. I want to take the pressure off. Now, it doesn't take a whiz to know that you're looking out for Number One. Well, listen to me, and you'll make a big splash very soon. Homer: Ooh, which way to the bathroom? Mr. Burns: Oh, it's the twenty-third door on the left. Mr. Burns: (After Homer came back) So, did you find the bathroom alright? Homer: Uh... Yeah...
Homer: Can you say daddy? Baby Lisa: Homer. Homer: No sweetie, daddy. Baby Lisa: Homer. Homer: D'oh!
Homer: Here's a lesson to you kids, never love anyone! Lisa: Not even you dad? Homer: Especially me!
Homer: 'Asleep at the switch?' I wasn't asleep, I was drunk! Bart: I believe you, dad.
Homer: Lighten up ladies. It's not cheating when you're wearing a costume.
Homer: All right, men. It's time to clean-up this town! (Pause) Principal Skinner: Meaning what exactly? Homer: You know, push people around, make ourselves feel big.
Marge: I guess we could get more involved in Bart's activities but then I'd be afraid of smothering him. Homer: Yeah, and then we'd get the chair. Marge: That's not what I meant. Homer: It was, Marge, admit it.
Bart: We're natural-born Carnies, dad. If only we weren't tied down with a family. Homer: Yeah. We should start our own game, where people throw ducks at balloons and nothing's the way it seems.
Homer: (Talking to 'Police Cops' producers) Uh...so, I just wanna know how come you made your Homer Simpson character so... Producer: Stupid?... Well, I can assure you, it happened organically. Homer: It better have!
TV Announcer: It's eleven o'clock... do you know where your children are? Homer: I told you last night... No I don't!
Homer: I won't lie to you, fatherhood isn't easy like motherhood.
Homer: I think Mr. Smithers picked me for my motivational skills. Everyone always says they have to work twice as hard when I'm around!
Homer: Look everyone! Now that I'm a teacher I've sewn patches on my elbows. Marge: Homer that's supposed to be leather patches on a tweed jacket, not the other way around. You've ruined a perfectly good jacket. Homer: Incorrect, Marge. Two perfectly good jackets!
Homer: Wait, I'm no missionary! I don't even believe in Jebus! Let me out. Pilot: Sorry, no can do. Homer: Oh, save me Jebus!
Ned Flanders: How do you silence that little voice that says 'think.' Homer: You mean Lisa? Ned Flanders: No, I mean common sense! Homer: Oh, that, that can be treated with our good friend alcohol.
Homer: How come bears can crap in the woods and I can't?
Homer: See boy, the real money is in bootlegging, not your childish vandalism.
Homer: Why wouldn't anyone give me any award? Lisa: You won a *Grammy*. Homer: An award worth winning.
Homer: I have misplaced my pants.
Marge: This terrible! How will the kids get home? Homer: I dunno. Internet?
Bart: Dad, you killed the zombie Flanders! Homer: He was a zombie?
Bart: Do you even have a job anymore? Homer: I think it's pretty obvious that I don't.
Homer: You couldn't fool your mother on the foolingest day of your life if you had an electrified fooling machine.
Homer: (After an ice cream cone has hit him in the face) Nice try, God.
Homer: Wait a minute, there's something bothering me about this place. I know! This lesbian bar doesn't have a fire exit! Enjoy your death trap ladies! Woman: What was her problem?
Homer: Marge, when I join an underground cult I expect a little support from my family.
Homer: Marge, quick, how many kids do we have? No time, I'll just estimate. 9!
Bart: Knock it off back there. Homer: But we're married. Bart: Ok, but keep it PG. Homer: How about R? Bart: PG-13. Homer: WOO-HOO! Adult situations!
Homer: Stupid T.V., be more funny...
Homer: No beer and no T.V. make Homer something something... Marge: Go crazy? Homer: Don't mind if I do.
Man: Sir, other customers need to use that dressing room! Homer: Dressing room? Uh oh.
Homer: I saw weird stuff in that place last night. Weird, strange, sick, twisted, eerie, godless, evil stuff. And I want in.
Homer: Hello, is this *President Clinton*? Good! I figured if anyone knew where to get some tang it would be you.
Bart: (Homer is eating a basket of fruit that has been sent to him) What did you get that for? Homer: For pushing Mr. Burns out of a fourth story window. Bart: Makes sense to me. Lisa: Did he die? Homer: What am I, a doctor?
Homer: If he's so smart, how come he's dead?
Homer: I know parts of our marriage are based on lies, but so are allot of good things, religion, American history...
Ned Flanders: You jumped bail Homer. I got to bring you in. Homer: What have you done with my family? Ned Flanders: I figured a good time to pick you up is when they were at Lisa's recital. Homer: And how did you know I wouldn't be there? Ned Flanders: Lucky guess.
Homer: Argh! It's the rapture! Quick, get the boy out of the house before God comes!
Homer: I couldn't even keep a promise I made to a tree.
Marge: You will not be getting a tattoo for Christmas. Homer: Yeah, if you want one you'll have to pay for it out of your own allowance.
Homer: Help! Fat man hanging from a tree!
Homer: How many grades does this school have?
Marge: Well, everybody's got a fear of something. Homer: Not everybody. Marge: Sock puppets! Homer: (Screams) Where? Where? (Runs off screaming)
Marge: I can't believe one of the most beautiful moments in our marriage is based on lies! Homer: You're just as bad as me, and you used to be better, so that makes you worse!
Mindy: Well, it looks like we'll be getting off together, uh, I mean, going down together, uh, I mean... Homer: That's okay, I'll just press the button for the stimulator, I mean elevator!
Homer: All normal people love meat. If I went to a barbeque and there was no meat, I would say 'You Goober! Where's the meat?.' I'm trying to impress people here Lisa. You don't win friends with salad.
Homer: Poachers are nature's way of keeping the balance. Whenever there are so many species that people get confused, an angry a poacher is born.
Homer: I'm sorry, I thought he was a party robot.
Homer: (After being told Springfield is now officially 'the world's fattest city' and looking directly into the camera) In your face, Milwaukee!
Moe: Ain't you gonna have a beer? Homer: Well, I really shouldn't, what with my massive blood loss and all. Although I do like the occasional beer!
Homer: Sorry doesn't put thumbs on the hand, Marge!
Homer: I don't like the looks of this place Marge. I don't see any standees for chips, standees for soda, I don't see any standees at all. Marge: From now on our family is eating healthy food that looks bad on the shelf but good in our colon.
Homer: Why is that man carrying a purse? Lisa: That's a reusable grocery bag. This store doesn't use plastic bags because they end up in the ocean and upset jellyfish mating rituals. Homer: Stupid horny jellyfish, neutering our dudes...
Homer: (At the dinner table) So, how was everyone's day at school? Bart: Horrifying! Lisa: Pointless! Marge: Exhausting! It took the children forty minutes to locate Canada on the map. Homer: Oh Marge, anyone can miss Canada, all tucked away down there.
Lisa: (Talking about here documentary about her family) I was just trying to accurately portray my unique and quirky home life. Homer: Quirky? Quirky is a grandma who gives people the finger. You made us look like monsters!
Marge: Homer, no! You'll kill us all! Homer: Or die trying...
Homer: Oh, I never wanted to be famous for being mean. I wanted to be famous for catching Santa Clause.
Homer: (Talking about Mr. Burns) He may have all the money in the world, but there's one thing he can't buy! Marge: What's that? Homer: (Pauses) A dinosaur.
Homer: From now on, there are three ways to do things: the right way, the wrong way, and the Max Power way. Lisa: Isn't that just the wrong way? Homer: Yeah, but it's faster.
Homer: What are you two laughing at? And if you say *Jimmy Fallon*, I'll know you're lying!
Homer: Lisa, all you need is a little help from your dad. Lisa: Well, we're supposed to do this without parental help. Homer: Sweetie, that's orphan talk.
Homer: Avenge me, son. Avenge my death.
Homer: Bart's teacher's name is Krabappel? I've been calling her Crandall!
Homer: Now Bart, since you broke Grandpa's teeth, he gets to break yours. Grandpa: This is going to be sweet.
Lisa: Dad, you've been driving in circles for twenty minutes! Why don't you just admit you don't know where the hospital is? Homer: Why don't you admit I know it's around here somewhere?
Lisa: Look at the 'wonders' of the computer age now. Homer: Wonders Lisa? Or blunders? Lisa: I think that was implied by what I said. Homer: Implied... Or implode?
Bart: I don't want to take drugs. Homer: Sure you do. All your favorite stars abuse drugs. *Brett Butler*, *Tim Allen*... Marge: *Tommy Lee*... Homer: *Andy Dick*. Bart: He's just flamboyant. Homer: Yeah, and I'm a size four.
Homer: I understand. Let us celebrate our agreement with the adding of chocolate to milk.
Homer: Listen, you big, stupid space creature. Nobody, but nobody, eats the Simpsons!
Homer: Oh, everything looks bad if you remember it.
Homer: Bart's having girl trouble. You better go talk to him. Marge: It's clown trouble, that's your responsibility. Homer: I thought I was in charge of bed time stories and pets dying. Marge: Yeah, well, we're adding clowns. Homer: Oh, fine, but you just bought yourself ear piercings and strange new feelings. Marge: Fine.
Homer: Oh, I'm in no condition to drive. Wait a minute. I don't have to listen to myself. I'm drunk.
Homer: Your mother seems really upset about something. I better go have a talk with her... during the commercial.
Marge: I'm afraid we're gonna need a bigger house. Homer: No, we won't. I got it all figured out. The baby can have Bart's crib, and Bart can sleep with us until he's 21. Marge: Won't that warp him? Homer: My cousin Frank did it. Marge: You don't have a cousin Frank. Homer: He became Francine back in '76. Then he joined that cult. I think his name is Mother Shabubu now.
Homer: ...and here I am using my own lungs like a sucker.
Homer: I hope I didn't brain my damage.
Homer: It's four a.m. You kids should have been in bed a half hour ago.
Homer: This is the first book I ever finished reading or pushing things into.
Homer: Kids, kids. I'm not going to die. That only happens to bad people. Bart: What about *Abraham Lincoln*? Homer: Uh, he sold poison milk to school children. Marge: Homer!
Marge: Homer, what are you doing? Homer: I'm driving up to the main building. They got valet parking. Marge: We can't drive this up there. They'll see the dent. They'll see the coat hanger antenna. Stop the car, we're walking. Homer: But Marge, valets! Maybe for once, someone will call me 'sir' without adding, 'you're making a scene.'
Homer: Kids, just because I don't care doesn't mean I don't understand...
Bart: Well, those planes are flying where they belong. Homer: That's right. Over the homes of poor people.
Homer: I can't believe we're paying to see something we get on T.V. for free! If you ask me, everybody in this theater is a giant sucker! Especially you!
Homer: I have a tendency to spoil special moments. (A pelican lands on his head and drops a fish into his pants) I'm sorry.
Homer: He didn't give you gay, did he? Did he?
Lisa: Quiet! It's time for the noblest *Nobel Prize* of all, the *Piece Prize*. Homer: I would kill for that...
Homer: (About an Egyptian mummy in the museum) Ooooh, pretty creepy. Still, I'd rather have him chasing me than the *Wolf-Man*.
Homer: I thought you guys didn't party on the Gayflower. Moe: Stop calling it that!
Homer: Hey, where can we get those metal dealies for his feet? Jockey: You mean horseshoes? Homer: Hey, what's with the attitude? I just wanted some dealies.
Homer: I'm so bulgy! Homer: (Homer looks at fish in the water) Mmm... unprocessed fish sticks.
Homer: I didn't raise him to be a quitter. It must have been you. You quit every job you've ever had. Cop, pretzel vendor, church counselor, professional gambler. Marge: He's doing what he thinks is best. Homer: Well, if quitting is the best, maybe I should just quit my job! (Homer walks over to the phone and dials Mr. Burns' number) Mr. Burns: Ahoy-hoy? Homer: Mr. Burns, this is Homer J. Simpson, the father of the big quitter! Well, I just wanted to tell you I'm a big quitter, too! And I quit! (Homer winks twice) Marge: Homer, Mr. Burns can't see you winking. Homer: So... (Screams, hangs up phone)
Homer: Fame was like a drug. But what was even more like a drug were the drugs.
Homer: Books are useless! I only ever read one book, *To Kill A Mockingbird*, and it gave me absolutely no insight on how to kill mockingbirds! Sure it taught me not to judge a man by the color of his skin... but what good does THAT do me?
Homer: When I first heard that Marge was joining the police academy, I thought it would be fun and zany, like that movie *Spaceballs*. But instead it was dark and disturbing. Like that movie, *Police Academy*.
Bart: I think sharing is overrated too. And helping others. And what's all this crap I've been hearing about tolerance? Homer: Your ideas are intriguing and I wish to subscribe to your newsletter.
Homer: (Homer tries to gain passage on an escape rocket) I am the piano genius from the movie *Shine*. Guard: And your name is...? Homer: Uhh... Shiney McShine.
Newspaper Editor: We're looking for a new food critic, someone who doesn't immediately pooh-pooh everything he eats. Homer: Nah, it usually takes a few hours.
Homer: There, there, Bart. If something's hard, then it's not worth doing.
Bart: I've learned that even made-up corporate mascots can lie to you. Homer: Did you hear that Foxie, the *Fox Network* fox?
Marge: I've brought somebody to help you. Homer: Is it *Batman*? Marge: It's a scientist. Homer: *Batman's* a scientist. Marge: It's NOT *Batman*.
Homer: Bad bees! Get away from my sugar! Ow! Ow Oh, they're defending themselves somehow!
Homer: All right, time to fill these slots with coins... specific coins? Oh, this hobby sucks. Homer: Son, all hobbies suck, but if you keep at it, you might find at the end you managed to kill some precious time. Bart: Wow. I never thought of it like that.
Homer: Oh yeah, what are you gonna do? Release the dogs? Or the bees? Or the dogs with bees in their mouth and when they bark, they shoot bees at you?
Homer: (Offering Lisa a donut) Donut? Lisa: Uhh... got any fruit? Homer: This one has purple in it. Purple's a fruit.
Homer: Oh, every thing's too damned expensive these days. This Bible cost 15 bucks! And talk about a preachy book! Everybody's a sinner! ...Except this guy.
Homer: Ahhh... sweet pity. Where would my love life be without it?
Homer: Peh. Science. Has science ever kissed a woman or won the *Super Bowl* or put a man on the moon? Homer: (Shortly afterwards) Help me, science!
Homer: Hey, there's a New Mexico?
Marge: Bart cooked us a five coarse romantic dinner. Homer: You had me at five coarse. You lost me at romantic, then you got me back at dinner.
Homer: There is no better violence then self-inflicted violence.
Marge: Homer did you know there is a family of possums living in here? Homer: I call the big one 'Bitey.'
Ned Flanders: You're going to kill us all! Homer: (Whining) ...but ice cream cake...
Insurer: This place Moe's you were at, just before the accident... this is a business of some kind? Homer's Brain: Don't tell him you were at a bar... but what else is open at night? Homer: It's a pornography store. I was buying pornography. Homer's Brain: He he! I would've never thought of that!
Homer: If there's one thing I've learned, it's that life is one crushing defeat after another until you just wish Flanders was dead.
Homer: What's the point of going out? We're just going to wind up back here, anyway.
Lisa: Dad, what's a *Muppet*? Homer: Well, it's not quite a mop, it's not quite a puppet, but man... (Laughs hysterically) So to answer your question, I don't know.
Homer: Aw, twenty dollars! I wanted a peanut! Homer's Brain: Twenty dollars can buy many peanuts! Homer: Explain how! Homer's Brain: Money can be exchanged for goods and services! Homer: WOO-HOO!
Homer: No, no, no, Lisa. If adults don't like their jobs, they don't go on strike. They just go in every day and do it really half-assed. That's the American way!
TV Announcer #1: Loaftime, the cable network for the unemployed, will be right back with more tips on how to win the lottery right after this. TV Announcer #2: Unemployed? Out of work? Sober? You sat around the house all day, but now it's Duff time. Duff, the beer that makes the days fly by. Duff T.V. Jingle: You can't get enough of the wonderful Duff. Duff Beer! Homer: Beer! Now there's a temporary solution.
Homer: Let the bears pay the bear tax. I pay the Homer tax. Lisa: That's the HOME OWNER tax. Homer: Well anyway, I'm still outraged!
Homer: That's it! You people have stood in my way long enough. I'm going to clown college!
Homer: Hey, now is the time for asking Mr. Burns anything. He is doped up or dying or something.
Homer: ...because that's the kind of guy I am... this week.
Homer: Watch your language moron.
Homer: Which ones Itchy? The car? Bart: The mouse. Homer: Oh, I guess it's not him then.
Marge: I won't have my children sitting alone on a cold dangerous street all night. Homer, you go too. Homer: Ohh... why can't they just take the gun?
Homer: I may be naked and reeking with panda love, but I have my dignity.
Homer: My heart was in the right place, you JERK!
Homer: I'll have to hit him where he lives. Bart: His house? Homer: Bingo.
Homer: Donuts. Is there anything they can't do?
Homer: Mr. Burns, I would like a raise. Mr. Burns: What kind of a raise? Homer: WHOPPING.
Lisa: Dad, where are the back seats? Homer: I had to sell them for gas money.
Lisa: Dad, the bride and the groom should cut the cake. Homer: Oh! that's just superstition.
George HW Bush: I am sorry I spanked your boy. Homer: Ooh! Ooh! in your face, Bush. Now apologize for the tax hike.
Marge: Homer, get ready. You're late for work. Homer: They said if I come in late again, they'll fire me. I cannot take that chance.
Homer: I'm not outta control! You're outta control! The whole freakin' system's outta control! You want the truth? You can't handle the truth! 'Cause when you reach over and stick your hand into a pile of goo that was your best friend's face! You'll know what to do... forget it Marge... it's China Town!
Homer: See Lisa, instead of one big-shot controlling all the media, now there's a thousand freaks Xeroxing their worthless opinions.
Homer: Well, time to go to work. Homer's Brain: Little do they know I'm ducking out early to take the Duff Brewery tour. Homer: Roll in at nine, punch out at five, that's the plan. Homer's Brain: Heh, heh, heh. They don't suspect a thing! (Camera pans down to Homer's mouth, but he doesn't say anything) Well, off to the plant. Homer: Then to the Duff Brewery. Homer's Brain: Uh, oh. Did I say that or just think it? Homer: I've got to think of a lie fast! Marge: Homer, are you going to the Duff Brewery? Homer: Aah! (Runs off)
Homer: Are you saying you're never going to eat any animal again? What about bacon? Lisa: No. Homer: Ham? Lisa: No. Homer: Pork chops? Lisa: Dad, those all come from the same animal. Homer: Heh heh heh. Ooh yeah, right, Lisa. A wonderful, MAGICAL animal...
Homer: If you really want something in this life, you have to work for it. Now quiet, they're about to announce the lottery numbers!
Homer: Marge, it's 3 a.m. Shouldn't you be cooking or something?
Homer: Where is Waldo? Aw! this is will be a lot easy without all these people here.
Marge: Don't we have to wait for Lisa? After all, she is the President. Homer: She knows when the dinner time is.
Homer: You know something Marge? It's not that hard being a film cricket.
Marge: Are you sure this is safe? Homer: Of course not.
Homer: Who wants to help poor people anyway? Nobody.
Homer: I have a 'TO-DO pile?'
Homer: Oh no, I'm sweating like *Roger Ebert*.
Homer: Me Homer. I'm hiding from *PBS*.
Homer: God bless those Pagans.
Homer: I'm sick of these constant bear attacks. It's like a freakin' country bear jambaroo around here!
Homer: There's still the little matter of the whereabouts of your wife. Maude Flanders: Uh, I'm right here. Homer: (Sarcastically) Oh, I see! Then I guess every thing's wrapped up in a neat little package! (Pauses) Homer: Really, I mean that. Sorry if it sounded sarcastic!
Mr. Burns: Why, it's *Fred Flintstone* and his lovely wife *Wilma*. (Maggie crawls in) Oh, and this must be little *Pebbles*. (Walks in) Mind if I come in? I brought chocolates. Homer: Yabba-dabba-doo!
Homer: Chief justice of the supreme court. What great men he would join. John Marshall, Charles Evans Hughes, Warren Berger, mmmm burger.
Otto: My name is Ot-to. I love to get blot-to! Hans Moleman: My name is Hans. Drinking has ruined my life. I'm 31 years old! Homer: My name is Homer and I'm just here because the Court made me come. Rev. Lovejoy: Homer, with our help you'll never touch a beer again. (Homer screams and jumps through the window)
Homer: I'm in a place where I don't know where I am!
Creepy Shop Owner: Take this object, but beware, it carries a terrible curse. Homer: Ooooh, that's bad. Creepy Shop Owner: But, it comes with a free Frogurt! Homer: That's good! Creepy Shop Owner: The Frogurt is also cursed. Homer: That's bad! Creepy Shop Owner: But you get your choice of topping! Homer: That's good! Creepy Shop Owner: The toppings contains Potassium Benzoate. (Homer stares blankly) ...That's bad. Homer: Can I go now?
Homer: Don't mess with the dead, boy, they have eerie powers.
Marge: Homer, don't make me chose between my man and my God, because you just can't win. Homer: There you are. Always taking someone else's side; Flanders, the Water Department, God...
Marge: Homer, you don't have to pray out loud. Homer: But he's way the hell up there!
Homer: Oh my God, we're having a simultaneous pass out!
Homer: Oh boy, dinner time! The perfect break between work and drunk.
Homer: (to Marge) Why don't you support my gibberish? I'd do it if you were stupid.
Marge: It's your new diet. Homer: But I have all those other diets I still haven't finished.
Homer: Oh, c'mon gravity. You used to be cool.
Homer: Marge, I'm watching an rerun of an important bowl game.
Homer: Like my tramp stamp? I got the idea from a show where people regret these.
Homer: *Coke* and *Pepsi* are the same thing! Wake up, people! (Laughs insanely)
Judge: Homer Simpson? You're a repeat offender. Homer: Three-peat. Judge: Bail is set at $25,000. Homer: PFPPFFT! I make that in a year.
Homer: Stop! In the name of a private citizen with no connection to the law.
Homer: (Snake is pointing a gun at Homer) Now let's think about this. If you shoot me I won't be able to stop you and you'll be free to go. But, someone may come after you. Probably not, given your reputation of shooting people who come after you. What I'm trying to say, is not shooting me now would be the biggest mistake of your life.
Warden: So, why do you want to be a guard here? Homer: I believe the children are the future... Unless we stop them now! Warden: Welcome aboard. (Holds a nightstick) This ends for beatin'. This ends for holdin'. Homer: When does training start? Warden: I just finished.
Scully: Homer, we're going to ask you a few simple yes or no questions. Do you understand? Homer: Yes. (Lie detector blows up)
Bart: What are you talking about? Homer: When a woman says nothing's wrong that means every thing's wrong. And when a woman says every thing's wrong that means EVERY THING'S wrong. And when a woman says something's not funny, you better not laugh your ass off!
Marge: This is the worst thing you've ever done. Homer: You say that so often that it lost its meaning.
Homer: Got any of that beer that has candy floating in it? You know, Skittlebrau? Apu: Such a beer does not exist, sir. I think you must have dreamed it. Homer: Oh. Well, then just give me a six-pack and a couple of bags of *Skittles*.
Homer: No Lisa. The only monster here is the gambling monster that has enslaved your mother. I call him Gamblor, and it's time to snatch your mother from his neon claws.
Rev. Lovejoy: Homer, I'd like you to remember Matthew 7:26. 'The foolish man who built his house upon the sand.' Homer: And you remember... Matthew 21:17. Rev. Lovejoy: 'And he left them and went out of the city, into Bethany, and he lodged there?' Homer: Yeah... Think about it.
Homer: Now, son, you don't want to drink beer. That's for daddies and kids with fake IDs.
Homer: Human garbage can to the rescue!
Homer: Get out here boy! I want to punish you before I get drunk and merciful!
Homer: Hey kids, wanna drive through that cactus patch? Bart: Yeah! Lisa: Yeah! Sideshow Bob: (Trailing the Simpsons under the car) No! Homer: Oh, two against one!
Homer: You can't keep blaming yourself. Just blame yourself once, and move on.
Homer: I'm so bored that I have figured out where the wallpaper pattern repeats. See it goes ships wheel, *Popeye* tattoo, *Gilligan* hat, fish with boobs and back to ships wheel. Lisa: What about this swordfish? Homer: Oh my life's work ruined!
Lisa: How did you write a song so fast? Homer: Most of it is plagiarized.
Homer: This movie will haunt me for the rest of my life! Just like *Cannonball Run II*!
Chief Wiggum: ...and once a man is in your home, anything you do to him is nice and legal. Homer: Is that so? Oh, Flanders! Won't you join me in my kitchen? Chief Wiggum: Uh, it doesn't work if you invite him. (Ned enters) Ned Flanders: Hey-dilly hey! Homer: (Sourly) Go home. Ned Flanders: (Unfazed) Too-dilly doo!
God: You know, sometimes I'd rather just sit back and watch football. Does St. Louis still have a team? Homer: No, they moved to Phoenix. God: Oh, yeah.
Homer: The lesson is: Our God is vengeful! O' spiteful one, show me who to smite and they shall be smoten!
Homer: You were gonna start a novel without informing me? Marge: Homer, you left two jobs and bought an ambulance without even a phone call! Homer: I also fed some ducklings. Marge: I know, I got your message.
Homer: It's like something out of that twilighty show about that zone.
Homer: This is one thing he didn't count on: my reckless indifference to human life.
Ned Flanders: You have to promise me something Homer. Homer: Sure, what is it? Ned Flanders: We have to do everything by the book. Homer: And you have to promise no didilies or doodilies. Ned Flanders: My friend, you have a deal-a-rooney. Homer: D'oh!
Homer: (To Ned) You know what your problem is? You haven't become as bad as the people we chase.
Homer: I can see you withholding sex or withholding cake, but withholding sexy cake? I know we have to move past this, but I don't see how.
Homer: How can you write such horrible things about me? Marge: You told me you liked it! You didn't read it at all! You lied to me! Homer: I didn't lie. I was writing fiction with my mouth.
Marge: Homie, I finished my novel... Homer: Wooh, typed. Marge: It's really important that you read it and tell me what you think. Homer: No problem. Awwww... 286 pages! Marge: It's double spaced. Homer: WOO-HOO! I'm half-way through!
Homer: I bet *Einstein* turned himself all sorts of colors before he invented the light bulb.
Carl: Hey, Homer. I'm your secret Santa. Merry Christmas, big guy. (Lenny hands Homer a DVD player) Homer: Oh, my God! A DVD player! Carl: And the first season of *Magnum P.I.*, with commentary by *John Hillerman*. Apparently, working in Hawaii was a pleasure. Homer: Oh, Carl, you remembered I like T.V.
Homer: Dear Lord, please protect this rocket house and all who dwell within the rocket house.
Bart: Wow, dad. You took a baptismal for me. How do you feel? Homer: (Peacefully) Oh, Bartholomew. I feel like *St. Augustine of Hippo* after his conversion by *Ambrose of Milan*. Ned Flanders: Wait, Homer. What did you just say? Homer: (Rudely) I SAID, SHUT YOUR UGLY FACE, FLANDERS! Ned Flanders: Oh, fair enough.
Mr. Sparkle: I am disrespectful to dirt! Can you not see that I am serious? Mr. Sparkle: Join me or die! Can you do any less? Mr. Sparkle: Aka ni taishite burei da. Yogore ni yoberu. Honki da yo. Homer: Why am I Mr. Sparkle?
Homer: Lord, I have to ask you something. What's the meaning of life? God: Oh Homer, I can't tell you that. You'll find out when you die. Homer: But I can't wait that long. God: You can't wait six months? Homer: (Moaning) No, tell me now. God: Well... okay. The meaning of life is...
Homer: Me lose brain? Uh, oh! Ha ha ha! Why I laugh?
Homer: A bear is eating my father! Selma: I'm Selma. Homer: A talking bear is eating my father!
Homer: Okay, don't panic! To find Flanders, you just have to think like Flanders... Homer's Brain: I'm a big four-eyed lame-o and I wear the same stupid shirt everyday and... The Springfield river!
Homer: I saw this in a movie about a bus that had to speed around a city, keeping its speed over fifty and if its speed dropped, it would explode! I think it was called... 'The Bus That Couldn't Slow Down.'
Homer: Remember, as far as anyone knows, we're a nice normal family.
Homer: I'd never thought I'd say this but, stupid Flanders.
Homer: (Answers phone) Y'ello. (Gasps) You want my opinion on current movies? Well, first of all, they're all perfect. Also, when's the *Cap'n Crunch* movie coming out? And will it be 'R' or a 'hard R'?
Homer: How many times do I have to say I'm sorry? Marge: You haven't said you're sorry! Homer: I know, I was hoping the number might be zero.
Homer: All right, let's not panic. I'll make the money by selling one of my livers. I can get by with one.
Lisa: (To Homer) I can't believe you stood mom up! Bart: Face it, Lis, men are dogs. The worse we treat you, the more you want us. Lisa: That's not what dogs do. Bart: (Laughing) You said 'dog doo!' You said 'dog doo!' Homer: (Laughing) She sure did!
Bart: Way to go, dad! Lisa: The perfect kiss! Homer: It was pretty delicious. Marge: It was as satisfying as a million *Hallmark* cards with all the right-size envelopes. (Lisa sighs dreamily) Homer: It felt like a cluster bomb wiping out a graveyard full of zombies. (Bart sighs dreamily)
Homer: Good things don't end in -eum; they end in -mania or -teria
Homer: Marge, don't discourage the boy. Weaseling out of things is important to learn. It's what separates us from the animals! ...Except the weasel.
Marge: Homer, has the weight loss tape reduced your appetite? Homer: Ah, lamentably no. My gastronomic rapacity knows no satiates.
Marge: Homer, it's very easy to criticize... Homer: ...and fun, too!
Homer: I couldn't help it. She knew my one weakness... That I'm weak.
Lisa: No, wait, wait! Bullfighting is a cruel pseudo-sport! Homer: Lisa's right! It's a cool, super sport!
Bart: Dad, how could you put my life in danger to save your own? Homer: You'll understand someday when you have kids!
Homer: Yeah Moe that team sure did suck last night. They just plain sucked! I've seen teams suck before, but they were the suckiest bunch of sucks that ever sucked. Marge: HOMER! Homer: I gotta go Moe my damn wiener kids are listening.
Marge: You shouldn't pressure Bart like that. Homer: If you know of a better way for me to live through my son, then tell me.
Homer: My dad never believed in me. I'm not going to make the same mistake; I'm going to be nicer to my son and meaner to my dad.
Homer: Marge, it takes two to lie. One to lie and one to listen.
Sideshow Bob: Homer, who can you think of who would have reason to kill you? Homer: Well, there's Mr. Burns, Fat Tony, the Emperor of Japan, ex-President *Bush*... Marge: ...the late *Frank Grimes*... Homer: ...*PBS*, *Stephen Hawking*, the angry little *Dixie Chick*... Marge: ...and the state of Florida. Sideshow Bob: How can an ordinary man have so many enemies? Homer: I'm a people person... who drinks. Sideshow Bob: Ahh...
Moe: Gee, this hotrod is souped-up six ways from Sunday. Never had you figured for a gear-head, Homer. Homer: Oh, yeah. I'm a real expert. Moe: (Opens hood) What is that, a six-barrel Holley carb? Homer: You betcha. Moe: Edelbrock intakes? Homer: Nothin' but. Moe: Meyerhoff lifters? Homer: Oh, yeah. Moe: I made that last one up. Homer: I see.
Homer: In this house, we obey the *Laws of Thermodynamics*!
Krusty: Perfect. Cut. Print. Kill the pig. Homer: What... you can't kill him if he's wearing people clothes!
Homer: Everyone knows rock attained perfection in 1974. It's a scientific fact.
Bart: Hey dad, remember how you said if I used a chainsaw unsupervised I'd hurt myself? Well, you were wrong. I hurt someone else.
Homer: Trying is the first step towards failure.
Homer: Girls are easy. Girls love daddy. Girls make birthday cards with glitter on them. Girls can marry a hockey player and get me seats to hockey games. Girls don't steal my knife. ...and I don't have to tell girls how their bodies work 'cause I don't know. Bart: You never told me how my body works. Homer: Point and shoot.
Homer: Oh, writing is hard.
Homer: If you show me where your bathroom is, I'll pretend to wash my hands.
Homer: Don't worry honey, daddy will fix that broken animal.
Homer: You heard me, I won't be in for the rest of the week... I told you! My baby beat me up!... No, it is not the worst excuse I ever thought up.
Homer: You're not the only one that can abuse a non profit organization!
Homer: And Lord, we are especially thankful for nuclear power, the cleanest, safest energy source there is. Except for solar, which is just a pipe dream.
Homer: Hey, if you don't like it, go to Russia!
Homer: Ah, T.V. respects me. It laughs WITH me, NOT at me!
Homer: Are you mad, woman? You never know when an old calendar might come in handy. Sure, it's not 1985 now, but who knows what tomorrow will bring? And these T.V. Guides... so many memories.
Homer: Your mother has this crazy idea that gambling is wrong. Even though they say it's okay in the Bible. Lisa: Really? Where? Homer: Uh... Somewhere in the back.
Homer: Ah, good ol' trustworthy beer. My love for you will never die.
Homer: That's it! Being abusive to your family is one thing, but I will not stand by and watch you feed a hungry dog! Go to your room!
Lisa: Wait a minute, rhinos don't come from eggs. Homer: What did you just see, Lisa? Lisa: But... Homer: What did you just see, Lisa?
Homer: Marge, where's that... metal deely... you use to... dig... food? Marge: You mean, a spoon? Homer: Yeah, yeah!
Homer: 60 cents? I could've made more money if I had gone to work.
Marge: It looks like there's going to be twice as much love in this house. Homer: You mean we're going to start doing it in the morning? Marge: No, were going to have another baby.
Homer: (Drunk) So I says, blue M&M, red M&M, they all wind up the same color in the end.
Homer: You put the beer in the coconut and throw the can away.
Homer: Ok, this is it. I have one last chance to make up for the things I said to my mom. I will avenge you! Lisa: It's not really avenging her dad. It's just the fulfillment of her last wish. Homer: I'm really glad you corrected me Lisa. People are always really glad when there corrected.
Guy: You're not supposed to like it! Homer: Show me the law that says I can't!
Homer: The rain forest? That's that thing Lisa likes.
Homer: Back you robots! Nobody ruins my family vacation but me! ...and maybe the boy.
Homer: If you're going to get mad at me every time I do something stupid, then I guess I'll just have to stop doing stupid things!
Homer: We played *Dungeons & Dragons* for three hours! Then I was slain by an elf.
Homer: Marge, I'm going to miss you so much. And it's not just the sex. It's also the food preparation.
Homer: The information superhighway showed the average person what some nerd thinks about *Star Trek*.
Homer: That's it! If I'm gonna be trapped inside the house I gotta go out and buy some beer.
Homer: ...lousy lovable dog.
Homer: Wow, a baby and a free burger. Could this be the best day of my life?
Homer: How about 'Screw Flanders?'
Homer: Well that's our book for the year. I think we've earned some T.V.
Homer: (Homer walks in on Otto playing loud rock music for Bart in the garage) Will you knock it off?! I can't hear myself think! (They stop playing) Homer's Brain: I want some peanuts. Homer: That's better!
Bart: Gee... Sorry for being born. Homer: I've been waiting for so long to hear that.
Homer: I know what is going on here. They did it to Jesus. Now they are doing it to me. Marge: Are you comparing yourself to our Lord? Homer: Only in bowling ability.
Homer: If God didn't want me to eat in church, he would've made gluttony a sin.
Homer: (Singing) My Bologna has a first name. It's H-O-M-E-R, my bologna has a second name. It's H-O-M-E-R.
Homer: Marge, there's an empty spot I've always had inside me. I tried to fill it with family, religion, community service, but those were dead ends! I think this chair is the answer.
Homer: Hey Flanders, it's no use praying. I already did the same thing, and we can't both win.
Homer: Marge we came to an appointment in the middle of the day, that's the most a parent can do.
Bart: Mom, dad, I'd give a kajillion dollars for you two to get back together. Homer: Make it 2 kajillion. Marge: Homer! Homer: We'll lose the first kajillion to taxes.
Marge: Whatever happened to please and thank you? Homer: I think they killed each other. You know, one of those murder-suicide deals.
Billy Corgan: *Billy Corgan*, *Smashing Pumpkins*. Homer: Homer Simpson, smiling politely.
Lisa: Dad, Bart's a vampire! Homer: Oh Lisa, you and your stories! Bart is a vampire! Beer kills brain cells! Now let's go back to that... building... thingy... where our beds and T.V... is.
Homer: If I could just say a few words... I'd be a better public speaker.
Bart: Why do we have to go to the Rec Center? I want to play with my friends. Homer: When you're older you'll miss these fun activities. Lisa: You're older, how come you don't do these fun activities? Homer: Uhh, 'cause no one's making me.
Homer: No matter how good you are at something, there's always about a million people better than you.
Homer: I'm not a bad guy! I work hard, and I love my kids. So why should I spend half my Sunday hearing about how I'm going to Hell?
Homer: And what if we picked the wrong religion? Every week, we're just making God madder and madder!
Lisa: Why are you dedicating your life to blasphemy? Homer: Don't worry, sweetheart. If I'm wrong, I'll recant on my deathbed.
Homer: Don't let Krusty's death get you down, boy. People die all the time, just like that. Why, you could wake up dead tomorrow! ...Well, good night.
Homer: Kids, let me tell you about another so-called 'wicked guy.' He had long hair and some wild ideas. He didn't always do what other people thought was right. And that man's name was... I forget. But the point is... I forget that, too. Marge, you know what I'm talking about. He used to drive that blue car?
Bart: What religion are you? Homer: You know, the one with all the well-meaning rules that don't work out in real life. Uh... Christianity.
Lisa: *Oedipus* is the one who killed his father and married his mother. Homer: Argh! Who paid for that wedding?
Homer: But Marge, it's uterUS not uterYOU!
Bart: Do you want me to watch and learn? Homer: No, that kind of creeps me out.
Homer: Oh, why do I always read the labels after?
Lisa: There is a big dumb animal I love even more than that horse. Homer: Oh no! What is it? A hippopotamus? Lisa: No, I mean you, you big dummy!
Lisa: I wish for world peace. Homer: Lisa, that was very selfish of you!
Homer: Ooh, a graduate student huh? How come you guys can go to the moon but can't make my shoes smell good?
Homer: Yeah, a raise. I've never been good enough at any job to deserve one before, but I'm damn good at this one. That's it! I'm gonna march right up to Al and say... (Cut to the Bowling Alley) Steve... I mean, Al! I think I deserve a raise.
Homer: The alien has a sweet, heavenly voice. Like Urkel. (*Family Matters*) And he appears every Friday night. Like Urkel. Chief Wiggum: Well, your story is very compelling, Mr. Jackass, I mean, Simpson. So I'll just type it up on my invisible typewriter.
Homer: WHOO-HOO! See that, boy? Your old man was right, not Flanders. We are doomed! In your face, Flanders.
Homer: The strong must protect the sweet.
Homer: Someday T.V. will be invented, and it will be free... Then it will cost money.
Homer: Oh Marge, I'm seeing a brand new side of you... me.
Homer: (Looking at a banner that says: Pardon My Intolerance) That banner has really paid for itself over the years.
Homer: I wanted to apologize for being such a jerk at dinner. And I thought the best way to do that is to come to your house and poke around.
Homer: Boy, don't blow up this mall. It has the cookie store that gives free samples.
Herb: Homer, I want you to design a car. A car for all the Homer Simpsons out there! And I wanna pay you $200,000 a year to do it! Homer: And I wanna let you!
Homer: (Flipping through the Bible) This book doesn't have any answers!
Homer: Maaarge, the dog is hungry. Marge: Well, then, feed him. Homer: Yes, Master. (Mumbles) Do I have to do everything around here?
Homer: The power of dreams has convinced me the threat is real.
Homer: Hi. It seems to me if a gun can protect something as important as a bar, it's good enough to protect my family.
Homer: (Dragging angel) Come on... Come on, angel. (Grunts) Marge: What are you doing with that? Homer: I'm locking it up in my safe-deposit closet with my other valuables. (Opens closet door) I'll just leave it in here a few years and let it appreciate in value. Bart: It's probably a million years old, dad. I think it's as valuable as it's going to get. Homer: (Scoffs) That's what they said about this *Billy Beer*, smarty-pants. (Pops tab and takes a couple of swigs) Ahhhh. We elected the wrong *Carter*.
Lanley: And so, 'mono' means 'one' and 'rail' means 'rail' and that concludes our intensive three week course. Otto: Wait, man! Who gets to be conductor? Lanley: Oh, right. I've looked over your progress with great detail, (Close-up of Lanley's notebook, which shows a stick figure drawing of himself going to Tahiti with the town's money) but I think this man clearly stands out above the rest. (Slowly moves his hand across the screen, which is so vague that it leads everyone to think they got the job) Homer: Who? Me? Lanley: Yeah, Sure.
Homer: Oh no! What have I done? I smashed open my little boy's piggy bank, and for what? A few measly cents, not even enough to buy one beer. Wait a minute, lemme count and make sure... not even close.
Homer: Alcohol, the cause of, and solution to, all of life's problems.
Homer: Marge, I was right! Everybody is whatever I think they are!
Homer: If I wake up tomorrow, we'll discuss it.
Lisa: A little tired of revenge are we? Homer: Yeah, I've done all I can do in that medium.
Ned Flanders: Homer, we have to ration the water carefully. It's our only hope! Homer: Oh, pardon me, Mr. 'Let's ration everything,' but what do you think we're floating on? Don't you know the poem? 'Water, water, everywhere, so let's all have a drink.'
Marge: Do you want your son to become Chief Justice of the Supreme Court, or a sleazy male stripper? Homer: Can't he be both, like the late *Earl Warren*? Marge: *Earl Warren* wasn't a stripper!
Homer: Television! Teacher, mother, secret lover.
Elderly Homer: Which one's the mouse? Elderly Bart: Itchy. Elderly Homer: Itchy's a jerk.
Homer: Homer no function beer well without.
Marge: Homer! Your butt just gave me a brilliant idea! Homer: Yep, it'll do that.
Homer: OOH! Floor pie!
Bart: Okay, I don't want Homer to come on the trip with me, so I'll just ask him and he'll say no. Then, it'll be his fault. Homer: Okay, I don't want to go on the trip with Bart, so if he asks me... I'll just say yes! Homer's Brain: Wait a minute! Are you sure this is how this kind of thing works? Homer: Shut up brain, or I'll stab you with a *Q-Tip*!
Homer: Thanks to your gloomy, depressing music, my children no longer hope for the future I can't afford to give them. Billy Corgan: Yeah, we try to make a difference.
Homer: When will I learn? The answer to life's problems aren't at the bottom of a bottle, they're on T.V.!
Homer: YOU GUYS ARE NUTS! All you can do is eat, sleep, mate, and roll around in your own filth! ...Where do I sign up?
Homer: I'm a white male aged 18 to 49, everyone listens to me, no matter how dumb my suggestions are.
Homer: Son, when you participate in sporting events, it's not whether you win or lose: it's how drunk you get.
Homer: Okay, Gabriel, this is a bar. It's where I go to drink alcohol, which is the mortal equivalent of your ambrosia. Gabriel: Homer, I am not an angel. Homer: Pfft. Well not with that temper. Homer: (Later and drunk) Look, the thing about my family is, there's five of us: Marge, Bart, girl Bart, the one who doesn't talk, and the fat guy. How I loathe him. (Falls off the barstool)
Homer: But remember, we never had this discussion Bart: What discussion? Homer: The one we just had about you doing bad things you stupid kid... Oh...
Lisa: I can't believe those idiot judges were impressed by glowing plastic tubes. Homer: Look Lisa! It glows. Ooooh!
Homer: Howdy, gents, I'm here to collect my free... (Is subdued and handcuffed by Lou and Eddie) Ow! Oh, my boating arm! What's going on? Chief Wiggum: You're under arrest, slime-bag. What's this punk in for, Lou? Lou: 235 unpaid parking tickets, totaling $175. Chief Wiggum: (Snickers) I hope you brought your checkbook, wise guy. Homer: (Annoyed) You lousy cops. Lucky for you, I'm double-parked, or I'd... (Slams pen) There. Now, could I please have my motorboat? Bart: (Later on, in the car) Dad, why aren't you saying anything? Where's our motorboat? Homer: (Avoiding the question) I didn't like it. The mast had termites. Lisa: Why would a motorboat have a mast? Homer: Because! The thing, it was.. Shut up!
Homer: I'm going to the back seat of my car, with the woman I love, and I won't be back for ten minutes!
Homer: (Meeting Aliens) Please don't eat me! I have a wife and kids. Eat them!
Homer: Oh dad, I never new you had dreams or emotions.
Bart: Dad, am I bad on the inside? Homer: Nooo, but the layers of bad on the surface go almost all the way to the center.
Homer: Ooh, I can't get enough of this blood pudding. Bart: The secret ingredient is blood. Homer: Blood? Ugh! I'll just stick to the brain and kidney pie, thank you.
Lisa: Dad! We did something very bad! Homer: Did you wreck the car? Bart: No. Homer: Did you raise the dead? Lisa: Yes! Homer: But the car's okay? Bart and Lisa: Uh-huh. Homer: Alright then!
Homer: What do we need a psychiatrist for? We know our kid is nuts.
Man: Be sure to stick around for the battle of the elementary school bands. Homer: Ohhh. Marge: Homer, Lisa's in that! Homer: I stand by my disappointed groan.
George Harrison: Hello Homer. I'm *George Harrison*. Homer: Oh my God! Oh my God! Oh my God! Where did you get that brownie? George Harrison: Over there, there's a whole pile of them. (Homer runs excitedly to where George pointed) George Harrison: What a nice fella.
Mr. Dondelinger: Alright class, here is your final exam, fifty questions, true or false. Homer: True. Mr. Dondelinger: Homer, that's not a question to the test! Homer: True. Mr. Dondelinger: Homer, just take the test and you'll do fine. Homer: False. Homer: All right brain, you don't like me, and I don't like you, but let's just get me through this, and I can get back to killing you with beer. Homer's Brain: It's a deal!
Homer: Marge, you're as beautiful as *Princess Leia* and as smart as *Yoda*.
Barney: You mean you were one of the original *Little Rascals*? Moe: Yeah. Homer: Which one were you? The ugly one? (Long pause) Were you the ugly one?
Homer: Kids, you tried your best and you failed miserably. The lesson is, never try.
Marge: Now Lisa, you're a vegetarian, but these cows have made a different choice.
Marge: I think it's a very nice idea. Don't you Homer? Homer: Do I have to do anything? Marge: No. Homer: Great. Fine. Go nuts!
Herb: Homer, You're the richest man I know. Homer: I feel the same way about you.
Bart: Is this one of those reality deals where a guy gets a million bucks for marrying Aunt Patty but they have to honeymoon in a box full of snakes? Homer: Son, that's the stupidest idea I ever heard... and I know exactly who would pay top dollar for it! (Picks up phone and dials) Recording: You've reached *FOX*. If you're pitching a show where gold-digging skanks get what's coming to them, press one. If you're pitching a rip-off of another network's reality show, press two. Please stay on the line... your half-baked ideas are all we've got.
Lisa: Everyone likes Whacking Day, but I hate it! Is there something wrong with me? Homer: Yes, honey. Lisa: Then what should I do? Homer: Just squeeze your rage into a bitter, little ball, and release it at an appropriate time! Like that day I hit the referee with the whiskey bottle. (In baby talk) Remember that? Lisa: Yeah... Homer: When daddy hit the referee? Lisa: Yeah... Homer: (Hugs Lisa) Yeah...
Homer: When I look at the smiles on all the children's faces, I just know they're about to jab me with something.
Homer: Animals are crapping in our houses, and we're picking it up. Did we lose a war? That's not America. That's not even Mexico!
Homer: Why does everything I whip leave me?
Grandpa: I'm going to live like a human in a real house! What's the catch? Homer: I'm using you. Grandpa: For what? Homer: My own devices. Grandpa: Alright.
Homer: Look, I'm not asking you to like me, I'm not asking you to put yourself in a position where I can touch your goodies, I'm just asking you to be fair.
Barney: Hey, Homer, you're late for English! Homer: Pffft, English, who needs that? I'm never going to England. Come on, let's go smoke!
Homer: Let's just go to bed, Marge. I'm on the biggest roll of my life.
Homer: (Visiting his high school guidance counselor) Hi, I'm Homer Simpson, I need some guidance, Counselor.
Homer: Quiet you kids. If I hear one more word, Bart doesn't get to watch cartoons, and Lisa doesn't get to go to college.
Marge: Homer, remember you promised you'd try to limit pork to six servings a week? Homer: Marge, I'm only human.
Homer: There's something wrong with that kid. She's so moral. Why can't she be more like... well, not like Bart, but there's got to be a happy medium.
Homer: Bart, pay attention! You might be telling this to your own son someday if something breaks!
Homer: Unlike most of you, I am not a nut.
Homer: Oh, how I miss T.V.! DEAR GOD, JUST GIVE ME ONE CHANNEL!
Homer: Our lives are in the hands of men no smarter than you or I. Many of them incompetent boobs. I know this because I've worked alongside them, gone bowling with them, watched them pass me over for promotions time and again.
Homer: You can't depend on me all your lives. You have to learn that there's a little Homer Simpson in all of us.
Homer: We have a great life here in Alaska, and we're never going back to America again!
Homer: The '80s were an idealistic time. The rise of *Supertramp*, the candidacy of *John Anderson*.
Marge: Homer, the plant called. They said if you don't show up tomorrow don't bother showing up on Monday. Homer: WOO-HOO! Four-day weekend.
Marge: All I'm saying is don't get too comfortable. Mr. Burns will be back tomorrow. Homer: Marge, you're right. We do have to have a party! Marge: Party? No! No parties! Homer: What about 'par-TAYs'? Marge: No 'par-tay's, no shindigs, no keggers, no hootenannies, no mixers, no raves, no box socials! Homer: Damn! (Gets out a card featuring him on a bike saying 'It's a box social!') And I looked so good on that bike...
Homer: I'm normally not a praying man, but if you're up there, please save me *Superman*.
Homer: Son, we all have to do things we don't want to. Like have jobs and families and responsibilities and having to be mister funny all the time. You think I wouldn't rather be nude in the forest like some ancient Pagan just dancing around playing the pan flute?
Homer: (As he is carried away) America rules! Our *Beatles* are much better than your precious *Rolling Stones*!
Marge: You have the right to remain silent. Homer: I choose to waive that right... WAAAAAAAAAAA!
Homer: I feel so empty, so alone, so... couchless.
Homer: Now listen son, I know we saw some awesome beat downs tonight, but remember don't try this at home. Do it at the school yard. Someplace where if you get hurt we can sue. Not just them, the school, the county, the state, and that jack ass *Joe Biden*.
Records Woman: Mr. Simpson, there are thousands of people like you with no discernible talent. Homer: Yeah! They're called 'Congress!'
Marge: (At tea) Hmm, I know what the other eleven forks are for, but what do you do with this one? Homer: (In a posh voice) Why Marge, I believe you're supposed to scratch your ass with it!
Homer: I'm having the best day of my life, and I owe it all to not going to Church!
Homer: (Thinking) I can't let Lisa find out. Time to do what I do best! Lie to a child!
Marge: Homer, I want to show the world how I feel about you! Homer: The world's really not that interested!
Homer: A grizzly bear with a chainsaw... now, there's a killing machine!
Ned Flanders: The Good Lord is telling me to confess to something... Homer: (While his fingers are crossed) Gay gay gay gay...
Homer: The thing that stood between us... the '90s, is almost over. Marge: You're right. But I'm worried about what's on the horizon: reality shows, *Britney Spears*, the suspicious number of home runs being hit... Homer: At least we know there'll never be a President worse than *Bill Clinton*! Imagine, lying in a deposition in a civil lawsuit. That's the worst sin a President could commit! Marge: There'll never be a worse President. Never. Homer: Never.
Homer: Well, excuse me for having enormous flaws that I don't work on!
Homer: I'm sorry of suspecting you of being soulless murderers of innocent children.
Homer: English side ruined. Must use French instructions. (Worried) LE GRILL? What the hell is that?
Homer: Lord, you got a first-class destination resort here, really top notch, but I can't enjoy myself knowing my family is suffering. God: Oh don't you talk about family suffering with me! My son went to Earth once. I don't know what you people did to him, but he hasn't been the same ever since. (Showing Jesus sitting on a swing looking down and spinning really slow) Homer: He'll be fine.
Mr. Burns: Simpson! I want to be loved. Homer: Well, I'll need some beer.
Marge: Allot of people sound like Sideshow Bob, like *Frasier* on *Cheers*. Homer: Or like *Frasier* on *Frasier*. Marge: Or like Lt. Commander Don Dodge on *Down Periscope*.
Homer: Wait, Lord? I have one more favor to ask. God: You want me to help you with your alcoholism. Homer: No, I'm in a good place with that. God: Why don't you just take these pamphlets. (Hands him a few pamphlets) Homer: (Stuffs them in his pocket) Yeah, I'll definitely read those later on.
Homer: (As No. 5) So, who brought us here? No. 6: I don't know. Homer: Did you bring us here? No. 6: No.
Marge: Oh, no! It's the Apocalypse! Bart, are you wearing clean underwear? Bart: Not anymore. Lisa: It's The Rapture, and I never knew true love! Homer: I never used those pizza coupons.
Homer: Are we going to let politics get in the way of our friendship? Ray Patterson: Friendship? You told people I lured children into my Gingerbread House! Homer: Ha ha. Yeah. That was just a lie.
Marge: Thanks for taking the kids on such short notice. Selma: We'll have fun, won't we kids? Bart: To get to Duff Gardens, I'd ride with Satan himself! Selma: That's the spirit! (To Marge and Homer) See you tonight! Lisa: Bye, dad! Don't eat any solids! Homer: But I love solids!
Homer: Lisa, if the Bible has taught us nothing else, and it hasn't, it's that girls should stick to girls sports, such as hot oil wrestling and foxy boxing and such and such.
Homer: Getting out of jury duty is easy. The trick is to say you're prejudiced against all races.
Homer: It's not easy to juggle a pregnant wife and a troubled child, but somehow I managed to fit in eight hours of T.V. a day.
Homer: Lisa, Vampires are make-believe, like elves, gremlins, and Eskimos.
Homer: How dare you expose my children to your tender feelings.
Homer: (Bart must take a penalty shot against Lisa) Oh my God, Marge, a penalty shot with four seconds left! The winner will be showered with praises, and the loser will be taunted and booed until my throat is sore!
Marge: We wouldn't be in this trouble if you'd just paid the heating bill! Homer: I thought global warming would take care of it! *Al Gore* can't do anything right!
Sean: I've never seen anyone win that many rounds of Bingo before. What's your secret? Homer: You have to cheat.
Homer: Video games, the reason this generation of Americans is the best yet.
Bart: A Home and Garden show? Everyone: Ohhhhhh. Bart: Mom, you said we were going to a video game expo. Lisa: You told me we were going to pick up trash by the freeway. Homer: You told me something but I wasn't listening.
God: (Sigh) What do you want, Homer? Homer: Just send me back to Earth and put off this whole rapture hoopdey-doof for another couple of years or so. God: But it's already started. To do what you're asking, I would have to turn back time. Homer: *Superman* did it! God: Fine, Mr. Smarty-Pants. I will undo the Apocalypse.
Bart: You did it, Dad! Homer: (Drunk) You can't prove I did it. Lisa: No, you saved our lives. Homer: I could do a lot of things if I had some money.
Homer: Now, Bart, I made this deal because I thought it would help you get better grades, and you didn't. But why should you pay for my mistakes?
Mark Hamill: Hey, thanks everybody. You know, I'm here as Luke Skywalker, but I'm also here to talk about *Sprint*. As you can see, you stand to save up to 17 cents a month over the more dependable providers... Database: Dahhhh, talk about *Star Wars*! Crowd: YEAH! Homer: You stupid nerds! He's trying to save you money on long distance!
Marge: How could you spend $4.6 million in a month? Homer: They let me sign checks with a stamp, Marge! A stamp!
Homer: Oh, people can come up with statistics to prove anything, Kent. 14% of people know that.
Homer: All right, book, I didn't read you and you didn't read me...
Homer: All right, boy. Time for the ultimate dare. I dare you to skateboard to Krusty Burger... and back... naked. Bart: How naked? Homer: Fourth base. Bart: But girls might see my doodle. Homer: Oh, I see. Then I hereby declare you chicken for life! Every morning, you'll wake up to, Good morning, chicken! At your wedding, I'll sing... bock bock ba-bock (Bart skates off) bock?
Homer: Remember that postcard Grandpa sent us from Florida of that alligator biting that woman's bottom? That's right, we all thought it was hilarious. But, it turns out we were wrong. That alligator was sexually harassing that woman.
Homer: Think about the real victims: *Calvin Klein*, *Gloria Vanderbilt*, and *Antoine Bugleboy*, people who saw an overcrowded market and said, 'Me too!'
Homer: Old people don't need companionship. They need to be isolated and studied so it can be determined what nutrients they have that might be extracted for our personal use.
Homer: How is education supposed to make me feel smarter? Besides, every time I learn something new, it pushes some old stuff out of my brain. Remember when I took that home winemaking course, and I forgot how to drive?
Homer: I've always wondered if there was a god. And now I know there is, and it's me.
Doctor: What you need is a good, long rest. I suggest Florida. Homer: Florida? But that's America's wang! Doctor: They prefer, 'The Sunshine State.'
Homer: Kill my boss? Do I dare live out the American dream?
Homer: To the Simpson-Mobile!
Homer: Don't feel bad boy. Everyone makes mistakes. Yours is just public and expensive.
Homer: How do you say 'taco' in Mexican?
Homer: That's it boy, I'm eating your yogurt! Marge: You ate his yogurt in the car. Homer: He didn't know that.
Homer: If he makes it that's my son.
Homer: Stupid kid, all you do is cost me money. Money I could be wasting.
Homer: That was awesome. I feel like the *Tiger Woods* of sex.
Homer: You never fail to nauseate me boy. Bart: Just call me barf Simpson. Homer: I wanted to but your mother was afraid kids might tease you.
Homer: You know how you wanted me to get that expensive operation? Well now we can afford a motorcycle.
Homer: Oh Marge, if there was a reality show called 'Fat Guys Love Their Wives' I'd be the first one on it.
Lisa: Mom, can Juliet sleep over? Marge: Are you're parents ok with that? They've never met us. Bart: We could be murderers. Homer: Could have been, if we didn't have kids.
Marge: Homer, the plant called. They said if you don't come in tomorrow, don't bother coming in Monday. Homer: Whoo-hoo! Four-day weekend!
Homer: (Sweetly) Oh, Marge. I've never been less angry to receive a book. Marge: (Happy) Awwww.
Homer: See boy, the real money is in bootlegging, not your childish vandalism.
Homer: Where will it be? North Korea, Iran, any thing's possible with Commander Kookoo Bananas in charge!
Homer: We're gonna be rich! We can finally start a family. Marge: We have a family. Homer: A better one!
Homer: We should exchange insurance information. I have none!
Mr. Burns: And this must be... er... Brat. Bart: Bart. Homer: Don't correct the man, Brat.
Homer: I don't mind being called a liar when I'm lying, or about to lie, or just finished lying, BUT NOT WHEN I'M TELLING THE TRUTH!
Gun Shop Owner: Well, you'll probably want the accessory kit. Holster... Homer: Oh, yeah. Gun Shop Owner: Bandoleer. Homer: Baby. Gun Shop Owner: Silencer. Homer: Mmm-hmm. Gun Shop Owner: Loudener. Homer: (Makes a drooling noise) Gun Shop Owner: Speed-cocker. Homer: Ooh, I like the sound of that. Gun Shop Owner: And this is for shooting down police helicopters. Homer: Oh, I don't need anything like that... yet. Just give me my gun! Gun Shop Owner: (Wrestles gun away from Homer) Sorry pal. The law requires a five day waiting period. We've got to do a background check. Homer: Five days? But I'm mad now! I'd kill you if I had my gun! Gun Shop Owner: (Dismissively) Yeah, well, ya don't.
Homer: If something goes wrong at the plant, blame the guy who can't speak English.
Bart: Dad, that's a sports bra. Homer: I don't care, as long as I get the support I need.
Homer: Does this make me look fat? Lisa: No, it makes you look like a tool of government oppression. Homer: But not fat?
Gun Shop Owner: Let's take a look at your background check. It says here you were in a mental hospital... Homer: Yeah. Gun Shop Owner: ...frequent problems with alcohol... Homer: Oh, Ho Ho Heh yeah. Gun Shop Owner: ...beat up President *Bush*. Homer: FORMER president. (The gun shop owner stamps Homer's forms) Potentially dangerous? Gun Shop Owner: Relax. It just limits you to three handguns or less. Homer: WOO-HOO!
Homer: I'm never going to be disabled. I'm sick of being so healthy.
Marge: (To Bart and Lisa) It's the first day of school. Homer: Heh, heh, heh. You're the government's problem now.
Homer: Insurance is the greatest deal ever. If I get hurt I get paid, and man do I get hurt.
Homer: Spread the word: 'Peace and Chicken.'
Homer: Sweet merciful crap! My car!
Homer: Fly the blimp you spoiled kid.
Homer: That is so much better then hospital beer.
Homer: Hey boy, watcha doin'? Bart: Experimenting with my butt. Homer: He he... my little *Einstein*.
Homer: Attention! Christians, Muslims, and Jews, I have come to gather you into a new faith. From now on, you shall be called Chris-Mu-Jews.
Betty White: Homer, you don't have $10,000, do you? Homer: No ma'am. Betty White: And you thought you could just stab your problems away? Homer: Yes ma'am, sorry ma'am.
Homer: I'm sure your wife is dating a lot of people in heaven! Ned Flanders: Are you sure? Homer: Positive, there's a lot of hot people up there. There's *John Wayne*, *Sherlock Holmes*... Ned Flanders: Ah, now Sherlock Holmes is a character. Homer: Oh he sure was! (Does a sexy growl)
Homer: SANCTUARY! SANCTUARY! Rev. Lovejoy: Ugh, why did I teach him that word?
Homer: See Marge? I told you they could deep-fry my shirt. Marge: I didn't say they couldn't, I said you shouldn't.
Homer: Would you look at those idiots? I paid my taxes over a year ago!
Homer: Operator! Give me the number for 911!
Homer: Don't humiliate me in front of my kid.
Homer: The real magic is raising three kids in this economy.
Homer: Lisa don't feel bad. Judas betrayed Jesus but he still got paid.
Homer: Alright buddy, I'm going to do to you what you should have done to my son a long time ago.
Homer: With me at your side our toast will do just what it's supposed too. Steal focus from the bride.
Homer: Marge, your penny-pinching rampage has gone too far! Marge: Oh, honey, I know it's not easy, but we've got to put money away. Homer: You can't enjoy money when you're dead, so why not have fun now? Marge: Don't you think you've had enough 'fun?' Last year you spent $5,000 on doughnuts, $2,000 on scalp massages, $500 on body glitter... Homer: Hey, I earn that money! While you lounge around here doing laundry and putting up drywall, I'm at work busting my hump! Marge: Oh, please! From what I hear, you waltz in there at 10:30, take a nap on the toilet, then sit around 'Googling' your own name until lunch! Homer: (Gasps) Who told you that? Marge: You shouted it while we were making love!
Homer: (After falling on his back) Where's the pain? ...Ouch! There it is...
Homer: (Looking at a bill from the insurance company) This was due two weeks ago. I'm not insured. Uh. For the first time in my life I'm financially responsible for my own actions.
Homer: I'm not in good hands. I'm in no hands. Like a bad neighbor no one is there.
Homer: But Mr. Burns gave me my job, and he hasn't fired me even after three meltdowns and one China Syndrome! I can't betray him!
Homer: Ooh, someone's traveling light! Lisa: Maybe you're just getting stronger. Homer: Heh heh, well I have been eating more!
Homer: A gun is not a weapon, Marge! It's a tool. Like a butcher's knife or a harpoon or... uh, a... an alligator.
Homer: You can't spell 'dishonorable' without 'honorable!'
Homer: Marge, the bathroom scale is lying again.
Bart: Dad, do you realize we put more work into this then all of my school work combined? Homer: If we win this we get a gift certificate. Bart: For what? Homer: Heh heh, it doesn't matter.
Homer: They took away our doughnuts at work. All I've had are my meals.
Homer: Breakfast in bed is so much better then breakfast in a chair.
Homer: Once again sleeping at work has saved my marriage.
Homer: After sex I'm not talking to you. Marge: Then there won't be any sex. Homer: You can't sex fire me, I sex quit.
Homer: I'm sorry, it's just so fun and easy to judge people based on religion.
Homer: You think you've got guts? Try raising my kids!
Homer: But, I'm no super genius!... Or are I?
Homer: A hundred dollars? Marge, how much is that in smackeroos? Marge: One-hundred. Homer: WHOO-HOO!
Bart: Dad, I wanna be a daredevil. Homer: Heh heh... Kids say such stupid things.
Homer: The Internet is on computers now?
Homer: Oh, I can't believe that until I see a fictional T.V. program espousing your point of view.
Homer: Well, now it's time for the best kind of bonding, sitting next to each other in silence, staring blankly at the T.V.
Homer: (Pointing to Bart) That kid has become a Dennis level menace!
Homer: Can't murder now. Eating.
Homer: Why on earth would a child go to the zoo?
Homer: Nothing is ever boobs or ice cream.
Homer: Stupid kid. Fooled by a silhouette.
Homer: Cookies! So delicious! Must buy house...
Homer: Stupid shopping list. Turning food into work...
Weather Presenter: (On T.V.) There's a 75% chance of hilarity! Homer: I like those odds.
Homer: I like my beer cold, my TV loud, and my homosexuals flaming.
Homer: God created the devil? Finally he did something cool.
Homer: Why did I bring the dog and the baby to the poison store?
Homer: Aaaagh! Catholics!
Homer: Oh, I was standing in this line to go to the bathroom but now my license is expired.
Homer: Maggie, you can't climb into the T.V. If you could, I'd make *Alex Trebec* answer some questions...
Judge: Homer Simpson, for causing a panic in the bank you are here by sentenced to one hundred hours of community service. Homer: Community service? But that's work. What about jail. Judge: Community service. Homer: No. I want to go to jail. Free food. Tear drop tattoos. Library books that come to you. I'll serve anything but the community.
Homer: The war is over and the future won. The past never had a chance man.
Homer: No child of mine will go without anything, ever... except quality health care.
Homer: What are you up too? Bart: Reading prayers and ignoring them, just like God.
Homer: Yeah, do you deliver falafels to the top of Mount Zion? Great! I'd like a large falafel with pepperoni, sausage, and extra cheese. Yes, I know what a falafel is...
Homer: You're right. I've been acting like telethon *Jerry Lewis* when I should be acting like rest of the year *Jerry Lewis*. Will you teach me how to put myself first?
Homer: C'mon lady have a heart. I'm sure your husband does stupid things sometimes. Nun: I'm married to Jesus. Homer: Yeah right, and I'm married to *Wonder Woman*.
Homer: (To Maggie) I'll be watching you too in case God is busy making tornadoes or not existing.
Homer: I can't do reefer comedy, I'm drunk. Two different animals.
Homer: (Playing golf) That shot is impossible! *Jack Nicholson* himself couldn't make it!
Moe: There it is! I bought it used from the *Navy*. This thing can flash fry a buffalo in forty seconds. Homer: (Whining) Forty seconds? But I want it now!
Homer: (Looking at a globe map, country being Uruguay) Hee hee! Look at this country! 'You are gay.'
Bart: Hey guys, just so you don't hear any wild rumors, I'm being indicted for fraud in Australia. Homer: Pfft. That's no reason to block the T.V.
Lisa: That's Latin dad, the language of *Plutarche*. Homer: *Mickey Mouse's* dog?
Marge: Homer, have you been licking toads again? Homer: I've not NOT been licking toads. (Licks a toad)
Homer: Their 'can do' will bail out our 'won't try' every time.
Homer: (Finding a bullet lodged in his arm) Let's see, cartilage, cartilage... muscle... NERVE! Artery... BULLET!
Homer: Sir? That's the kind of respect you have to strangle out of an American kid.
Homer: Animals can get sick? Professor Frink: I'm going to talk to the girl from now on. Homer: You're the nerd.
Homer: Pfft flowers, the painted whores of the plant world.
Homer: I never thought of fatherhood as something that could affect a kid.
Homer: Dasher, Dancer... Prancer... Nixon, Comet, Cupid... Donna Dixon.
Homer: Ireland doesn't like pubs anymore. It's as if Danish people stopped liking sleek modern design.
Homer: Moe, something terrible has happened. The Irish have become hard working and sober.
Homer: A thousand dollars? That's what my house is worth.
Lisa: Dad! Our lives! Homer: Fine.
Homer: First good news... two of your kids are not locked in the car.
Homer: Cake, will you do me the honor of making my stomach the happiest bag of acid in the world? You will!?
Homer: ...but I ask you. Who does smoking actually hurt? Except the smokers, those around him, and the unborn children of the pregnant women we let in free on expectant mothers drink free night?
Homer: America is the *New York Yankees* of countries, powerful and respected until the year 2000.
Homer: I'm chained up like a common bicycle.
Marge: You sure know how to please a woman. Homer: As long as it doesn't involve loosing weight, or changing my pants.
Grandpa: Well, at least you never tried to kill me. Homer: Just with indifference.
Homer: Pretty ironic, a cross being used to kill someone...
Homer: If Marge doesn't worry about stuff then that leaves... me! Help me mayonnaise!
Homer: Oh my God. My son is a looser and my daughter's a loner. Way to go Marge.
Homer: Oh no! No bees! Oooh, now who will sting me and walk all over my sandwiches?
Homer: I never dreamed the future could be scary.
Homer: Any part of a cookie you can't eat is just a waist of time.
Bart: Hey Homer, I can't find the safety goggles for the power saw. Homer: If stuff starts flying, just turn your head! Bart: Oh. Check.
Mr. Burns: You will work for me? Homer: I already work for you.
Homer: Word is, protons are the new electrons.
Homer: Oh my God. Like *Mozart* and *Johnny Knoxville* my genius cannot be stopped.
Homer: Oh, why doesn't anything kill me?
Homer: Oh, Ned. I never dreamed under those iddilies and diddilies there was a dude.
Homer: I booked us a room at a very romantic hotel. Marge: Garden view? Homer: Ocean view... obstructed. Marge: Ohhhh...
Homer: Why is this happening to me? Dr. Hibert: Well I do have an idea, but just to be sure, let's run some expensive tests.
Marge: Why can't our son just behave? Homer: Well Marge, you did have that one sip of alcohol while you were pregnant.
Homer: Bart, with $10,000 we'd be millionaires! We could buy all kinds of useful things like... love!
Homer: I finally killed you sisters. I'm the happiest magic guy in pretend land.
Homer: Hey, white chocolate's not even chocolate. It doesn't even contain cocoa solids.
Homer: This chocolate needs more chocolate.
Homer: Chocolate isn't supposed to hop.
Homer: What? Dammit, I was dreaming! Why is life so unfair? All I want is the ability to eat everything in sight and turn into a giant ball! Is that too much to ask? Damn you reality!
Homer: Hey, you're like that rabbit thing from that book about a girl named *Alice* who goes to *Wonderland*. What was it called? Oh yeah, *Snow White* in stupid town.
Homer: Mmmmm... white chocolate.
Bart: Bad influence, my ass! How many times have I told you? Never listen to your mother!
Bart: Joe's Taxidermy. You snuff 'em, we stuff 'em.'
Bart: Hey, I never refuse food from strangers.
Bart: Dad, do you have to hang out at my school? It's bad enough I have to be here three days a week.
Bart: After trying four times to explain it to Homer, I explained it to mom and we were on our way!
Bart: Hey, cool, I'm dead.
Bart: So this is setting the table. If I'd known how easy this was I would have just done it instead of throwing all those tantrums.
Bart: Dad, you must really love us to sink so low.
Marge: Alright, children. Let me have those letters and I'll send them to Santa's workshop in the North Pole. Bart: Oh please, there's only one fat guy that brings us presents and his name ain't Santa.
Bart: You were like a brother to me. We were going to take wood shop together and make nunchucks. And then take people to our lockers and then show them our nunchucks.
Bart: Seymour, I'll bet you a steak dinner those books are still here. All we have to do is search every locker. Principal Skinner: Oh, Bart, I'm not sure random locker searches are permitted by the Supreme Court. Bart: Pfffffft. Supreme Court. What have they done for us lately? Principal Skinner: Let's move.
Bart: Homer, I'll bet when you were ten, you were stealing beers, kissing girls, and tipping dinosaurs.
Bart: Okay, but don't let our hands touch. It's gay. Rod: What does gay mean? Bart: Well, it means you used to be afraid, but now you're not. Rod: (To his father) I'm gay, daddy! I'm gay! Mrs. Simpson made me gay! (Ned glares at Marge) Marge: Ummm... I'm pretty sure he's saying 'I'm okay.'
Bart: Dad, why'd you bring me to a gay steel mill?
Bart: Poor Krusty, he's become the lowest form of life... a sidekick.
Bart: Why are great things always ruined by women? The Army. The *Fantastic Four*. Think how awesome *American Idol* would be with just *Simon* and *Randy*. Homer: Hehehe... Oh Bart, you say that now, but when you're grown up you'll just think it.
Bart: Now let's put it on the shelf and never look at it again.
Lisa: Ahh, you just ruined six months work. Bart: I'm sorry it wasn't a year. Lisa: Ohh, you're going to regret the day you were born. Bart: I already do. It's too close to Christmas.
Bart: You're Krusty the Clown. One of Look Magazine's 100 most promising clowns of 1958. Krusty: Lot of suicides in that group. Funny suicides. Hehe, but still...
Bart: Sorry, I'm late. I didn't realize you had to turn the oven on to bake stuff.
Mr. Burns: Hello, young fellow. I haven't forgotten you. Here. Bart: Wow, a crowbar! Lisa: It's to open the crate, stupid.
Bart: He even took my stamp collection! Lisa: You have a stamp collection? (The family starts laughing, The phone rings and Bart answers) Nelson: (Over phone) Stamp collection? Ha-ha!
Lisa: I knew someday mom would violently rise up and cast away the shackles of our male oppressors. Bart: Ah, shut your yap.
Bart: (Walking on pogo stilts) Hey, Lis, check it out: pogo stilts. These were banned in all 50 states. (One pogo springs into the air and hits something) Homer: (Off screen) Ow! Ohh! What happened?
Lisa: We've made a terrible mistake! This tunnel comes out in the worst possible place! Bart: An elephants butt?
Marge: Whaddya say, it'll be B.L.A.M. Bart, Lisa, And Mom, huh? Bart: Mom, when I want lame and nerdy, I'll call Milhouse... No offense.
Bart: I'm not calling you a liar but... I can't think of a way to finish that sentence.
Bart: AAH! You ate my homework?... I didn't know dogs really did that.
Bart: Cross you heart, hope to die. Stick a needle in your eye. Jam a dagger in your thigh. Eat a horse manure pie!
Bart: Good-bye, Japan! I'll miss your *Kentucky Fried Chicken* and your sparkling, whale-free seas.
Bart: What a day, eh Milhouse? The sun is out, birds are singing, bees are trying to have sex with them... as is my understanding.
Bart: Dad, thanks to television, I can't remember what happened eight minutes ago... No, really, I can't! It's a serious problem... What are we all laughing about?
Bart: Mom, can we go Catholic so we can get communion wafers and booze?
Bart: We should be safe from Milhouse here. Being at sea level always gives him nose bleeds.
Bart: Ha ha! He's such a bitch!
Bart: I don't need a brother, and no dream will convince me I do.
Marge: A branch must have knocked out a power lines. Bart: Fine, I'll see what's on T.V. Marge: That runs on electricity also. Bart: Alright, I'll watch a *DVD*. There's no way that runs on electricity. Marge: Mmmmm... Bart: Really? Does *Obama* know about this?
Bart: I wash myself with a rag on a stick.
Bart: What's wrong, mom? Thinking about your marriage?
Homer: Homer do good? Bart: Actually, you've doomed us all. Again.
Bart: Listen here Cringle. I may have been naughty this year, but by today's standards, naughty's nothing. I didn't get anybody pregnant. I didn't *Facebook* a kid to death. Make with my dirt bike.
Lisa: Our Father, who art in Heaven... Bart: Lisa, this is neither the time, nor the place!
Marge: (Looking out the window) There's something about flying a kite at night that is so unwholesome. Bart: (Creepily) Hello, mother dear...
Lisa: Bart, *Pablo Neruda* says 'Laughter is the language of the soul.' Bart: I am familiar with the works of *Pablo Neruda*.
Bart: I never thought it was humanly possible, but this both sucks AND blows.
Bart: War is neither glamorous nor fun. There are no winners, only losers. There are no good wars, with the following exceptions: The *American Revolution*, *World War II*, and the *Star Wars Trilogy*.
Bart: (Singing) You don't win friends with salad! You don't win friends with salad!
Lisa: I don't even know if I should go. I don't even like him! Bart: You're right, Lis. You shouldn't go. It wouldn't be honest! I'll go, disguised as you! Lisa: But what if he wants to hold hands? Bart: I'm prepared to make that sacrifice! Lisa: What if he wants a kiss? Bart: I'm prepared to make that sacrifice! Lisa: What if he... Bart: You don't wanna know how far I'll go!
Homer: Are we gonna die, son? Bart: Yeah, but at least we're going to take a lot of innocent people with us.
Bart: It's craptacular.
Bart: (To Homer) Hit the road you big load.
Lisa: Oh Bart, I am so glad everything is O.K. Bart: Well not everything, apparently somebody switched your face with a butt. Ha ha ha...
Bart: So, Grandpa, not that I'm anxious to go but, I've been here ten minutes, which is like seven hours in kid's years.
Homer: Boy, you don't have to follow in my footsteps. Bart: Don't worry, I don't even like using the bathroom after you. Homer: WHY, YOU LITTLE-!
Bart: Wow, my father an astronaut. I feel so full of... what's the opposite of shame? Marge: Pride? Bart: No, not that far from shame. Homer: Less shame? Bart: Yeaaaaah...
Bart: Well, I'm flunking math, and the other day I was a little attracted to Milhouse.
Brad Goodman: Young man, what made you yell out that remark? Bart: I dunno. Brad Goodman: You just wanted to... express yourself, yes? Bart: I do what I feel like. Brad Goodman: Why, that's marvelous! 'I do what I feel like.' Ladies and gentlemen... this little boy here is the inner child that I've been talking about. Lisa: (Shocked) What?
Bart: Awwwe man!
Lisa: Congratulations, you're officially a sociopath. Bart: Hey, at least I'm on a path.
Bart: Who knew a troubled person could be creative.
Lisa: Everything I know tells me this story doesn't end with you sitting here telling it to us! Bart: Get off the edge of your seat. They got married, had kids and bought a cheap T.V.!
Homer: You went to a sugar factory? Were there *Oompa-Loompas*? Bart: There was one in a cage. But he wasn't moving.
Bart: I think I read somewhere that cows like being killed.
Tractor: Come on Bart, ride me... Bart: Uh... I better not. Tractor: (Imitating chicken) Imaginary Chicken: He's insulting the both of us. Bart: Let's go!
Bart: Try not to move dad, you swallowed allot of motor oil.
Bart: I'm glad we're stranded. It'll be just like the *Swiss Family Robinson*, only with more cursing! We're gonna live like kings. Damn hell ass kings.
Bart: You're damned if you do and you're damned if you don't.
Bart: You could just rent it until the market recovers. Which will be never.
Bart: Dad, you must really love us to sink so low.
Marge: Bart, are you drinking whiskey? Bart: I'm troubled.
Bart: Wait a minute, this ain't no genius copter, this is *Con-Air*.
Bart: Two kinds of Irish people? What are they fighting over? Who gets to sleep in the bathtub?
Marge: That laughter sounds like the result of misbehavior. Bart! How did you get a cell phone? Bart: The same way you got me, by accident on a golf course.
Bart: (Over the radio) Rod! Todd! This is God! Rod: How did you get on the radio? Bart: Whaddya mean, how did I get on the radio? I created the universe! Stupid kid! (Rod and Tod fall to their knees and clasp their hands) Todd: Forgive my brother. We believe you. Bart: Talk is cheap. Perhaps a test of thy faith. Walk through the wall! I will remove it for you... (Rod gets up and obediently walks into the wall and smacks his head into it) Bart: ...later! (Laughs) Todd: What do you want from us? Bart: I got a job for you. Bring forth all the cookies from your kitchen and leave them on the Simpsons' porch. Rod: But those cookies belong to our parents. Bart: Ugh! Look, do you want a happy God or a vengeful God? Todd: (Quickly) Happy God! Bart: Then quit flapping your lips and make with the cookies! Rod and Todd: Yes, sir!
Homer: We're proud of you, boy! Bart: Thanks, dad. But part of this 'D-' belongs to God!
Marge: Alright, children. Let me have those letters and I'll send them to Santa's workshop in the North Pole. Bart: Oh please, there's only one fat guy that brings us presents and his name ain't Santa.
Bart: Ah, the system works. Just ask *Klaus Von Bulow*.
Bart: Just what in my long sad history of frogs makes you think I can take care of a bird?
Bart: I just have one question, is curling a real thing? Lisa: Yeah, or is it a cover up for a grown up thing we're not supposed to know about. Bart: Like the time you said dad was taking a weekend leadership seminar, when he was really stuck in a barrel at the junk yard.
Bart: Dear God, we paid for all this stuff ourselves, so thanks for nothing.
Bart: Joe's Crematorium. You kill em, we grill em.
Bart: Oh, what idiot put the dump so far away from where people live?
Bart: Kids don't deliver newspapers anymore, it's just creeps in trucks.
Bart: How can someone so much like me be a loser?
Bart: (To Homer) You work hard, or at least you're out of the house a lot.
Bart: Mom, what would you do if someone you cared about might be a loser but they thought they were awesome? Marge: Are you talking about your father? Bart: That loser? No. I'm talking about this guy who's nineteen and never really grew up.
Bart: Dad, Lisa making me see things from both sides again. Homer: Lisa, I warned you about that. Lisa: Shouldn't Bart have all the information he needs to make an informed decision? Homer: Uh... you... Now you're doing it to me! Ohh...
Bart: As much as I hate that man right now, you gotta love that suit.
Bart: I've been scorched by Krusty before. I got a rapid heartbeat from his Krusty brand vitamins, my Krusty calculator didn't have a seven or an eight, and Krusty's autobiography was self-serving with many glaring omissions. But this time, he's gone too far!
Bart: Cleaning graffiti off a statue makes a mockery of everything I stand for.
Bart: My killing teacher says I'm a natural.
Bart: Hey, quit sayin' bad stuff about my town, man! Shelby: Why don't you make me? Bart: I don't make trash, I burn it. Shelby: Then I guess you're a garbage man. Bart: I know you are, but what am I? Shelby: A garbage man. Bart: I know you are, but what am I? Shelby: A garbage man. Bart: I know you are, but what am I? Shelby: A garbage man. Bart: Takes one to know one!
Bart: No problemo!
Bart: Blond guys aren't dumb, their evil. Like in the *Karate Kid* and World War II.
Marge: You stay here. Bart: Oh, I hate being stuck at home. Marge: Play with Lisa. Bart: You don't play with Lisa you play to spite her.
Bart: Are you sure this will work? Milhouse: Hey, this is the *DVD* my parents used to make me. Bart: So... it kinda works.
Bart: Where do you want it? Mouth or the eyes? Homer: OOH, mouth. Bart: Eyes it is!
Bart: (Drunk) I miss Flanders. There... I said it!
Bart: Did someone order a happy ending?
Bart: Ya'know, I used to think you were stuck in an emasculating, go-nowhere job. Homer: Heh, heh... kids. Bart: But now, I want to follow in your footsteps. Homer: (Excited) Do you want to change your name to Homer Junior? The kids can call you Ho-Ju! Bart: ...I'll get back to you.
Bart: So, you're one of those don't call me a chick, chicks eh?
Bart: Why would anybody wanna touch a girls butt? That's where cooties come from!
Bart: (Talking to Homer) It's just so hard not to listen to T.V., it's spent so much more time raising us than you have.
Bart: I'm only ten and I already have two mortal enemies.
Bart: They'll never believe a Simpson killed a Flanders by accident.
Bart: Looks like I have the house to myself for a while. I can do anything I want. First I'm going to take a bath, then I'm going to eat some vegetables, then I'm going to get to bed nice and early without T.V.
Bart: Why the crap do we have to go to church anyway?
Bart: Stupid angry mob! Chasing me because I shine a harsh light on modern society. Oh, now I know how *Dane Cook* feels.
Marge: Bart, how many hours a day do you watch T.V.? Bart: Six. Seven if there's something good on.
Bart: Must fight Satan, make it up to him... later.
Bart: You're turning me into a criminal when all I wanna be is a petty thug.
Bart: Jeeze, pick up a book.
Bart: Whoa, you don't look like a mom, you look happy.
Bart: Hey, its got to be good if Satan put his name on it...
Bart: I know everything about addiction you can learn from watching dad.
Bart: Babies? We go one of those... overrated.
Bart: This town can't teach its kids or collect its garbage, but we lead the nation in pointless revenge.
Bart: Hey man, don't have a cow.
Bart: You don't say 'kill' you say 'prank.' Like mom and dad say 'snuggle' when they really mean is 'let's lock the door and hug.'
Bart: All these years I've been petting lambs when I should have been shoving them in my mouth.
Bart: (While being interviewed live by Kent Brockman) I just want everyone to know that this was a really crappy camp. Can I say 'crappy' on TV? Kent Brockman: Yes, on this network, you can.
Bart: Eat my shorts.
Bart: If fairy tales have taught us anything is that first wives are perfect, second wives are horrible. Homer: Just the opposite of real life.
Bart: (To Homer) I would rather take my chances in a hot car then go into the store with you.
Bart: I think I just met the thing I'm going to die on.
Bart: We're Simpsons dad. We're not capable of good behavior.
Bart: C'mon toilet. If you can handle dad you can handle this.
Bart: Look at me, I'm Otto! I'm 100 years old and I drive a school bus! (Drives very crazy)
Bart: So I can get a dollar for every ball I find? And if a cell phone costs $100 how many balls do I need? Dr. Hibbert: This is why my kids go to private school.
Bart: Utah? Home of America's most powerful weirdoes!
Bart: I'll be Gus, the lovable chimney sweep. Clean as a whistle, sharp as a thistle. Best in all *West Minster*! Yeah!
Bart: Joke if you will, but did you know most people use 10% of their brains?... I am now one of them.
Bart: Memo to self: Shut up, Lisa.
Bart: Teachers should not be allowed to live by their students. We're natural enemies like *George Washington* and *Abraham Lincoln*.
Bart: Nothing beats a weapon made of weapons.
Bart: I'm a Simpson. And a Simpson never gives up until he has tried at least one easy thing.
Bart: Beef jerky? The queen of all the jerkies.
Bart: I can do that, but I don't wanna.
Bart: You don't fight like a girl or even a Milhouse.
Bart: Cost of paper, five cents. A mother's love, priceless.
Bart: (Mockingly at Lisa) Ha Ha. They left without you. Lisa: They left without you too, you idiot. Bart: If I'm such an idiot, how come I'm the smartest kid in third grade? Lisa: Because you've already done it once. (Pause) Bart: You've lost me.
Lisa: (In jail) Thanks a lot, everybody. Now, I'll never get into an Ivy League school. Bart: (Taunting) You're going to *Stanford*, you're going to *Stanford*... (Homer joins in) Homer and Bart: You're going to *Stanford*! You're going to *Stanford*! Lisa: Take it back! Take it back! Homer: Oh... okay... *STANFORD*!
Bart: You're probably wondering about the coat hangers. They're to block the satellite that's been spying on me.
Bart: Sure, I can do something destructive.
Marge: But, you wanted those toys. Bart: I wanted them 'til I got them.
Bart: We're not losers. Lisa: No you two are winners, big winners. When I grow up I want to marry a big winner like you guys.
Bart: Come on, people, this poetry isn't going to appreciate itself.
Bart: A log cabin? What am I, *Davy Crockett*? Also, who's *Davy Crockett*?
Lisa: Bart you can't just run away from this. Bart: You're right, I can bike away much faster and ring the bell to drowned out bad thoughts.
Sherri: Hey, Bart. Our dad says your dad is incompetent. Bart: What does 'incompetent' mean? Terri: It means he spends more time yakking and scarfing down donuts than doing his job. Bart: Oh, okay. I thought you were putting him down.
Bart: What did those women expect? When you sign a contract with *FOX*, you know you're gonna be betrayed and humiliated!
Bart: *George Burns* was right. Show business is a hideous bitch goddess. Lisa: Cheer up, Bart. Milhouse is still going to need a true friend, someone to tell him he's great. Someone to rub lotion on him. Someone he can hurl whiskey bottles at when he's feeling low. Bart: You're right, Lis! I can suck up to him! Like the religious people suck up to God!
Bart: Eh, making teenagers depressed is like shooting fish in a barrel.
Bart: Can I go mom? Can I? Marge: Is you're room clean? Bart: No. Marge: Good, that will give me something to do while you're at the game.
Bart: That's the last time I get you guys a Christmas gift at the last minute.
Bart: Who needs a knife this big? Marge: It's probably a de-boner. Bart: Ha ha, boner.
Bart: Wait in line for a book? You tell 'em Bart says 'Hey.' Homer: C'mon boy, all the nerds are doing it. Bart: I'm not a nerd. I'm a jock who is too cool for sports.
Bart: I didn't do it, no one saw me do it, there's no way you can prove anything!
Bart: How come you don't get mad when I torment real animals. Lisa: I do! It enrages me.
Milhouse: (About to jump in the water) I don't want to live in the world without Bart! Marge: (Gasps) Can he swim? Bart: What do you think?
Smithers: What time is it? Bart: Twelve eighty. No wait. What comes after twelve? Smithers: One. Bart: No, after twelve.
Bart: (Talking on the phone with the Australian father) Hey, I think I hear a dingo eating your baby.
Bart: Christmas is a time when people of all religions come together to worship Jesus Christ.
Bart: I've said it before, and I'll say it again... aye carumba!
Bart: I thought you Hindus we're supposed to love everybody. Lisa: I'm a freakin' Buddhist.
Bart: Hey, the only thing I bring home are notes to my parents, and those do not arrive the way they left.
Bart: Who's the black private dick that's a sex machine with all the chicks?
Bart: Martin was like Jesus, only real.
Bart: What'cha doing mom? Going crazy?
Todd: Hi Bart! Bart: Get bent!
Bart: Krusty owes me one for perjuring myself during a deposition.
Bart: (Answering the front door) Principle Skinner? This is bogus man. You know the rules, two letters and a conference before I get a home visit.
Lisa: Mom, Bart's drinking coffee. Bart: It's not coffee it's hot *Pepsi*.
Bart: Why are we getting dressed up, mom? Are we going to *Black Angus*? Marge: Well, you might say we're going to the best steakhouse in the whole universe. Bart: So we're NOT going to *Black Angus*?
Bart: There's no such thing as a soul. It's just something they made up to scare kids, like the boogeyman or *Michael Jackson*.
Bart: Inside every hardened criminal beats the heart of a ten-year-old boy.
Bart: Have you noticed that dad gets the disease they talk about in the in flight magazine?
Bart: You know, I've done a lot of bad stuff through the years. I guess now I'm paying the price. But there's so many things I'll never get a chance to do: smoke a cigarette, use a fake ID, shave a swear word in my hair.
Lisa: I think it's ironic that dad saved the day while a slimmer man would have fallen to his doom. Bart: And I think it's ironic that for once dad's butt prevented the release of toxic gas... Marge: Bart!
Bart: I am through with working. Working is for chumps. Homer: Son, I'm proud of you! I was twice your age when I figured that out.
Bart: Why would anyone want to hurt me? I'm this century's *Dennis the Menace*!
Bart: 'Don't do what Donny Don't does.' They could have made this clearer.
Bart: You know who else was really into row boats? Jesus, and he could have turned his row boat into a *Jet-Ski* but he didn't.
Bart: Aren't we forgetting the true meaning of Christmas? You know, the birth of Santa.
Bart: After trying four times to explain it to Homer, I explained it to mom and we were on our way!
Bart: Her only hope was a plucky young boy and his slow-witted father.
Patty: You see, Aunt Selma has this crazy obsession with not dying alone. So, in desperation, she joined this prison pen-pal program. Her new sweetie's a jailbird. Bart: Cool! He can teach us how to kill a man with a lunch tray.
Bart: What's Santa's Little Helper doing to that dog? Looks like he's trying to jump over, but he can't quite make it.
Bart: I can't stand to see you so upset, Lis, unless it's from a rubber spider down your dress. Hmm, that gives me an idea. Note for later: Put rubber spider down Lisa's dress.
Bart: I don't know! I don't know why I did it, I don't know why I enjoyed it, and I don't know why I'll do it again!
Bart: What if you're a really good person, but you get into a really, really bad fight and your leg gets gangrene and it has to be amputated. Will it be waiting for you in heaven?
Bart: Remember, you can always find East by staring directly at the sun.
Dave Shutton: What's your name, son? Bart: I'm Bart Simpson, who the hell are you? Dave Shutton: I'm Dave Shutton. I'm an investigative reporter who's on the road a lot, and I must say that in my day, we didn't talk that way to our elders. Bart: Well, this is my day, and we do sir.
Homer: I don't have the discipline necessary to be a hippie. Bart: You'd be a great hippie, dad. You're lazy and self-righteous!
Lisa: (Wakes up Bart) Bart: Lisa! It's 6 a.m.! Something's wrong. dad died! Lisa: No no, he's fine! Bart: Well, whaddya know, I'm relieved.
Lisa: A rose by any other name smells as sweet. Bart: Not if you call them 'Stench Blossoms.' Homer: Or 'Crapweeds.' Marge: I'd sure hate to get a dozen 'Crapweeds' for Valentine's Day. I'd rather have candy. Homer: Not if they were called 'Scumdrops.'
Bart: (To Milhouse) How can someone with glasses so thick be so stupid?
Bart: Teenagers are so dumb.
Bart: The sun never sets on the Bart-ish empire.
Bart: Great, now I got nothin' to play except the games I bought yesterday and I'm totally sick of them.
Bart: Mmmm... this is so weird. The only Simpsons game I can think of is the one where we all pretend dad isn't an alcoholic.
Bart: What are you worried about? You have video game powers on your side. It's like cheating, but cheating. Homer: WOO-HOO cheating!
Marge: Mrs. Van Houten? I'm Bart's mother. We met in the emergency room when the boys drank paint. Mrs. Van Houten: I remember.
Marge: Homer, I told you this morning, no guns at the dinner table! Homer: You said the breakfast table. Marge: It's the same table!
Marge: How are you enjoying your ham, Homey? Homer: Tastes so bitter, it's like ashes in my mouth... Marge: Hmmm. It's actually more of a honey glaze.
Marge: I told you kids you were going to send your father to the crazy house! Bart: No, mom, you said poor house. Marge: I SAID CRAZY HOUSE!
Bart: Hey, mom! dad's in a mental institution! Marge: Oh, my God... mother was right!
Bart: I miss you, dad. Mom won't let me read *Hagar the Horrible*. Marge: I just don't think it's funny.
Marge: Well, it could be a good chance to get to know our neighbors outside of a courtroom setting.
Marge: Don't let it get you down. So Mr. Burns doesn't take you seriously. Big woop. Who gives a doodle, whoopie ding-dong-doo! Homer: Thanks for trying, but I'll be at Moe's. Marge: So my husband goes to a bar every night. Whoop dee doo. Who gives a bibble. Gabba-gabba hey.
Homer: But it's St. Valentines Day! God wants us to do it. Marge: You're so cute when you're begging for sex. But I'm just too tired.
Marge: I guess one person can make a difference. But most of the time, they probably shouldn't.
Marge: Only your father could take a part-time job at a small town paper and wind up the target of international assassins.
Marge: That was very sweet of the Queen, letting you go in exchange for taking *Madonna* back to America. Madonna: I'm telling you! I'm English! Marge: English women don't pump gas naked!
Marge: I didn't sacrifice my period for second place!
Marge: Five more water heaters and we get a free water heater.
Marge: This house is full of surprises, but this is the first good one.
Marge: Oh, pumps are shoes. That explains allot.
Marge: I just made a 3,700 mile car trip. I need to wash up.
Marge: Now, let's take you to a place where a black man can blend in... Canada.
Marge: Oh Bart, I don't care that this is just an act, you've finally become the boy every mother dreams of, a girl.
Marge: My son's a good for something.
Marge: There, there, Homer. You've caused plenty of industrial accidents and you've always bounced back.
Homer: I KILLED MR. BURNS! I got mad and punched him right in his 104 year old face! Marge: Okay... maybe every thing's alright. Maybe if you go apologize to him, he won't even fire you... if he's alive.
Marge: Long-time reader, first time stander-upper!
Marge: It's very open minded of you to have Bart's Muslim friend's Muslim family over.
Marge: You couldn't predict 6:00 at 5:30!
Marge: Bart you've always been a handful, but you've never interfered with my reproductive freedom. Why now?
Marge: Homer, what's going on? The violin, pants with a crease, why? Homer: Marge, you deserve a wedding day that, unlike our children, was planned in advance.
Marge: History's like an amusement park. Except, instead of rides, you have dates to memorize.
Marge: If someone did eat Bart's shorts, they would have a stomach full of pocket garbage!
Marge: Homey, let's pick up those hitch hikers. They don't look like the stabby kind. Lisa: Mom, you said all hitch hikers were all drug crazed thrill seekers. Marge: I said they were thrill crazed drug seekers. Don't put words in my mouth.
Homer: Lord help me, I'm just not that bright. Marge: Oh, Homer, don't say that. The way I see it, if you raise three children who can knock out and hogtie a perfect stranger, you must be doing something right.
Bart: What is that? A quarter? Milhouse: A *Chuck-E-Cheese* token? Marge: No! It's a *Sacagawea* dollar! You can trade it in at the bank for a regular dollar! Huh? Huh?
Homer: In your face, space coyote! Marge: (Confused) Space coyote?
Marge: That Shary Bobbins is a miracle worker. The kids love her, the house is spotless, and my hair's grown back. It's so full and thick it can support a beach umbrella!
Marge: Well most women will tell you that you're a fool to think you can change a man, but those women are quitters! Lisa: What? Marge: When I first met your father, he was loud, crude, and piggish. But I worked hard on him, and now he's a whole new person. Lisa: Mom? Marge: He's a changed man, Lisa! Lisa: Oh, right...
Marge: Maggie is walking by herself. Lisa got straight A's. And Bart... well, we love Bart.
Marge: ...and that's the life of Mozart. Thank God he died young. I gotta get dinner on the stove.
Marge: Look at them! They've jumped on the one franchise I might possibly have considered thinking about becoming interested in.
Marge: Homer, I thought our marriage could survive anything, but last night, you not only crossed the line, you threw up on it.
Marge: Aw geez, I just swept the Circle of Death!
Homer: 3... 2... 1... Happy New Year! Marge: ...of school!
Lisa: But I'm so angry. Marge: You're a woman. You can hold on to it forever.
Marge: I'm proud of you, Homer. You have given a chance for everyone to express love in its most purest form... a binding legal contract.
Marge: We don't need T.V. to have family fun. Why don't we play *Monopoly*? Lisa: (Walking to the closet where the board games are kept) Which version? (Flips through different versions) We've got '*Star Wars*' Monopoly, Rasta-Mon-Opoly, Galip-Olopoly, Edna Krabappoly... Marge: Let's stick to original *Monopoly*. The game's crazy enough as it is. (Holds up one of the playing pieces) How can an iron be a landlord?
Man: Folks, how often have you opened the morning paper only to have the rubber band fly off and hit you right in the eye? Marge: Never. But it's my number one concern.
Marge: Well, did you call one of your friends? Lisa: Hah! These are my only friends: grown up nerds like *Gore Vidal*, and even he's kissed more boys that I ever will. Marge: Girls, Lisa. Boys kiss girls.
Marge: It was pretty exciting. But celery's pretty exciting too.
Bart: Where are you going? Marge: Shopping. Every time this town riots the malls are deserted.
Marge: (To Homer) Who was I to think you could mail an envelope?
Homer: I'm sorry, Marge, but sometimes I think we're the worst family in town. Marge: Well maybe we should move to a larger community.
Marge: Somebody throw the goddamn bomb!
Marge: The mailman did the other side of the street before our side. Turns out it was a substitute.
Marge: Bart, what are you doing? You're indoors at an outdoor party.
Marge: No one in this family is hurling rotten anything at anyone.
Marge: This was such a pleasant St. Patrick's day until the Irish people showed up.
Marge: (Talking about Homer's eating habits) I didn't used to mind it when he would lock the bathroom door and snack off, but when he's getting regular, night after night after night?
Marge: Homer, I'd like you to forgive me for doing the right thing. Homer: Oh, Marge! Marge: We've squabbled over money before. Hmm... never this much. I mean, I know this is different than that time I washed your pants with a $20 in the pocket.
Marge: I don't want to alarm anyone, but I think there's a li'l al-key-hol in this punch.
Marge: I brought you a tuna sandwich. They say it's brain food. I guess because there's so much dolphin in it, and you know how smart they are.
Marge: Homer, I've gone through seven years of receipts, and you've spent less on gifts for me than you have on temporary tattoos.
Marge: Homer, you know how unpredictable the French are. One minute they're kissing a woman's hand, then next, they're chopping off her head!
Marge: You know, *Fox* turned into a hard-core sex channel so gradually, I didn't even notice.
Marge: You know, when I was a girl, I always dreamed of being in a Broadway audience.
Marge: Now I'm gonna warn you kids, the next part of the story gets a little 'WB'...
Marge: God didn't give you legs to use a scissors.
Marge: You're home early. Homer: Can't a guy rush home to see his beautiful... Marge: Moe's is closed, huh? Homer: Yeah, now what am I supposed to do?
Marge: This country's so historic. For all we know, Jesus could have given a talk in conference Room C.
Homer: Marge, would you mind if we just cuddle? Marge: Cuddling is for after.
Marge: 'Ultimate' makes everything worse.
Marge: I can hear your sarcasm from inside the house and the dishwasher's on. What's going on here? Lisa: Mr. Flanders invited us to Israel. I think he wants to get dad into heaven. Bart: Great more Hell for me.
Marge: Call me a killjoy, but because I think this is not to my taste, no one else should be able to enjoy it.
Marge: Oh Bart, why couldn't you have gotten a paper route like other boys?
Marge: Homey, I'm going to be a dancer. Homer: Go-go or boring? Marge: Boring!
Marge: I'm sorry, but I know God would never ask a mother to sacrifice her child for the good of the world... again.
Marge: Bart! I've had it with you! I'm taking away all your T.V. privileges. Bart: You already did that. Marge: Ok, then video games. Bart: That too. Marge: No more non-dice board games. Bart: What? you can't take my Boulderdash! Marge: I just did!
Marge: Hey kids! I made your favorite cookies: Christmas trees for the girls and bloody spearheads for Bart.
Homer: Our family was suffering through its worst crisis ever. Bart was miserable at school, and Lisa's gifts were going to waste. Bart: Uh, Homer? It's five years later, and I'm still miserable at school. Lisa: And my gifts are still going to waste! Marge: And sometimes I feel so smothered by this family I just want to scream until my lungs explode! (The rest of the family stares at Marge for a moment and she takes a deep breath) Marge: I'll go start dinner now. Homer: You do that.
Marge: I'd like to visit that Long Island place, if only it were real.
Bart: Wow, so that's how Lisa got her sax! Homer: Next, I'll tell you the origin of Maggie's pacifier! Marge: What origin? We got it for $1.95 down at the *Safeway*!
Marge: You like *Shake n' Bake*. You used to put it in your coffee.
Marge: I'll just have a cup of coffee. Bartender: Beer it is. Marge: No, I said coffee. Bartender: Beer. Marge: Cof-fee. Bartender: Be-er. Marge: C-O... Bartender: B-E...
Marge: Homer, don't take this personally, but I've obtained a court order to prevent you from planning this wedding.
Marge: Tuck-in time! All aboard the sleepy train to visit *Mother Goose*. Barty's stop is Snoozyland to rest his sweet caboose.
Marge: Well, if loving my kids is lame, then I guess I'm just a big lame.
Marge: Grocery shopping is so exciting! It's like unwrapping presents from yourself.
Marge: Homer, I don't want to leave Springfield. I've dug myself into a happy little rut here and I'm not about to hoist myself out of it.
Bart: Mom, what if there's a really bad crummy guy who's going to jail but I know he's innocent? Marge: Well Bart, your Uncle Arthur used to have a saying 'Shoot 'em all and let God sort them out.' Unfortunately one day he put his theory into practice. It took seventy-five Federal Marshals to bring him down. Now let's never speak of this again. Bart: Mom, What if I can get this guy off the hook? Should I do it? Marge: Honey, you should listen to your heart and not the voices in your head, like a certain uncle did, one grave December morn...
Marge: Now that's what I call breakneck speed!
Marge: We've got to get her out of there. Babies are not supposed to sleep on their stomach on a cake.
Marge: Well, maybe you shouldn't listen to a thirty year old T.V. show that only got on the air because the creator had evidence that the network president ran over a guy.
Marge: This food has got to go. It's full of chemicals, trans-fats and hard pore-corn.
Marge: (After turning on the kitchen sink) Hot comes out of hot. It's like I'm dreaming.
Bart: You're like the Jesus of carpentry! Marge: Aww, what a sweet blasphemy.
Marge: Ok, remember our deal, everyone gets to return one Christmas present with no hurt feelings.
Lisa: Mom, aren't you going to step in and stop this? Marge: Usually, your father's crackpot schemes fail once he sees something good on T.V. But this season...
Marge: She's such a butt-hole.
Marge: No, you should never raise your hand to a child. Just leave the crust on their sandwiches. They'll get the message.
Marge: Homer, can you please turn down those blimp engines and tell me where you are?
Marge: Martha, the house looks beautiful. It's like Christmas with a childless gay couple.
Marge: I don't mind you peeing in the shower as long as you're taking a shower.
Marge: Homer, of all the things you've done... going into space, attending clown college, joining the *Navy*, I'd never thought you'd join the *Army*.
Marge: What you're saying is so understandable. And really, your only crime was violating U.S. Law.
Marge: They should call it a 'Tall Island Iced Tea.'
Marge: This tree reminds me of your father. It's round in the middle, thinning on top, and your hands get sticky when you touch it.
Homer: Aah, listen... since all the other fun stuff is out of bounds, how 'bout a little Bible-thumping in the crow's nest? What do you say Miss... Marge: Constance Prudence Chastity Goodfaith. Homer: D'oh! Marge: My friends call me Marge. Marge Obedience Temperance Sex-won't. Homer: D'oh!
Roger Myers Jr.: Where are our ideas gonna come from, huh? Her? (Points at Marge) Marge: Uh, how about... Ghost Mutt?
Marge: You can't say 'sex' on the Internet!
Marge: That's not how a family vacation works. We do things together while you're father has fun without us.
Bart: I'd sell my soul for a formula one racing car. (Devil Flanders appears) Devil Flanders: Heh, heh, heh, that can be arranged. Bart: Changed my mind. Sorry. (Devil Flanders vanishes) Marge: Bart, stop pestering Satan!
Bart: I'm not going on the dang field trip. Marge: Bart! Watch your language... Oh.. you did.
Marge: My life is pretty boring. The other day some Jehovah's Witnesses came to the door and I wouldn't let them leave. They finally snuck away when I went to make lemonade.
Bart: After they watch a foreign film. I was so bored I cut the ponytail off the guy in front of us. (Holds pony tail to his head) Look at me, I'm a grad student. I'm 30 years old and I made $600 last year. Marge: Bart, don't make fun of grad students. They've just made a terrible life choice.
Marge: Homer, is this how you pictured married life? Homer: Yeah, pretty much, except we drove around in a van solving mysteries.
Marge: I'm going into the dining room to have a conversation. If you want to join me, fine. (Leaves room) Hello Marge, how's the family? I don't want to talk about it. Mind your own business! Homer: Keep it down in there, everybody!
Marge: You know Homer, when I found out about this I went through a wide range of emotions. First I was nervous, then anxious, then wary, then apprehensive, then kinda sleepy, then worried, and then concerned. But now I realize that being a spaceman is something you have to do. Homer: Who's doing what now?
Marge: Bart, don't use the 'Touch of Death' on your sister.
Marge: If *Gahndi* can go without eating through a three hour movie, then I can do this.
Marge: I Googled 'Girls Having Fun' and after wading through ninety-seven thousand pages of porn, I found crazy bowling.
Marge: That flattens my soda pop.
Marge: Go out on a Tuesday? Who am I, *Charlie Sheen*?
Marge: No more Simpson's movies. One was plenty.
Marge: At least in other sports their trying to put a ball in a net or zone. In this sport they don't try to put anything in anything... and if they did I wouldn't want to see it.
Marge: Chet, I have one simple request. Please go out of business and donate all your profits to charity.
Marge: Damn these sturdy foreign-built phones.
Marge: You know, the courts may not be working any more, but as long as everyone is videotaping everyone else, justice will be done.
Marge: Just between us gals, he hasn't been this frisky in years!
Marge: Now lets all forget our troubles with a big bowl of strawberry ice cream!
Marge: You should listen to your heart, and not the voices in your head.
Lisa: Mom! Dad's on PBS! Marge: Mmm. They don't show police chases, do they?
Nelson: Shoplifting is a victimless crime, like punching someone in the dark.
Nelson: (Running away) Running away rules!
Nelson: Ha, Ha... You feel self-conscious.
Nelson: I better get going, It's getting late. My mom is going to wake up soon. She gets upset if someone is not there to tell her where she is.
Bart: Ow! What are you doing? Nelson: Uh, I got bored so I started slapping you.
Nelson: You're an octo-wussy. Oooh, look at me, I'm Bart Simpson, I'm scared to use a gun, I wanna marry Milhouse, I walk around like this... lalalalalalalala.
Nelson: Hey I'm sure it's just a phase, like when I used to stand on the overpass and drop computers on the freeway.
Marge: Where's your dad in all of this? Nelson: He went out for a pack of cigarettes and never came back. He said smell ya later, but he never smelled me again.
Marge: Aren't you the boy who beats up my son? Nelson: Probably, what's your name? Marge: Simpson. Nelson: Oh yeah, Bart Simpson. Spiky hair, soft kidneys, always hitting himself.
Nelson: Hey Einstein, what's a million add a million? Lisa: Two million. Nelson: Oh...
Nelson's Father: Good game, son. We're going to celebrate at *Hooters*. Nelson: Ah... I don't wanna bother mom at work.
Nelson: Haw-Haw.
Nelson: Yeah, I've been held back more times then I can count. Which I guess is why I keep getting held back.
Nelson: You think you're so smart don't you Simpson? Bart: We're both in the same reading group. I think you know how smart I am...
Nelson: If no ones getting mad, are you really being bad?
Nelson: I walked nineteen miles for this?
Nelson: Maybe you could trick your parents into having a baby. The way my mom nearly tricked *Charles Barkley*.
Bart: Did you think we went too far? Nelson: Nah, booze only makes you do things you already wanted to do.
Nelson: Woah! She gets to use the real scissors. Nice!
Nelson: My mom ran off with my birthday clown.
Nelson: God, If you don't bring my Lisa back safe, ants will burn tonight.
Nelson: This funeral just got depressing.
Nelson: (Talking about the Kwik-E-Mart) I like how Kwik is spelled with a 'K.' It's a quicker way of spelling quick.
Nelson: We've been doing a lot of upper body work on Bart. Today let's pound his kidneys.
Nelson: (On the movie *Naked Lunch*) I can think of at least two things wrong with that title!
Nelson: Check it out, a freezer geezer!
Nelson: Let chaos reign!
Nelson: Girls are so lame, isn't that right headless *Darth Vader*? What's that? You miss your girl friend armless Malibu Stacy wrapped in hockey tape?
Nelson: Ha, Ha... Hey, that hurts. No wonder no one came to my birthday party.
Lisa: 'Nuke the whales?' You don't really believe that, do you? Nelson: I dunno. Gotta nuke something.
Grandpa: That's my son up there! Man: What, the balding fat-ass? Grandpa: Uh, no, the... Hindu guy.
Grandpa: Did you spend an unforgettable night with a soldier from the *U.S. Army* in 1944? You did! Was he from the first inventory division? He was! And was he a gentle caring lover? He was? Sorry I bothered you.
Grandpa: Sorry I never saw you again. I just felt the cultural differences between us were too great. Plus as the boat pulled away from the dock I thought you looked fat.
Grandpa: Ooooh. Just leave me in the car with the window open a crack. Homer: That's the plan!
Grandpa: Let's see... I'm an Elk, a Mason, a communist... I'm the president of the Gay and Lesbian Alliance for some reason. Ah, here it is! The Stonecutters.
Grandpa: What's so unappealing about hearing your elderly father talk about sex? I had seeeeex.
Grandpa: Yep, the Simpsons have never married or even shook hands with anyone interesting. In a world of 31 flavors, we're the cup of water they rinse the scoops in.
Grandpa: I got a funny story about that. Well, it's not so much funny as it is long.
Grandpa: I thought I'd never hear the screams of pain or see the look of terror in a young man's eyes. Thank heaven for children.
Grandpa: (Talking to Homer) Make me proud... or at least less ashamed.
Grandpa: I can finally afford a crazy stripper wife!
Grandpa: You two look good, open casket good.
Grandpa: Dear Mr. President, There are too many states nowadays. Please eliminate three. P.S. I am not a crack-pot.
Grandpa: A doctor? I already got enough doctors touching me and poking me and squeezing me up here and jiggling me down there, and that's just the receptionist!
Grandpa: Anyway, long story short, is a phrase whose origins are complicated and rambling.
Grandpa: I always get the blame around here! Who threw a cane at the T.V.? Who fell into the china hutch? Who got their dentures stuck on the toilet?
Grandpa: We can't bust heads like we used to, but we have our ways. One trick is to tell 'em stories that don't go anywhere. Like the time I took the ferry over to Shelbyville. I needed a new heel for my shoe, so I decided to go to Morganville, which is what they called Shelbyville in those days. So, I tied an onion to my belt, which was the style at the time. Now to ride the ferry cost a nickel, but in those days, nickels had pictures of bumblebees on them. 'Gimme five bees for a quarter,' you'd say. Now, where were we? Oh, yes. The important thing was, I had an onion on my belt, which was the style at the time. They didn't have white onions, because of the war. The only thing you could get was those big yellow ones.
Grandpa: Homer, you're as dumb as a mule and twice as ugly.
Grandpa: Sour cream and chives? In my day all we put on potatoes was pine needles and barber hair. I hate this century.
Grandpa: She did things your mother would never do. Like have sex for money.
Grandpa: Flanders feeds me people food. Homer: Well I can't compete with that.
Grandpa: Here you go, ya ingrate! Think of me when you're havin' the best sex of your life!
Grandpa: Not many people know I was the first person to own a radio in Springfield. Weren't much on the airwaves those days, just *Edison* reciting the alphabet. 'A,' he'd say, then 'B'... 'C' would usually follow...
Grandpa: When I read your magazine, I don't see one wrinkled face or single toothless grin. For shame! To the sickos at '*Modern Bride*' magazine.
Grandpa: What're you cacklin' about, fatty? Too much pie, that's your problem.
Grandpa: You're never to old to ruin things for the young.
Grandpa: (Trying to peel a banana) Give up the goods you yellow devil!
Grandpa: (After crashing his car into the wall) This building cut me off!
Grandpa: The good Lord lets us grow old for a reason, to find fault in everything he's created.
Grandpa: The last time those meteors came we thought the sky was on fire. Naturally we blamed it on the Irish. We hanged more than a few...
Grandpa: I'll be deep in the cold, cold ground before I acknowledge Missoura!
Grandpa: The older I get the more I like the taste of hot water.
Grandpa: I'll take that secret to my grave, or urn, or medical school dissection table, or where ever you're dumping me. Homer: Listen wrinkles, if you know something that will cheer up my little girl you better spill it or I will make things very uncomfortable for you. (Adjusts the thermostat)
Grandpa: Dear Advertisers, I am disgusted with the way old people are depicted on television. We are not all vibrant, fun-loving sex maniacs. Some of us are bitter, resentful individuals who remember the good old days when entertainment was bland and inoffensive. The following is a list of words I never want to hear on television again...
Bart: (To Grandpa Simpson) We need to know your first name. Grandpa: You're making my tombstone! Lisa: No, we're just curious! Grandpa: Well, let's see... first name, first name. Well, whenever I get confused, I just check my underwear! (He whips them off without taking off his pants) It holds the answer all the important questions! Call me... (Checking the name) Abraham Simpson! Lisa: Grandpa... how did you take off your underwear without taking off your pants? Grandpa: (Confused) I don't know!
Grandpa: That doll is evil, I tells ya. Evil! Eeeeeeviillll! Marge: Grandpa, you said that about all the presents. Grandpa: I just want attention.
Bart: But Grandpa, didn't you wonder why you were getting checks for doing absolutely nothing? Grandpa: I figured it was 'cause the *Democrats* were in power again.
Marge: Grandpa, are you sitting on the apple pie? Grandpa: I sure hope so...
Grandpa: You're in the newspaper business? Oh, something that's going to die before I do.
Grandpa: Nurse, another round of waters in your finest paper cups.
Grandpa: I want to put salt on things.
Grandpa: My dream is to be able to walk up the stairs like an eight year-old girl.
Grandpa: Sure is hell to have your husband around all the time ain't it? Marge: At least in hell the heat still works.
Grandpa: Someone's listening to me. Now I know how a radio feels.
Grandpa: *Grover Cleveland* spanked me on two non-consecutive occasions.
Grandpa: My car gets forty rods to the hogshead and I'm sticking to it.
Maude Flanders: Everyone turn around and look at this! Grandpa: What is it? A Unitarian?
Santa: If you like, I can take you to see your brother now. Grandpa: Will we be back in time for the *Tournament of Roses Parade*? Santa: Probably not. Grandpa: Good, I hate that crap. Santa: Yeah, me too.
Grandpa: The grass is sharper than the grass in my day...
Grandpa: I used to be with it, but then they changed what 'it' was. Now, what I'm with isn't it, and what's 'it' seems weird and scary to me.
Grandpa: My story begins in nineteen dickety two, we had to say dickety because the Kaiser stole our word twenty. I chased that rascal to get it back, but gave up after dickety six miles.
Grandpa: My Homer is not a communist. He may be a liar, a pig, an idiot, a communist, but he is not a porn star.
Lisa: Bart, do you realize what this means? The next time we fall asleep we could die! Grandpa: Ehhh, welcome to my world.
Grandpa: We're the baddest punks in our age bracket!
Mayor Quimby: Can't we have one meeting that doesn't end with digging up a corpse?
Mayor Quimby: Oh no! Without the booze these guys remember how much they hate each other.
Leonard Nimoy: I think this vessel could do at least warp 5. Mayor Quimby: Yes, and may the force be with you. Leonard Nimoy: Do you even know who I am? Mayor Quimby: Of course I do. Weren't you one of the *Little Rascals*?
Mayor Quimby: We're twice as smart as the people of Shelbyville. Just tell us your idea, and we'll vote for it!
Mayor Quimby: Ich bin ein Springfielder. Homer: Mmmmm. Jelly Donuts.
Mayor Quimby: Yes there is a comet and yes it is heading for our town. (Scattered clapping) You uh, don't need to applaud that.
Mayor Quimby: Oh, dear God. Can't this town go one day without a riot?
Mayor Quimby: What the hell made me think *Michael Jackson* would visit this jerkwater berg?
Mayor Quimby: Check out the rack on the blonde in the forth row.
Mayor Quimby: All those in favor of building this decadent monument of excess, say I.
Mayor Quimby: Very well then, instead of fleeing this town, I'll stay here and grow fat off kickbacks and slush funds.
Mayor Quimby: Our city will not negotiate with terrorists. Is there a city nearby that will?
Mayor Quimby: You are tampering with forces you can't understand. We have major corporations sponsoring this event.
Mayor Quimby: You can't seriously want to ban alcohol. It tastes great, makes woman appear more attractive, and makes a person virtually invulnerable to criticism.
Mayor Quimby: Vote Quimby.
Mayor Quimby: Please use your time in line wisely to *Sophie's Choice* your child.
Mayor Quimby: Everything I've said about terrorism 'till now was fear mongering, but today I monger the truth.
Mayor Quimby: All right, settle down, people. We are all upset by Mr. Burns' plan to block out our sun. It is time for decisive action! I have here a polite but firm letter to Mr. Burns' underlings who, with some cajoling, will pass it along to him or at least give him the gist of it. Mayor's Bodyguard: (Whispering) Sir, a lot of people are stroking guns... Mayor Quimby: Also, it has been brought to my attention that a number of you are stroking guns. Therefore, I will step aside and open up the floor...
Mayor Quimby: Remember, if anyone asks, you're my niece from out of town. Lady: I am your niece, uncle Joe! Mayor Quimby: Good Lord! I'm an abomination!
Mayor Quimby: Watch it, you walking tub of donut batter! Chief Wiggum: Hey, I got pictures of you, Quimby. Mayor Quimby: You don't scare me. That could be anyone's ass!
Marge: My name is Marge Simpson and I have an idea. It may sound a little boring at first. Mayor Quimby: Chat away. I'll just amuse myself with some pornographic playing cards.
Mayor Quimby: I stand by my racial slur.
Milhouse: I'm not a nerd, Bart. Nerds are smart.
Bart: Milhouse, it's me! Check out the caller ID on your phone. Milhouse: Blocked number? That service is $3.65 a month. Did you switch places with a millionaire kid that looks just like you?
Bart: Well if your souls real where is it? Milhouse: It's kinda in here... and when you sneeze, that's your soul trying to escape. Saying God bless you crams it back in, and when you die, it squirms out and flies away! Bart: What if you die in a submarine at the bottom of the ocean. Milhouse: Oh, it can swim, it's even got wheels, incase you die in the desert and have to drive to the cemetery.
Milhouse: *Alf Pogs*! Remember *Alf*? Well he's back... in *Pog* form!
Milhouse: Hey! My shoes are soaked but my cuffs are bone dry! Every thing's coming up Milhouse!
Milhouse: I will be a nerd fish.
Bart: I am so gonna try out for that. Milhouse: Me too, but I hope you get it. Bart: No, I hope you get it. Milhouse: Well, I really hope you get it. Bart: Yeah, I hope I get it too. Later. Milhouse: For a second there he hoped I got it.
Milhouse: I can help you sir, and I answer to no one.
Milhouse: So this is what it feels like when doves cry.
Milhouse: (The school bell rings) School's out! Up yours, Krabappel! (Milhouse runs off, no one else moves) Mrs. Krabappel: Well, I'm glad the rest of you remembered that summer vacation starts at the end of the day, not the beginning. (Krabappel motions to a clock that reads 9 a.m.)
Milhouse: The 'House always wins.
Milhouse: How could Krabappel take my cell phone? I'm only on month one of a sixty month plan.
Bart: You grew tired of always being in my shadow. Milhouse: No, I like your shadow, it's nice and cool.
Milhouse: The *Statue of Liberty*? Where are we?
Milhouse: First girls ruined *Sex and the City*, and now this.
Milhouse: You're right. I guess no one has ever written a book to help a middle aged woman turn her life around.
Milhouse: What is it with cherubs? I mean, are they barfing or something?
Milhouse: Woah, that text was totally worth the fifteen cents it cost to receive it.
Milhouse: Jeez... if it's in a book, it's gotta be true!
Milhouse: I'm not a smart nerd. I'm just a weak nerd.
Milhouse: Maybe I was promoted to green belt to early.
Bart: This dame is really into you. Milhouse: She sure is. This morning I got to second base, on our walk around the softball diamond.
Milhouse: Wow! She's everything I want to be...
Milhouse: Bart, it's not always a good idea to meet your hero. I once followed *Santa* home from the department store, and what I saw wasn't pretty.
Milhouse: You leave that to the Baron and me.
Milhouse: You said I never had a goldfish, but why'd I have a bowl Bart? Why'd I have a bowl?
Milhouse: Back off, Bart! She's with the 'House now.
Milhouse: My non-lazy eye...
Milhouse: I'm the second coolest kid in the world!
Milhouse: I have nothing to offer you but my love. Mr. Burns: I specifically said, 'No geeks!' Milhouse: But my mom says I'm cool.
Milhouse: I don't know, my dad's a pretty big wheel down at the cracker factory.
Milhouse: Why do you have a social worker? I am the one with stigmata.
Milhouse: But, I'm all Milhouse! Plus, my mom says I'm the handsomest guy in school!
Milhouse: Trust me Bart, it's better to walk in on both your parents instead of just one of them.
Milhouse: If I wasn't your friend, I'd tell you, you sucked.
Bart: Do you realize what this means? Milhouse: Yeah, but you say it first.
Bart: What's it like riding a girl's bike? Milhouse: It's disturbingly comfortable.
Milhouse: This is great. Not only am I not learning, I'm forgetting stuff I used to know.
Bart: Hey Milhouse, guess where I'm calling from? Milhouse: Well, I know you don't have a cell phone, so you must be in your kitchen, or one of your bedrooms, unless you have a wall jack in your basement. That would be huge! Bart: Look outside the window. Milhouse: I'm not supposed to look out the window when I'm alone. Bart: Just do it!
Milhouse: This is where I come to cry.
Milhouse: If death can happen to a fish, then it can happen to anyone.
Milhouse: Bart, I don't want you to see me cry. Bart: Aw come on, I've seen you cry a million times. You cry when you scrape your knee, you cry when we're out of chocolate milk, you cry when you're doing long division and you have a remainder left over. Milhouse: Well, I didn't want you to see me cry THIS time.
Milhouse: It's called lice, and it's nothing to be ashamed of!
Milhouse: There's plenty of Milhouse to go around.
Milhouse: Weekend dad wanted a DVD player...
Milhouse: It was just like *Romeo and Juliet*, only it ended in tragedy.
Milhouse: Wow! This is like *Speed 2* only it's on a bus.
Milhouse: It's just like Venice, but without the Black Plague.
Maude Flanders: Neddy doesn't believe in insurance. He considers it a form of gambling.
Maude Flanders: Faster Neddy! Ned Flanders: I can't its a *Geo*!
Homer: What? Flanders! You're the devil? Devil Flanders: Ho ho! It's always the one you least suspect!
Maude Flanders: Neddy, I've had just about all I can take of Homer Simpson's torso. I'll go get some hot dogs. Ned Flanders: No foot-longs. Maude Flanders: I know, they make you uncomfortable.
Maude Flanders: It's a miracle!
Rod: Jesus cries blood every time you lie.
Ned Flanders: Oh, it's the Four Elephants of the Apocalypse! Maude Flanders: (Sleepily) That's 'Horsemen' Ned. Ned Flanders: Gettin' closer.
Todd: I get to clothe the leper. Rod: Lucky! Ned Flanders: Supper time boys! Todd: Oh boy, liver! Rod: Iron helps us play!
Maude Flanders: I've been going to Bible classes. They're teaching me to be more judgmental.
Marge: Homer, you've got to stop insulting everyone, especially your boss! Homer: Marge, the comedy roast is an American tradition. It's what gives us the freedom to criticize our social betters... Hey Flanders! You smell like manure. Ned Flanders: Uh oh. Better cancel that dinner party tonight. Thanks for the nose-news, neighbor!
Ned Flanders: Okily-dokily!
Ned Flanders: ...as a Christian I assume the worst.
Todd: Dad, the heathen's getting away! Ned Flanders: I see him, son.
Ned Flanders: Our G-rated treat tonight is a film from my favorite year... yester.
Ned Flanders: Hidely-ho, neighborino!
Ned Flanders: I didn't do diddly, and certainly not squat.
Ned Flanders: Homer, affordable tract housing made us neighbors, but you made us friends.
Ned Flanders as a Puritan: Great Chief Wiggum, we could never have survived our first year in the new world without you. I almost regret what we Europeans are going to do with you. Chief Wiggum as an Indian: What are ya gonna do? Ned Flanders as a Puritan: Give ya the biggest piece of pumpkin pie! ...Also we are going to take your land and wipe you out. Who wants whipped topping?
Ned Flanders: (At Moe's Restaurant) Well! I expected that type of language at *Denny's*, but not here!
Ned Flanders: Sometimes Maude, God bless her, she underlines passages in my Bible because she can't find hers. Homer: Thank God they don't keep guns in the house.
Rex Banner: Are you the Beer Baron? Ned Flanders: Well, if you're talking about root beer, I plead guilt-diddily-ildly as char-didily-arged! Rex Banner: He's not the Baron, but he sounds drunk. Take him in.
Ned Flanders: I okely-dokely-schmokely do!
Ned Flanders: Well, when the sun goes down it means God's gone to China, to watch over those good folks.
Ned Flanders: Oh, what better way to celebrate our wedding night then to keep an unmarried couple apart.
Ned Flanders: As the elephant said to the peanut vendor, toss those in my trunk.
Ned Flanders: (In Las Vegas) The lights, the noise, the letter 'X.' It's all designed to inflame the senses. I'm over stimulated. I've gotta get out of this town.
Ned Flanders: Son of a diddly!
Marge: Hi Ned. Where are the boys? Ned Flanders: Oh, there grounded. I found out Rod watched a commercial for *Grey's Anatomy* and Tod took a full day to tell me.
Ned Flanders: There is no bot, like a robot! (David the robot hits Flanders in the crotch and he falls to the ground) Ned Flanders: Aaw, my Flander-doodles!
Ned Flanders: I wish we lived in a place more like the America of yesteryear that only exists in the brains of us *Republicans*.
Ned Flanders: Sorry to break character, but these stunt pants are getting mighty toasty! Maude Flanders: Uh, roll, Neddie, roll. Ned Flanders: It's not working... it just spreads the flames!
Ned Flanders: I don't need to be told what I think... by anyone living.
Rod: Are you jealous of Brother Homer? Ned Flanders: Maybe just a little bit. Rod: I'm jealous of girls 'cause they get to wear dresses. Ned Flanders: One problem at a time, boy.
Ned Flanders: Hi-diddly-ho, neighbors!
Ned Flanders: Just as I feared. Her Buddhism has led her directly to witchcraft.
Ned Flanders: I've gone from lookey-lou to talkie-too.
Ned Flanders: Saved by the bell from an eternity in Hell.
Ned Flanders: Reverend, care for some of my devil's food cake? Rev. Lovejoy: Is that really devil's food? Ned Flanders: No, it's just angel food with chocolate on top. Rev. Lovejoy: Umm-hmm, I knew it.
Homer: Ned I never thought I'd say this but, we make a great team. Ned Flanders: Us? A Team? As the salad said to the soup: I'm all mixed up!
Ned Flanders: Oh man! That's harder to swallow then evolution.
Homer: Who wants feet steak? Ned Flanders: De-meat those feet!
Ned Flanders: Yep, Springfield is cleaner then the Lord's hand towels.
Ned Flanders: You know, I wouldn't mind Homer laying naked in his hammock. But does he have to string it up higher then the fence line?
Ned Flanders: Homer, my friend. Of all the false Messiahs today you came closest to the truth.
Rod: What are you doing, daddy? Ned Flanders: Imploring some people I never met to pressure a government with better things to do to punish an innocent man for doing something that nobody saw. That's what I'm doing! Rod: Daddy, we think you need a new mommy. Ned Flanders: First things first!
Ned Flanders: I'll have a Shirley... No, a virgin... No, a children's... Oh, what the heck? You only live once. Give me a white wine spritzer!
Ned Flanders: Bless the grocer for this wonderful meat, the middleman who jacked up the price, and let's not forget the humane but determined boys at the slaughterhouse.
Todd: Daddy, what are taxes paying for? Ned Flanders: Ohoho... everything! Policemen, trees, sunshine, and let's not forget the folks who just don't feel like working, God bless 'em!
Ned Flanders: I'm a murderer! I'm a mur-diddley-urgler!
Ned Flanders: Edna, call me *Delta Airlines* 'cause I can't handle your extra baggage.
Homer: What if we switched wives? Would that help? Ned Flanders: For the last time, NO!
Ned Flanders: Look at that, you can see the four states that border Springfield: Ohio, Nevada, Maine, and Kentucky! Bart: Oh yeah.
Ned Flanders: That concludes our Halloween show for this year. I just wanna say that for watching this network, you're all going to Hell and that includes *FX*, *Fox Sports*, and our newest devil's portal, the *Wall Street Journal*. Welcome to the club!
Ned Flanders: Bart and Homer can't go Catholic. The Romans have been separate from us since the *Season of Lourdes* in 1573 and that was about our holy right to come to church with wet hair! ...Which we've since abolished.
Homer: Hey, Flanders, check out my new satellite dish. Ned Flanders: (Whistles) Boy, that's jim dandy roof candy. I'd love to come over sometime and watch that Church Channel. Homer: I bet you would. Ned Flanders: Oh, you'd win that bet. Seems like I'm spending all my money on religious pay-per-view, or as I like to call it, 'pray-per-view.' Homer: Damn your sparkling wordplay! Ned Flanders: And bless your humble home. (Homer growls in response)
Ned Flanders: I think I may be coveting my own wife!
Homer: If you ask me, you were trying to play God. Ned Flanders: That's the worst sin of all... for some reason.
Ned Flanders: Homer, do you know why I'm a Christian? Homer: Your parents made you?
Ned Flanders: (To Homer) You come all the way to Jerusalem, the happiest place on earth, and all the pictures in your camera are of funny soda pops?
Ned Flanders: And thank you Lord, for letting me see this wonderful place where the end of the world will soon begin.
Ned Flanders: The old city! That's where B.C. turned into A.D.!
Ned Flanders: Nothing like a luke-warm glass of water to Jeckel down this Hyde.
Ned Flanders: Oh Reverend, I've been working my Bible to the bone trying to save that man.
Ned Flanders: Homer Simpson, you are the most infuriating, *Netflix* DVD burgluring, Bar-B-Que not putting out, man I've ever met.
Ned Flanders: Thank you for coming. Now lets start with the words everyone likes to hear. Welcome to Bible study!
Todd: I wish Homer was my father. Ned Flanders: ...And I wish you didn't have the devil's curly hair.
Ned Flanders: Ok, boys, when you meet Jesus, be sure to call Him Mr. Christ. Todd: Will Buddha be there? Ned Flanders: No!
Ned Flanders: Look at that, you can see the four states that border Springfield: Ohio, Nevada, Maine, and Kentucky! Bart: Oh yeah.
Ned Flanders: Oh, right as rain! Or, as we say around here, 'left as rain,' heh heh.
Ned Flanders: At times like these, I used to turn to the Bible and find solace, but even the good book can't help me now. Homer: Why not? Ned Flanders: I sold it to you for seven cents. Homer: Ohh...
Ned Flanders: And I guess I'm just a caveman. If they existed. Which they didn't.
Ned Flanders: I think I swallowed a toothpick!
Ned Flanders: Excuse me. With all this racket my boys can't get their sixteen hours sleep.
Ned Flanders: One cran-bran for the flan-man. Mrs. Krabappel: What did he want? Bart: Beats me. I just gave him a banana.
Ned Flanders: There's only one God. Just one. Well, sometimes there's three.
Ned Flanders: They've broken every commandment except one. Carl: Hey Lenny, covet some chili fries? Lenny: You bet. Ned Flanders: That's it. The whole shebang.
Ned Flanders: I've done everything the Bible says... even the stuff that contradicts the other stuff!
Ned Flanders: My Satan sense is tingling! To the root cellar, boys!
Ned Flanders: (Reading) ...and *Harry Potter*, and all his wizard friends... went straight to Hell for practicing witchcraft. Todd: Yay! (Ned throws the book into the burning fireplace)
Judge: Case dismissed! Lionel Hutz: Your Honor... Do I still get paid?
Lionel Hutz: Mr. Simpson, the state bar forbids me from promising you a big cash settlement. But just between you and me, I promise you a big cash settlement.
Lionel Hutz: Lionel Hutz, court-appointed attorney. I'll be defending you on the charge of... Murder one! Wow! Even if I lose, I'll be famous!
Lionel Hutz: This all goes back to the Frank Wallbanger case of '78. How about that! I looked something up! These books behind me don't just make the office look good, they're filled with useful legal tidbits just like that!
Lionel Hutz: Lionel Hutz, executor of Ms. Bouvier's estate. She left a video-will so I earn my fee simply by pressing the 'play' button. Pretty sweet, eh?
Lionel Hutz: To my executor, Lionel Hutz, I leave $50,000. Marge: Mr. Hutz! Lionel Hutz: You'd be surprised how often that works, you really would.
Lionel Hutz: Don't worry, Homer. I have a foolproof strategy to get you out of here. Surprise witnesses, each more surprising than the last. The judge won't know what hit him. Officer: Pipe down Hutz!
Lionel Hutz: Now Marge, you've come to the right place. By hiring me as your lawyer, you also get this smoking monkey.
Lionel Hutz: And so, ladies and gentleman of the jury I rest my case. Judge: Hmmm. Mr. Hutz, do you know that you're not wearing any pants?
Lionel Hutz: Mr. Simpson, I was just going through your garbage, and I couldn't help overhearing that you need a babysitter. Of course, being a highly-skilled attorney, my fee is $175 an hour. Homer: We pay eight dollars for the night, and you can take two popsicles out of the freezer. Lionel Hutz: Three. Homer: Two. Lionel Hutz: Ok, two, and I get to keep this old bird cage. Homer: Done! Lionel Hutz: Still got it.
Lionel Hutz: Mr. Simpson, don't you worry. I watched *Matlock* in a bar last night. The sound wasn't on, but I think I got the gist of it.
Lionel Hutz: And as for your case, don't you worry. I've argued in front of every judge in this state... often as a lawyer.
Lisa: Excuse me, Mr. Hutz. Are you a shyster? Lionel Hutz: How does a nice little girl like you know a big word like that?
Lionel Hutz: Ladies and gentlemen, I'm going to prove to you not only that Freddy Quimby is guilty, but that he is also innocent of not being guilty.
Lionel Hutz: Mr. Mayor, is it true you rigged the election? Sideshow Bob: No, I did not. Lionel Hutz: (Pause) Kids, help.
Lionel Hutz: I'll have you know the contents of that dumpster are private! You stick your nose in, you'll be violating attorney-dumpster confidentiality.
Lionel Hutz: Milhouse baby! Lionel Hutz, your new agent, unauthorized biographer and drug dealer... er keeper awayer.
Lionel Hutz: It's a thorny legal issue, all right. I'll need to refer to the case of Finders vs. Keepers.
Judge: Mr. Hutz we've been in here for four hours. Do you have any evidence at all? Lionel Hutz: Well, Your Honor. We've plenty of hearsay and conjecture. Those are kinds of evidence.
Bailiff: Do you promise to tell the truth the whole truth and nothing but the truth, so help you God? Marge: Mmm... Yes, I do. Lionel Hutz: She sounded like she was taking that awful seriously.
Lionel Hutz: Hutz is the name Mr. Simpson. Lionel Hutz, attorney-at-law. Here's my card. It turns into a sponge when you put it in water.
Bart: Mr. Hutz, when I grow up I want to be a lawyer just like you. Lionel Hutz: Good for you son. If there is one thing America needs, it's more lawyers.
Lionel Hutz: I move for a bad court thingy. Judge: You mean a mistrial. Lionel Hutz: Right! That's why you're the judge and I'm the law-talking guy. Judge: You mean the Lawyer? Lionel Hutz: Right.
Lionel Hutz: Mrs. Simpson, you're in luck. Your sexual harassment suit is exactly what I need to help rebuild my shattered practice. Care to join me in a belt of scotch? Marge: It's 9:30 in the morning. Lionel Hutz: Yeah, but I haven't slept in days.
Lionel Hutz: This is the greatest case of false advertising I've seen since I sued the movie *The Never Ending Story*.
Lionel Hutz: Uh oh, we've drawn Judge Snyder. Marge: Is that bad? Lionel Hutz: Well, he's kind of had it in for me ever since I accidentally ran over his dog. Actually, replace 'accidentally' with 'repeatedly,' and replace 'dog' with 'son.'
Lionel Hutz: That was a right-pretty speech, sir. But I ask you, what is a contract? *Webster's* defines it as 'an agreement under the law, which is unbreakable.' Which is unbreakable!... Excuse me, I must use the restroom.
Marge: I'm sorry, but my mother said, if you can't say anything nice about someone, you shouldn't say anything at all. Homer: (Whispering) Will that hold up in court? Lionel Hutz: No, I've tried it.
Lionel Hutz: Yeah, but what is truth? If you follow me.
Lionel Hutz: Oohhhh, he's gonna win.
Barney: So next time somebody tells you Carney folk are good, honest people, you can spit in their faces for me!
Barney: Hey, better yet, Bart could shoot a deer! That's like shooting a beautiful man.
Barney: You should only drink to enhance your social skills.
Barney: The guys at the AA meeting are not going to believe this.
Barney: Hi Homer! Thanks for inviting me to your barbeque. Homer: Oh, Barney! You brought a whole beer keg! Barney: Yeah. Where can I fill it up?
Barney: These fumes aren't as fun as beer. Sure, I'm all dizzy and nauseous, but where's the inflated sense of self-esteem?
Barney: An election? That's one of those deals where they close the bars isn't it?
Barney: Uh oh, my heart just stopped. Ah... there it goes.
Barney: *David Crosby*? You're my hero! David Crosby: Oh, you like my music? Barney: You're a musician?
Barney: (To Moe) What kind of a drunk do you take me for? (Turns around) Hmm... someone spilt beer into this ashtray! (Drinks beer out of the ashtray)
Barney: Since they stopped testing on animals, a guy like me can really clean up!
Barney: I'm just saying that when we die there's going to be a planet for the French, a planet for the Chinese, and we'll all be a lot happier. Lisa: Mr. Gumble, you're upsetting me. Barney: No, I'm not.
Barney: Jeez, is that what I look like when I'm drunk?
Barney: No it's not okay. I broke barstools, befouled your broom closet, and made sweet love to your pool table, which I then befouled.
Barney: Hey, Homer, I'm worried about the beer supply. After this case, and the other case, there's only one case left.
Barney: 40 dollars? This better be the best damn beer ever... (Drinks beer) You got lucky.
Barney: Uh, oh. I smell something stinky. Oh, it's me.
Bart and Lisa: Good-bye, Shary Bobbins! Marge: Thanks for everything! Barney: So long, *Superman*!
Barney: Jesus must be spinning in his grave!
Barney: Hello, my name is Barney Gumble, and I'm an alcoholic. Lisa: Mr. Gumble, this is a *Girl Scouts* meeting. Barney: Is it, or is it you girls can't admit that you have a problem?
Barney: Ah that's just drunk talk, sweet beautiful drunk talk.
Barney: Next, they're gonna show my movie. Bart: You made a movie? Barney: I made a movie? No wonder I was on the cover of *Entertainment Weekly*.
Barney: I don't know where you pixies came from, but I like your pixie drink.
Barney: Aaah! Natural light!
Carl: Wait a minute, Duff owns the Springfield Isotopes? Since when?
Lenny: Three hours of half-naked guys fighting like animals. Carl: Just like the ancient Romans. Lenny: Yeah, except their empire was falling apart. Carl: Yeah, stupid Romans.
Carl: Oh no! Homer's going over those falls! Lenny: Oh good! He snagged that tree branch. Carl: Oh no! The branch broke off! Lenny: Oh good! He can grab onto them pointy rocks! Carl: Oh no! Them pointy rocks broke his arms and legs. Lenny: Oh good! Those helpful beavers are swimming out to save him! Carl: Oh no! They're biting him, and stealing his pants!
Carl: According to the map, the cabin should be right here. Lenny: Hey, maybe there is no cabin. Maybe it's one of them metaphorical things. Carl: Oh yeah, yeah... Like maybe the cabin is the place inside each of us, created by our goodwill and teamwork. Lenny: Oh! ...Nah, they said there would be sandwiches.
Lenny: You know what's even better is Jesus, he's like six Leprechauns. Carl: Yeah, but he's harder to catch.
Lenny: There's nothing like revenge for getting back at people. Carl: Vengeance isn't too bad either.
Carl: Lenny, sending some outgoing mail? Lenny: You know it! Carl: Yeah, I think I'll send some tomorrow. Lenny: I hear that!
Carl: Lenny and Carl. I kinda like the sound of that!
Lenny: Ohh, that book I ordered is going to be delayed.
Carl: Homer, you don't look fat. Homer: Oh Carl, you're a liar, and I love it.
Carl: What does your fortune say? Lenny: 'You will enjoy the company of others.' Wow, that exactly what I'm enjoying right now. Spooky.
Lenny: Are these business cards or passports to a better future?
Homer: I want everyone to know that this is Ned Flanders... my friend! Lenny: What did he say? Carl: I dunno. Somethin' about being gay.
Carl: This candy is sub par. Any religion that embraces carob is not for Carl Carlson.
Homer: Hey, what does this job pay? Carl: Nothin'. Homer: D'oh! Carl: Unless you're crooked. Homer: WOO-HOO!
Carl: It's all relative. I mean, is Lenny really that dumb, is Barney really that drunk, is Homer really that bald, fat, and lazy? (Lenny, Barney, and Homer look dejected; Carl turns to camera) See, this is why I don't talk much.
Carl: You know I'm sick and tired of people assuming I'm good at basketball just because I'm African American. (Slam Dunks the ball)
Smithers: Now pair off as I draw your names. Lenny... and Carl. Carl: Aw, nuts. Uh... I mean... aw nuts.
Lenny: Late night swimming and alcohol, it's a winning combination!
Lenny: There's something wonderful about being drunk outdoors.
Lenny: Here's to us. The unsupervisables.
Carl: Why don't you do here what you do at the nuclear plant, namely suck...
Carl: Great safety report Homer. No melt-downs all week.
Carl: People who get shot in the chest are such big babies.
Carl: Yeah, you know, those Germans aren't so bad. Lenny: Sure they made mistakes in the past, but hey, that's why pencils have erasers!
Lenny: So then I said to the cop, 'No, you're driving under the influence... of being a jerk.'
Lenny: I say *Phantom Menace* sucked more! Carl: I say *Attack of The Clones* sucked more!
Lenny: I don't get what he's doing, and I'm smart. Not book smart or street smart or brain smart, but... somethin'.
Lenny: The buttons look like they're sewed on, but they're actually held on with hot wax.
Lenny: Carl, can I die before you? I couldn't bare to watch you die. Carl: Alright, but be quick about it!
Milhouse: When a man loves a woman... Lenny: Which one are you, the man or the woman? Carl: Questioning the kid's sexuality, well done! (They fist-pound each other)
Carl: Lets make litter of the literati! Lenny: That was too clever! You're one of them! (Punches him)
Lenny: My eye! I'm not supposed to get pudding in it!
Sideshow Bob: By the way, I'm aware of the irony of appearing on T.V. in order to decry it, so don't bother pointing that out.
Bart and Lisa: AAAGH! SIDESHOW BOB! Sideshow Bob: Oh, we've been through so much together. Please, just call me Bob. Bart and Lisa: AAAGH! BOB!
Sideshow Bob: Hah! Attempted murder? Now honestly, what is that? Do they give a *Nobel Prize* for attempted chemistry? Do they?
Sideshow Bob: Well that settled that argument. You can't read a magazine and drive!
Sideshow Bob: I'll be back. You can't keep the *Democrats* out of the *White House* forever, and when they get in, I'm back on the streets, with all my criminal buddies.
Lawyer: Well, what about that tattoo on your chest? Doesn't it say Die, Bart, Die? Sideshow Bob: No, that's German for 'The Bart, The.' Parole Judge: No one who speaks German can be evil.
Sideshow Bob: You want the truth! You can't handle the truth! No, truth handler you! Bah! I deride your truth handling abilities!
Sideshow Bob: Well, if it isn't my arch-nemesis Bart Simpson. And his sister Lisa to whom I'm fairly indifferent.
Sideshow Bob: Homer, to identify your assailant, I must follow you through the course of a normal day. Just do as you usually do and the killer will reveal himself. Homer: Gotcha. (Cut to Homer and Sideshow Bob hang gliding) Sideshow Bob: This is a 'normal day?' Homer: I... just wanted to impress you.
Chief Wiggum: It's over, Bob. Sideshow Bob: By Lucifer's Beard! Chief Wiggum: Uh, yeah. Cuff him, boys.
Sideshow Bob: Urgh. Rakes, my arch-enemy. Bart: I thought I was your arch-enemy. Sideshow Bob: I have a life outside of you, Bart.
Sideshow Bob: Your guilty conscience may move you to vote *Democratic*, but deep down you long for a cold-hearted *Republican* to lower taxes, brutalize criminals, and rule you like a king.
Sideshow Bob: No children have ever meddled with the *Republican Party* and lived to tell about it.
Barlow: Sideshow Bob, councilman Les Whinen says that you're not experienced enough to be mayor. Sir, what do you have to say about that? Sideshow Bob: I'd say that Les Whinen ought to do more thinking and less whining!
Sideshow Bob: Ah, corn chips. The perfect snack... for revenge!
Sideshow Mel: (Drunk) Every one's always kissing your ass. Well, I'm not afraid to tell you you're a *bleep*.
Sideshow Mel: The crowd is abuzz and agog as the celebrity blimp approaches. And look, here is America's favorite waste of taxpayer dollars: the *Blue Angels*!
Sideshow Mel: I'll miss you, Krusty. So will the other sideshows... Except Sideshow Bob.
Sideshow Mel: Can we move this meeting along? I pay my taxes, I expect my orange drink! (Groundskeeper Willie serves Sideshow Mel orange drink) Sideshow Mel: (Taking a sip) Ambrosia!
Troy McClure: Hi, I'm Troy McClure. You may remember me from such other medical films as 'Mommy, What's On That Man's Face?' and 'Alice Doesn't Live Here Anymore.'
Troy McClure: Welcome to the Knowledgeum, I'm Troy McClure. You may remember me from such automated information kiosks as 'Welcome to Springfield Airport' and 'Where's Nordstrom?' While you're enjoying our Hall of Wonders, your car unfortunately will be subject to repeated break-ins and... (Fades) Homer: What'd he say? What about my car?
Troy McClure: Hi, I'm Troy McClure. You may remember me from such other nature films as 'Earwigs, Ewww' and 'Man vs. Nature: The Road To Victory.'
Troy McClure: Hi. I'm Troy McClure. You might remember me from such public service videos as 'Designated Drivers, the Lifesaving Nerds' and 'Phony Tornado Alarms Reduce Readiness.'
Troy McClure: Hi, I'm Troy McClure. You may remember me from such educational films as 'Two Minus Three Equals Negative Fun' and 'Firecrackers: The Silent Killer.'
Troy McClure: And now the cows are taken to the killing floor. Don't let the name worry you though. It's a actually a grate which allows material to sluice through.
Troy McClure: My good looks paid for that pool, and my talent filled it with water. Hi, I'm Troy McClure, your future uncle. Lisa: Hi. I remember you from such filmstrips as 'Locker Room Towel Fight: the Blinding of Larry Driscoll.' Troy McClure: You know, I was one of the first to speak out against horseplay.
Selma: But... don't you love me? Troy McClure: Sure I do! Like I love *Fresca*. Isn't that enough? The only difference between our marriage and any one else's is we know ours is a sham.
Troy McClure: Hi. I'm Troy McClure. You may remember me from such self help tapes as 'Smoke Yourself Thin' and 'Get Some Confidence, Stupid!'
Troy McClure: Don't kid yourself, Jimmy. If a cow ever got the chance, he'd eat you and everyone you care about!
Troy McClure: Yes, 'The Simpsons' have come a long way since an old drunk made humans out of his rabbit characters to pay off his gambling debts. Who knows what adventures they'll have between now and the time the show becomes unprofitable? I'm Troy McClure, and now leave you with what we all came here to see, hardcore nudity!
Troy McClure: Hi. I'm Troy McClure, you might remember me from such Driver's Ed films as 'Alice's Adventures through the Windshield Glass' and 'The Decapitation of Larry Leadfoot.'
Troy McClure: Hi. I'm Troy McClure, you might remember me from such celebrity funerals as '*Andre The Giant*, We Hardly Knew Ye' and '*Shemp Howard*, Today We Mourn A Stooge.'
Troy McClure: Troy! Mac Parker. Ever hear of *Planet of the Apes*? Troy McClure: Uh... the movie or the planet? Troy McClure: The brand-new multimillion dollar musical. And you are starring... as the human. Troy McClure: It's the part I was born to play, baby!
Troy McClure: Gay? I wish! If I were gay there'd be no problem!
Duffman: (Watering his plants) That brown spot needs some H2O! Oh yeah!
Duffman: Duffman thrusting in the direction of the problem!
Duffman: New feelings brewing inside Duffman... What... would Jesus do?
Duffman: Duffman's pension has been mismanaged... Oh yeah!
Duffman: Are you there God? It's me... Duffman!
Duffman: That's a mug you don't want to chug!
Duffman: Are you ready for some Duff love?
Duffman: Everything going dark, like Duff Stout. The beer that made Ireland famous.
Duffman: Are you ready to get DUFFED?
Titanya: But Duffman, you said if I slept with you I wouldn't have to touch the drunk! Duffman: Duffman... says a lot of things! Oh, yeah!
Duffman: Duffman could use an eye-opener.
Duffman: This Reich will last a thousand beers!
Duffman: Hey Duff lovers! Does anyone in this bar loooove Duff? Carl: Hey, it's Duffman! Lenny: *Newsweek* said you died of liver failure. Duffman: Duffman can never die, only the actors who play him. Oh yeah!
Duffman: Duffman can't breathe! OH NO!
Professor Frink: Pi is exactly 3.
Professor Frink: Oh, well to be honest, the ray only has evil applications. You know my wife will be happy, she's hated this whole death ray thing from day one.
Professor Frink: These unfortunate people here will be instantly killed. This circle, which I am sad to say we are in, will experience a slower, considerably more painful death.
Professor Frink: Brace yourselves gentlemen. According to the gas chromatograph, the secret ingredient is... love? Who's been screwing with this thing?
Professor Frink: Although we can't reach the boy, we can freeze him with liquid nitrogen so that future generations can rescue him.
Professor Frink: You've got to listen to me. Elementary Chaos Theory tells us that all robots will eventually turn against their masters and run amok in an orgy of blood and the kicking and the biting with the metal teeth and the hurting and shoving.
Professor Frink: Man! If this is happening here, I'd hate to think what's happening at Euro Itchy and Scratchy Land. Mm-hey.
Professor Frink: As you can see, I have created a lemon ball so sour it can only be safely contained in a magnetic field. The candy, known as 77X42... Bwei... Where the hell is the candy? Homer: (The candy is in his mouth) I don't know.
Smithers: Oh, Mr. Burns, we'll thaw you out the second they discover the cure for seventeen stab wounds in the back. How we doing, boys? Professor Frink: Well, we're up to fifteen.
Professor Frink: Ha ha wha. Oh, sorry I'm late. There was trouble at the lab with the running and the exploding and the crying when the monkeys stole the glasses off my head. Wh-ha ha.
Professor Frink: Oh no... No no, I felt that. You didn't carry the one you foolish person. Now you'll incur the penalties with the compound interest and the wrath and the truncheons.
Professor Frink: Weh, uh, alright just stay calm Frinky. These babies will be in the stores while he's still grappling with the pickle matrix bhay-gn-flay-vn.
Professor Frink: Right, step away foolish amateurs, just keep back, keep out of it. The role is mine with the acting and the groupies and the 'Luke, Luke, save me' with the lightsabre and the vwing, vwing, vwing.
Professor Frink: Mmm-hai-hey, let's see now, we have the Monsterometer, Flipper-finder, Hoax-a-scope which is important for the looking and finding.
Professor Frink: Stupid machine, oh wait a minute, this isn't the Monsterometer, it's the Frog-Exaggerator Mm-hai.
Lisa: Only one person in a million would find that funny. Professor Frink: Yes, we call that the *Dennis Miller* ratio.
Professor Frink: The compression and expansion of the longitudinal waves cause the erratic oscillation, you can see it there, of the neighboring particles. Little Girl: Eh! Professor Frink: Yes... what is it, what, what is it? Little Girl: Can I play with it? Professor Frink: No you can't play with it. You won't enjoy it on as many levels as I do... Oh, the colors children!
Professor Frink: Unshrink you? Well, that would require some sort of a re-bigulator, which is a concept so ridiculous, it makes me want to laugh out loud and chortle, hmm-hey-ahh, but not at you, O' holiest of gods, with the wrathfulness and vengeance and the blood reign and the hey, hey, hey, it hurts me.
Professor Frink: Aw, for glaven out loud.
Krusty: And now, in the spirit of the season: start shopping. And for every dollar of Krusty merchandise you buy, I will be nice to a sick kid... For legal purposes, sick kids may include hookers with a cold.
Krusty: Don't blame me! It's the *Percadan*. If you ask me, that stuff rots your brain... And now a word from our new sponsor... *Percadan*, OH CRAP!
Krusty: So, have a merry Christmas, a happy Hanukkah, a kwaazy Kwanza, a tip-top Tet, and a solemn, dignified, Ramadan. And now a word from my God, our sponsors!
Krusty: I thought they were due! That game was fixed! The *Globetrotters* used a ladder for Pete's sake! C'mon! He's just holding out the ball, take it!
Krusty: Thirty-five years in show business and already nobody remembers me. Just like what's his name, and whos-its, and you know, that guy, who always wore a shirt.
Maude Flanders: I don't think we're talking about love here, we're talking about S-E-X in front of the C-H-I-L-D-R-E-N! Krusty: (Standing in background) Sex Cauldron? I thought they shut that place down?
Krusty: They drove a dump truck full of money up to my house! I'm not made of stone!
Krusty: Well, since I'm fresh out of options, I guess all that is left is for me to get a show on... ugh... *Fox*. What do you say? Fox Executive: I don't know... Krusty: Oh, come on, you guys are famous for taking chances on crap!
Bart: Krusty, they fed us gruel! They forced us to make wallets for export, and one of the campers was eaten by a bear! Krusty: Oh, my God! Bart: Actually, the bear just ate his hat. Krusty: Was it a nice hat? Bart: Oh yeah. Krusty: Oh, my God!
Krusty: I can pull a better cartoon out of my aaaa-heh-heh-heh...
Krusty: Can't I get a cup of coffee without doing a monkey dance for you freaks?
Krusty: You here for the trampoline? Homer: Yeah. What's the deal? Krusty: Well, I used to do a lot of tumbling in my act, but I'm phasing it out for more dirty limericks. There once was a man named 'Enis'...
Krusty: THIS AIN'T MAKEUP!
Krusty: Mousey and Catsey, aren't they great?
Krusty: A great man once observed that 90% of success is showing up on time. Sorry I'm four hours late.
Krusty: Hey! That's my Madonna gag! That guy stole my gag! Sideshow Mel: And you stole it from last night's episode of 'Pardon My Zinger.' Krusty: Stole, made up, what's the difference?
Krusty: Homer gave me a kidney once. It wasn't his, I didn't need it, and it came with postage due, but it was a lovely gesture.
Krusty: Ya! I'm a senator! Lisa: Congressman. Krusty: Whatever!
Krusty: (On T.V.) YOU PEOPLE ARE PIGS! (Cries) I personally, am going to spit in every fiftieth burger! Homer: I like those odds!
Krusty: Kids, we need to talk for a moment about Krusty Brand Chew Goo Gum Like Substance. We all knew it contained spider eggs, but the hantavirus? That came out of left field. So, if you're experiencing numbness and/or comas, send five dollars to: Antidote, P.O. Box...
Krusty: My house is dirty. Buy me a clean one.
Krusty: Entertain the troops? No way! What have they ever done for me?
Krusty: Oh God, please don't tell me I died on the operating table again.
Krusty: I work like I drink, alone or with a monkey watching me.
Chief Wiggum: (To Krusty) Hey, find your nose funny man. Krusty: There was cocaine in there. I won't last an hour.
Sideshow Bob: (Sideshow Bob wins an Emmy while in prison) This is one more Emmy than you'll ever win, you bantering jack-in-the-box! Krusty: Just don't drop that thing in the shower, Bob!
Krusty: Kill the child!
Krusty: Don't drag your kid into this.
Krusty: Now see here little miss scene stealer, I'm the star of the show. You're just the reason people tune in.
Krusty: Why do clown things always happen to clowns?
Krusty: Girls don't laugh and they don't buy cigars.
Krusty: Rule number one: Never be better then me. ...And I'm pretty bad.
Krusty: Hey, if my writers knew how to appeal to girls they wouldn't be writers.
Guard: Evening Mr. Krusty. Great show last... Krusty: Sorry, I can't act like you matter.
Krusty: Hey *George Washington*! See if you think this is funny!
Krusty: I never thought I would make it past 400 episodes, well with the drinking and the smoking and the fact that I am just not that good.
Krusty: If you can find a greasier sandwich, you're in Mexico!
Bart: Do you think about your father a lot? Krusty: All the time. Except when I'm at the track. Then it's all business.
Nelson: Well, my mom says you're a selfish lover. Krusty: I know what I want and I get it.
Krusty: I'm quitting show business, I just wanted to leave with a little class, you jack ass!
Krusty: Hey, that's my check cashing arm you stupid...
Krusty: I am really, really, sorry for everything I've been charged with... and all the stuff you don't know about yet.
Krusty: Hey, hey if it isn't my old friend... you.
Krusty: I'll perform at your birthday party... sober.
Krusty: There are only two rules in T.V., don't swear and don't whip it out! It's not rocket science!
Krusty: Nicely done kid! You're the best thing that's happened to this business since... Lisa: Mitsy Gainer? Krusty: I was going to say cheap Korean animation, but sure...
Krusty: Hey, hey! Krusty-Brand show T-Shirts are made for kids by kids! And we pass the 'slavings' (Wink) onto you! (Laugh) We got all your favorite characters: Itchy, Scratchy, Poochie, Austin Powers-Itchy, Itchy-Poochie, Scratch-Bob Itch-Pants, Confederate Itchy, and Osama bin Scratchy.
Krusty: Hey, Yutz! Guns aren't toys! They're for family protection, hunting dangerous or delicious animals, and keeping the King of England out of your face!
Krusty: Now for my favorite part of the show... What does that say? Talk to the audience! Ugghhh, this is always death...
Krusty: Ahhh, there's nothing better than a cigarette. Unless it's a cigarette lit with a hundred dollar bill!
Marge: How could you choose that film? Krusty: (Talking about his bribe) Lets say it moved me... to a bigger house! Oh no, I said the loud part quiet and the quiet part loud!
Krusty: I'm sitting here with a smokin' monkey and I don't even know what the hell you are! Sideshow Mel: Oh Krusty, you can be so cruel when you're sober.
Krusty: Are you guys any good at covering up youthful and middle-aged indiscretions? Mr. Burns: Are these indiscretions romantic, financial, or treasonous? Krusty: Russian hooker. You tell me.
Krusty: A joke, ah... oh... ok! A man walks into a bar with a small piano, and a twelve-inch pianist... whooaaa hooaaa... I can't tell that one! Huh huh huh huh huh!
Krusty: Bart, I need your fingerprints on a pair of candlesticks. Meet me in the conservatory chop, chop! Don't worry, everything will be all right...
Sea Captain: Yar, I'm not attractive.
Sea Captain: Arr, that's handsome Pete, he dances for nickels.
Sea Captain: Arr, someone should be keelhauled for that one!
Sea Captain: Arr, sometimes I wonder why I bother plunderin' at all.
Sea Captain: Arr, matee, narry a warning light to be seen. Clear sailin' ahead for our precious cargo. Sailor: Uh, would that be the hot pants, sir? Sea Captain: Aye, the hot pants.
Mr. Burns: One last question, have you ever seen the sun set... at 3 p.m.? Sea Captain: Aye, once, when I was sailin' 'round the Arctic. Mr. Burns: Shut up, you!
Sea Captain: I am the sailing instruct-arrrrr. And on movie night, I run the project-arrrrr. Only PG, nothin' Rrrrrr. Yarrrr.
Sea Captain: Yarr, it's kind of you to deliver these copies of 'Jugs.' They'll keep my men from resorting to homosexuality... fer about 10 minutes. Harr, Harr, Harr. Sailor: You should talk! Sea Captain: Yarr.
Sea Captain: Yarr, not a looker among 'em.
Sea Captain: (Reads a fortune cookie) 'You will take a short sea voyage.' Yarr, I'll enjoy that.
Sea Captain: Aye, 'tis a sugary brine.
Sea Captain: Eh, you know I run a small academy for lobsters like this one. We stress tough love, daily chores, and the like.
Sea Captain: Arr, ye call that an anchor?
Sea Captain: Arr, Squiddy, I got nothin' against ya. I just heard there was gold in yer belly. Ha ha Harr, Harr Harr.
Sea Captain: Arr, you're truly the catch of the day.
Ned Flanders: Well, I guess it's just you and me, Sea Captain. Sea Captain: Are you coming on to me? 'Cause I don't do that... on land.
Comic Book Guy: The Internet King? I wonder if he could provide faster nudity...
Comic Book Guy: Oh, a sarcasm detector. Oh, that's a REALLY useful invention!
Comic Book Guy: *Stan Lee* never left. I'm afraid his mind is no longer in mint condition.
Comic Book Guy: I've spent my entire life doing nothing but collecting comic books... and now there's only time to say... LIFE WELL SPENT!
Comic Book Guy: And the cost of your innocent accident is... twenty-five dollars, please! Milhouse: But that's the money Aunt Sophia gave me for Greek Orthodox Easter... Comic Book Guy: I hate when they tell me things about themselves.
Comic Book Guy: That is a rare photo of *Sean Connery* signed by *Roger Moore*.
Comic Book Guy: These 'Bat Pants' have been shredded by the *Riddler*. Dry Cleaner Clerk: No, just your ass. Comic Book Guy: That's what I call my ass.
Milhouse: Why does Bart have a comic book? Comic Book Guy: Your questions have become more redundant and annoying then the last three *Highlander* movies.
Comic Book Guy: (Eating *Peeps*) If only the real chicks went down this easy.
Comic Book Guy: Inspired by the most logical race in the galaxy, the Vulcans, breeding will be permitted once every seven years. For many of you this will mean much less breeding, for me, much much more.
Comic Book Guy: Now make like my pants and split!
Comic Book Guy: Welcome to Shaolin Kung Fu. 10,000 years of knowledge of will be passed on to those whose parents signed a permission slip. The rest of you have just purchased very expensive pajamas.
Comic Book Guy: Last night's Itchy and Scratchy was, without a doubt, the worst episode ever. Rest assured that I was on the Internet within minutes, registering my disgust throughout the world.
Comic Book Guy: Very well. I must get back to my comic book store, where I dispense the insults rather than receive them.
Comic Book Guy: Ack. There is no emoticon to express what I am feeling right now.
Comic Book Guy: Oh, loneliness and cheeseburgers are a dangerous mix.
Comic Book Guy: Quit butting in please. Your I.Q. is a mere 155 while mine is a muscular 170.
Marge: Thanks for coming over. Comic Book Guy: (Happily) Thanks for giving me your pregnancy pants... I've never known comfort like this.
Comic Book Guy: Human Contact: the final frontier.
Comic Book Guy: Hey, Nostra-dumbass, did the Rapture come? I can't recall. In fact, I can recall, and it didn't, and you suck.
Comic Book Guy: No groaning in my store.
Comic Book Guy: Traitor! Your heart is blacker than your turtle neck.
Bart: Ok, here's my offer. All this primo Krusty merchandise for that copy of Radioactive Man vs. *Muhammad Ali*. Comic Book Guy: My counter offer, Radioactive Man meets the *Kansas City Royals*. Bart: How about Radioactive Man vs. restless leg syndrome?
Marge: Should the Simpsons get a horse? Comic Book Guy: Excuse me, I believe this family already had a horse, and the expense forced Homer to work at the Kwik-E-Mart with hilarious consequences. (Pause) Homer: Does anyone care what this guy thinks? Crowd: No!
Comic Book Guy: Behold, the ultimate *Pog*.
Comic Book Guy: *Richard Dean Anderson*, of the four 'Star' franchises: Wars, Trek, Gate, and Search, 'Gate' is easily in my top three! Richard Dean Anderson: I get that a lot.
Comic Book Guy: If you are waiting for the *Hi and Lois* signing, you are too late. It has been moved to the Springfield Colosseum.
Comic Book Guy: No banging your head on the display case please, it contains a very rare Mary Worth in which she has advised a friend to commit suicide. Thank you.
Comic Book Guy: Yes, this should provide adequate sustenance for the *Dr. Who* marathon.
Comic Book Guy: Question, is your name *Ridley Scott* or *James Cameron*? Homer: No, it's Homer. Comic Book Guy: Then I would thank you to stop peering at my screenplay, 'Homer.' And if I see a movie where computers threaten our personal liberties, I will know you have stolen my idea. Homer: But I'm just waiting for my kid. (Thinking) Mental note: steal his idea.
Comic Book Guy: Are you the creator of *Hi and Lois* because you are making me laugh.
Comic Book Guy: Ooh, your powers of deduction are exceptional. I can't allow you to waste them here when there are so many crimes going unsolved at this very moment. Go, go, for the good of the city.
Comic Book Guy: Worst 'Cosmic Wars' ever!
Comic Book Guy: I played hardball with Hollywood. The closest I will ever come to playing a sport in my life.
Comic Book Guy: But *Aquaman*, you cannot marry a woman without gills, you're from two different worlds.
Comic Book Guy: Lace: The Final Brassiere.
Comic Book Guy: *Superman* I have believed in you for years. If you can here me now please come help me dig this giant grave!
Comic Book Guy: I'm interested in upgrading my twenty eight point eight kilo-baud internet connection to a one point five megabit fiber-optic T-1 line. Will you be able to provide an IP router that's compatible with my token ring Ethernet LAN configuration? Homer: Can I have some money now?
Comic Book Guy: Ooh, once again my underwear has become tangled in a cow-catcher.
Comic Book Guy: Come back! Those are prescription pants!
Comic Book Guy: Stop right there! I have the only working phaser ever built. It was fired only once to keep *William Shatner* from making another album.
Lisa: May I have that seat? Comic Book Guy: Yes! If you can answer me these questions three. Question the first!... Lisa: Never mind.
Comic Book Guy: Oh, is there a Klingon word for loneliness. (Looks in dictionary) Ah yes, galdak.
Comic Book Guy: Nooo, it's no longer a collectible!
Comic Book Guy: Ahhh, Ohhh, customers, how I hate them.
Comic Book Guy: *Stan Lee* insulted me! But in *Bizzaro World*, that means he likes me!
Comic Book Guy: You'd think that would deter me, but no!
Comic Book Guy: Shortness of breath, left arm and chest pains, can't go on describing symptoms much longer...
Comic Book Guy: Are you kidding me five dollars? This is radioactive man comic number 1000, and look, if you poor food on it, it bounces off onto lesser comics.
Comic Book Guy: Egad, a maniac cutting a swath of destruction! This is a job for the *Green Lantern*, *Thundra*, or possibly... *Ghost Writer*.
Comic Book Guy: With great hunger comes great responsibility.
Comic Book Guy: Would you be jolly if *Comic-Con* was moving to Anaheim?
Comic Book Guy: I still wear your bra.
Groundskeeper Willie: You maniacs! You blew it up! God damn ya! God damn ya to hell! Comic Book Guy: Hey, less references, more mopping.
Groundskeeper Willie: Sounds like that gopher I caught in me lawn mower...
Groundskeeper Willie: Me bleachers have been weaponized.
Principal Skinner: Well, William, I'm back! So...how did you spend your summer? Groundskeeper Willie: I made millions in software and lost it at the track. Ach!
Groundskeeper Willie: Make way for Willie!
Groundskeeper Willie: Oh Lord, let me finish this hallway so you can send me to hell a happy man.
Groundskeeper Willie: You bath-takin' underpants-wearin' lily-hugger!
Bart: This place smells, and something's dripping from the ceiling. Groundskeeper Willie: The smell is manure and the dripping is manure.
Marge: Now, how are we going to get my Homey back? Groundskeeper Willie: I'll kidnap him for fifty, deprogram him for a hundred, and kill him for five hundred. Marge: No, no. Just the first two. Groundskeeper Willie: Alright. I'll throw in the killin' for free.
Groundskeeper Willie: There's nary an animal alive that can outrun a greased Scotsman.
Groundskeeper Willie: Yup. I bought your mutt. And I 'ate him! I 'ate his little face. I 'ate his guts! And I 'ate the way he's always barking! So I gave him to the church! Bart: Oh, I see. You hated him so you gave him to the church. Groundskeeper Willie: Right. And one more thing, I also 'ate the mess he left on me rug... Ya heard me!
Groundskeeper Willie: Now, the kilt was only for day-to-day wear. In battle, we donned a full-length gown covered in sequins.
Groundskeeper Willie: I warned ya about the colored chalk, didn't I warn ya? That chalk was forged by Lucifer himself!
Groundskeeper Willie: It won't last. Brothers and sisters are natural enemies. Like Englishmen and Scots! Or Welshmen and Scots! Or Japanese and Scots! Or Scots and other Scots! Damn Scots! They ruined Scotland!
Groundskeeper Willie: All right Skinner, that's the last time you'll slap your Willie around.
Groundskeeper Willie: If it was up to me, I'd let you go, but the gods have a temper, and they've been drinking all day.
Groundskeeper Willie: I lost all me 'screw you' money. Principal Skinner: I'm sorry, Willie. Groundskeeper Willie: Screw you!
Groundskeeper Willie: Bonjoooouur, ya cheese-eatin' surrender monkeys!
Groundskeeper Willie: Just say the word, and I'll bury this hoe in his back. I can make it look like suicide.
Kent Brockman: The results are in: for Sideshow Bob, one hundred percent; and for Joe Quimby, one percent. And we remind you there is a one percent margin of error.
Kent Brockman: Top O' the mornin' to ye on this gray, drizzly afternoon. Kent O' Brockman live on Main Street, where today, everyone is a little bit Irish! Eh-heh, everyone except, of course, for the Gays and Italians.
Kent Brockman: I'm Kent Brockman, on the eleven o'clock news tonight... a certain type of soft drink has been found to be lethal, we won't tell you which one until after sports and the weather with Sonny Storm.
Kent Brockman: Tonight a city weeps, as for the first time ever, a hockey arena becomes the scene of violence following a concert by *Spinal Tap*.
Kent Brockman: Good morning everybody, panic is gripping Springfield as giant advertising mascots rampage through the city. Perhaps it's just part of some daring new ad campaign, but what new product could justify such carnage?
Kent Brockman: Just miles from your doorstep, hundreds of men are given weapons and trained to kill. The government calls it the *Army*, but a more alarmist name would be... The Killbot Factory.
Kent Brockman: Down here at Springfield Mall, a storm-addled crowd seems to have turned its rage on the Leftorium. Surprisingly, people are grabbing things with both hands, suggesting it's not just southpaws in this rampaging mob.
Kent Brockman: Ladies and gentlemen, I've been to Vietnam, Iraq, and Afghanistan, and I can say without hyperbole that this is a million times worse than all of them put together.
Kent Brockman: The government just issued an *Orange Alert*, which again means... nothing.
Kent Brockman: America has a tradition of turning outlaws into legends after their deaths. *Billie the Kid*, *Bonnie and Clyde*, Jesus Christ, now joining them is Sideshow Bob.
Kent Brockman: ...and the elephant who couldn't stop laughing was put to death.
Kent Brockman: Eenie meenie miney Moe: Is Homer a hero? The answer is... 'No.'
Kent Brockman: Forget it! We'll do this next week. Camera Man: But the eclipse is today. Kent Brockman: There's an eclipse when I SAY there's an eclipse.
Kent Brockman: A solar eclipse is like a woman breast feeding in a restaurant. It's free. It's beautiful. But under no circumstances should you look at it.
Kent Brockman: Authorities say the phony pope can be recognized by his high-top sneakers, and incredibly foul mouth.
Kent Brockman: I am not chipping in on a birthday cake for that jackass Arnie Pie, let him eat... This is Kent Brockman, live at...
Kent Brockman: Things aren't as happy as they used to be down here at the unemployment office. Joblessness is no longer just for philosophy majors. Useful people are starting to feel the pinch.
Kent Brockman: Hello, I'm Kent Brockman, and welcome to another edition of 'Smartline.' Are cartoons too violent for children? Most people would say 'No. Of course not. What kind of stupid question is that?' But one woman says 'yes'... Marge Simpson.
Kent Brockman: This is Kent Brockman with a special live report from the headquarters of Krusty opponent John Armstrong. How can I prove we're live?... Penis!
Kent Brockman: ...and that fluffy kitten played with that ball of string, all through the night. And on a lighter note, a Kwik-E-Mart clerk was brutally murdered...
Kent Brockman: Professor, without knowing precisely what the danger is, would you say it's time for our viewers to crack each other's heads open and feast on the goo inside? Professor: Yes I would Kent.
Kent Brockman: And in environmental news, scientists have announced that Springfield's air is now only dangerous to children and the elderly.
Kent Brockman: A new mood is in the air in Springfield, a refreshing as a pre-moistened towelette. Folks are finally accepting their feelings, and really communicating with no holding back, and this reporter thinks it's about f***ing time.
Kent Brockman: So, whether you're Christian or just non-Jewish, everybody loves Santa Claus!
Kent Brockman: I'm here at Springfield Elementary where this morning the three R's stand for rowdiness, ransacking, and eeeeResponsibility.
Kent Brockman: I've said it before, and I'll say it again. Democracy simply doesn't work.
Kent Brockman: Now at the risk of being unpopular this reporter places the blame for all of this squarely on you, the viewers.
Kent Brockman: Lock your doors, bar your windows, because the next advertisement you see could destroy your house and eat your family.
Kent Brockman: Thousands of people are gunned down each day in Springfield, but until now, none of them where important.
Kent Brockman: Call the weekend guy, I don't care.
Kent Brockman: The cure, take two tickets and see the game on Sunday morning... Warning tickets should not be taken internally.
Kent Brockman: Yeah, I know I'm on. But I don't care. I don't read the news until I get my danish. Go ahead, try to find a replacement.
Kent Brockman: Ladies and gentlemen, uh, we've just lost the picture, but what we've seen speaks for itself. The Corvair spacecraft has apparently been taken over, 'conquered' if you will, by a master race of giant space ants. It's difficult to tell from this vantage point whether they will consume the captive Earthman or merely enslave them. One thing is for certain, there is no stopping them. The ants will soon be here. And I, for one, welcome our new insect overlords. I'd like to remind them as a trusted T.V. personality, I can be helpful in rounding up others to toil in their underground sugar caves.
Kent Brockman: I guess you can call him the little turtle who couldn't! Check our website for recipes.
Kent Brockman: Coming up next, can yodeling cure cancer? Of course not.
Kent Brockman: Tragic news tonight, 120 dead in a tidal wave in Kuala Lala, pure. Kuala Lum, per... (Crosses it out) France!
Kent Brockman: This just in, I'm pissed off!
Kent Brockman: This just in, go to hell!
Kent Brockman: ...and as you can guess, this barely qualifies as news.
Cletus: (On a telephone pole) Hey, you know what? I could call my Ma while I'm up here. Hey, Ma! Get off the danged roof!
Cletus: Hot damn! No more sitting in the dirt at the drive-in.
Cletus: Hey, slow down I wants to talk to ya! Give us 300 pretzels! Marge: (Talking to Homer) You see, a little persistence and patience, paid off. That'll be $300! Cletus: I don't think so, you see I got 300 coupons. Marge: Hmmm, I should of set limit one per customer. Cletus: Shoulda, but didn't. Ok, now hand them over! (Turning to the house) HEY KIDS! WE EATIN DINNER TONIGHT! C'MON! Tiffany, Heather, Cody, Dillan, Dermit, Jordan, Tailor, Brittney, Wesley, Rumor, Skyle, Cassidy, Zoe, Cloe, Max, Hunter, Kendel, Katelyn, Noah, Sasha, Morgan, Kira, Ean, Lauren, Kubert, Phil!
Cletus: Well, I'm here to win back Brandine. She been making eyes at that photographer what come to document our squaller.
Cletus: He really speaks to me, the average Joe six-tooth. Brandine: When did you get another tooth? Cletus: The sidewalk.
Cletus: Stranger, you're trespassing on my dirt farm.
Brandine: (To Cletus) You are the most wonderful husband and son... I ever had.
Brandine: Now Cletus, why did ya haf to park next to my parents? Cletus: Now, Now, Hun, they're my parents too...
Cletus: Someone done stoled my wheels.
Cletus: (At the car wash) All right youngens, bath time. Cover up your eyes and drop your britches! Who wants wax?
Gravedigger: Dang Blasted! Isn't anybody in this dad-gummed cemetery dead? Hans Moleman: (Popping out of a coffin) I didn't want to make a fuss, but now that you mention it...
Lisa: You love Moleman! You're gay for Moleman! Bart: No, you're gay for Moleman. Hans Moleman: (Morosely) No one's gay for Moleman.
Hans Moleman: The eating of an orange is a lot like a good marriage.
College Girl: She's worse than that 80 year old who pretended to be a freshman. Hans Moleman: I just wanted a place to sit down.
Hans Moleman: My doctor never told me that. I had to hear it from *Phish*.
Dr. Hibbert: Cancel all my appointments. Hans Moleman: But I need that kidney now!
Hans Moleman: I was saying Boo-urns.
Hans Moleman: Lesbian? This isn't my *Army* reunion. Gay man in Army clothes: You're coming home with me. Hans Moleman: Yes, Colonel.
Hans Moleman: You cost me five minutes of my life and I want them back! Apu: I am sorry, sir. Hans Moleman: Never mind, I would have just wasted them anyway.
Hans Moleman: You call that a knife? THIS is a knife! ...oooohh, down I go.
Hans Moleman: Are you really allowed to execute people in a local jail?
Hans Moleman: A poem by Hans Moleman: I think that I shall never see, my cataracts are blinding me.
Hans Moleman: Today, part four of our series of the agonizing pain in which I live every day.
Disco Stu: Disco Stu has ouzo for two-zo. Bart: I'll leave you guys alone. Disco Stu: Disco Stu was talking to you.
Disco Stu: Hey, Disco Stu doesn't advertise.
Disco Stu: ...so does Stu. Edit that so it rhymes with something.
Disco Stu: Disco Stu got addicted to the white stuff in the seventies. (Holding a bag of sugar)
Disco Stu: Disco Stu can still boogaloo.
Disco Stu: Did you know that disco record sales were up 400% for the year ending 1976? If these trends continues... AAY!
Disco Stu: The South will boogie again!
Disco Stu: Disco Stu just got an annulment from John Paul II. Boogie down!
Disco Stu: Back away, not today, disco laday!
Disco Stu: Disco Stu likes disco music.
Disco Stu: I hate disco, its all I've talked about so long, people think I'm a one note guy! (Gasp!) Its just getting harder, you know?
Disco Stu: Disco Stu should have disco ducked.
President Schwarzenegger: I'm was elected to LEAD, not to READ.
Rainier Wolfcastle: I would cry like a baby that was just hit by a hammer!
Rainier Wolfcastle: Remember when I said I would eat you last? I lied.
Rainier Wolfcastle: The entire movie is two hours of me standing in front of a brick wall. It cost 80 million dollars. Jay Sherman: How do you sleep at night? Rainier Wolfcastle: On top of a big pile of money, with many beautiful ladies.
Woman: Well, you certainly broke up that meeting. Rainier Wolfcastle: Right now I'm thinking about holding another meeting... in bed.
Jay Sherman: Your shoes are untied. Rainier Wolfcastle: From here they appear to be tied, but I shall go in for a closer inspection... On further inspection, these are loafers.
Rainier Wolfcastle: I have purchased the Springfield YMCA. I plan to tear it down and turn the land into a nature preserve. There, I will hunt the deadliest game of all... Man.
Rainier Wolfcastle: Have you ever noticed how men leave the toilet seat up? That's the joke.
Rainier Wolfcastle: Here's my impression of *Woody Allen*. (Doesn't change his voice at all) 'I'm a neurotic little nerd who likes to sleep with little girls.'
Rainier Wolfcastle: I would cry if my tear ducts weren't so muscular.
Rainier Wolfcastle: Laughing time is ovah.
Rainier Wolfcastle: Leave me a message after the beep... BUT DON'T BE A MESSAGE HOG USING UP ALL MY TAPE!
Rainier Wolfcastle: Let my muscles hug you.
Rainier Wolfcastle: MENDOZA!
Rainier Wolfcastle: Maria, my mighty heart is breaking. I'll be in the Humvee.
Rainier Wolfcastle: McBain to base! Under attack by Commie-Nazis!
Rainier Wolfcastle: My eyes! The goggles do nothing!
Rainier Wolfcastle: My *Ferrari*! I had to do awful things to pay for her.
Rainier Wolfcastle: My libido has been terminated.
Rainier Wolfcastle: My new film is a mixture of action and comedy. It's called 'McBain: Let's Get Silly.'
Rainier Wolfcastle: That's some outfit, Skoey. It makes you look like a homosexual. (Audience boos) Well, maybe you all are homosexuals, too.
Rainier Wolfcastle: Up and at-dem!
Fat Tony: Then it's decided. Our website name will be 'crime.org.'
Fat Tony: I haven't cried this much since I paid to see *Godfather III*.
Fat Tony: Welcome to my house. And to answer your first question... Yes, we do have pasta.
Fat Tony: That bird just touched my car. You know what to do.
Lenny: Is that Wacky Tobacky? Fat Tony: The wackiest.
Mayor Quimby: With prohibition repealed, how long will it take you to flood this town with alcohol again? Homer: Sorry, but I'm not in that business anymore! Fat Tony: (To Mayor) Four minutes.
Fat Tony: You are not a pet. You are not a friend. You are nothing to me.
Fat Tony: Johnny Tightlips, can you see the shooter? Johnny Tightlips: I see a lot of things. Fat Tony: You know, you could be a little more helpful!
Fat Tony: Gentlemen, remove your guns from your holsters. Louie: Shoulder or ankle? Fat Tony: Surprise me.
Snake: (After robbing Moe) Goodbye, student loan payments!
Snake: I told the guard I was going out for a pack of cigarettes, but then I like totally stabbed him.
Snake: Nice try, but no donut, cops!
Ned Flanders: Young man what would you mother say if she knew you were shooting nice people in the brain? Snake: She'd say that year off from *Princeton* was the worst decision I ever made.
Homer: Will you duel or are you a coward? Snake: Would a coward do this... BYE! (Runs off)
Snake: Ho, dude, you did NOT smile. We eat for free. Come on, Shoshanna, let's roll. Moe: But I sang you the potato stuffings. Come on! I sang you the potato stuffings.
Snake: Get off my lawn, coppers! Or I'll totally turn the sprinklers on!
Snake: Hey, baby, listen carefully. Someone's been editing my biography on *Wikipedia*. I want you to kill him.
Snake: I'm gonna win you back even if I have to pistol whip this guy all night.
Snake: You're looking good, baby. Why did we ever break up? Gloria: You pushed me out of a moving car! Snake: The cops were chasing us. I needed to lighten the load, and, um... protect you. Ha ha.
Snake: If they're smart, Kent, they'll stay off the main roads. It's all here in my book, 'Ten Habits Of Highly Successful Criminals.'
Snake: Tell them I'll be on *Conan* Thursday with *Heather Locklear* and *Third Eye Blind*.
Jebediah Springfield: Who will come and live a life devoted to chastity, abstinence, and a flavorless mush I call rootmarm?
Jebediah Springfield: Spirituous beverages are hereby prohibited in Springfield under penalty of catapult.
Jebediah Springfield: I did not tame the legendary buffalo. It was already tame, I merely shot it.
Jebediah Springfield: I was, what are you talking about, Shelbyville? Why would we want to marry our cousins? Shelbyville: Because they're so attractive. I, I thought that was the whole point of this journey.
Jebediah Springfield: People, our search is over! On this site we shall build a new town where we can worship freely, govern justly, and grow vast fields of hemp for making rope and blankets.
Chairman: Dr. Nick, this malpractice committee has received a few complaints against you. Of the 160 gravest charges, the most troubling are performing major operations with a knife and fork from a seafood restaurant. Dr. Nick: But I cleaned them with my napkin.
Dr. Nick: I will perform any operation for the low, low price of $129.95!
Dr. Nick: Call 1-800-DOCTORB! The 'B' is for bargain!
Mr. McCraig: Dr. Nick Riviera! Remember me? Dr. Nick: Well, if it isn't my old friend Mr. McCraig, with a leg for an arm, and an arm for a leg!
Dr. Nick: Eww... blood!
Dr. Nick: You've tried the best, now try the rest!
Dr. Nick: Don't worry, you won't feel a thing... until I jam this down your throat!
Dr. Nick: The coroner? Ohh, I am so sick of that guy!
Dr. Nick: Such a nice day, I think I'll go out the window!
Dr. Nick: (Looking at a human body book) That's how we look inside? It's DISGUSTING! (Turns a page) Oh, that woman swallowed a baby.
Dr. Nick: The most rewarding part was when he gave me my money.
Dr. Nick: (Flashback to the 70's) Seriously, baby, I can prescribe anything I want.
Dr. Nick: (As Homer is falling asleep for surgery) What the hell is that?
Dr. Nick: (Singing) The knee bone's connected to the... something. The something's connected to the... red thing. The red thing's connected to my wristwatch... Uh ohh...
Dr. Nick: Hi everybody!
Dr. Nick: Inflammable means flammable? What a country!
Smithers: Sir, there may be never be another time to say... I love you, sir. Mr. Burns: Oh, hot dog. Thank you for making my last few moment on Earth socially awkward.
Smithers: (After hauling Homer away) Careful, men. He wets his pants.
Mr. Burns: All I wanted was to destroy our delicate ecosystem and this is the thanks I get. Smithers: I'm sorry sir, want me to have some goons rough up *Al Gore*? Mr. Burns: I'd like that.
Mr. Burns: Smithers, I've been thinking. Is it wrong to cheat to win a million-dollar bet? Smithers: Yes, sir. Mr. Burns: Let me rephrase that. Is it wrong if I cheat to win a million-dollar bet? Smithers: No, sir. Who would you like killed?
Mr. Burns: No one will want to kiss me after this, eh, Smithers? Smithers: Well, it's their loss, sir.
Mr. Burns: The watchdog of public safety, is there any lower form of life? Smithers: Don't worry sir, I rounded up our less gifted employees and led them into the basement.
Smithers: Don't let me off the hook that easily sir. I failed you and I'll never forgive myself. Never never never never.
Smithers: I've got to find a replacement that won't outshine me. Perhaps if I search the employee evaluations for the word 'incompetent.' Seven hundred fourteen names! Huh, better be more specific. Lazy, clumsy, dimwitted, and monstrously ugly. (714 matches on computer screen) Ah nuts to this, I'll just go get Homer Simpson.
Homer: Mr. Smithers, I don't understand 2700 of my new duties. Smithers: Well, the van's leaving... pick one duty that's going to give you the most trouble. Homer: Umm... what do I do incase of a fire? Smithers: Sorry, can't hear you, bye!
Mr. Burns: Nonsense! Dogs are idiots! Think about it, Smithers. If I came into your house and started sniffing at your crotch and slobbering all over you, what would you say? Smithers: If you did it, sir?
Mr. Burns: Smithers, do you think you could dig up *Al Jolson*? Smithers: Ummm... remember we tried that, sir? Mr. Burns: Oh right, he's dead... and rather pungent. The rest of that night is something I'd like to forget.
Mr. Burns: Smithers there's a rocket in my pocket. Smithers: You don't have to tell me sir.
Crowd: BOOOOOO! Mr. Burns: are they... booing me Smithers? Smithers: Uhh, no sir... they're saying boo-urns! boo-urns!
Smithers: I'm allergic to bee stings. They cause me to, uh, die.
Smithers: In the next few weeks were going to introduce a medical plan that covers illness.
Lunch Lady Doris: More testicles means more iron.
Lunch Lady Doris: There's very little meat in these gym mats.
Miss Hoover: I fail to see the educational value of this assembly. Mrs. Krabappel: Ah, it will be one of their few pleasant memories when they're pumping gas for a living.
Mrs. Krabappel: All right, children, it's book report time. We'll go in alphabetical order. Today will be A-M. Bart: Saved! I love being a S-S-S-S-Simpson! Mrs. Krabappel: Let's see, we have no A's. So we'll go right to the B's. Bart? Bart: Huh? Mrs. Krabappel: Ha!
Mrs. Krabappel: Seymour, the children are playing in the hole again.
Mrs. Krabappel: I'm a teacher in a bathroom with a student. That's why most of these people are here in the first place.
Mrs. Krabappel: Class, in order to explain why your hormones will soon make you an easy target for every smooth-talking Lothario with his own car and tight jeans, I will now show a short sex education film. Ezekiel and Ishmael, in accordance with your parents' wishes, you may step out into the hall and pray for our souls.
Samantha: How will we know when we fall in love? Mrs. Krabappel: Oh, don't worry children. Most of you will never fall in love, but will marry out of fear of dying alone!
Ned Flanders: Well, I guess this is a case where we'll have to agree to disagree. Principal Skinner: I don't agree to that. Mrs. Krabappel: Neither do I.
Mrs. Krabappel: Bart Simpson, will you stop putting your hand up! You haven't had one right answer all day!
Bart: My father invented that drink, and if you'll allow me to demonstrate... Mrs. Krabappel: Bart, are those liquor bottles? Bart: I brought enough for everybody! Mrs. Krabappel: Take those to the teacher's lounge. You can have what's left at the end of the day.
Bart: (After Bart has lost the election) I demand a recount! Mrs. Krabappel: (Counts the votes gleefully) One for Martin. Two for Martin. Would you like another recount? Bart: No. Mrs. Krabappel: (Rubbing it in) Well, I just want to make sure. One for Martin. Two for Martin. (Laughs)
Mrs. Krabappel: (Blows whistle) Now class remember, I don't want this field trip to be a repeat of our infamous visit to the Springfield State Prison. So I want all to be on your best behavior, especially you Bart Simpson. Bart: Mrs. Krabappel, I didn't unlock that door.
Mrs. Krabappel: Now, I don't want you to worry, class. These tests will have no effect on your grades. They merely determine your future social status and financial success... if any.
Otto: (About Springfield Gorge) Hey, this thing's pretty gnarly. I bet you could throw a dead body in there, and no one would eeeeever find it. Bart: Otto, I'm going to leap over Springfield Gorge on my skateboard. Otto: You know, Bart, as the only adult here, I feel I should say something... Bart: What? Otto: Cooool!
Otto: (Studying for a driver test) 'Alcohol increases your ability to drive.' (Flips pages of his book for the answer) False! Oh, man!
Bart: (Bart tries to encourage Otto to take his driver's test) You can do it, Otto. You're the coolest adult I've ever met. Otto: Wow! I've never been called an adult before. I've been tried as one, but...
Patty: (Otto is at the DMV for the first time) My name's Patty, and I'll be testing you. When you do good, I use the green pen. When you do bad, I use the red pen. Any questions? Otto: Yeah, one. Have you always been a chick? I-I-I mean, I don't want to offend you, but you were born a man, weren't you? You can tell me. I'm open-minded. Patty: I won't be needing this (Drops the green pen)
Otto: (Staring at hands) They call them fingers but I never see them fing. (Pauses) Oh there they go...
Otto: Why is there a steering wheel in my bedroom?
Otto: 'Shemp' is 'hemp' spelled backwards! Homer: Ha Ha! ...And 'Otto' is 'Otto' spelled backwards! Otto: Oh, now I'm scared...
Principal Skinner: (Otto is spanking Bart) Are you handing out corporal punishment to that child? Otto: Can't stop now. Spanking kid. Principal Skinner: (Grabbing Otto's hand) You are suspended from bus driving. With pay. Otto: NOOOOOO!
Jimbo: You let me down, man! Now I don't believe in nothin' no more! I'm going to law school. Homer: NOOOOOOOOO!
Jimbo: I heard that guy's ass has its own Congressman!
Dolph: Oh, man! You kissed a girl! Jimbo: That is so gay!
Martin: Finally, my plan has come to fruition. Soon I'll be queen of summertime. Uh... King! King!
Principal Skinner: Hmm. Whoever did this is in very deep trouble! Martin: And a sloppy speller, too. The preferred spelling of wiener is W-I-E-N-E-R, although E-I is an acceptable ethnic variant. Principal Skinner: Good point.
Frank Ormand: You know, you sound like me. The old me. Which was, ironically, the young me!
Steven Tyler: Hello, St. Louis! Joe Perry: That's Springfield, Steven. Steven Tyler: Yeah, right, right.
Neil Armstrong: This is one small step to firing your ass!
Chris Martin: So, where are you from Homer? Homer: Here.
Bob Dole: Maybe *Bob Dole* should run. *Bob Dole* thinks *Bob Dole* should run. Actually *Bob Dole* just likes hearing *Bob Dole* talk about *Bob Dole*. *Bob Dole*!
Oscar the Grouch: Give us the money! Elmo: Elmo knows where you live!
George HW Bush: If he thinks *George Bush* won't go into the sewer, well then he doesn't know *George Bush*.
Richard Dean Anderson: You're into *MacGyver*? That show was so stupid! 'Oh, I'm *MacGyver*! I can make a bomb out of a banana peel and a toaster!'
Tom Hanks: Hello, I'm *Tom Hanks*. The U.S. Government has lost its credibility, so it's borrowing some of mine...
Ed Begley Jr.: I prefer a vehicle that doesn't hurt Mother Earth. It's a go-cart, powered by my own sense of self-satisfaction.
Homer: (Reading 'Internet for Dummies: Remedial Edition') Oh, they have the Internet on computers now. Marge: Homer, *Bill Gates* is here. Homer: *Bill Gates*? Billionaire computer nerd *Bill Gates*? Oh, my God. Oh, my God. Get out of sight, Marge. I don't want this to look like a two-bit operation. Bill Gates: Mr. Simpson? Homer: You don't look so rich. Bill Gates: Don't let the haircut fool you. I'm exceedingly wealthy. Homer: (Sotto voice) Get a load of the bowl job, Marge. Bill Gates: Your Internet ad was brought to my attention but I can't figure out what, if anything, CompuGlobalHyperMegaNet does. So, rather than risk competing with you, I've decided simply to buy you out. Homer: (Softly) This is it, Marge. I poured my heart and soul into this business and now it's finally paying off. We're rich! Richer than astronauts! Marge: (Softly) Homer, quiet! You'll queer the deal. Homer: Oh, right. (Out loud) I reluctantly accept your proposal. Bill Gates: Well, everyone always does. Buy him out, boys. (Assistants begin breaking things on Homer's dining table-turned-office) Homer: Hey, what the hell's going on? Bill Gates: Oh, I didn't get rich by writing checks. (Cackles loudly)
Ringo Starr: Look fellas! It's Lisa in the sky.John Lennon: No diamonds, though. George Harrison: Look out for the canapy drawing of *Queen Victoria*! (The submarine crashes into it) The Beatles: Ooooh, oh God! No! Help us! Help us! Help us!
Dean Peterson: Good Lord, that sounds like a pig fainting!
Uncle Sam: This money will go to partially cover the cost of a study to decide what to do with the money.
Guy: What a wonderful film about horrible people. Woman: There like the family from hell on acid that's on steroids.
Homer: Doc, this is all too much. I mean, my son, a genius? How does it happen? Dr. Pryor: Well, genius-level intelligence is usually the result of hereditary and environment... (Sees Homer staring blankly) although in some cases it's a total mystery.
Souvenir Shop Employee: Hey tough luck pal. You can't fight the souvenir industry. We're too powerful.
Homer: Did you see that? I did the deed, open the gates! St. Peter: (Reading a newspaper) What? Oh sorry, I didn't see that. Homer: What? I thought you guys saw everything! St. Peter: No, you're thinking of Santa Claus. Homer: Well I'll be damned! St. Peter: Afraid so. (Pulls a cord, sending Homer to Hell)
Judge Snyder: Does the defense have any closing remarks? Gil: Uh, not at this time, your honor. Judge Snyder: This is the only time. Gil: Oh, uh, then no.
Narrator: Next week on 'Behind the Laughter.' Huckleberry Hound: I was so gay, but I couldn't tell anybody...
Homer: I can't go to prison! They pee in a cup and throw it at you, I saw it in a movie. Johnson: You won't be seeing any prison movies where you're going, prison!
Concert Manager: Homer, nothing's more important to me than the health and well-being of my freaks. I'm sending you to a vet.
Telephone Operator: The fingers you have used to dial are too fat. To obtain a special dialing wand, please mash the keypad with your palm now.
Martin: Uh, sir, why don't you just use real cows? Painter: Cows don't look like cows on film. You got to use horses. Ralph: What do you do if you want something that looks like a horse? Painter: Usually we just tape a bunch of cats together.
Executive: If word gets out about this, Crazy Clown airlines will be a laughing stock.
Judge Snyder: Homer Simpson, for attempted insecticide and aggravated buggery, I sentence you to 200 hours of community service!
PA: Welcome to Japan, folks. The local time is tomorrow.
Seminar Speaker: First, let me assure you that this is not one of those shady pyramid schemes you've been hearing about. No, sir. Our model is the trapezoid!
Broker: Your stock in the power plant just went up for the first time in ten years. Homer: I own stock? Broker: Yes, all the employees got some in exchange for waiving certain Constitutional rights.
Priest: So how many wives will you be marrying today, Mr. Simpson? Bart: Just one. Priest: Pssh. What are you, gay?
Dr. Hibbert: I'm afraid that your son is in a deep coma and would never wake up. Homer: Well, at least he's not dead. Dr. Hibbert: I should say so. This way I can bill you every day.
Jesse: I'm a level five vegan. I won't eat anything that casts a shadow.
Chinese Ambassador: You pay now! Now! Bart: What happened to you, China? You used to be cool. Chinese Ambassador: Hey, China still cool. You pay later. Later!
Jasper: Is this seat taken, little girl? Bart: I'm not a girl! Are you blind? Jasper: Yes.
Homer: Oh no, I've only got a few more minutes till they stop selling those breakfast balls! (George Bush is all ready ordering in front) D'oh! George George HW Bush: Let's see what you folks have here, a Krusty Burger? Well that doesn't sound very appetizing. What kind of stew do you have? Squeaky Voiced Teen: (Over radio) Uh... we don't have any stew. Agent Ray Johnson: Why don't you just get the cheese burger sir? George George HW Bush: That's really more of a weekend thing, Ray. Homer: (Impatient) HEY JERK! MOVE YOUR FANNY! (Beeps car horn) George George HW Bush: Ray, that man's louder than *World War II*! Go see what the rhubarb is will ya? (Agent Johnson approaches Homer's car) Agent Ray Johnson: Sir, could you pop your hood, please? (Homer does so, then Agent Johnson unscrews the car horn) Homer: Hey! my taxes pay for that horn!
Bleeding Gums Murphy: You've made an old jazzman happy Lisa. Mufasa: You must avenge my death Kimba... uh, I mean *Simba*. Darth Vader: *Luke*, I am your father. James Earl Jones: This is *CNN*. Bleeding Gums Murphy: Will you guys pipe down? I'm saying goodbye to Lisa! Mufasa, Vader, and Jones: We're, sorry.
Australian Man: You call that a knife? This is a knife! Bart: That's not a knife. That's a spoon. Australian Man: Alright, alright, you win. Heh. I see you've played knifey-spooney before.
Photographer: C'mon, sweetheart, smile! I bet you have a beautiful smile. Why don't you share it with the world? (Lisa smiles, exposing her braces) Photographer: (Gasps) There is no God!
Dr. Wolfe: How often do you brush, Ralph? Ralph: Three times a day, sir. Dr. Wolfe: Why must you turn my office into a house of lies? Ralph: You're right. I don't brush. (Starts to cry) I don't brush! Dr. Wolfe: Let's look at a picture book. The 'Big Book of British Smiles.' (Dr. Wolfe takes out a book and shows Ralph page after page of decaying, rotten British smiles) Ralph: (Crying) That's enough! That's enough!
Technician #1: I got it! We can just shut off the power! Technician #2: No such luck. It's solar powered. Technician #1: (Disgusted) Solar power. When will people learn?
Lanley: Are you stuck in a dead-end job? Homer: Maybe! Lanley: Are you squandering the precious gift of life in front of the idiot box? Homer: What's it to ya? Lanley: Are you on your third beer of the evening? Homer: Does whiskey count as beer? Lanley: Well maybe it's time you joined the exciting field of monorail conducting by enrolling at the Lanley Institute! (Photograph shows an impressive building) TV Announcer: Actual institute may not match photo.
Anchor: Welcome to *Fox News*, your voice for evil.
Firefighter: Do you know how many fires are started by birthday candles? If you do, tell me. It would settle a bet down at the station house. I say five, Gus says a million.
Brazilian Kidnapper: Look at all that pink and purple. Our money sure is gay.
Homer: Can you let me out of the boat? Brazilian Kidnapper: What for? Homer: (Whining) I have to go. Brazilian Kidnapper: (Agitated tone) Again? Homer: I'm sorry, I have a bladder the size of a Brazil nut. Brazilian Kidnapper: We just call them nuts here.
Bart: Yo, Dr. S., have you seen Milhouse today? Dr. S.: No. Bart: Okay, thanks. Dr. S.: Wait! Did you know that there's a direct correlation between the decline of *Spirograph* and the rise in gang activity? Think about it. Bart: I will. Dr. S.: No, you won't.
Lisa: Wait a second! You planted a phony skeleton for me to find! This was all a big hoax! Mall Owner: (Chuckles) Not a hoax, a publicity stunt. Lisa: You exploited people's deepest beliefs just to hawk your cheesy wares? Well, we are outraged! Aren't we? Chief Wiggum: Oh. Oh, yeah. Yeah, we're outraged. Very, uh... Very much so. But look at all the stores! A *Pottery Barn*! Moe: And 20% off everything? Hey, does that include rat spray? Mall Representative: Oh, yeah.
Judge: Lisa Simpson, you are charged with destruction of a historic curiosity, a misdemeanor. But in a larger sense, this trial will settle the age-old question of science versus religion. Let the opening statements commence. Lawyer: Your Honor, over the coming weeks, and months, we intend to prove Lisa Simpson willfully destroyed... Lenny: (Points to window) There's the angel! (Murmuring) (The courtroom empties) Judge: I find the defendant not guilty. As for science versus religion, I'm issuing a restraining order. Religion must stay 500 yards from science at all times.
Mr. Sparkle: (Japanese Commercial) Super Lucky Best Wash Ever!
Banner: It's not up to us to choose which laws we want to obey. If it were, I'd kill everyone who looked at me cockeyed!
"""
    def simpsons(self, irc, msg, args):
        """
            A Random quote from The Simpsons.
        """
        plist = [x for x in Simpsons.quotes.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply(p.strip(), prefixNick=False)

Class = Simpsons

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
