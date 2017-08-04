# test RPG learning experiment
import sys
import os
import random

weapon = {"Great Sword":40}
class Player:# base player class
    def __init__(self, name):
        self.name = name    
        self.maxhealth = 100
        self.health = self.maxhealth
        self.base_attack = 10
        self.gold = 50
        self.potions = 1
        self.weapon = ["Rusty sword"]
        self.curweapon = ["Rusty sword"]

    @property
    def attack(self):
        attack = self.base_attack
        if(self.curweapon == "Rusty sword"):
           attack += 5
        if(self.curweapon == "Great Sword"):
           attack += 15
        return attack

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
    print("WELCOME TO THE STORE!!!")
    print("What can I get for ya travler?")
    print("1.) Weapons")
    print("2.) Potions")
    print("3.) Leave Store")

    options = input("->")
    if(options == "1"):
        print("What weapon would you like?")
        print("1. Great Sword")
        option2 = input("->")
        if(option2 in weapon):
            if(PlayerIG.gold >= weapon[option2]):
                PlayerIG.gold -= weapon[option2]
                PlayerIG.weapon.append(option2)
                print("You have purchased a %i" % weapon[option2])
                store()
            else:
                print("You are to poor scrub!")
                store()
    elif(options == "2"):
        if(PlayerIG.gold >= 5):
            PlayerIG.potions +=1
            PlayerIG.gold -= 5
            store()
        else:
            print("To poor scrub!")

    elif(options == "3"):
        start1()
    else:
        print("Not a valid choice")
        store()



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
    rand1 = random.randint(1,3)
    if(rand1 == 1):
        print("You got away!")
        start1()
    else:
        print("You failed to get away!")
        EAttack = random.randint(1, 2)
    
    if(EAttack == 2):
        print("Enemy Missed!!")
    else:
        print("Enemy deals %i damage" % (enemy.attack))
        PlayerIG.health -= enemy.attack

    fight()

def drinkpot():
    if(PlayerIG.potions <= 0):
        print("You have no potions!")
        fight()
    else:
        print("You drink a potion!")
        PlayerIG.health += 50
        if(PlayerIG.health >= PlayerIG.maxhealth):
            PlayerIG.health = PlayerIG.maxhealth
        PlayerIG.potions -= 1
        fight()
    pass
def win():
    print("You WIN")
    enemy.health = enemy.maxhealth
    PlayerIG.gold += enemy.goldagain
    PlayerIG.potions +=1
    print("You gain %i gold and 1 Potion" % enemy.goldagain)
    start1()

def die():
    print("YOU DIE!")
    main()

# START OF GAME

main()
