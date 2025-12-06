from tkinter import *
from tkinter import messagebox
import pyshorteners
root = Tk()
root.geometry("444x344")
root.title("URL Manager")
def shotner():
    shoyneer = pyshorteners.Shortener()
    shot_url = shoyneer.tinyurl.short(Entry_URL.get())
    shote_url.insert(0, shot_url)
root.configure(bg="lightgrey")
f1 = Frame(root, bg="lightblue", bd=5)
l_URL = Label(f1, text="Enter URL")
Entry_URL = Entry(f1, width=40)
shot_url_label = Label(f1, text="Shortened URL")
shote_url = Entry(f1)
btn_shorten = Button(f1, text="Shorten URL", command=shotner)
l_URL.grid(row=0, column=0, padx=5, pady=5)
Entry_URL.grid(row=0, column=1, padx=5, pady=5)
shot_url_label.grid(row=1, column=0, padx=5, pady=5)
shote_url.grid(row=1, column=1, padx=5, pady=5)
btn_shorten.grid(row=2, columnspan=2, pady=10)
f1.pack(pady=20)
root.mainloop()