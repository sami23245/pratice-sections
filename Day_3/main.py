import os
import json
import turtle

class Database:
    def __init__(self):
        shapes = {"triange","Right_triangle"}
class shapes(Database):
    def Triangle(self,shapes):
        for i in range(5):
            for j in range(i):
                print("*", end="")
            print()
    def Right_triangle(self,shapes):
        rows = 5

        for i in range(rows, 0, -1):   # starts from 5 → 1
            for j in range(i):
                print("*", end="")
            print()
    def up_down_right_tr(self,shapes):
        rows = 5

        for i in range(rows, 0, -1):
            print(" " * (rows - i) + "*" * i)
    def empty_dimond(self,shapes):

        rows = 5

        # Top Triangle (hollow)
        i = 1
        while i <= rows:
            # print spaces (to center)
            j = 0
            while j < rows - i:
                print(" ", end="")
                j += 1

            # print stars with hollow center
            k = 0
            while k < (2 * i) - 1:
                if k == 0 or k == (2 * i) - 2:
                    print("*", end="")
                else:
                    print(" ", end="")
                k += 1

            print()
            i += 1


        # Bottom Triangle (hollow)
        i = rows - 1
        while i > 0:

            # spaces
            j = 0
            while j < rows - i:
                print(" ", end="")
                j += 1

            # stars hollow
            k = 0
            while k < (2 * i) - 1:
                if k == 0 or k == (2 * i) - 2:
                    print("*", end="")
                else:
                    print(" ", end="")
                k += 1

            print()
            i -= 1
    def triangle2(self):
        t = turtle.Turtle()
        for _ in range(3):
            t.forward(100)
            t.left(120)
        turtle.done()
    def right_triangle2(self):
        t = turtle.Turtle()
        t.forward(150)
        t.left(90)
        t.forward(100)
        t.goto(0, 0)
        turtle.done()
    def palogram(self):
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

            
if __name__=="__main__":
    sh = shapes()
    # sh.Triangle(shapes="1234")
    # sh.Right_triangle(shapes="124")
    # sh.up_down_right_tr(shapes="123")
    # sh.empty_dimond(shapes="123")
    # sh.triangle2()
    # sh.right_triangle2()
    sh.palogram()
