# Name: Faiyam Islam 
# Date: 8/02/22
# Description: Flower challenge
# Comment out the function calls at the bottom of the program 
# to see different shapes

import turtle
import random
import time

window = turtle.Screen()
myPen = turtle.Turtle()
myPen.speed(0)
myPen.hideturtle()

def flower_draw():
  while True:
    for i in range(12):
      myPen.penup()
      myPen.goto(0, 0)
      myPen.pensize(1)
      myPen.pendown()
      for j in range(100):
        myPen.color(random.randint(100, 200), j, random.randint(100, 200))
        myPen.forward(1)
        myPen.pensize(j)
      myPen.right(30)
      time.sleep(0.5)

def ice_draw():
  while True:
    for i in range(12):
      myPen.penup()
      myPen.goto(0, 0)
      myPen.pensize(100)
      myPen.pendown()
      for j in range(100):
        myPen.color(j, random.randint(100, 200), random.randint(100, 200))
        myPen.forward(1)
        myPen.pensize(100 - j)
      myPen.right(30)
      time.sleep(0.5)

flower_draw()
# ice_draw()