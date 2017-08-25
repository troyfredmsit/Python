import turtle
import math
import random
import os
import sys


#set screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("RPG Game")

#draw border 600X600
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("grey")
border_pen.penup()
border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
    border_pen.fd(600)
    border_pen.lt(90)
border_pen.hideturtle()

class entity():
    def __init__(self):
        self.name = ""
        self.color = "blue"
        self.shape = "triangle"
        self.x = 200
        self.y = 200
        self.hp = 0
        self.damage = 0
        self.heading = 0

    def turtle_setup():
        #create Player turtle
        player = turtle.Turtle()
        player.color(self.color)
        player.shape(self.shape)#for the gif it would be player.shape("player.gif")
        player.penup()
        player.speed(0)
        player.setposition(0,-250)
        player.setheading(90)
        playerspeed = 15
   
##main loop
    




