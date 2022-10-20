# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('cadetblue')

# Draw border
mypen = turtle.Turtle()
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
mypen.color('white')
for side in range(4):
    mypen.forward(600)
    mypen.left(90)
mypen.hideturtle

# Create player turtle
player = turtle.Turtle()
player.color ('olive')
player.shape('turtle')
player.penup() # Shape won't leave line when it moves
player.speed(0)

# Create food
food = turtle.Turtle()
food.color("green")
food.shape("circle")
food.penup()
food.speed(0)
food.setposition(random.randint(-290, 290), random.randint(-290, 290))

# Set speed variable
speed = 1

# Define functions
def turn_left():
    player.left(30)

def turn_right():
    player.right(30)

def increase_speed():
    global speed
    speed += 1

def decrease_speed():
    global speed
    speed -= 1

def isCollision(t1, t2):
    pos = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if pos < 20:
        return True
    else:
        return False

# Set keyboard binding
turtle.listen()
turtle.onkey(turn_left, 'Left')
turtle.onkey(turn_right, 'Right')
turtle.onkey(increase_speed, 'Up')
turtle.onkey(decrease_speed, "Down")

while True:
    player.forward(speed)

    # Boundary player checking x coordinate
    if player.xcor() > 290 or player.xcor() <-290:
        player.right(161)

    # Boundary player checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(151)

    # Collision checking
    if isCollision(player, food):
        food.setposition(random.randint(-290, 290), random.randint(-290, 290))

