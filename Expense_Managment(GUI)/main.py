from tkinter import *
from tkinter import messagebox
from tkinter import ttk as te
import openpyxl
import os
import json


root = Tk()
root.title("Expense Management System")
root.geometry("600x400")
root.config(bg="lightblue")
frame_f1 = Frame(root,)
frame_f1 = Frame(root)
frame_f1.pack()
Enter_expense_frame = LabelFrame(frame_f1, text="Enter Expense")
Enter_expense_frame.grid(row=0, column=0)
l_no_expense = Label(Enter_expense_frame, text="No. of Expenses:")
E_no_expense = Entry(Enter_expense_frame)
l_no_expense.grid(row=0, column=0)
E_no_expense.place_configure(x=120, y=5)
E_no_expense.grid(row=0, column=1)
root.mainloop()