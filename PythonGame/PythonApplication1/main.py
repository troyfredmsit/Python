# test RPG learning experiment
import sys
import os
import random

class Player:# base player class
    def __init__(self, name):
        self.name = name    
        self.maxhealth = 100
        self.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.potions = 1

class Goblin:
    def __init__(self, name):
        self.name = name    
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
        self.goldagain = 10
GoblinIG = Goblin("Goblin")
        
class Zombie:
    def __init__(self, name):
        self.name = name    
        self.maxhealth = 70
        self.health = self.maxhealth
        self.attack = 7
        self.goldagain = 15
ZombieIG = Zombie("Zombie")

def main(): # our main function 
    print("welcome to the game!\n")
    print("1.) Start")
    print("2. Load")
    print("3.) End")
    option = input("-> ")

    if(option == "1"):
        start()
    elif(option == "2"):
        pass
    elif(option == "3"):
        sys.exit()
    else:
        main()

def start(): # the start feature
    print("Hello what is your name?")
    option = input("-> ")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start1():
    print(" Hey how are you %s?" % (PlayerIG.name))
    print("Attack %i" % (PlayerIG.attack))
    print("Health %i" % (PlayerIG.maxhealth))
    print("Gold %i" % (PlayerIG.gold))
    print("Potions %i\n" % (PlayerIG.potions))

    print("1.) Fight")
    print("2. Store")
    print("3.) Save")
    print("4.) Exit")

    option = input("->")
    if(option == "1"):
        prefight()
    elif(option == "2"):
        store()
    elif(option == "3"):
        pass
    elif(option == "4"):
        sys.exit
    else:
        start1()

def prefight():
    global enemy
    enemynum = random.randint(1,2)
    if(enemynum == 1):
        enemy = GoblinIG
    else:
        enemy = ZombieIG
    fight()

def fight():
    print("%s       VS      %s" % (PlayerIG.name,enemy.name))
    print("%s's Health: %d : %d      %s's Health: %i : %i" % (PlayerIG.name, PlayerIG.health, PlayerIG.maxhealth, enemy.name, enemy.health,enemy.maxhealth))
    print("Potions %i:\n" % (PlayerIG.potions))
    
    print("1.) Attack")
    print("2. Potion")
    print("3.) Run")

    option = input('-> ')
    if(option == "1"):
        attack()
    elif(option == "2"):
        drinkpot()
    elif(option == "3"):
        run()
    else:
        fight()

    

def store():
    pass

def attack():
 
    PAttack = random.randint(1, 2)
    EAttack = random.randint(1, 2)
    if(PlayerIG.health <= 0):
      print("Your dead")
      die()
    if(enemy.health <= 0):
      print("Enemy is dead")
      win()

    if(PAttack == 1):
        print("YOU MISS!!!")
    else:
        enemy.health -= PlayerIG.attack
        print("You deal %i damage" % (PlayerIG.attack))

    if(EAttack == 2):
        print("Enemy Missed!!")
    else:
        print("Enemy deals %i damage" % (enemy.attack))
        PlayerIG.health -= enemy.attack
    fight()
    
 
def run():
    pass
def drinkpot():
    if(PlayerIG.potions <= 0):
        print("You have no potions!")
        fight()
    else:
        print("You drink a potion!")
        PlayerIG.health += 10
        PlayerIG.potions -= 1
        fight()
    pass
def win():
    print("You WIN")
    main()
def die():
    print("YOU DIE!")
    main()

# START OF GAME

main()
