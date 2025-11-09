import tkinter as tk
from tkinter import messagebox
import json
import random

class Database:
    def __init__(self):
        self.employees = {
            "E101": {"name": "Ali", "role": "Manager", "salary": 80000, "team": ["E102", "E103"], "attendance":12},
            "E102": {"name": "Sara", "role": "Employee", "salary": 40000, "manager": "E101", "attendance":12},
            "E103": {"name": "Bilal", "role": "Intern", "salary": 20000, "manager": "E101", "attendance":12},
            "E104": {"name": "Nida", "role": "HR", "salary": 60000, "attendance":12}
        }

class EmployeeGUI:
    def __init__(self, master, db):
        self.master = master
        self.db = db
        master.title("Employee Management")
        
        # Login UI
        self.label = tk.Label(master, text="Enter your Employee ID:")
        self.label.pack()
        
        self.entry = tk.Entry(master)
        self.entry.pack()
        
        self.login_button = tk.Button(master, text="Login", command=self.login)
        self.login_button.pack()
        
        self.logout_button = tk.Button(master, text="Logout", command=self.logout)
        self.logout_button.pack()
        self.logout_button.config(state="disabled")
        
        self.info_frame = tk.Frame(master)
        self.info_frame.pack(pady=10)
        
    def login(self):
        self.ID = self.entry.get()
        if self.ID in self.db.employees:
            self.emp = self.db.employees[self.ID]
            messagebox.showinfo("Login Successful", f"Welcome {self.emp['name']} ({self.emp['role']})")
            self.show_options()
            self.login_button.config(state="disabled")
            self.logout_button.config(state="normal")
        else:
            messagebox.showerror("Error", "Wrong ID")
    
    def logout(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
        self.login_button.config(state="normal")
        self.logout_button.config(state="disabled")
    
    def show_options(self):
        for widget in self.info_frame.winfo_children():
            widget.destroy()
            
        tk.Label(self.info_frame, text="Select an option:").pack()
        
        tk.Button(self.info_frame, text="Attendance", command=self.show_attendance).pack(fill='x')
        tk.Button(self.info_frame, text="Today's Task", command=self.show_task).pack(fill='x')
        tk.Button(self.info_frame, text="Salary", command=self.show_salary).pack(fill='x')
        tk.Button(self.info_frame, text="Exit", command=self.logout).pack(fill='x')
    
    def show_attendance(self):
        messagebox.showinfo("Attendance", f"This month's attendance: {self.emp['attendance']}")
    
    def show_task(self):
        messagebox.showinfo("Task", "No task today")
    
    def show_salary(self):
        messagebox.showinfo("Salary", f"This month's salary: {self.emp['salary']}")

if __name__ == "__main__":
    root = tk.Tk()
    db = Database()
    gui = EmployeeGUI(root, db)
    root.mainloop()
