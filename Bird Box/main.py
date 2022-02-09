# Name: Faiyam Islam
# Date: 9/02/22
# Description: Using Turtle Library to create a Python program which draws a little bird box

import turtle

bird = turtle.Turtle()
bird.speed(5)
bird.pensize(4)
bird.color("Olive")

bird.penup()
bird.goto(-100,0)
bird.down()

bird.fillcolor("Olive")
bird.begin_fill()
for i in range(3):
  bird.fd(200)
  bird.left(120)
bird.end_fill()

bird.fd(25)
bird.right(90)

bird.fillcolor("Peachpuff")
bird.begin_fill()
for i in range (4):
  bird.fd(150)
  bird.left(90)
bird.end_fill()

bird.penup()
bird.left(90)
bird.fd(75)
bird.right(90)
bird.fd(25)
bird.right(90)
bird.pendown()

bird.color("Black")
bird.fillcolor("Black")
bird.begin_fill()
bird.circle(25)
bird.end_fill()
