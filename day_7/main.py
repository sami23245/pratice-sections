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
        self.all_expenses = []
    def save(self,path):
        with open(path, "w") as f:
            json.dump(self.expencess_data, f, indent=5)

    def load(self,path):
        with open(path,'r') as f:
            self.expencess_data = json.load(f)
class main(Data_Expencess):
    def ex(self,n,Id):
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

                expense_dict = {
                    "purpose": e,
                    "amount": ea,
                    "remaning ammount":Total_ammount
                }
                self.all_expenses.append(expense_dict)
            rac = str(input("Enter any record num to save in format[record123]:"))
            self.expencess_data[rac] = self.all_expenses
            self.save(path)
        elif(option1 == 2):
            self.load(path)
            rec = str(input("Enter your record num:"))
            if rec in self.expencess_data:
                print(self.expencess_data[rec])
            else:
                print("ID dose not exit.....")
        else:
            print(Fore.RED + "Invalid option.....")
            print(Style.RESET_ALL)
if __name__ == "__main__":  
    # create object   
    m = main()
    m.load(path)
    print(m.load(path))
    m.ex(n='123',Id=type)