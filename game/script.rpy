# Use the format define [variable] = Character('[character name]') to make a new variable for a character.
# Makes your job easier 
define y = Character('Y/N')
define m = Character('Mom')
define a = Character('???')
define j = Character('Jerma985')
define x = Character('JEX Elbertson')
define r = Character('Jeremy Elbertson')
define e = Character('Jester985')
define f = Character('Malfoil')
define t = Character('Jeter Jarker')
define d = Character('Spiderjerm')
define s = Character('Sus Guy')
define w = Character('Jerma Store Worker') #the worker in Megurine Luka
define g = Character('Random Ass Girl 1')
define G = Character('Randome Ass Girl 2')
define l = Character('Lunch Guy')
define M = Character('Mr. Mustacheguy')

# Money and inventory
$ jermabucks = 0
$ items = []
$ gifts = []

# Affinity points
default points = 25

#Stats
$ Strength = 0
$ Dexterity = 0
$ Intelligance = 0
$ Constitution = 0
$ Charisma = 0

transform bounce:
    yoffset 0
    easein .1 yoffset -30
    easeout .1 yoffset 0
    yoffset 0
    pass

# BEGINNING OF ACT 0

label start:
    show bg room night
    y "Phew! I'm pooped!"
    y "I can't wait to start my day and go to my first day of school tomorrow!"
    "*shuffling*"
    y "..."
    y "Fuck! I forgot to go to registration. How could I forget?!"
    y "Oh right. I can just register online."
    y "Thank the heavens for technology."
    label name1:
        $ y = renpy.input("Now, time to put my name...")
        $ y = y.strip()
    y "Did I type it right?"
    menu:
        "Yes! This is my name!":
            jump start1
        "No! This is not my name!":
            jump name2
    label name2:
        "Ugh... I must be tired... let me try again."
        jump name1
label start1:
    y "Now for my pronouns..."
    menu:
        "He/Him":
            $ sub = "he"
            $ con = "he's"
            $ obj = "him"
            $ poss = "his"
            $ poss_adj = "his"
            $ ref = "himself"
        "She/Her":
            $ sub = "she"
            $ con = "she's"
            $ obj = "her"
            $ poss = "hers"
            $ poss_adj = "her"
            $ ref = "herself"
        "They/Them":
            $ sub = "they"
            $ con = "they're"
            $ obj = "them"
            $ poss = "theirs"
            $ poss_adj = "their"
            $ ref = "themselves"
        "Ze/Hir":
            $ sub = "ze"
            $ con = "ze's"
            $ obj = "hir"
            $ poss = "hirs"
            $ poss_adj = "hir"
            $ ref = "hirself"
        "Xe/Xem":
            $ sub = "xe"
            $ con = "xe's"
            $ obj = "xem"
            $ poss = "xyrs"
            $ poss_adj = "xyr"
            $ ref = "xemselves"
        "E/Em":
            $ sub = "e"
            $ con = "e's"
            $ obj = "em"
            $ poss = "eirs"
            $ poss_adj = "eir"
            $ ref = "eirself"
        "Fae/Faer":
            $ sub = "fae"
            $ con = "faer's"
            $ obj = "faer"
            $ poss = "faers"
            $ poss_adj = "faer"
            $ ref = "faerself"
    label pronoun1:
        "So my pronouns are [sub]/[obj]?"
    menu:
        "Yes!":
            jump start2
        "No!":
            "Ugh... I'm so sleepy... let me do that again."
            jump start1
label start2:
    y "Okay! Sleepy time!"
    show bg room day
    with fade
    y "Ugh... I didn't sleep too well..."
    m "Honey! Breakfast is ready!"
    y "COMING!"
    y "Bleugh... Why do I have to keep eating mom's cooking..."
    y "{i}I've always gotten sick eating anything she's made.{/i}"
    y "{i}I wish dad was here in the morning instead...{/i}"
    y "{i}Forget the upset stomatch. Today's my first day of school and I'm so excited!{/i}"
    y "{i}I've got all my classes right here."
    y "{i}Haha... I know I'm gonna have trouble looking for the right rooms...{/i}"


label startroad1:
    show bg road day
    with fade
    y "Wow! What a beautiful day!"
    y "Surely no one is gonna run into me while I'm trying to appreciate the nice sky!"
    y "...Wait"
    y "What's that sound? It sounds like someone's running-"
    show jerma running
    with hpunch
    y "OOF!"
    hide jerma running
    y "Hey! What the hell?! Watch where you're going-"
    show jerma neutral
    with dissolve
    y "Jerma! Where were you? I've waiting this entire time!"
    show jerma neutral at bounce, center
    j "Omg, I'm so sorry! I forgot to set the timer on my phone and- and- I totally forgot!"
    y "Jerma, you dunce! Quit being a late Andy and actually show up when I tell you to!"
    y "{i}This is Jerma985. My childhood best friend. We've known each other ever since we were in kindergarten!{/i}"
    y "{i}We sadly had to split to different high schools. But, my dad found a new job in this area so I was able to register for Jermaverse Academy!{/i}"
    y "{i}When I told Jerma, he was so ecstatic that he wouldn't shut up about it.{/i}"
    y "{i}Well... I would be excited too if Jerma didn't arrive to literally everthing 10 minutes late.{/i}"
    j "So... um... How's your morning been?"
    menu:
        "It's been great!":
            jump morning1_a
        "It's okay.":
            jump morning1_b
        "It's been awful...":
            jump morning1_c
    label morning1_a:
        y "It's been great! I was so excited that I almost shit myself!"
        j "Oh my God! Me too! Except for the shitting part."
        jump startroad2
    label morning1_b:
        y "Eh. It's alright I guess."
        j "Oh. Okay then."
        jump startroad2
    label morning1_c:
        y "Ugh... It was awful Jerma. I was so tired this morning that I wanted to stay in bed."
        j "Geez. Sorry about that. I know how you feel."
        jump startroad2
    label startroad2:
        j "Anyway, let's get to school quickly!"
        j "We're gonna be late!"
    hide jerma neutral

label school1:
    show bg entrance day
    with fade
    y "Wow... So this is Jermaverse Academy. It's so big..." 
    show jerma neutral at bounce, center
    with easeinright
    j "I heard the school's principle funded the entire thing! I heard he's incredibly loaded."
    a "Well, well, well... If it isn't Jerma985. Who's the cutie standing next to you?"
    y "Huh?"
    show jerma neutral at right
    show jex neutral at left
    with easeinleft
    y "{i}Woah.{/i}"
    y "{i}Who the hell is this stuck-up guy?"
    y "{i}He's pretty tall too. I wonder who he is."
    hide jerma neutral
    show jerma angry at bounce, right
    j "Hey! Fuck off, Jex! If you even think about flirting with [y] I swear I'll-"
    show jex neutral at bounce
    x "You sure have balls to talk to your senior like that, Jerma."
    show jex neutral at bounce
    x "Anyway, what's your name beautiful?"
    y "Uh- It's [y]. I'm a second year student here."
    x "[y]... That's a nice name."
    x "You said you were a second year, right? I don't think I've ever seen your face around here before."
    y "Oh. I just transferred here so that might explain it."
    x "Ah... So you're a transfer. I see."
    x "Excuse my rudeness. My name is JEX Elbertson. But for you hun, you can call me Jex."
    x "I'm a third year at Jermaverse Academy and the president of the Archery Club. The best of the best."
    x "Anyway, what do you think of the academy so far?"
    y "Oh! It's really nice! It looks so much better in person too!"
    x "Glad you like it here. Hope you enjoy your stay."
    x "Oh, and Jerma. Make sure you bring your cute friend with you next time you come by the practice hall. See you around sweetheart."
    hide jex neutral
    with easeinleft
    show jerma neutral at center
    with easeinleft
    j "..."
    j "...Um"
    show jerma neutral at bounce, center
    j "Hey... Sorry about that. Jex can be a little-"
    y "Oh no, it's fine. I think Jex is a great guy!"
    y "{i}What a weirdo...{/i}"
    y "So, I think Jex said something about you coming by the practice hall. I didn't know you were in the Archery Club Jerma!"
    j "Ha. No actually. Jex just makes me drop his bows and stuff off. He makes me clean them."
    y "Wow. That sound tedious."
    y "Maybe I should stop by the pratice hall too..."
    show jerma angry at bounce, center
    j "What? Don't tell me you're going there to see that jerk!"
    menu:
        "What? No way!":
            jump jerma1
        "Oh. No reason really.":
            jump jerma2
        "Heck yeah! I want to see Jex in action!":
            jump jerma3
    label jerma1:
        y "No silly! I want to help you clean the bows. That must be tiring for you so."
        show jerma neutral 
        j "Oh. Haha! Thanks but I'm pretty good on my own. But thanks for the offer."
        y "Whatever you say Jerma haha."
        y "{i}I wonder if Jex yells at him for being late too.{/i}"
        jump school2
    label jerma2:
        y "No reason. Just curious. That's all."
        show jerma neutral 
        j "Oh. Okay. If you say so."
        y "{i}What the heck's up with him? He's be acting weird since Jex showed up.{/i}"
        jump school2
    label jerma3:
        y "Well if he says he's the best of the best, I kinda want to see Jex in action."
        show jerma neutral 
        j "I can be pretty good too..."
        y "What?"
        j "Haha! Nothing!"
        jump school2
    label school2:
        show jerma neutral 
        j "Anyway, I was planning on showing you around the school. But, I kinda don't know where to start..."
        j "So I'll just let you walk around and figure it out yourself!"
        y "Wow... World's best tour guide..."
        j "Haha! Don't be like!"
        j "So, where to first [y]?"
        menu:
            "Go inside the school":
                jump locker_start
            "Go down the left road":
                jump left_road
            "Go down the right road":
                jump right_road

default jammed_locker = False
label entrance:
    hide jerma neutral
    show bg entrance day
    with blinds
    menu:
        "Go inside the school":
            jump locker
        "Go down the left road":
            jump left_road
        "Go down the right road":
            jump right_road
# The jammed locker is used as a plot point by Sus Guy in anyone's route. 
# Sus will mention that y/n's locker is jammed because of how many times he broke into it.
# Y/n rightfully freaks out because noboady knows about the jammed locker except for them and Jerma.
label locker_start:
    hide jerma neutral
    show bg lockers day
    with blinds
    y "I gotta change my shoes then."
    show jerma neutral
    with dissolve
    y "Jerma? Which one's my locker?"
    j "Let me see your paper."
    j "Hmm..."
    show jerma neutral at bounce, center
    j "I think it's this one. I'll put the code in for you since I'm so nice."
    y "Aw... Thanks Jerma!"
    "*rattling*"
    y "What's wrong? Did you put in the wrong code?"
    j "Oh no, don't worry. I remember this locker. This one gets jammed all the time."
    j "You're going to have to punch it to get it open. Like this!"
    "*punch*"
    j "Tada!"
    y "Thank you Jerma! I'll remember to... uh... punch it every time I open it."
    y "Wait. How did you know this locker is jammed?"
    j "Oh, because it used to be mine. I complained to the school because I was getting super annoyed with it."
    j "Oh well, looks like you're stuck with the jammed locker now, [y]! Haha!"
    y "Bastard..."
    j "Anyway... Where to next, [y]?"
    $ jammed_locker = True
    menu:
        "Go inside cafeteria":
            jump cafeteria_chef
        "Go down the left hall":
            jump left_hall
        "Go down the right hall":
            jump right_hall
        "Go outside the school":
            jump entrance
label locker:
    hide jerma neutral
    show bg lockers day
    with blinds
    menu:
        "Go inside cafeteria":
            jump cafeteria
        "Go down the left hall":
            jump left_hall
        "Go down the right hall":
            jump right_hall
        "Go outside the school":
            jump entrance

label cafeteria_chef:
    hide jerma neutral
    show bg cafeteria day
    with blinds
    y "The cafeteria's pretty nice."
    show jerma neutral at bounce, center
    with easeinright
    j "That's right! Usually the students here bring their own lunch."
    j "But for those who aren't as fortunate to eat their mom's cooking, they come here!"
    y "Huh. I guess I'm gonna be eating cafeteria food then."
    l "HEY! What the hell are you kids doing in here?!"
    l "School hasn't even started yet!"
    show jerma neutral at bounce, center
    j "Oops! Sorry lunch guy! We're just looking around. Don't mind us!"
    y "Who was that guy? Is he the chef?"
    j "Chef might be an over statement. He's the guy that serves our food."
    j "Don't worry, he's always this grumpy. You'll get used to it."
    y "If you say so."
    j "Where to next, [y]?"
    menu:
        "Go to the lockers":
            jump locker
        "Go to the left door":
            jump left_hall
        "Go to the right door":
            jump right_hall
        "Go to the front door":
            jump track_baseball

label cafeteria:
    hide jerma neutral
    show bg cafeteria day
    with blinds
    menu:
        "Go to the lockers":
            jump locker
        "Go to the left door":
            jump left_hall
        "Go to the right door":
            jump right_hall
        "Go to the front door":
            jump track

label track_baseball:
    y "Cool track. Looks like it's also baseball field."
    y "{i}I think I see some students practicin over there.{/i}"
    "Hey captian! Welcome back! How was your summer?"
    j "Pretty good! I assume you had a good one too!"
    y "It's nice to see you're still into baseball, Jerma!"
    y "But, when the fuck did you become the captian? You never mentioned it at all!"
    j "Just a few month ago! I guess I forgot to tell you. Haha!"
    y "Forgetful Andy..."
    y "So I guess this makes you the club prez then?"
    j "Yup! Jealous to see your best friend as the baseball captian now?"
    y "Eh... Not really."
    y "Oh! Do you mind if I ask you some questions about the Baseball Club!"
    j "OMG! Are you finally gonna play baseball with me?!"
    y "Uh... Sure. I'm still not good at sports so I'll think about it."

default base_do = False
default base_time = False
default base_day = False

label track:
    hide jerma neutral
    show bg track day
    with blinds

label track_baseball2:
    if base_do and base_time and base_day:
        jump track_baseball3
    menu:
        j "Ask away, [y]!"
        "What do you do here?"
        "When time does club start"

label kyudojo:
    show bg kyudojo day
    with dissolve

default kyudo_do = False
default kyudo_time = False
default kyudo_day = False

label kyudojo2:
    if kyudo_do and kyudo_time and kyudo_day:
        jump kyudojo3
    menu:
        x "So, any questions, beautiful?"
        "What do you do here?" if not kyudo_do:
            $ kyudo_do = True
            jump hall_do
        "What time does club start?" if not kyudo_time:
            $ kyudo_time = True
            jump hall_time
        "What day do you guys show up?" if not kyudo_day:
            $ kyudo_day = True
            jump hall_day
    label hall_do:
        y "What do you guys do in the Archery Club?"
        x "Pretty much all the basic stuff that involes kyudo. Bow safety, shooting, all that stuff."
        x "It's pretty simple for beginners to learn too. So anyone is welcome."
        x "Every time you come by and practice, your constitution and dexterity will increase."
        y "Oh cool! I'll be sure to think about it."
        x "Take all the time you need. We'll be seeing you future rookie."
        jump kyudojo2
    label hall_time:
        x "After school"
        jump kyudojo2
    label hall_day:
        x "Every Tuesday and Thursday."
        jump kyudojo2

label kyudojo3:
    y "Thanks for the talk Jex. I should be heading out now so see you!"
    x "Of course sweetheart. Come by anytime to see my amazing beauty."
    y "Uh... Sure..."
    x "You should probably leave quickly then. Your friend looks like he's about to kill someone with those eyes."

label classroom1:
    y "Woah."
    y "That guy's got one intense death stare."
    y "Is he looking at me? Kinda creepy not gonna lie."
    y "..."
    y "Damn... I wanted to sit in the back of the classroom near the window like a shounen protagonist."
    y "But this guy took the seat I wanted. *huff*"
    y "Whatever, I'll just take the seat next to him."
    y "Let's just hope he doesn't kill me when I least expect it."

    y "Hm... I wonder if that weirdo is still looking at me."
    y "Yup. Still looking at me."
    y "I feel like this guy has been staring at me for hours."
    y "..."
    y "Jesus Christ. It's giving me the heeby geebies."
    y "I should probably leave as quickly as possible so I don't have to deal with this tense atmosphere."
    "*zip*"
    y "Man, he sure is acting sus. Wonder what's up with him."

label road2:
    y "Wow. School was interesting today."
    y "*yawn* I'm so tired."
    "*russling*"
    y "{i}Huh.{/i}"
    y "{i}What the hell was that.{/i}"
    y "{i}It's so dark though. I doubt anyone is out this late at night.{/i}"
    y "Hello? Anyone one there?"
    "..."
    "......"
    "........."
    y "Okay... Probably just my imagination."
    y "Welp, time to go home and drown myself in soy sauce. It's well deserved."

label classroom_act1:
    M "And that is exactly why Bang Bang Bang is the best written song from the 2000s."
    M "HEY! Yeah youuuuu new kid! Are you even listening?!"
    y "Huh? Oh yeah I am-"
    M "If so then answer this question."
    M "What was the first inevation by the Mesopotamians?"
    y "But, you weren't even-"
    M "Answer the DAMN QUESTION!"
    menu:


label jerma_store:
    w "Hi! Welcome to the Jerma Store! If you need any help, let me know!"

# This section is Sus Guy's Good Ending. If anything, it's too messed up to be even called a good ending lmao. But, it's Sus Guy so *shrug*
if points >= 75:
    jump susgood_end
elif points <= 25:
    jump susbad_end
label susgood_end:
    s "So... What do you say [y]? Should I kill him?"
    menu:
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
        "Yes":
            jump susgoodend2
    label susgood_end2:
        j "[y]? What the fuck? You can't be serious!"
        y "Don't You undersand Jerma?"
        y "I only need Sus in my life."
        y "Don't need you anymore."
        j "[y] please! Let's talk it out! Can we-"
        b "*shing*"
        s "Now... Nobody stands in our way, [y]."
        s "Nobody will EVER stand in the way of our love."

return