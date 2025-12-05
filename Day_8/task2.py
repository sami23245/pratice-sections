import tkinter as tk
from tkinter import *

root = Tk()
root.geometry("444x344")
root.config(bg="black")
root.title("Login")
l_ = Label(root,text="username")
p_ = Entry(root)
c_ = Label(root,text="password")
d_ = Entry(root,show="-")
b_ = Button(root,text="LOGIN")
l_.grid(row=2,column=2)
p_.grid(row=2,column=3)
c_.grid(row=3,column=2)
d_.grid(row=3,column=3)
root.mainloop()