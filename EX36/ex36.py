from sys import exit


def health(i, n):
    health = 1 + n
    health = health - i
    print "  *  Your current health points: %d / 3  *  " % health
    if health == 0:
        dead("You used up all your health, game over,")



def instruction():

    print """
    Instructions:
    1. Your health points is 1/3 when you start the game.
    2. You can find the extra health points when you explore
    3. If the health points is equal to zero, the game is over.

    Enter "okay" if you read the instructions.
    """

    confirm = raw_input("> ")
    if "okay" in confirm or "Okay" in confirm or "OK" in confirm or "ok" in confirm:
        start()
    else:
        dead("Man, please read the instructions.")


def dining_room():

    print "You walk into the dining room."
    print "There is a box on the dining table."
    print "What will you do?"
    box_moved = False

    while True:
        choice = raw_input("> ")

        if choice == "open":
            print "You find letters inside the box."
        elif choice == "move" and not box_moved:
            print "Nothing happens."
            print "You can also shake it."
            box_moved = True
        elif choice == "shake" and box_moved:
            dead("The box exploded!")
        else:
            print "Try move it , open it or shake it."




    print "This room is full of gold. How much do you take?"

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")

def kitchen():
    print "You enter to the kitchen."
    print "There is a refrigerator and cupboard."
    print "You decide to get some food."
    print "Which one will you open?"
    choice = raw_input("> ")

    if choice == "refrigerator":
        food = ['rotten apple', 'rotten egg', 'rotten meat']
        print "The food: %s" % food
        choice_food = raw_input("> ")
        if choice_food == 'rotten meat':
            print "You eat the meat and your health point + 1"
            health(-1, 0)
            print "You walk out of the kitchen."
            toilet2()
        elif "rotten egg" in choice_food or "rotten apple" in choice_food:
            dead("Oops, you cannot eat vegetables, it is poisonous to you.")
        else:
            dead("You stumble around the kitchen until you starve to dead.")
    elif choice == "cupboard":
        print "unfortunatly, it's empty."
        kitchen()


def toilet2():
    print "You enter to the toilet."
    print "Here you see the mirror and the sink."
    print "The mirror is destroyed by some shape stuff, probably a hammer."
    print "You decide to search around or walk toward the mirror."

    choice = raw_input("> ")

    if "walk toward the mirror" in choice or "walk " in choice or "mirror" in choice:
        print "You look into the mirror"
        print "A tall man with grey skin is standing in front of the mirror"
        print "His skin is putrid, he or it looks like a zombie."
        print "Who is it?"
        print "er......Is it me?"
        print "hmm......my memory is fragmented"
        print "I was hurted by a zombie. And I became a zombie."
        print "I will eat whatever I saw including human."
        print "This is the reason why I locked myself here since I don't want to hurt any of my friends and family"
        dead("You remember you are the zombie and stay in the house.")

    elif "search around" in choice or "search" in choice:
        print "You find a hammer"
        print "It seems hard enough to break the window."
        choice_hammer = raw_input("> ")
        if "break the window" in choice_hammer or "break" in choice_hammer or "window" in choice_hammer or "break window" in choice_hammer:
            print "You broke the window and walk out to the street."
            print "A man is shouting at you, 'Help! Here is a zombie!'"
            print "You hear a gunshot and see someone is shooting at you."
            print "Your health point - 1"
            health(1,1)
            print "It hurts but you can still move."
            print "You scratch the man and escape successfully."
            exit(0)
    else:
        print "%r is not a good choice," % choice
        dead("You stumble around the toilet until you starve to dead.")


def toilet():
    print "You enter to the toilet."
    print "Here you see the mirror and the sink."
    print "The mirror is destroyed by some shape stuff, probably a hammer."
    print "You decide to search around or walk toward the mirror."

    choice = raw_input("> ")

    if "walk toward the mirror" in choice or "walk " in choice or "mirror" in choice:
        print "You look into the mirror"
        print "A tall man with grey skin is standing in front of the mirror"
        print "His skin is putrid, he or it looks like a zombie."
        print "Who is it?"
        print "er......Is it me?"
        print "hmm......my memory is fragmented"
        print "I was hurted by a zombie. And I became a zombie."
        print "I will eat whatever I saw including human."
        print "This is the reason why I locked myself here since I don't want to hurt any of my friends and family"
        dead("You remember you are the zombie and stay in the house.")
    elif "search around" in choice or "search" in choice:
        print "You find a hammer"
        print "It seems hard enough to break the window."
        choice_hammer = raw_input("> ")
        if "break the window" in choice_hammer or "break" in choice_hammer or "window" in choice_hammer or "break window" in choice_hammer:
            print "You broke the window and walk out to the street."
            print "A man is shouting at you, 'Help! Here is a zombie!'"
            print "You hear a gunshot and see someone is shooting at you."
            health(1,0)
    else:
        print "%r is not a good choice," % choice
        dead("You stumble around the toilet until you starve to dead.")

def dead(why):
    print why, "Try again!"
    exit(0)

def start():
    print "You wake up in the dim house and you feel hungry."
    print "The house is quite familiar to you, maybe you have been to here before."
    print "When you decide to open the door of the house, you discover the door is locked by someone..."
    print "So, you start to look around and find the way out."
    print "There is a kitchen, toilet and dining room."
    print "Which one do you choose to go?"
    health(0, 0)

    choice = raw_input("> ")

    if choice == "kitchen":
        kitchen()

    if choice == "toilet":
        toilet()

    if choice == "dining room":
        dining_room()
    else:
        print "%r is not a good choice," % choice
        dead("You stumble around the house until you starve to dead.")

instruction()
