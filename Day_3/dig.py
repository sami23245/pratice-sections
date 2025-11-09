import turtle

t = turtle.Turtle()
t.speed(3)

# Set outline and fill color
t.color("black", "lightblue")   # (outline, fill)

t.begin_fill()

# Parallelogram sides
for _ in range(2):
    t.forward(150)   # top/bottom length
    t.left(60)       # angle
    t.forward(100)   # side length
    t.left(120)      # angle

t.end_fill()

turtle.done()
