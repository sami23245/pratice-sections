# import tkinter
import json
import os
import colorama
from colorama import Fore, Back, Style, init
path = r"C:\Users\Samis\OneDrive\Desktop\learning\pratice-sections\day_7\account.json"

init() 
class Data_Expencess:
    def __init__(self):
        self.expencess_data = {
            "expense1": "uses less",
            "expense2": "over prise",
            "expense3": "not necessery",
            "expense4": "too cheap",
        }
        Id = 0
        Id = Id + 1
        self.all_expenses = []
        self.expencess_data[f"records{+ Id}"] = self.all_expenses

    def save(self,path):
        with open(path, "w") as f:
            json.dump(self.expencess_data, f, indent=5)

    def load(self,path):
        with open(path,'r') as f:
            self.expencess_data = json.load(f)
class main(Data_Expencess):
    def ex(self,n):
        option2 = 1
        x = 0
        print(Fore.RED + "For make new list for expencess press [1]:")
        print("For update list of expencess press ---[2]:")
        print(Style.RESET_ALL)
        option1 = int(input("Enter your desire option:"))
        # while (option2 == 1):
        if (option1 == 1):
            Total_expencess = int(input(Fore.GREEN + "Enter no of expencess:"))
            Total_ammount = int(input("Enter no of ammount--- :"))
            print(Style.RESET_ALL)
            while(x < Total_expencess):
                x = x +1
                # s_no = randint(1,100)
                # print(f"Your serial no is{s_no}")
                Td = "ID_" + str(x)
                print(Td)
                e = input(Fore.LIGHTRED_EX + "Enter purpose of this expense:")
                print(Style.RESET_ALL)
                ea = int(input("Enter ammount:"))
                per = (ea / Total_ammount)*100
                if(per >= 80):
                    print(Fore.RED + self.expencess_data["expense1"])
                elif(per <80 and per >=70):
                    print(Fore.GREEN + self.expencess_data["expense2"])
                    print(Style.RESET_ALL)
                elif(per <70 and per >=40):
                    print(Fore.LIGHTWHITE_EX + self.expencess_data["expense3"])
                else:
                    print(self.expencess_data["expense4"])
                    print(Style.RESET_ALL)
                Total_ammount = Total_ammount - ea
                print(Fore.RED + f"Your remmaning ammount is [{Total_ammount}]")
                print(Style.RESET_ALL)
                last_id = 0
                if "records" in self.expencess_data['records']:
                    last_id = self.expencess_data['records']["id"]  # get id of the last record
                new_id = last_id + 1

                expense_dict = {
                    "id": new_id,
                    "purpose": e,
                    "amount": ea
                }
                self.all_expenses.append(expense_dict)
            self.expencess_data["records"] = self.all_expenses
            self.save(path)
        elif(option1 == 2):
            Id = input("Enter your id:")
if __name__ == "__main__":
    # d = Data_Expencess    # create object   
    m = main()
    m.load(path)
    print(m.load(path))
    m.ex(n='123')