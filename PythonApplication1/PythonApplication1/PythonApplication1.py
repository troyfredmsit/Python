##Import statements
import random
import math
import os

## This is an RPG game that has no set class and actively hunts the player as they try to get through the missions.
## The system will revolve around the required stats to use anything from gear to spells to skills.
# STR - adds to carry ability, damage with weapons
# END - adds to HP and tired stat
# INT - Adds to mana pool and ability to understand complexity.
# AGL - Adds to % hit and parry and stealth



class Character():
    def __init__(self):
        self.name = ""
        self.current_hp =100
        self.max_hp = 100
        self.current_weapon = "unarmed"
        self.inventory = []
        self.armor = 0
        self.magic_resist = 0
        self.STR = 5
        self.AGL = 5
        self.END = 5
        self.INT = 5
        self.base_damage = 5

    def getSTR(self):
        return self.STR
    def getAGL(self):
        return self.AGL
    def getEND(self):
        return self.END
    def getINT(self):
        return self.INT
    def getcurrent_hp(self):
        return self.current_hp
    def getcurrent_weapon(self):
        return self.current_weapon

    def setSTR(self,STR):
        self.STR = STR
    def setAGL(self,AGL):
        self.AGL = AGL
    def setEND(self,END):
        self.END = END
    def setINT(self,INT):
        self.INT = INT
    def setcurrent_hp(self,damage):
        self.current_hp = current_hp - damage
    def setcurrent_weapon(self,weapon):
        self.current_weapon = current_weapon
    def setname(self,name):
        self.name = name

def MainLoop():
    #get a start menu up
    #get the player to give us a name
    #allocate stats
    #start game.
    MainMenu()

def MainMenu():
    print("Welcome to an RPG adventure!")
    print("############################")
    print("#  Please chose an option  #")
    print("#  1) PLAY                 #")
    print("#  2) LOAD                 #")
    print("#  3) EXIT                 #")
    Choose = input("->>")
    if Choose == '1':
        Play()
    elif Choose == '2':
        Load()
    elif Choose == '3':
        os.system('exit')
    else:
        print("Please choose a viable option 1-3")
        MainMenu()
def Play():
    print("Welcome to the world ov vengence where you can be anything you like.")
    print("There are no classes traveler, just choices. Stats will unlock abilities, skills and capabilities")
    print("But choose wisely, to much emphasis on one stat may hurt you later!")
    choice = input("Choose a character name : ")
    if choice != "":
        Player = Character()
        Player.setname(choice)
        print("Welcome %s" %choice)
        print("Strength: %s" %Player.getSTR())
        print("Agility: %s" %Player.getAGL())
        print("Intellect: %s" %Player.getINT())
        print("Hit Points: %s" %Player.getcurrent_hp())
        print("Weapon: %s" %Player.getcurrent_weapon())
        Intro()
    else:
        print("No true hero can have no name!")
        Play()
def Intro():
    print("The air is crisp, the morning dew lingering in the air.")
    print("You look at the tiny village, hidden in the mountains, safe from the war.")
    print("They are fine hiding here, but adventure calls to you and with nothing more")
    print("than, the shirt on your back and a bag of food, you set out.")
    print("")
    print("The road is long leading to Millian Village and the sun will not be up forever")
    print("With a heavy heart you whisper words meant for your mother 'I'm sorry, but I have to do this.' and press on.")
    Start()

def Start():
    print("What would you like to do?")
    print("1) Press on to Millian Village")
    print("2) Realize your to young and return home")
    choice = input("->")
    if choice == '1':
        MillianVillage()
    elif choice == '2':
        CrapEnd()
    else:
        print('pick a real choice')
        Start()
def MillianVillage():
    pass
def CrapEnd():
    print("You realize you suck at life and when your village is destoryed, you die knowing it.")
    os.system('exit')
MainLoop()
pause = input("")