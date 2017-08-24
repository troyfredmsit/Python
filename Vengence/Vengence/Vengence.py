#python space invaders learning experiment
#by Troy Fred

import turtle
import os
import math
import random


#set screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders!")
wn.bgpic("space.gif")

#register the gif
turtle.register_shape("invader.gif") #this is how you make the system aware of your image.
turtle.register_shape("player.gif")


#draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()
#Set score to 0
score = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290,280)
scorestring = " SCORE %s" %score
score_pen.write(scorestring, False, align = "left", font=("Arial",14, "normal"))
score_pen.hideturtle()

#create Player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")#for the gif it would be player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed = 15



# choose number of enemies
number_of_enemies = 5

#create empty list
enemies = []

#add enemies to list
for i in range(number_of_enemies):
    #create the enemy
    enemies.append(turtle.Turtle())
for enemy in enemies:
    #Create the enemy
    enemy.color("red")
    enemy.shape("circle")
    enemy.penup()
    enemy.speed(0)
    x = random.randint(-200,200)
    y = random.randint(100,250)
    enemy.setposition(x,y)
    enemyspeed = 2

#move player left and right
def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -280:
        x = -280
    player.setx(x)

def move_right():
    x = player.xcor()
    x += playerspeed
    if x > 280:
        x = 280
    player.setx(x)

#createbullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()
bulletstate = "ready"
bulletspeed = 20

#define bullet state
#ready ready-to fire
#fire - firing.

def fire_bullet():
    #declare bulletstate as a global
    global bulletstate
    if bulletstate == "ready" :
       bulletstate = "fire"
       #move bullet to just above player
       x = player.xcor()
       y = player.ycor() + 10
       bullet.setposition(x,y)
       bullet.showturtle()

#create keyboard listener
turtle.listen()
turtle.onkey(move_left,"Left")
turtle.onkey(move_right,"Right")
turtle.onkey(fire_bullet,"space")

def is_collision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+ math.pow(t1.ycor()-t2.ycor(),2))
    if distance < 15:
        return True
    else:
        return False



#main game loop
while True:
    for enemy in enemies:
        #move enemy
        x = enemy.xcor()
        x += enemyspeed
        enemy.setx(x)

        #reverse enemy when you hit the screen edge
        if enemy.xcor() > 280:
            #move all enemies down
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1
        if enemy.xcor() < -280:
            #move all enemies direction
            for e in enemies:
                y = e.ycor()
                y -= 40
                e.sety(y)
            enemyspeed *= -1

        if is_collision(bullet, enemy):
            #reset bullet
            bullet.hideturtle()
            bulletstate = "ready"
            bullet.setposition(0, -400)
            #rest enemy
            enemy.setposition(-200, 250)
            #update score
            score+=10
            scorestring = "Score: %s" %score
            score_pen.clear()
            score_pen.write(scorestring, False, align = "left", font=("Arial",14, "normal"))
#Check for collision between the two.
        if is_collision(player, enemy):
            player.hideturtle()
            enemy.hideturtle()
            print("Game OVER NOOOOOOOOB!")
            break
    
            #move bullet
    if bulletstate == "fire":
       y = bullet.ycor()
       y += bulletspeed
       bullet.sety(y)

    if bullet.ycor() > 275:
       bullet.hideturtle()
       bulletstate = "ready"
        
