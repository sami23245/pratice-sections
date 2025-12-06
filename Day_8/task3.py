from tkinter import * #importing * from tkinter makes all the classes and functions of tkinter available
from tkinter import messagebox # importing messagebox module from tkinter for displaying message boxes
root = Tk()
def login_database(): #function to handle login logic
    username = "Sami"
    password = "1234"
    if entery_username.get() == username and entery_password.get() == password: #checking if entered credentials match predefined ones
        # print("login successful")
        messagebox.showinfo(title="Login Status", message="Login Successful") #showing success message box
    else:
        # print("login failed")
        messagebox.showerror(title="Login Status", message="Login Failed")
root.geometry("444x344")
root.title("password manager")
f1 = Frame(root, bg="lightblue", bd=5)
l_username = Label(f1, text="Username")
entery_username = Entry(f1)
label_password = Label(f1, text="Password")
entery_password = Entry(f1, show="*") # Entry widget with masked input for password
button_login = Button(f1, text="Login",command=login_database) # Button to trigger login function
l_username.grid(row=0, column=0, padx=10, pady=10,sticky="news")
entery_username.grid(row=0, column=1, padx=10, pady=10,sticky="news")
label_password.grid(row=1, column=0, padx=10, pady=10,sticky="news")
entery_password.grid(row=1, column=1, padx=10, pady=10,sticky="news")
button_login.grid(row=2, column=0, columnspan=2, pady=10,sticky="news")
f1.pack()
root.mainloop()