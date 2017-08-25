##Pythong RPG Example
#IMPORT STATEMENTS----------------------
import cmd
import textwrap
import sys
import os
import time
import random
#END IMPORT STATEMENTS------------------

screen_width = 100

#### PLAYER SETUP ####
class player:
    def __init__(self):
        self.name = ''
        self.job = ""
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = "b2"
        self.game_over = False

myPlayer = player()

#### TITLE SCREEN ####

def title_screen_selections():
    option = input('->> ' )
    if option.lower() == ("play"):
        setup_game()
    elif option == ("help"):
        help_menu()
    elif option == ("exit"):
        sys.exit()
    while option.lower() not in ['play','help','quit']:
        print("please enter a valid command")
        option = input('->> ' )
        if option.lower() == ("play"):
            setup_game()
        elif option == ("help"):
            help_menu()
        elif option == ("exit"):
            sys.exit()  

def title_screen():
    os.system('clear')
    print("########################################")
    print("#       WELCOME TO THE TEXT RPG!       #")
    print("#             - PLAY -                 #")
    print("#             - HELP -                 #")
    print("#             - QUIT -                 #")
    print("########################################")
    title_screen_selections()

def help_menu():
    print('Type what you want to do such as play, help or quit')
    print('use up down left and right to move')
    print('use look to inspect something.')
    title_screen_selections()

## GAME INTERACTIVITY ##

def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('# ' + myPlayer.location.upper() + ' #')
    print('# ' + zonemap[myPlayer.location][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print('\n' + '===========================')
    print('What would you like to do?')
    action = input("-->>")
    acceptable_actions = ['move','go','travel','walk','quit', 'examine','inpsect','look']
    while action.lower() not in acceptable_actions:
        print("unknown action, try again.\n")
        action = input("-->>")
    if action.lower() == 'quit':
        sys.exit()
    elif action.lower() in ['move','go','travel','walk']:
        player_move()
    elif action.lower() in ['examine','inspect','interact','look']:
        player_examine()

def player_move():
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ["up","north"]:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ["down","south"]:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)
    elif dest in ["left","west"]:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ["right","east"]:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)


def player_examine():
    if zonemap[myPlayer.location][SOLVED]:
        print("You exhausted this zone already.")
        prompt()
    elif zonemap[myPlayer.location][UNSOLVED]:
        print("you look at shit.")
        prompt()
    else:
        print("It is a thing with a doodad.")
        prompt()


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location()






#### MAP ####
"""
a1, a2 ....
-----------------
|   |   |   |   | a4
-----------------
|   |   |   |   | b4 .....
-----------------
|   |   |   |   |
-----------------
|   |   |   |   |

"""
ZONENAME = ""
DESCRIPTION = 'description'
EXAMINATION = 'exam'
SOLVED = False
UP = 'up', 'north'
DOWN = 'down', 'south'
LEFT = 'left', 'west'
RIGHT = 'right', 'east'


solved_places = {'a1': False, 'a2': False,'a3': False, 'a4': False,
                 'b1': False, 'b2': True,'b3': False, 'b4': False,
                 'c1': False, 'c2': False,'c3': False, 'c4': False,
                 'd1': False, 'd2': False,'d3': False, 'd4': False
                 }

zonemap = {
    'a1': {
        ZONENAME: "Town Market",
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP: '',
        DOWN: 'b1',
        LEFT: '',
        RIGHT: 'a2',
    },
    'a2': {
        ZONENAME: 'Town Entrance',
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP:'',
        DOWN: 'b2',
        LEFT: 'a1',
        RIGHT: 'a3',
    },
    'a3': {
        ZONENAME: 'Town Square',
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP: '',
        DOWN: 'b3',
        LEFT: 'a2',
        RIGHT: 'a4',
    },
    'a4': {
        ZONENAME: 'Town Hall',
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP: '',
        DOWN: 'b4',
        LEFT: 'a3',
        RIGHT: '',
    },
    'b1': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP: 'a1',
        DOWN: 'c1',
        LEFT: '',
        RIGHT: 'b2',
    },
    'b2': {
        ZONENAME: '',
        DESCRIPTION: 'This is your home',
        EXAMINATION: 'Your home looks the same as every other shit hole',
        SOLVED: True,
        UP: 'a2',
        DOWN: 'c2',
        LEFT: 'b1',
        RIGHT: 'b3',
    },
    'b3': {
        ZONENAME: '',
        DESCRIPTION: 'description',
        EXAMINATION: 'exam',
        SOLVED: False,
        UP: 'a3',
        DOWN: 'c3',
        LEFT: 'b2',
        RIGHT: 'b4',
    },  
  }

#### GAME FUNCTIONALITY ####
def main_game_loop():
    while myPlayer.game_over is False:
        prompt()

def setup_game():
    os.system('clear')
    question1 = "hello, whats your name?\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("-->>")
    myPlayer.name = player_name
    
    question2 = "hello, whats your Job?\n"
    question2added = "you can play as warrior,mage,priest"
    for character in question2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_job = input("-->>")
    valid_jobs = ['warrior','mage','priest']

    if player_job.lower() in valid_jobs:
        myPlayer.job = player_job
        print(" you are now a " + player_job + "!!")
    while player_job not in valid_jobs:
        player_job = input("-->>")
        if player_job.lower() in valid_jobs:
            myPlayer.job = player_job
            print(" you are now a " + player_job + "!!")
    if myPlayer.job is 'warrior':
        self.hp = 120
        self.mp = 20
    if myPlayer.job is 'mage':
        self.hp = 40
        self.mp = 120
    if myPlayer.job is 'priest':
        self.hp = 60
        self.mp = 60

    question1 = "Welcome, " + myPlayer.name + " the " + player_job + ".\n"
    for character in question1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.05)
    player_name = input("-->>")
    myPlayer.name = player_name

    speech1 = "welcome to this fantasy world.\n"
    speech2 = "I hope it treats you well.\n"
    speech3 = "Just don't get to lost.\n"
    speech4 = "hehehehehe\n"


    for character in speech1:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)
 
    for character in speech2:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.03)

    for character in speech3:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.1)
 
    for character in speech4:
        sys.stdout.write(character)
        sys.stdout.flush()
        time.sleep(0.2)

    os.system('clear')
    print("###################################")
    print("Shall we start")
    main_game_loop()


title_screen()