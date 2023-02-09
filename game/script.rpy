define y = Character('Y/N')
define a = Character('???')
define j = Character('Jerma985')
define J = Character('Jester985')
define x = Character('Jex')
define s = Character('SusGuy')

label start:
    show bg room day
    y "Wow! What a beautiful morning!"
    y "I can't wait start my day and go to my first day at school tomorrow!"
    y "Fuck! I forgot to go to registration. How can I forget?!"
    y "It's alright, I'll just register online."
    y "Thank the heavens for technology."
    with fade

label road1:
    show bg road day
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
        j "That's great! I'm so happy you're doing well."
        jump road2
    label morning1_b:
        y "Eh. It's alright I guess."
        j "Oh. Okay then."
        jump road2
    label morning1_c:
        j "Geez. Sorry you had such bad morning."
        j "Hope you feel better!"
        jump road2

label road2:
    j "Anyway, let's get to school quickly!"
    j "We're gonna be late!"

label school1:
    show entrance day
    with fade
    show jerma neutral
    y "Wow... So this is Jermaverse Academy. It's so big..."
    y "I heard the school's priciple funded the enter thing! I heard he's incredibly loaded."
    a "Well, well, well... If it isn't Jerma985. Who's the cutie standing next to you?"
    y "Huh?"
    show jex neutral
    with easeinleft
    y "{i}Holy shit! What a hottie!{/i}"
    j "Hey! Fuck off Jex! If you even have a thought about flirting with"
    x "You sure have balls to talk to your senior like that Jerma."
    x "Anyway, what's your name beautiful?"
    y "Um... Its"

return