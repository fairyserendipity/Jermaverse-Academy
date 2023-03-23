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
    
label start:
    show bg room night
    with fade
    y "Hnnn..."
    y "It's so early..."
    y "{i}Ugh... I barley got any sleep...{/i}"
    y "..."
    y "{i}I can't go back to sleep either...{/i}"
    "*shuffling*"
    y "{i}I guess I'll go to school early.{/i}"
    y "{i}Is the practice hall even open during this time?{/i}"
    y "Better to check than feel sorry."
    show bg kyudojo morning
    with fade
    y "It's so damn foggy. How can you even train in this weather?"
    y "Wait. Is there someone already here?"
    y "...!"
    y "It's... Jex? What's he doing here at this hour?"
    y "..."
    y "His form is incredible. No wonder he's the club president."
    y "I... I can't believe what I'm watching...!"
    y "He's so focused and serious. I've never seen him like this."
    x "*pant* Not good enough..."
    y "Um... Hey Jex!"
    x "Oh- Hey [y]! W-What are you doing here? School hasn't even started yet."
    y "Yeah I know. I woke up wayyyy early than I thought so I thought it'll be a good idea to train my archery skills."
    x "Oh... I that so..."
    y "{i}Is Jex okay? I've never seen him this stressed before.{/i}"
    y "Jex. You looked amazing when you were shooting!"
    y "The form, the contact, I've never seen you this serious before!"
    x "Hah... So you thinks that's amazing?"
    x "Well, it's not good enough for me."
    y "What? How can you get better than that?"
    x "I have to get better than them."
    x "If I can't... Then I'm a failure..."
    y "No... Jex, you're not a failure."
    x "[y], do you know why I'm so scrict with everyone here except for everyone else?"
    y "No, why?"
    x "Because it's the only thing that is holding up my dignity."
    x "You know how Jeremy is my cousin right?"
    x "Our family is notorius for holding high standards."
    x "I'm already seen as a failure by my behavior and attitude."
    x "All I've been known for is being a playboy with no care in the world."
    x "So I started doing archery to help fill in that hole."
    x "But, all people who wanted to join used it as an excuse to get close to me and not care for the art form."
    y "And... That's why people kept leaving the Archery Club. Right?"
    x "Exactly. I was known for being too strict and serious that I didn't fit into everyone's playboy fantasy."
    x "So, I thought if I was the one to carry our team we might have a chance."
    x "But... I'm just so far away from my goal."
    x "No matter how hard I try... I just- I just can't get better."
    y "Jex... I... I'm so sorry that you feel that way."
    x "Don't apologize, [y]. It isn't your fault."
    x "I should be the one that's sorry. I'm sorry for using my charms to get what I want..."
    x "But... For some reason, you were the only person who didn't imediently fall for me and chose to stay for this long. Why?"
    y "I like archery, Jex. That's why. You made something that was complicated easy for me to understand."
    y "Seeing you care so much about it made me want to care too."
    y "And... I don't want you to tread this path alone. If you don't mind."
    y "Come on! Let's practice together. Even if we aren't at our best, it's nice to just be here with someone."
    x "Ha. I guess you're right. Pick up your bow, [y]! We're going to be here until sunrise."
    with fade
    y "{i}Jex and I shot arrows until the school bell rang. It was probably the best practice section I've ever had.{/i}"
    y "{i}I got to learn more about Jex. His goals and his struggles. It made him feel so much more human.{/i}"
    y "{i}Seeing his vulnerable side, his true self, made me feel so...{/i}"
    y "..."
    y "{i}There's no way I'm in love with him haha...{/i}"
    y "{i}Like he'll ever love me back.{/i}"
    y "..."
    y "{i}I just hope he's happy no matter what. Even if the person he loves isn't me.{/i}"
    y "{i}What am I even thinking of winning over a playboy's heart?{/i}"

label jex_valentines:
    y "Today's the day! It's Valentines Day!"
    y "I can't wait to give my gift to Jex hehe."
    y "Spent all of last night making these chocolates. I hope they're not too bad."
    y "There he is! He looks a lot better now. Thank god."
    y "Oh. He's surrounded by girls obviously."
    g "Hehe~ Do you like them Jex?"
    x "Yes sweetheart. They're quite lovely."
    G "What about mine Jex? How's my gift?"
    x "I think they're all wonderful in their own unique way."
    "Aw come on! You gotta pick your favorite!"
    "Yeah Jex! Which one do like best."
    "*giggling*"
    y "I think I'll just leave then."
    y "Forget it. Why even try?"
    a "WAIT!!!"
    x "*pant* Wait... *pant* [y]... *pant* please..."
    y "Oh Jex! Do you need something?"
    y "Hold on, sit down. You look like you're gonna die"
    x "No thanks... The floor is dirty."
    y "No fucker, I mean the bench."
    y "So... did you need something from me? It must be pretty urgant if you ran all the way here for me."
    x "Oh no. It's nothing really. I just wanted to see if you were here today."
    x "I didn't see you all morning! Were you late or something? You're notoriusly known for being early."
    y "I was here the whole time actually haha. I guess you didn't see me."
    x "Is that so. Make sure to come to the hall to practice then! See you later."
    y "Wait! Uh-"
    x "What is it, [y]?"
    y "Uh- So you know how today's Valentines Day right? I got you something."
    x "Holy shit. Did you make this?"
    y "Yeah, I actually spent all night."
    x "Wow. You know, I've been andicipating this entire time haha!"
    x "I was excited about getting your gift the most!"
    y "Wait really? But you got so many from those girls."
    x "Well, I get them every year so it doesn't really matter much to me."
    x "But this gift from you means so much to me because it's from someone I know."
    y "Haha! Yeah. Think of it as a friend to a friend."
    x "Yeah sure. I'll see you later then [y]."