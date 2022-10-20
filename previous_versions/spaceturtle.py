# Turtle Graphics Game - Space Turtle Chomp

import turtle

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('cadetblue')

# Create player turtle
#player = turtle.Turtle()
player.color ('olive')
player.shape('turtle')
player.penup() # Shape won't leave line when it moves

# Set speed variable
speed = 1

while True:
    player.forward(speed)