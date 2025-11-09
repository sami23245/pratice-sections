import turtle
import math
import winsound  # Works on Windows

# Setup screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Bouncing Ball in Circle")
screen.tracer(0)  # Turn off automatic animation for smoother movement

# Draw circle boundary
boundary = turtle.Turtle()
boundary.hideturtle()
boundary.penup()
boundary.goto(0, -200)  # Circle radius 200
boundary.pendown()
boundary.pensize(3)
boundary.color("white")
boundary.circle(200)

# Ball setup
ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.speed(0)
ball.goto(0, 0)

# Ball movement variables
dx = 2
dy = 2
radius = 200
score = 1

# Main loop
while True:
    # Move the ball
    ball.setx(ball.xcor() + dx)
    ball.sety(ball.ycor() + dy)
    
    # Check distance from center
    distance = math.sqrt(ball.xcor()**2 + ball.ycor()**2)
    
    if distance >= radius:
        # Bounce the ball
        angle = math.atan2(dy, dx)
        angle = math.pi + angle
        speed = math.sqrt(dx**2 + dy**2)
        dx = speed * math.cos(angle)
        dy = speed * math.sin(angle)
        
        # Play sound
        winsound.Beep(1000, 100)  # frequency 1000Hz, duration 100ms
        
        # Multiply score by 2
        score *= 2
        print("Score:", score)
    
    screen.update()
