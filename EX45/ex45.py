from sys import exit
from random import randint
from Tkinter import *
import time
import calendar
import random
items = [];


class Scene(object):

    def enter(self):
        # if the function enter is not defined yet, you can see the above sentence.
        print "This scene is not yet set."
        exit(1)

class Engine(object):
    # initiate the map
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finised_game')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # be sure to print out the last scene
        current_scene.enter()

class GameItems(Scene):
    def enter(self):
        # special scene
        print "You found something!"
        print "Your current items: ", items
        # use choice to randomly get a string
        a = random.choice(["Apple", "Orange", "Pears", "Coins"])
        items.append(a);
        print "You found the: ", a
        print "\n"
        print "Your items:", items
        print "\n"
        b = random.choice(['end_game', 'room_with_pic'])
        return b

class EndGame(Scene):
    # random choose a sentence
    sentence = [
"A bad choice may lead to dead.",
"Game over",
"It is better to try again, come back later!",
"You trapped in the grave and starve to death."

    ]

    def enter(self):
        print EndGame.sentence[randint(0, len(self.sentence)-1)]
        exit(1)


class EntranceOfGrave(Scene):
    # first scene
    def enter(self):
        print "A creepy voice that comes from the sulpture in the grave:"
        print "Welcome to the grave of King Padraig."
        print "As a guardian, I must warn you."
        print "This is a place which full of treasure. However the the chance of being killed is 89%"
        print "\n"
        print "What is your choice?"
        print "* Hint: enter, destroy the sculpture or beg *"


        choice = raw_input("> ")
        if choice == "enter":
            return 'room_with_pic'
        elif choice == "destroy":
            return 'end_game'
        elif choice == 'beg':
            return 'game_items'
        else:
            print "I don't understand your choice."
            return 'entrance'



class RoomWithPic(Scene):

    def enter(self):
        print "The door slowly opened in front of you."
        print "You gaze into the darkness inside the door and walk towards it."
        print "\n"
        print "* You find a touch near the entrance, you have no idea who leave it here. *"
        print "\n"
        items.append("touch");
        print "Your current items: ", items
        print "It seems quite useful, isn't it?"
        print "Are you sure to use the touch?"

        choice = raw_input('> ')

        if choice == "yes" or choice == "Yes":
            print "You switch on the touch and can barely see the room."
            print "\n"
            print "\n"
            print "You find a paper on the ground"
            print "* Hint: It is better for you to remember the number of square *"
            print "Close it if you are finished reading it."
            #sets the  __name__ variable to have the value "__main__"
            if __name__ == '__main__':
                can = Tk()
                can.title('Canvas')
                # setup a canvas with width and height to draw squre on it
                canvas = Canvas(can,width = 400,height = 400,bg = 'yellow')
                # draw the first squre
                a = randint(100,300)
                b = randint(100,300)
                x0 = a
                y0 = a
                y1 = b
                x1 = b
                for i in range(6):
                    # draw the othe square by using for loop
                    # get random number using randint in random
                    canvas.create_rectangle(x0,y0,x1,y1)
                    x0 = randint(100,300)
                    y0 = x0
                    x1 = randint(100,300)
                    y1 = x1

                canvas.pack()
                can.mainloop()
            print "You saw a old square sculpture, it has ten button (0-9)"
            print "Which one would you choose?"
            print "* Hint: the answer is related to the paper you discoverd. *"


            ans = raw_input("> ")

            if ans == "6":
                print "Hmmm."
                print "OK, you can pass now."
                return 'roome_with_cal'
            elif ans == "beg":
                return 'game_items'
            else:
                print "It's not a good choice."
                return 'end_game'



class RoomWithCal(Scene):

    def enter(self):
        print "A secret door is opened."
        print "You find some sketch on the wall."
        print "You walk closer to see what is it."
        print "\n"
        # import the time and use the calendar function
        cal = calendar.month(1800, 1)
        print "It is a calendar:"
        print cal;
        print "\n"
        print "You keep walking on the room and find a box"
        print "It seems that you need the password to open the combination lock on the box"
        print"* Hint: first Wednesday, second Monday, third Sunday"

        ans = raw_input("> ")

        if ans == "11326":
            print "Correct!"
            print "You opened the box and get the key."
            print "You opended the door next to you."
            print "\n"
            return 'the_library'
        else:
            print "BOOM!!!"
            return 'end_game'


class TheLibrary(Scene):

    def enter(self):
        print "You enter the the_library."
        print "The guardian said, "
        print "'No, you cannot pass through, unless you have a password(3 digits)'"
        print "You have 5 chance to do it."


        correct_ans = "%d%d%d" % (randint(1,9), randint(1,9), randint(1,9))
        #I use the print function to get the answer directly and check the game
        #print correct_ans
        ans = raw_input("Your answer> ")
        ans_count = 0

        while ans != correct_ans and ans_count < 5:
            print "Try again!"
            ans_count += 1
            ans = raw_input("> ")

        if ans == correct_ans:
            print "Lucky!"
            print "\n"
            return 'escape_room'
        else:
            print "Guardian said, 'Wrong!'"
            return 'end_game'


class EscapeRoom(Scene):

    def enter(self):
        print "Through a whole day of scare and suffering,"
        print "You finally reach to the last room."
        print "The coffin located at the middle of the room"
        print "You saw a small line of text:"
        print "\n"
        print "If you want to leave, you should knock the coffin with the correct times."
        print "* Hint from 1-9 *"


        correct_ans = randint(1,9)
        #check using print
        #print correct_ans
        ans = raw_input("> ")


        if ans == correct_ans:
            # do the count down by using function sleep and while-loop
            print "You hear a weird sound comes out from the coffin"
            count = 0
            n = 5
            while (count < n):
                ncount = n - count
                print ncount
                time.sleep(1)
                count += 1
            print "You cannot open the coffin."
            return 'end_game'
        else:
            print "You hear a weird sound comes out from the coffin"
            count = 0
            c = 5
            while (count < c):
                ncount = c - count
                print ncount
                time.sleep(1)
                count += 1
            print "\n"
            print "You won!"
            print "\n"
            return 'finised_game'

class FinishedGame(Scene):

    def enter(self):
        print "You won the game! Good job."
        print "You take along your inventories %s and go home." %items
        return 'finised_game'

class Map(object):
    # set up the map
    scenes = {
        'entrance': EntranceOfGrave(),
        'room_with_pic': RoomWithPic(),
        'roome_with_cal': RoomWithCal(),
        'the_library': TheLibrary(),
        'escape_room': EscapeRoom(),
        'game_items': GameItems(),
        'end_game': EndGame(),
        'finised_game': FinishedGame(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

game_map = Map('entrance')
game = Engine(game_map)
game.play()
