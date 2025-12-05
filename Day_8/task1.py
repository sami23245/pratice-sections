import tkinter as tk
from tkinter import *
WIDTH = 600
HEIGHT = 400
BALL_RADIUS = 15
OBSTACLE_WIDTH = 60
OBSTACLE_HEIGHT = 15
root = tk.Tk()
root.geometry("444x344")
root.title("Expencees manager")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black")
t_label = Label(root,text="password")
t_label.grid(row=5,column=3)
c_la = Entry(root,show="*")
c_la.grid(row=5,column=5)
v_label = Label(text="username",)
v_label.grid(row=10,column=3)
d_la = Entry()
d_la.grid(row=10,column=5)
root.mainloop()