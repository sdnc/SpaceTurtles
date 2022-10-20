# Turtle Graphics Game - Space Turtle Chomp
import turtle
import math
import random
import os

# Set up screen
turtle.setup(650,650)
wn = turtle.Screen()
wn.bgcolor('black')
wn.bgpic('kbgame-bg.gif')
wn.tracer(3)

# Draw border
mypen = turtle.Turtle()
mypen.color('black')
mypen.penup()
mypen.setposition(-300, -300)
mypen.pendown()
mypen.pensize(3)
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

# Create variable score
score = 0

# Create food
maxFoods = 10
foods = []

for i in range(maxFoods):
    new_food = turtle.Turtle()
    new_food.color("limegreen")
    new_food.shape("circle")
    new_food.penup()
    new_food.speed(0)
    new_food.setposition(random.randint(-290, 290), random.randint(-290, 290))
    foods.append(new_food)
    for food in foods:
        food.shapesize(.5)

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
        os.system('afplay bounce.mp3&')

    # Boundary player checking y coordinate
    if player.ycor() > 290 or player.ycor() <-290:
        player.right(151)
        os.system('afplay bounce.mp3&')

    # Move food around
    for food in foods:

        food.forward(3)

        # Boundary food checking x coordinate
        if food.xcor() > 290 or food.xcor() <-290:
            food.right(182)
            os.system('afplay bounce.mp3&')

        # Boundary food checking y coordinate
        if food.ycor() > 290 or food.ycor() <-290:
            food.right(95)
            os.system('afplay bounce.mp3&')

        # Collision checking
        if isCollision(player, food):
            food.setposition(random.randint(-290, 290), random.randint(-290, 290))
            food.right(random.randint(0, 360))
            os.system('afplay chomp.mp3&')
            score += 1

            # Draw the score on the screen
            mypen.undo()
            mypen.penup()
            mypen.color('red')
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring ="Score: %s" % score
            mypen.write(scorestring, False, align='left', font=('Arial', 14, 'normal'))
