
label start:

define y = Character('Name')

define j = Character('Jerma985')
define J = Character('Jester985')
define x = Character('Jex')
define s = Character('SusGuy')

show bg room

y "Wow! What a beautiful morning!"
y "I can't wait start my day and go to my first day at school tomorrow!"
y "Fuck! I forgot to go to registration. How can I forget?!"
y "It's alright, I'll just register online."
y "Thank the heavens for technology."

with fade

label road:
    show bg road
	y "Wow! What a beautiful day!"
	y "Surely noone is gonna run into me while I'm trying to appreciate the nice sky!"
	y "...Wait"
	y "What's that sound? It sound like someones running-"
	y "OOF!"
	y "Hey! What the hell?! Watch where you're going-"
	show jerma confused
        with fade
	y "Jerma! Where were you? I've waiting this entire time!"
	j "Omg, I'm so sorry! I forgot to set the timer on my phone and- and- I totally forgot!"
	y "Jerma, you dunce! Quit being a late Andy and actually show up when I tell you to!"
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
    jump morning1

label morning1_b:
    j "Oh. Ok."
    jump morning1

label morning1_c:
    j "Geez. Sorry you had such bad morning."
    j "Hope you feel better!"
    jump morning1

label morning1:
    j "Anyway, let's get to school quickly!"
    j "We're gonna be late!"

return
