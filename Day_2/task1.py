import os
import json
import random

path = r"C:\Users\Samis\OneDrive\Desktop\learning\pratice-sections\Day_2"

class Database:
    def __init__(self):
        a = random.randint(1000,2600)
        a1 = random.randint(1000,2600)
        a2 = random.randint(1000,2600)
        a3 = random.randint(1000,2600)
        a4 = random.randint(1000,2600)
        self.employees = {
            "E101": {"name": "Ali", "role": "Manager", "salary": 80000, "team": ["E102", "E103"], "attendance":12},
            "E102": {"name": "Sara", "role": "Employee", "salary": 40000, "manager": "E101", "attendance":12},
            "E103": {"name": "Bilal", "role": "Intern", "salary": 20000, "manager": "E101", "attendance":12},
            "E104": {"name": "Nida", "role": "HR", "salary": 60000, "attendance":12}
            }

    def save_to_file(self,path):
        with open (path,"w") as file:
            json.dump(self.employees, file, indent=5)
    def load_from_file(self,path):
        with open(path,"r") as file:
            self.employes = json.load(file)
class Employe(Database):
    def E101(self,employees):#manager
        print("--welcome[Ali]--")
        print("for Attendance 1:")
        print("for Today task 2:")
        print("for salery ----3:")
        print("for Exit ------4:")
        def attendance():
            
            while True:
                option1 = int(input("Enter your option:"))
                if option1 == 1:
                    print(f"Your this mounth attendance is {self.employees[ID]['attendance']}")
                elif option1 == 2:
                    print(f"No task today")
                elif option1 == 3:
                    print(f"Your this mounth attendance is {self.employees[ID]['salary']}")
                else:
                    print("bye bye")
                    break
        attendance()
            

    def E102(self,employees):#employe
        print("--welcome[Sara]--")
        print("for Attendance 1:")
        print("for Today task 2:")
        print("for salery ----3:")
        print("for Exit ------4:")
        def attendance():
            
            while True:
                option1 = int(input("Enter your option:"))
                if option1 == 1:
                    print(f"Your this mounth attendance is {self.employees[ID]['attendance']}")
                elif option1 == 2:
                    print(f"No task today")
                elif option1 == 3:
                    print(f"Your this mounth attendance is {self.employees[ID]['salary']}")
                else:
                    print("bye bye")
                    break
        attendance()
    def E103(self,employees):#inter
        print("--welcome[Bilal]--")
        print("for Attendance 1:")
        print("for Today task 2:")
        print("for salery ----3:")
        print("for Exit ------4:")
        def attendance():
            
            while True:
                option1 = int(input("Enter your option:"))
                if option1 == 1:
                    print(f"Your this mounth attendance is {self.employees[ID]['attendance']}")
                elif option1 == 2:
                    print(f"No task today")
                elif option1 == 3:
                    print(f"Your this mounth attendance is {self.employees[ID]['salary']}")
                else:
                    print("bye bye")
                    break
        attendance()
    def E104(self,employees):#hr
        print("--welcome[Naida]--")
        print("for Attendance 1:")
        print("for Today task 2:")
        print("for salery ----3:")
        print("for Exit ------4:")
        def attendance():
            
            while True:
                option1 = int(input("Enter your option:"))
                if option1 == 1:
                    print(f"Your this mounth attendance is {self.employees[ID]['attendance']}")
                elif option1 == 2:
                    print(f"No task today")
                elif option1 == 3:
                    print(f"Your this mounth attendance is {self.employees[ID]['salary']}")
                else:
                    print("bye bye")
                    break
        attendance()
if __name__ == "__main__":
    E = Employe()
    DB = Database()
    print("--welcome--")
    while True:
        ID = input("Enter your id:")
        if (ID in DB.employees):
            if (ID == "E101"):
                print("login secussful--")
                print(f"Your name is {DB.employees[ID]['name']} and your login Id is {DB.employees[ID]['role']}")
                E.E101(employees="E101")
                # break
            elif(ID == "E102"):
                print("login secussful--")
                print(f"Your name is {DB.employees[ID]['name']} and your login Id is {DB.employees[ID]['role']}")
                E.E102(employees="E102")
                break
            elif(ID == "E103"):
                print("login secussful--")
                print(f"Your name is {DB.employees[ID]['name']} and your login Id is {DB.employees[ID]['role']}")
                E.E103(employees="E103")
                break
            elif(ID == "E104"):
                print("login secussful--")
                print(f"Your name is {DB.employees[ID]['name']} and your login Id is {DB.employees[ID]['role']}")
                E.E104(employees="E104")
                break
            else:
                print("your ID is not in database")
            break
        else:
            print("Wrong id")
            attemts = 0
            attemts = attemts + 1
            if attemts >= 2:
                option = input("For Exit 1:")
                if(option == 1):
                    break
