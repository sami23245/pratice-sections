from tkinter import *
from tkinter import messagebox
from tkinter import ttk as te
import os
import sqlite3


root = Tk()
# root.geometry("444x344")
root.title("Data Entery Form")
def submit():
    accpted = terms_and_con_var.get()
    if accpted != "Accepted":
        messagebox.showwarning("Terms and Conditions", "You must accept the terms and conditions to proceed.")
        return
    else:
        # user info
        first_name = E_fname.get()
        last_name = E_lname.get()
        title = title_combo.get()
        age = spinbox_age.get()
        nacinationaly = E_nationality.get()

        print(f"First Name: {first_name} {last_name}")
        print(f"title : {title},Age: {age},nationality: {nacinationaly}")


        # university info
        course_completed = spinbox_completed_courses.get()
        semester = spinbox_semester.get()
        reg_status = regesteration_ststus_var.get()

        print(f"Registration Status: {reg_status}")
        print(f"Completed Courses: {course_completed}, Semester: {semester}")
        print("-----------------------------------------------------------")

        # Save to database
        conn = sqlite3.connect('university_data.db')
        table_creation_query = '''CREATE TABLE IF NOT EXISTS students_data
                                (first_name TEXT, last_name TEXT,
                                 title TEXT, age INTEGER, nationality TEXT,
                                 registration_status TEXT,
                                 completed_courses INTEGER, semester INTEGER)
                                 '''
        # insert data
        Data_insert_query = '''Insert INTO students_data
                            (first_name, last_name, title, age, nationality,
                             registration_status, completed_courses, semester) values
                             (?,?,?,?,?,?,?,?)'''
        Data_insert_tuple = (first_name, last_name, title, age, nacinationaly,
                             reg_status, course_completed, semester)
        coursour = conn.cursor()
        coursour.execute(Data_insert_query, Data_insert_tuple)
        conn.commit()
        messagebox.showinfo("Data Saved", "Your data has been saved successfully.")
        # conn.execute(table_creation_query)
        conn.close()


    # terms and conditions
frame = Frame(root)
frame.pack()
user_info_frame = LabelFrame(frame, text="User Information")
user_info_frame.grid(row=0, column=0)
university_info_frame = LabelFrame(frame, text="University Information")
university_info_frame.grid(row=1, column=0,sticky="WENS")
Terms_and_con_frame = LabelFrame(frame, text="Terms and Conditions")
Terms_and_con_frame.grid(row=2, column=0,sticky="WENS")
fname_label = Label(user_info_frame, text="First Name")
E_fname = Entry(user_info_frame)
E_lname = Entry(user_info_frame)
lname_label = Label(user_info_frame, text="Last Name")
fname_label.grid(row=0, column=0)
lname_label.grid(row=0, column=1)
E_fname.grid(row=1, column=0)
E_lname.grid(row=1, column=1)
title_label = Label(user_info_frame, text="Title")
title_combo = te.Combobox(user_info_frame, values=["Mr.", "Ms.", "Dr.", "Prof."])
title_label.grid(row=0, column=2)
title_combo.grid(row=1, column=2)
l_age = Label(user_info_frame, text="Age")
spinbox_age = te.Spinbox(user_info_frame, from_=0, to=120)
l_age.grid(row=2, column=0)
spinbox_age.grid(row=3, column=0)
l_nationality = Label(user_info_frame, text="Nationality")
E_nationality = te.Combobox(user_info_frame, values=["American", "Canadian", "British","East blue","westoros","old valeria","god vally", "Other"])
l_nationality.grid(row=2, column=1)
E_nationality.grid(row=3, column=1)
for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
l_regestration_status = Label(university_info_frame, text="Registration Status")


regesteration_ststus_var = StringVar()
c_regestration_status = Checkbutton(university_info_frame, text="Registered", 
                                    variable=regesteration_ststus_var,onvalue="Registered", offvalue="Not Registered")


l_comple_courses = Label(university_info_frame, text="Completed Courses")
spinbox_completed_courses = te.Spinbox(university_info_frame, from_=0, to=127)
l_semester = Label(university_info_frame, text="Semester")
spinbox_semester = te.Spinbox(university_info_frame, from_=1, to=12)
l_regestration_status.grid(row=0, column=0)
c_regestration_status.grid(row=1, column=0)
l_comple_courses.grid(row=0, column=1)
spinbox_completed_courses.grid(row=1, column=1)
l_semester.grid(row=0, column=2)
spinbox_semester.grid(row=1, column=2)

for widget in university_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)
l_terms = Label(Terms_and_con_frame, text="I accept the terms and conditions")

terms_and_con_var = StringVar()
c_terms = Checkbutton(Terms_and_con_frame,variable=terms_and_con_var,onvalue="Accepted", offvalue="Not Accepted")
l_terms.grid(row=0, column=1)
c_terms.grid(row=0, column=0)
b_submit = Button(frame, text="Submit",command=submit)
b_submit.grid(row=3, column=0, pady=10,sticky="NEWS")
root.mainloop()