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

label jester_firstday:
    y "{i}Alright. Today is my first day at the Drama Club!{/i}"
    y "{i}Wow. There's not that many people here. I wonder why.{/i}"
    a "[y]? Is that you?"
    y "Omg! Miku! You're in this club"

label jester_b:
    e "Hey I've got something to tell you!"
    y "Oh? What is it Jester?"
    e "I'm no traitor. But~ I can't really keep it in longer."
    e "You know Jerma?"
    y "Yeah duh."
    e "Well... he has a crush on you!"
    y "What! He does?!"
    y "H-how do you know?"
    e "Because its soooo obvious, duh~"
    e "For an observate person, you're pretty dense [y]."

label jester_h:
    y "It's so interesting..."
    e "Huh? What is?"
    y "You're always so goofy and free spirited."
    y "But... You're kind of a people pleaser, huh."
    e "Oh? What makes you say that?"
    y "I mean, no one can really see it. But, you've always been known as a troublemaker for a long time and people kind of expect that from you."
    y "That's why its normal for people to back away from you because of your personality."
    e "Well... Yeah! I am pretty weird after all."
    y "But, for anyone who does get close to you, you go so flustered and awkward."
    e "Oh, really?"
    y "Yeah! It's cute but also kind sad."
    y "You sort of push people away because that's what you're used to. I noticed it the first time we met."
    y "But, over time you stopped. Why?"
    e "..."
    e "Ha..."
    e "You've really hit the nail on the head for that one."
    e "Honestly, I didn't except you join the Drama Club because of how close you were to Jerma."
    e "Then you showed up and... I became disoriated."
    e "It was the first time I ever felt this way. I became so confused."
    e "So, I just acted how I normal did, hoping to drive you away like everyone else."
    e "But you were so persistent and practiced like no one I have seen before."
    e "You are a damn, good actor. I salute to that."
    e "But, even now I'm still questioning why."
    e "You should be with Jerma! Not me!"
    e "After all you guys share feeling for each other! He desearves you, not his stupid, idiot brother!"
    y "Woah woah woah. Hold it there e-clown."
    y "I never said I liked Jerma back."
    e "H- Oh wait. You didn't?"
    e "..."
    e "Oh."
    e "Well."
    e "Then, who do you like?"
    y "Not telling."
    e "Aw~ Come on! I thought we promised to exchange secrets!"
    y "Well techically you shared someone elses secret with me so it doesn't count."
    e "Damn you got me there. Haha!"
    y "We talked and talked until school was finally over."
    y "I was so glad Jester shared his true nature with me."
    y "Well technaclly I kinda forced it out but..."
    y "..."
    y "Abviousley I couldn't tell Jester I liked him."
    y "If I was gonna share a secret, I was better off sharing someone elses than my own."
    y "The last thing I want is to ruin is my friendship with Jester and Jerma at the same time.."

label jester_prom:
    "In which I am offering myself to you."
    "!!!"
    "Jester... You're... offering me your flute?"
    "Yes. This flute has always been with me since birth. It represent me as a person so much that I consider it to be a part of me."
    "And... I want you to have it."
    "But... Your flute means so much to you."
    "Is it really okay?"
    "Of course! After all, I want to show you my true self this time. No more faking!"
    "Kinda ironic coming from an actor."
    "After all I can always just buy a new one."
    "Ugh... It's kinda sticky."
    "Where has this flute been?"
    "Teehee! It's a secret!"
    "Motherfucker! I thought we promised to not keep secrets!"
    "Hehe! If you really think its too much than you can just throw it in the washer!"
    "But, wouldn't it break?"
    "Nah! It's pretty surdy. It can take way harder hits and still be intack."

    