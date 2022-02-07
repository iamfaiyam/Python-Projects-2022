# Name: Faiyam Islam 
# Date: 7/02/22
# Description: Polygon Drawer App

import turtle

# Name of your turtle
koopa = turtle.Turtle()

# Make sure the name of the shape is wrapped between the quotation/double quotation marks
koopa.shape("turtle")
koopa.speed(0) 

# Calculate interior angle of a polygon 

# Declare how many sides your polygon has, must be > 0 
n_sides = int(input("Amount of sides: "))
external_angle = 360/n_sides

# The angle we want our turtle to start drawing a new polygoni, must be > 0 
orientation_angle = int(input("Angle: "))

# Numbers of polygons we want to draw
n_polygons = 360/orientation_angle

for polygon in range(int(n_polygons)):
  for new_side in range(n_sides):
    
    koopa.forward(50) 
    koopa.left(external_angle) 
    
  koopa.left(orientation_angle)
  
  