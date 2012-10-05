
import supybot.utils as utils
from supybot.commands import *
import supybot.plugins as plugins
import supybot.ircutils as ircutils
import supybot.callbacks as callbacks
from random import choice

class Deep(callbacks.Plugin):
    """Add the help for "@plugin help Zen" here
    This should describe *how* to use this plugin."""
    threaded = True

    thoughts = """
        If trees could scream, would we be so cavalier about cutting them down?  We might, if they screamed all the time, for no good reason.
        To me, it's a good idea to always carry two sacks of something when you walk around.  That way, if anybody says, "Hey, can you give me a hand?"  You can say, "Sorry, got these sacks."
        A funny thing to do is, if you're out hiking and your friend gets bitten by a poisonous snake, tell him you're going to go for help, then go about ten feet and pretend that *you* got bit by a snake. Then start an argument with him about who's going to go get help. A lot of guys will start crying. That's why it makes you feel good when you tell them it was just a joke.
        A good way to threaten somebody is to light a stick of dynamite. Then you call the guy and hold the burning fuse up to the phone. "Hear that?" you say. "That's dynamite, baby."
        After I die, wherever my spirit goes, I'm going to try to get back and visit my skeleton at least once a year, because, "Hey, old buddy, how's it going?"
        Ambition is like a frog sitting on a Venus Flytrap. The flytrap can bite and bite, but it won't bother the frog because it only has little tiny plant teeth. But some other stuff could happen and it could be like ambition.
        Anytime I see something screech across a room and latch onto someones neck, and the guy screams and tries to get it off, I have to laugh, because what is that thing.
        As I bit into the nectarine, it had a crisp juiciness about it that was very pleasurable - until I realized it wasn't a nectarine at all, but A HUMAN HEAD!!
        As the evening sky faded from a salmon color to a sort of flint gray, I thought back to the salmon I caught that morning, and how gray he was, and how I named him Flint.
        As the light changed from red to green to yellow and back to red again, I sat there thinking about life. Was it nothing more than a bunch of honking and yelling? Sometimes it seemed that way.
        As we were driving, we saw a sign that said "Watch for Rocks." Marta said it should read "Watch for Pretty Rocks." I told her she should write in her suggestion to the highway department, but she started saying it was a joke - just to get out of writing a simple letter! And I thought I was lazy!
        At first I thought, if I were Superman, a perfect secret identity would be "Clark Kent, Dentist," because you could save money on tooth X-rays. But then I thought, if a patient said, "How's my back tooth?" and you just looked at it with your X-ray vision and said, "Oh it's okay," then the patient would probably say, "Aren't you going to take an X-ray, stupid?" and you'd say, "Aw fuck you, get outta here," and then he probably wouldn't even pay his bill.
        Before you criticize someone, walk a mile in their shoes. That way, you'll be a mile from them, and you'll have their shoes.
        Better not take a dog on the space shuttle, because if he sticks his head out when you're coming home his face might burn up.
        Children need encouragement. If a kid gets an answer right, tell him it was a lucky guess. That way he develops a good, lucky feeling.
        Consider the daffodil. And while you're doing that, I'll be over here, looking through your stuff.
        Contrary to what most people say, the most dangerous animal in the world is not the lion or the tiger or even the elephant. It's a shark riding on an elephant's back, just trampling and eating everything they see.
        Dad always thought laughter was the best medicine, which I guess is why several of us died of tuberculosis.
        Even though I was their captive, the Indians allowed me quite a bit of freedom. I could walk freely, make my own meals, and even hurl large rocks at their heads. It was only later that I discovered that they were not Indians at all but only dirty-clothes hampers.
        Fear can sometimes be a useful emotion. For instance, let's say you're an astronaut on the moon and you fear that your partner has been turned into Dracula. The next time he goes out for the moon pieces, wham!, you just slam the door behind him and blast off. He might call you on the radio and say he's not Dracula, but you just say, "Think again, bat man".
        For mad scientists who keep brains in jars, here's a tip: Why not add a slice of lemon to each jar, for freshness.
        He was a cowboy, mister, and he loved the land. He loved it so much he made a woman out of dirt and married her. But when he kissed her, she disintegrated. Later, at the funeral, when the preacher said, "Dust to dust," some people laughed, and the cowboy shot them. At his hanging, he told the others, "I'll be waiting for you in heaven--with a gun.
        Here's a good gag if you go swimming in a swamp and when you come out you're all covered with leeches. Just say, "Hey, has anybody seen my raisins?" (Because leeches kind of look like big raisins.)
        Here's a good tip for when you go to the beach: A sand dollar may look like a nice cracker that someone left, but trust me, they don't taste like it.
        I believe in making the world safe for our children, but not our children's children, because I don't think children should be having sex.
        I bet a fun thing would be to go way back in time to where there was going to be an eclipse and tell the cave men, "If I have come to destroy you, may the sun be blotted out from the sky." Just then the eclipse would start, and they'd probably try to kill you or something, but then you could explain about the rotation of the moon and all, and everyone would get a good laugh.
        I bet a funny thing about driving a car off a cliff is, while you're in midair, you still hit those brakes! Hey, better try the emergency brake!
        I bet one legend that keeps recurring throughout history, in every culture, is the story of Popeye.
        I bet the main reason the police keep people away from a plane crash is they don't want anybody walking in and lying down in the crash stuff, then, when somebody comes up, act like they just woke up and go, "What was THAT?!"
        I bet when the Neanderthal kids would make a snowman, someone would always end up saying, "Don't forget the thick, heavy brows." Then they would all get embarrassed because they remembered they had the big hunky brows too, and they'd get mad and eat the snowman.
        I can picture in my mind a world without war, a world without hate. And I can picture us attacking that world, because they'd never expect it.
        I can still recall old Mister Barnslow getting out every morning and nailing a fresh load of tadpoles to the old board of his. Then he'd spin it round and round, like a wheel of fortune, and no matter where it stopped he'd yell out, "Tadpoles! Tadpoles is a winner!" We all thought he was crazy. But then we had some growing up to do.
        I can't stand cheap people. It makes me real mad when someone says something like, "Hey, when are you going to pay me that $100 you owe me?" or "Do you have that $50 you borrowed?" Man, quit being so cheap!
        I don't think I'm alone when I say I'd like to see more and more planets fall under the ruthless domination of our solar system.
        I guess I kinda lost control, because in the middle of the play I ran up and lit the evil puppet villain on fire. No, I didn't. Just kidding. I just said that to help illustrate one of the human emotions, which is freaking out. Another emotion is greed, as when you kill someone for money, or something like that. Another emotion is generosity, as when you pay someone double what he paid for his stupid puppet.
        I guess we were all guilty, in a way. We all shot him, we all skinned him, and we all got a complimentary bumper sticker that said, "I helped skin Bob."
        I hope if dogs ever take over the world, and they chose a king, they don't just go by size, because I bet there are some Chihuahuas with some good ideas.
        I hope life isn't a big joke, because I don't get it.
        I hope that after I die, people will say of me: "That guy sure owed me a lot of money."
        I hope that someday we will be able to put away our fears and prejudices and just laugh at people.
        I hope they never find out that lightning has a lot of vitamins in it, because do you hide from it or not?
        I remember how my Great Uncle Jerry would sit on the porch and whittle all day long. Once he whittled me a toy boat out of a larger toy boat I had. It was almost as good as the first one, except now it had bumpy whittle marks all over it. And no paint, because he had whittled off the paint.
        I remember that one fateful day when Coach took me aside. I knew what was coming. "You don't have to tell me," I said. "I'm off the team, aren't I?" "Well," said Coach, "you never were really ON the team. You made that uniform you're wearing out of rags and towels, and your helmet is a toy space helmet. You show up at practice and then either steal the ball and make us chase you to get it back, or you try to tackle people at inappropriate times." It was all true what he was saying. And yet, I thought something is brewing inside the head of this Coach. He sees something in me, some kind of raw talent that he can mold. But that's when I felt the handcuffs go on.
        I scrambled to the top of the precipice where Nick was waiting. "That was fun," I said. "You bet it was," said Nick. "Let's climb higher." "No," I said. "I think we should be heading back now." "We have time," Nick insisted. I said we didn't, and Nick said we did. We argued back and forth like that for about 20 minutes, then finally decided to head back. I didn't say it was an interesting story.
        I think a good gift for the President would be a chocolate revolver. and since he is so busy, you'd probably have to run up to him real quick and give it to him.
        I think a good product would be "Baby Duck Hat." It's a fake baby duck, which you strap on top of your head. Then you go swimming underwater until you find a mommy duck and her babies, and you join them. Then all of the sudden, you stand up out of the water and roar like Godzilla. Man those ducks really take off! Also Baby Duck Hat is good for parties.
        I think one way the cops could make money would be to hold a murder weapons sale. Many people could really use used ice picks.
        I think somebody should come up with a way to breed a very large shrimp. That way, you could ride him, then after you camped at night, you could eat him. How about it, science?
        I think someone should have had the decency to tell me the luncheon was free. To make someone run out with potato salad in his hand, pretending he's throwing up, is not what I call hospitality.
        I think the mistake a lot of us make is thinking the state-appointed shrink is our friend.
        I wish a robot would get elected president. That way, when he came to town, we could all take a shot at him and not feel too bad.
        I wish everybody would have to have an electric thing implanted in our heads that gave us a shock whenever we did something to disobey the president. Then somehow I get myself elected president.
        I wish I had a dollar for every time I spent a dollar, because then, yahoo! I'd have all my money back.
        I wish I had a Kryptonite cross, because then you could keep both Dracula AND Superman away.
        I wish I lived back in the old west days, because I'd save up my money for about twenty years so I could buy a solid-gold pick. Then I'd go out West and start digging for gold. When someone came up and asked what I was doing, I'd say, "Looking for gold, ya durn fool." He'd say, "Your pick is gold," and I'd say, "Well, that was easy." Good joke, huh.
        I wish I would have a real tragic love affair and get so bummed out that I'd just quit my job and become a bum for a few years, because I was thinking about doing that anyway.
        I wish outer space guys would conquer the Earth and make people their pets, because I'd like to have one of those little beds with my name on it.
        I wish scientists would come up with a way to make dogs a lot bigger, but with a smaller head. That way, they'd still be good as watchdogs, but they wouldn't eat so much.
        I wouldn't be surprised if someday some fishermen caught a big shark and cut it open, and there inside was a whole person. Then they cut the person open, and in him is a little baby shark. And in the baby shark there isn't a person, because it would be too small. But there's a little doll or something, like a Johnny Combat little toy guy---something like that.
        I'd like to be buried Indian-style, where they put you up on a high rack, above the ground. That way, you could get hit by meteorites and not even feel it.
        I'd like to see a nature film where an eagle swoops down and pulls a fish out of a lake, and then maybe he's flying along, low to the ground, and the fish pulls a worm out of the ground. Now that's a documentary!
        I'd like to see a nude opera, because when they hit those high notes, I bet you can really see it in those genitals.
        I'd rather be rich than stupid.
        I'm not afraid of insects taking over the world, and you know why? It would take about a billion ants just to AIM a gun at me, let alone fire it. And you know what I'm doing while they're aiming it at me? I just sort of slip off to the side, and then suddenly run up and kick the gun out of their hands.
        I'm telling you, just attach a big parachute TO THE PLANE ITSELF! Is anyone listening to me?!
        If a kid asks where rain comes from, I think a cute thing to tell him is "God is crying." And if he asks why God is crying, another cute thing to tell him is "Probably because of something you did.
        If any man says he hates war more than I do, he better have a knife, that's all I have to say.
        If I ever get real rich, I hope I'm not real mean to poor people, like I am now.
        If I ever opened a trampoline store, I don't think I'd call it Trampo-Land, because you might think it was a store for tramps, which is not the impression we are trying to convey with our store. On the other hand, we would not prohibit tramps from browsing, or testing the trampolines, unless a tramp's gyrations seemed to be getting out of control.
        If I lived back in the wild west days, instead of carrying a six-gun in my holster, I'd carry a soldering iron. That way, if some smart-aleck cowboy said something like "Hey, look. He's carrying a soldering iron!" and started laughing, and everybody else started laughing, I could just say, "That's right, it's a soldering iron. The soldering iron of justice." Then everybody would get real quiet and ashamed, because they had made fun of the soldering iron of justice, and I could probably hit them up for a free drink.
        If I was the head of a country that lost a war, and I had to sign a peace treaty, just as I was signing I'd glance over the treaty and then suddenly act surprised. "Wait a minute! I thought WE won!
        If the Vikings were around today, they would probably be amazed at how much glow-in-the-dark stuff we have, and how we take so much of it for granted.
        If they ever come up with a swashbuckling School, I think one of the courses should be Laughing, Then Jumping Off Something.
        If trees could scream, would we be so cavalier about cutting them down? We might, if they screamed all the time, for no good reason.
        If you define cowardice as running away at the first sign of danger, screaming and tripping and begging for mercy, then yes, Mr. Brave man, I guess I'm a coward.
        If you ever catch on fire, try to avoid seeing yourself in the mirror, because I bet that's what REALLY throws you into a panic.
        If you ever fall off the Sears Tower, just go real limp, because maybe you'll look like a dummy and people will try to catch you because, hey, free dummy.
        If you ever reach total enlightenment while you're drinking a beer, I bet it makes beer shoot out your nose.
        If you ever teach a yodeling class, probably the hardest thing is to keep the students from just trying to yodel right off. You see, we build to that.
        If you go flying back through time and you see somebody else flying forward into the future, it's probably best to avoid eye contact.
        If you go parachuting, and your parachute doesn't open, and you friends are all watching you fall, I think a funny gag would be to pretend you were swimming.
        If you make ships in a bottle, I bet the thing that really makes your heart sink is when you look in, and there at the wheel is Captain Termite.
        If you saw two guys named Hambone and Flippy, which one would you think liked dolphins the most? I'd say Flippy, wouldn't you? You'd be wrong, though. It's Hambone.
        If you think a weakness can be turned into a strength, I hate to tell you this, but that's another weakness.
        If you were a pirate, you know what would be the one thing that would really make you mad? Treasure chests with no handles. How the hell are you supposed to carry it?!
        If you were a poor Indian with no weapons, and a bunch of conquistadors came up to you and asked where the gold was, I don't think it would be a good idea to say, "I swallowed it. So sue me."
        If you were an ancient barbarian, I bet a real embarrassing thing would be if you were sacking Rome and your cape got caught on something and you couldn't get it unhooked, and you had to ask another barbarian to unhook it for you.
        If you're a cowboy and you're dragging a guy behind your horse, I bet it would really make you mad if you looked back and the guy was reading a magazine.
        If you're a horse, and someone gets on you, and falls off, and then gets right back on you, I think you should buck him off right away.
        If you're a Thanksgiving dinner, but you don't like the stuffing or the cranberry sauce or anything else, just pretend like you're eating it, but instead, put it all in your lap and form it into a big mushy ball. Then, later, when you're out back having cigars with the boys, let out a big fake cough and throw the ball to the ground. Then say, "Boy, these are good cigars!"
        If you're a young Mafia gangster out on your first date, I bet it's real embarrassing if someone tries to kill you.
        If you're an ant, and you're walking along across the top of a cup of pudding, you probably have no idea that the only thing between you and disaster is the strength of that pudding skin.
        If you're an archeologist, I bet it's real embarrassing to put together a skull from a bunch of ancient bone fragments, but then it turns out it's not a skull but just an old dried-out potato.
        If you're ever selling your house, and some people come by, and a big rat comes out and he's dragging the rattrap because it didn't quite kill him, just tell the people he's your pet and that's a trick you taught him.
        If you're in a war, instead of throwing a hand grenade at the enemy, throw one of those small pumpkins. Maybe it'll make everyone think how stupid war is, and while they are thinking, you can throw a real grenade at them.
        If you're robbing a bank and you're pants fall down, I think it's okay to laugh and to let the hostages laugh too, because, come on, life is funny.
        Instead of a trap door, what about a trap window? The guy looks out it, and if he leans too far, he falls out. Wait. I guess that's like a regular window.
        Instead of trying to build newer and bigger weapons of destruction, we should be thinking about getting more use out of the ones we already have.
        Is there anything more beautiful than a beautiful, beautiful flamingo, flying across in front of a beautiful sunset? And he's carrying a beautiful rose in his beak, and also he's carrying a very beautiful painting with his feet. And also, you're drunk.
        If you ever drop your keys into a river of molten lava, let'em go, because, man, they're gone.
        It makes me mad when I go to all the trouble of having Martha cook up about a hundred drumsticks, then the guy at the Marineland says, "You can't throw chicken to the dolphins. They eat fish." Sure they eat fish, if that's all you give them. Man, wise up.
        It takes a big man to cry, but it takes a bigger man to laugh at that man.
        It's easy to sit there and say you'd like to have more money. And I guess that's what I like about it. It's easy. Just sitting there, rocking back and forth, wanting that money.
        It's true that every time you hear a bell, an angel gets its wings. But what they don't tell you is that every time you hear a mouse trap snap, and Angel gets set on fire.
        Just because swans mate for life, I don't think its that big a deal. First of all, if you're a swan, you're probably not going to find a swan that looks much better than the one you've got, so why not mate for life?
        Laurie got offended that I used the word "puke." But to me, that's what her dinner tasted like.
        Life, to me, is like a quiet forest pool, one that needs a direct hit from a big rock half-buried in the ground. You pull and you pull, but you can't get the rock out of the ground. So you give it a good kick, but you lose your balance and go skidding down the hill toward the pool. Then out comes a big Hawaiian man who was screwing his wife beside the pool because they thought it was real pretty. He tells you to get out of there, but you start faking it, like you're talking Hawaiian, and then he gets mad and chases you...
        Many people think that history is a dull subject. Dull? Is it "dull" that Jesse James once got bitten on the forehead by an ant, and at first it didn't seem like anything, but then the bite got worse and worse, so he went to a doctor in town, and the secretary told him to wait, so he sat down and waited, and waited, and waited, and waited, and then finally he got to see the doctor, and the doctor put some salve on it? You call that dull?
        Maybe in order to understand mankind we have to look at that word itself. MANKIND. Basically, it's made up of two separate words "mank"and "ind." What do these words mean? It's a mystery and that's why so is mankind.
        Most of the time in the Middle Ages it was probably real bad being stuck down in a dungeon. But some days, when there was a bad storm outside, you'd look out your little window and think, "Boy, I'm glad I'm not out in that."
        Most people don't realize that large pieces of coral, which have been painted brown and attached to the skull by common wood screws, can make a child look like a deer.
        Once when I was in Hawaii, on the island of Kauai, I met a mysterious old stranger. He said he was about to die and wanted to tell someone about the treasure. I said, "Okay, as long as it's not a long story. Some of us have a plane to catch, you know." He started telling his story, about the treasure and his life and all, and I thought: "This story isn't too long." But then, he kept going, and I started thinking, "Uh-oh, this story is getting long." But then the story was over, and I said to myself: "You know, that story wasn't too long after all." I forget what the story was about, but there was a good movie on the plane. It was a little long, though.
        One thing kids like is to be tricked. For instance, I was going to take my little nephew to DisneyLand, but instead I drove him to an old burned-out warehouse. "Oh, no," I said, "DisneyLand burned down." He cried and cried, but I think that deep down he thought it was a pretty good joke. I started to drive over to the real DisneyLand, but it was getting pretty late.
        One thing vampire children have to be taught early on is, don't run with wooden stakes.
        Probably the earliest flyswatters were nothing more than some sort of striking surface attached to the end of a long stick.
        Probably to a shark, about the funniest thing there is is a wounded seal, trying to swim to shore, because WHERE DOES HE THINK HE'S GOING?!
        Somebody told me it was frightening how much topsoil we are losing each year, but I told that story around the campfire and nobody got scared.
        Sometimes I think I'd be better off dead. No, wait, not me, you.
        Sometimes I think the world has gone completely mad. And then I think, "Aw, who cares?" And then I think, "Hey, what's for supper?"
        Sometimes I think you have to march right in and demand your rights,even if you don't know what your rights are, or who the person is you're talking to. Then on the way out, slam the door.
        Sometimes when I feel like killing someone, I do a little trick to calm myself down. I'll go over to the persons house and ring the doorbell. When the person comes to the door, I'm gone, but you know what I've left on the porch? A jack-o-lantern with a knife stuck in the side of it's head with a note that says "You." After that I usually feel a lot better, and no harm done.
        Sometimes when I reflect back on all the beer I drink I feel ashamed. Then I look into the glass and think about the workers in the brewery and all of their hopes and dreams. If I didn't drink this beer, they might be out of work and their dreams would be shattered. Then I say to myself, 'It is better that I drink this beer and let their dreams come true than to be selfish and worry about my liver.'
        Sometimes you have to be careful when selecting a new name for yourself. For instance, let's say you have chosen the nickname "Fly Head." Normally you would think that "Fly Head" would mean a person who has beautiful swept-back features, as if flying through the air. But think again. Couldn't it also mean "having a head like a fly"? I'm afraid some people might actually think that.
        Sometimes, when I drive across the desert in the middle of the night, with no other cars around, I start imagining: What if there were no civilization out there? No cities, no factories, no people? And then I think: No people or factories? Then who made this car? And this highway? And I get so confused I have to stick my head out the window into the driving rain---unless there's lightning, because I could get struck on the head by a bolt.
        The crows seemed to be calling his name, thought Caw.
        The face of a child can say it all, especially the mouth part of the face.
        The first thing was, I learned to forgive myself. Then, I told myself, "Go ahead and do whatever you want, it's okay by me."
        The memories of my family outings are still a source of strength to me. I remember we'd all pile into the car - I forget what kind it was - and drive and drive. I'm not sure where we'd go, but I think there were some trees there. The smell of something was strong in the air as we played whatever sport we played. I remember a bigger, older guy we called "Dad." We'd eat some stuff, or not, and then I think we went home. I guess some things never leave you.
        The most unfair thing about life is the way it ends. I mean, life is tough. It takes up a lot of your time. What do you get at the end of it? A death. What's that, a bonus? I think the life cycle is all backwards. You should die first, get it out of the way. Then you live in an old age home. You get kicked out when you're too young, you get a gold watch, you go to work. You work forty years until you're young enough to enjoy your retirement. You do drugs, alcohol, you party, you get ready for high school. You go to grade school, you become a kid, you play, you have no responsibilities, you become a little baby, you go back into the womb, you spend your last nine months warm, happy, and floating... You finish off as an orgasm.
        The next time I have meat and mashed potatoes, I think I'll put a very large blob of potatoes on my plate with just a little piece of meat. And if someone asks me why I didn't get more meat, I'll just say, "Oh, you mean this?" and pull out a big piece of meat from inside the blob of potatoes, where I've hidden it. Good magic trick, huh?
        The people in the village were real poor, so none of the children had any toys. But this one little boy had gotten an old enema bag and filled it with rocks, and he would go around and whap the other children across the face with it. Man, I think my heart almost broke. Later the boy came up and offered to give me the toy. This was too much! I reached out my hand, but then he ran away. I chased him down and took the enema bag. He cried a little, but that's the way of these people.
        The whole town laughed at my great-grandfather, just because he worked hard and saved his money. True, working at the hardware store didn't pay much, but he felt it was better than what everybody else did, which was go up to the volcano and collect the gold nuggets it shot out every day. It turned out he was right. After forty years, the volcano petered out. Everybody left town, and the hardware store went broke. Finally he decided to collect gold nuggets too, but there weren't many left by then. Plus, he broke his leg and the doctor's bills were real high.
        The wise man can pick up a grain of sand and envision a whole universe. But the stupid man will just lay down on some seaweed and roll around until he's completely draped in it. Then he'll standup and go, "Hey, I'm Vine Man."
        There are many stages to a man's life. In the first stage, he is young and eager, like a beaver. In the second stage, he wants to build things, like dams, and maybe chew down some trees. In the third stage, he feels trapped, and then "skinned." I'm not sure what the fourth stage is.
        To me, boxing is like a ballet, except there's no music, no choreography and the dancers hit each other.
        To me, clowns aren't funny. In fact, they're kind of scary. I've wondered where this started and I think it goes back to the time I went to the circus, and a clown killed my dad.
        To me, it's a good idea to always carry two sacks of something when you walk around. That way, if anybody says, "Hey, can you give me a hand?", you can say, "Sorry, got these sacks."
        Too bad when I was a kid there wasn't a guy in our class that everybody called the "Cricket Boy", because I would have liked to stand up in class and tell everybody, "You can make fun of the Cricket Boy if you want to, but to me he's just like everybody else." Then everybody would leave the Cricket Boy alone, and I'd invite him over to spend the night at my house, but after about five minutes of that loud chirping I'd have to kick him out. Maybe later we could get up a petition to get the Cricket Family run out of town. Bye, Cricket Boy.
        Too bad you can't buy a voodoo globe so that you could make the earth spin real fast and freak everybody out.
        Too bad you can't just grab a tree by the very tiptop and bend it clear over the ground and then let her fly, because I bet you'd be amazed at all the stuff that comes flying out.
        We tend to scoff at the beliefs of the ancients. But we can't scoff at them personally, to their faces, and this is what annoys me.
        We used to laugh at Grandpa when he'd head off and go fishing. But we wouldn't be laughing that evening when he'd come back with some whore he picked up in town.
        What is it that makes a complete stranger dive into an icy river to save a solid gold baby? Maybe we'll never know.
        When I found the skull in the woods, the first thing I did was call the police. But then I got curious about it. I picked it up, and started wondering who this person was, and why he had deer horns.
        When I was a kid my favorite relative was Uncle Caveman. After school we'd all go play in his cave, and every once in a while he would eat one of us. It wasn't until later that I found out that Uncle Caveman was a bear.
        When the age of the Vikings came to a close, they must have sensed it. Probably, they gathered together one evening, slapped each other on the back and said, "Hey, good job."
        When you die, if you get a choice between going to regular heaven or pie heaven, choose pie heaven. It might be a trick, but if it's not, mmmmmmm, boy.
        When you die, if you go somewhere where they ask you a bunch of questions about your life and what you learned and all, I think a good way to get out of it is just to say, "No speaka English."
        When you go in for a job interview, I think a good thing to ask is if they ever press charges.
        When you're riding in a time machine way far into the future, don't stick your elbow out the window, or it'll turn into a fossil.
        Whenever I see an old lady slip and fall on a wet sidewalk, my first instinct is to laugh. But then I think, what is I was an ant, and she fell on me. Then it wouldn't seem quite so funny.
        Whenever someone asks me to define love, I usually think for a minute, then I spin around and pin the guy's arm behind his back. NOW who's asking the questions?
        Whenever you read a good book, it's like the author is right there, in the room talking to you, which is why I don't like to read good books.
        Whether they find a life there or not, I think Jupiter should be called an enemy planet.
        Why do people in ship mutinies always ask for "better treatment"? I'd ask for a pinball machine, because with all that rocking back and forth you'd probably be able to get a lot of free games.
        You can't tell me that cowboys, when they're branding cattle, don't sort of "accidentally" brand each other every once in a while. It's their way of letting off stress.
        You know what would be the most terrifying thing that could ever happen to a flea? Getting caught inside a watch somehow. You don't even care, do you?
        You know what would make a good story? Something about a clown who make people happy, but inside he's real sad. Also, he has severe diarrhea.
    """

    def deep(self, irc, msg, args):
        """
        Deep Thoughts, by Jack Handy
        """
        plist = [x for x in Deep.thoughts.split("\n") if len(x.strip())]
        p = choice(plist)
        irc.reply("Deep Thought: " + p.strip(), prefixNick=False)

Class = Deep

# vim:set shiftwidth=4 tabstop=4 expandtab textwidth=79:
