import json
import os
class DataBase:
    def __init__(self):
        self.filepath = r"C:\Users\Samis\OneDrive\Desktop\learning\pratice-sections\school_ManGMENT\school_database.json"
        if os.path.exists(self.filepath):
            with open(self.filepath, "r") as f:
                # self.students = data['students']
                # self.teachers = data["teachers"]
                # self.admin = data["admin"]
                data = {
                "students": self.students ,
                "teachers": self.Teachers ,
                "admin": self.Admin,
                "permissions": self.permissions
                }
                data = json.load(f)
                print("Database loaded--------")
            #TODO
        else:

            self.students = {
                "Spc23" : {"Name":"Ali","Class":"9th","Program":"Science","Condition":"Great","Schlorship":"Yes on 80%","Marks":98},
                "Spc24" : {"Name":"Sara","Class":"12th","Program":"ICS","Condition":"Good","Schlorship":"NO","Marks":89},
                "Spc25" : {"Name":"Zoro","Class":"8th","Program":"Science","Condition":"Normal","Schlorship":"Yes on 45%","Marks":56},
                "Spc26" : {"Name":"Samina","Class":"7th","Program":"Arts","Condition":"Bad","Schlorship":"Yes on 25%","Marks":39},
                "Spc27" : {"Name":"Moiz","Class":"7th","Program":"Science","Condition":"Normal","Schlorship":"No","Marks":67}
            }
            self.Teachers = {
                "Tec23" : {"Name":"Dark king","Specific_skill":"Computer","Salary":54000,"Feedback":"Great","Class_Teacher":"9th"},
                "Tec24" : {"Name":"Sun God","Specific_skill":"Math","Salary":67000,"Feedback":"Great","Class_Teacher":"12th"},
                "Tec25" : {"Name":"Red Hair","Specific_skill":"Bio","Salary":78000,"Feedback":"Great","Class_Teacher":"11th"},
                "Tec26" : {"Name":"Beast King","Specific_skill":"Arts","Salary":34000,"Feedback":"Great","Class_Teacher":"11th"},
            }
            self.Admin = {
                "Adm23" : {"Name":"Nami","Role":"IT Spalist","Salary":50000,"Incharge":"Regesteration"},
                "Adm24" : {"Name":"Robin","Role":"Data Sintest","Salary":50000,"Incharge":"Data Managment"},
                "Adm25" : {"Name":"Sanji","Role":"Finance Spalist","Salary":50000,"Incharge":"Finance"},
            }
            self.permissions = {   # role-based permissions
                "student": ["view_own_data"],
                "teacher": ["view_students", "modify_attendance"],
                "admin": ["add_user", "remove_user", "modify_data"]
            }
            self.programs = ["ICS", "ADP", "BSC","B.com","I.com","B.Tech"]
            self.Scholarships = {
                "Bignner" : {"persent":"50%","Eligiblity":"55%"},
                "IT" : {"persent":"55%","Eligiblity":"60%"},
                "PM" : {"persent":"89%","Eligiblity":"90%"},
                "CM-Punjab1" : {"persent":"40%","Eligiblity":"55%"},
                "CM-Punjab2" : {"persent":"75%","Eligiblity":"80%"},
                "Uni-1" : {"persent":"50%","Eligiblity":"60"}
            }
    def save(self):
        data = {
            "students": self.students,     # ✅ correct spelling
            "teachers": self.Teachers,
            "admin": self.Admin,
            "permissions": self.permissions
        }
        with open(self.filepath, "w") as f:
            json.dump(data, f, indent=4)
            print("Saved")

class Admin(DataBase):
    def add_student(self, ID, name): #Add student
        Name = input("Enter Name:")
        ID = input("Enter name of student ID: ")
        list = input("For program list yes:")
        if list == "yes":
            print(self.programs)
            program = input("Enter your program:")
        else:
            program = input("Enter your program:")
        sch = int(input("Enter number for schloship eligiblity:"))
        if sch>=90:
            self.Scholarships["PM"]["Eligiblity"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("Appalied")
        elif sch >=80 and sch <90:
            self.Scholarships["PM"]["CM-Punjab2"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("Appalied")
        elif sch >=70 and sch <80:
            self.Scholarships["PM"]["Eligiblity"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("hii")
        elif sch >=60 and sch <70:
            self.Scholarships["PM"]["Eligiblity"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("hii")
        elif sch >=60 and sch <60:
            self.Scholarships["PM"]["Eligiblity"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("hii")
        elif sch >=40 and sch <60:
            self.Scholarships["PM"]["Eligiblity"]
            app = input("if want to apply enter yes:")
            if app == True:
                print("hii")
        else:
            print("Not eligible")
        while True:
            try:
                if ID in self.students:
                    raise ValueError("Student already exists!")
                else:
                    print(f"✅ Added student {Name} with ID {ID}")
                    print(f"✅ Added student {program} ")
                    self.save()
                    break
            except ValueError as e:
                print(f"⚠️ {e}")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")

    def salary(self): #change teacher Salary
        ID = input("Enter name of Teacher ID: ")
        n_salary = int("Enter new salary:")
        self.Teachers[ID]['Salary']
        self.students[ID][ID]["Salary":[n_salary]]
        print(self.Teachers[ID]['Salary'])
        print("hii")
    def salary(self,ID,name): #change teacher subject
        name = input("Enter name of Teacher ID: ")
        self.students[ID] = {"Name": name,"Specific_skill":[]}



class Teacher(DataBase):
    pass



class Student(DataBase):
    def __init__(self):
        return self.students[self.id]["attendance"]
if __name__ == "__main__":
    # db = DataBase()
    Ad = Admin(students="sami")
    Ad.add_student("Spc27", "Moiz")
    # Ad.salary("tec27",'luffy')
    # db.save()

    # print("--weelcome--")
    # print("For login (Student/Teacher) 1:")
    # print("For new regesteration ------2:")
    # print("For admin ------------------3:")
    # print("For Exit -------------------5:")
    # while True:
    #     ID = input("Enter your id:")
    #     if id in db.students:
    #         pass
    #     elif ID in db.Teachers:
    #         pass
    #     else:
    #         print(f"id not found")
    #         break