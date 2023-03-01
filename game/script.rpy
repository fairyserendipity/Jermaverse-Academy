define y = Character('Y/N')
define m = Character('Mom')
define a = Character('???')
define j = Character('Jerma985')
define J = Character('Jester985')
define x = Character('JEX Elbertson')
define s = Character('Sus Guy')
define b = Character(' ')
define w = Character('Jerma Store Worker')

$ jermabucks = 0
$ items = []
$ gifts = []
default points = 25

# Code for items and inventory
init -1 python:
    import renpy.store as store
    import renpy.store as renpy
    from operator import attrgetter 
    inv_page = 0
    item = None 
    

#define gui.text_font = "ArchitectsDaughter.ttf"

transform bounce:
    yoffset 0
    easein .1 yoffset -30
    easeout .1 yoffset 0
    yoffset 0
    pass

label start:
    show bg room night
    y "Phew! I'm pooped!"
    y "I can't wait start my day and go to my first day at school tomorrow!"
    b "*shuffling*"
    y "..."
    y "Fuck! I forgot to go to registration. How can I forget?!"
    y "Oh right. I can just register online."
    y "Thank the heavens for technology."
    label name1:
        $ y = renpy.input("Now time to put my name...")
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
        "It/Its":
            $ sub = "it"
            $ con = "its"
            $ obj = "its"
            $ poss = ""
            $ poss_adj = 
            $ ref = 
        "Xe/Xem":
            $ sub = 
            $ con = 
            $ obj = 
            $ poss = 
            $ poss_adj = 
            $ ref = 
        "E/Em":
            $ sub = 
            $ con = 
            $ obj = 
            $ poss = 
            $ poss_adj = 
            $ ref = 
        "Ze/Hir":
            $ sub = 
            $ con = 
            $ obj = 
            $ poss = 
            $ poss_adj = 
            $ ref = 
        "Fae/Faer":
            $ sub = 
            $ con = 
            $ obj = 
            $ poss = 
            $ poss_adj = 
            $ ref = 
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
    with dissolve
    y "Ugh... I didn't sleep to well..."
    m "Honey! Breakfast is ready!"
    y "COMING!"
    y "Bleugh... Why do I have to keep eating mom's cooking..."
    y "{i}I've always gotten sick eating anything she's made.{/i}"
    y "{i}I wish dad was here in the morning instead...{/i}"
    y "{i}Forget the upset stomatch. Today's my first day at school and I'm so excited!{/i}"
    y "{i}I've got all my classes right here."
    y "{i}Haha... I know I'm gonna have trouble looking for the right rooms...{/i}"


label startroad1:
    show bg road day
    with fade
    y "Wow! What a beautiful day!"
    y "Surely noone is gonna run into me while I'm trying to appreciate the nice sky!"
    y "...Wait"
    y "What's that sound? It sound like someones running-"
    show jerma running
    with hpunch
    y "OOF!"
    hide jerma running
    y "Hey! What the hell?! Watch where you're going-"
    show jerma neutral
    with dissolve
    y "Jerma! Where were you? I've waiting this entire time!"
    show jerma neutral at bounce
    j "Omg, I'm so sorry! I forgot to set the timer on my phone and- and- I totally forgot!"
    y "Jerma, you dunce! Quit being a late Andy and actually show up when I tell you to!"
    y "{i}This is Jerma985. My childhood best friend. We've known each other ever since we were in kindergarden!{/i}"
    y "{i}We sadly had to split to different high schools. But, my dad found a new job in this area so I was able to register for Jermaverse Academy!{/i}"
    y "{i}When I told Jerma, he was so estatic that he wouldn't shut up about it.{/i}"
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
    j "I heard the school's principle funded the enter thing! I heard he's incredibly loaded."
    a "Well, well, well... If it isn't Jerma985. Who's the cutie standing next to you?"
    y "Huh?"
    show jerma neutral at right
    show jex neutral at left
    with easeinleft
    y "{i}Holy shit! What a hottie!{/i}"
    y "{i}Oh my God! I can't believe I've seen someone this attractive before!"
    y "{i}Wha- What do I say...? I'm so nervous...!"
    hide jerma neutral
    show jerma angry at bounce, right
    j "Hey! Fuck off Jex! If you even have a thought about flirting with [y] I swear I'll-"
    show jex neutral at bounce
    x "You sure have balls to talk to your senior like that Jerma."
    show jex neutral at bounce
    x "Anyway, what's your name beautiful?"
    y "Um... Its [y]... I'm a second year student here."
    x "[y]... That's a nice name."
    x "You said you were a second year, right? I don't think I've ever seen your face around here before."
    y "Oh! Uh- I just transferred here so... That might explain it."
    x "Ah... So you're a transfer. I see."
    x "Excuse my rudeness. My name is JEX Elbertson. But for you hon, you can call me Jex."
    x "I'm a third year at Jermaverse Academy and the president of the Rifle Club. What do you think of it so far?"
    y "Oh! It's really nice! It looks so much better in person too!"
    x "Glad you like it here. Hope you enjoy your stay."
    x "Oh, and Jerma. Make sure you bring your cute friend with you next time to come by the shooting range. See you around sweetheart."
    hide jex neutral
    with easeinleft
    show jerma neutral at center
    with easeinleft
    j "..."
    j "...Um"
    show jerma neutral at bounce, center
    j "Hey... Sorry about that. Jex can be a little-"
    y "Oh no, it's fine! I think Jex is a great guy!"
    j "...So that's your type, huh..."
    y "What?"
    j "Oh- Uh- I said that's how it is!"
    y "Okay..."
    y "So, I think Jex said something about you coming by the shooting range. I didn't know you were in the Rifle Club Jerma!"
    j "Ha. Well, I've always been interested in guns and stuff."
    y "Maybe I should stop by the shooting range too..."
    show jerma angry at bounce, center
    j "What? Don't tell me you're going there to see that jerk!"
    menu:
        "What no way! I'm going because you're in it!":
            jump jerma1
        "Oh. No reason really.":
            jump jerma2
        "Heck yeah! I want to see Jex in action!":
            jump jerma3
    label jerma1:
        y "No silly! I'm going because you're in it!"
        j "Oh yeah! Haha!"
    label jerma1:
        $ j += 2
    label jerma2:
        $ j = 0
    label jerma3:
        
label classroom1:
    y "Woah."
    y "That guy's got one intense death stare."
    y "Is he looking at me? Kinda creepy not gonna lie."
    y "..."
    y "Damn... I wanted to sit in the back of the classroom near the window like a shounen protaginist."
    y "But this guy took the seat I wanted. *huff*"
    y "Whatever, I'll just take the seat next to him."
    y "Let's just hope he doesn't kill me when least expected."

    y "Hm... I wonder if that weirdo is still looking at me."
    y "Yup. Still looking at me."
    y "I feel like this guy has been staring at me for hours."
    y "..."
    y "Jesus Christ. It's giving me the heeby geebies."
    y "I should probably leave as quickly as possible so I don't have to deal with this tense atmosphere."
    b "*zip*"
    y "Man, he sure is acting sus. Wonder what's up with him."

label road2:
    y "Wow. School was interesting today."
    y "*yawn* I'm so tired."
    b "*russling*"
    y "{i}Huh.{/i}"
    y "{i}What the hell was that.{/i}"
    y "{i}It's so dark though. I doubt anyone is out this late at night.{/i}"
    y "Hello? Anyone one there?"
    b "..."
    b "......"
    b "........."
    y "Okay... Probably just my imagination."
    y "Welp, time to go home and drown myself in soy sauce. It's well desearved."


label jerma_store:
    w "Hi! Welcome to the Jerma Store! If you need any help, let me know!"
    menu:
        "Salmon"
        "Beef"
        "Pork"
        "Pasta"
        "Rice"
        "Flour"
        ""

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