import turtle
import os
import random
import math

#setup the screen
wn = turtle.Screen()
wn.bgcolor("red")
wn.title("Simple turtle game.")
## end set up screen

##create the border class
class Border(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.penup()
        self.hideturtle()
        self.speed(0)
        self.color("white")
        self.pensize(5)

    def draw_border(self):
        self.penup()
        self.goto(-300,-300)
        self.pendown()
        self.goto(-300,300)
        self.goto(300,300)
        self.goto(300,-300)
        self.goto(-300,-300)

#make class for player.
class Player(turtle.Turtle): #this is basically inheritance from the turtle.Turtle class

    def __init__(self):## initial init
        turtle.Turtle.__init__(self) ### init from the main class we inherit from.
        self.penup()
        self.shape("triangle")
        self.color("white")
        self.speed(0)
        self.speed = 1

    def move(self):
        self.forward(self.speed)

        #border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() <-290:
            self.left(60)

    def turn_left(self):
        self.left(30)
    def turn_right(self):
        self.right(30)
    def increase_speed(self):
        self.speed += 1
    def decrease_speed(self):
        self.speed -= 1
#end making player class

class Goal(turtle.Turtle):

    def __init__(self):## initial init
         turtle.Turtle.__init__(self) ### init from the main class we inherit from.
         self.penup()
         self.shape("circle")
         self.color("green")
         self.speed(0)
         self.speed = 5
         self.goto(random.randint(-250,250),random.randint(-250,250))
         self.setheading(random.randint(0,360))
    def jump(self):
        self.goto(random.randint(-250,250), random.randint(-250,250))
        self.setheading(random.randint(0,360))
    
    def move(self):
        self.forward(self.speed)

        #border checking
        if self.xcor() > 290 or self.xcor() < -290:
            self.left(60)
        if self.ycor() > 290 or self.ycor() <-290:
            self.left(60)

def is_collision(t1,t2):
    a = t1.xcor()-t2.xcor()
    b = t1.ycor()-t2.ycor()
    distance = math.sqrt((a ** 2)+(b ** 2))
    if distance <20:
        return True
    else:
        return False



#initiate the player and border
player = Player()
border = Border()

#initiate the border
border.draw_border()

#create list for goals.
goals = []
for count in range(6):
    goals.append(Goal())

#turn on listener
turtle.listen()
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.increase_speed, "Up")
turtle.onkey(player.decrease_speed, "Down")

#speed up game with a tracer
wn.tracer(0) #0 stops the screen from being updated.

#mainloop
while True:
    wn.update()
    player.move()
 
    for goal in goals:#goes through the list of goals created earlier to move them and the check for collisons.
        goal.move()
        if is_collision(player,goal):
            goal.jump()