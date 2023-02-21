define y = Character('Y/N')
define m = Character('Mom')
define a = Character('???')
define j = Character('Jerma985')
define J = Character('Jester985')
define x = Character('JEX Elbertson')
define s = Character('SusGuy')

#define gui.text_font = "ArchitectsDaughter.ttf"

transform bounce:
    yoffset 0
    easein .1 yoffset -30
    easeout .1 yoffset 0
    yoffset 0
    pass

label start:
    show bg room day
    y "Wow! What a beautiful morning!"
    y "I can't wait start my day and go to my first day at school tomorrow!"
    y "Fuck! I forgot to go to registration. How can I forget?!"
    y "It's alright, I'll just register online."
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
    y "Ugh... I didn't sleep to well..."
    m "Honey! Breakfast is ready!"
    y "COMING!"
    y "Bleugh... Why do I have to keep eating mom's cooking..."
    y "{i}I've always gotten sick eating anything she's made.{/i}"
    y "{i}Maybe it's the fact that she knows that I'm FUCKING LACTOSE INTOLERANT AND KEEPS PUTTING DAIRY IN MY FOOD.{/i}"
    y "{i}Forget the upset stomatch. Today's my first day at school and I'm so excited!{/i}"
    y "{i}I've got all my classes right her"

label road1:
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
        jump road2
    label morning1_b:
        y "Eh. It's alright I guess."
        j "Oh. Okay then."
        jump road2
    label morning1_c:
        y "Ugh... It was awful Jerma. I was so tired this morning that I wanted to stay in bed."
        j "Geez. Sorry about that. I know how you feel."
        jump road2

label road2:
    j "Anyway, let's get to school quickly!"
    j "We're gonna be late!"
    hide jerma neutral

label school1:
    show bg entrance day
    with fade
    y "Wow... So this is Jermaverse Academy. It's so big..." 
    show jerma neutral at bounce, center
    with easeinright
    j "I heard the school's priciple funded the enter thing! I heard he's incredibly loaded."
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
    show jerma neautal at center
    with easeinleft
    j "..."
    j "...Um"
    j "Hey... Sorry about that. Jex can be a little-"
    y "Oh no, it's fine! I think Jex is a great guy!"
    j "...So that's your type, huh..."
    y "What?"
    j "Oh- Uh- I said that's how it is!"
    y "Okay..."
    y "So, I think Jex said something about you coming by the shooting range. I didn't know you were in the Rifle Club Jerma!"
    j "Ha. Well, I've always been interested in guns and stuff."
    y "Maybe I should stop by the shooting range too..."
    j "What? Don't tell me you're going there to see that jerk!"
    menu:
        "What no way! I'm going because you're in it!":
            jump
        "Oh. No reason really.":
            jump
        "Heck yeah! I want to see Jex in action!":
            jump 
label school2:
    j "Alrighty, so where to first?"
    menu:
        "Lockers"
        "Left road"
        "Right road"
    

return