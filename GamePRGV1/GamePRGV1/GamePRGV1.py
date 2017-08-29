#RPG Game with Turtle graphics

#Imports
import random
import turtle
import io
import math
##End Import

#set screen#
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("RPG")


#Create a Base class for Enemies and Players
class Entity(turtle.Turtle):
    def __init__(self, name):
        turtle.Turtle.__init__(self)
        ## Turtle graphics peramiters ##
        self.penup() 
        self.shape("triangle") 
        self.color("white") 
        self.speed(0) 
        self.speed = 1 

        ## Game char based stats
        self.name = name
        self.hp = 0
        self.mana = 0
        self.status = ""
        self.effects = []
        self.damage = 0
        self.base_class = ""
        self.level = 2
        self.STA = 10
        
   ## SETTERS ##
    def sethp(self,damage):
        self.hp = hp - damage
    def setEffects(self):
       self.effects.append()

   ## GETTERS ##
    def gethp(self):
        return self.hp
    ### Initiation code ###
    def set_stats(self,base_class):
        if base_class == "Warrior":
            self.STA = 20
            self.hp = self.STA * self.level * 2
            self.mana = 0
            self.shape("square")
            self.base_class = base_class
        elif base_class == "Mage":
            self.STA = 10
            self.hp = self.STA * self.level * 1
            self.mana = 100
            self.shape("circle")
            self.base_class = base_class
        elif base_class == "Rogue":
            self.STA = 15
            self.hp = self.STA * self.level * 1
            self.mana = 100
            self.shape("triangle")
            self.base_class = base_class
        else:
            self.STA = 15
            self.hp = self.STA * self.level * 1
            self.mana = 20
            self.shape("star")
    
            


class Player(Entity):
    def __init__(self,name):
        super().__init__(name)
        self.inventory = []
        self.current_weapon = ""
        self.potions = 0
        self.gold = 0
        self.setposition(200,200)
        self.color("Red")
        self.speed = 0

    def turn_left(self):
        self.left(30)
    def turn_right(self):
        self.right(30)
    def increase_speed(self):
        self.speed += 1
    def decrease_speed(self):
        self.speed -= 1
    def move(self):
        self.forward(self.speed)



class MOB(Entity):
    def __init__(self, name):
        super().__init__(name)
        self.gold = 0
        self.loot = []
        self.mob_type = ""
        self.aggro = ""
        self.goto(random.randint(-250,250),random.randint(-250,250))
        self.setheading(random.randint(0,360))
        self.color("green")

class Border(turtle.Turtle): 
   def __init__(self): 
    turtle.Turtle.__init__(self) 
    self.penup() 
    self.hideturtle() 
    self.speed(0) 
    self.color("black") 
    self.pensize(5) 
 
   def draw_border(self): 
    self.penup() 
    self.goto(-300,-300) 
    self.pendown() 
    self.goto(-300,300) 
    self.goto(300,300) 
    self.goto(300,-300) 
    self.goto(-300,-300) 

border = Border()
ent1 = Entity("entity1")
ent2 = Player("Player1")
ent3 = MOB("MOB1")

ent1.set_stats("Warrior")
ent2.set_stats("Mage")
ent3.set_stats("Rogue")



#turtle Listener#
turtle.listen()
turtle.onkey(ent2.turn_left,"Left")
turtle.onkey(ent2.turn_right,"Right")
turtle.onkey(ent2.increase_speed,"Up")
turtle.onkey(ent2.decrease_speed,"Down")

def welcome_screen():



inpu = input("")

