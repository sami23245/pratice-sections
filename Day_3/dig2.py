import turtle
import time

# Create screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()

# Starting variables
gravity = 0.4
velocity = 0    # falling speed
y = 200         # starting height

while True:
    velocity = velocity - gravity   # gravity pulls ball down
    y = y + velocity                # update ball position
    ball.sety(y)

    # When ball hits the ground
    if y <= -200:
        velocity = velocity * -0.85  # reverse direction + lose little energy

    time.sleep(0.01)  # slow animation down
