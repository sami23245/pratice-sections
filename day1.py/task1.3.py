import colorama
import json
import os
import random

path = r"C:\Users\Samis\OneDrive\Desktop\learning\pratice-sections\day1.py\accounts.json"

class Data_base:
    def __init__(self):
        a = random.randint(1000,2600)
        a1 = random.randint(1000,2600)
        a2 = random.randint(1000,2600)
        a3 = random.randint(1000,2600)
        a4 = random.randint(1000,2600)
        a5 = random.randint(1000,2600)
        self.accounts = {
            a: {"name": "Al", "balance": 20000, "type": "savingAccount" , "pin": a},
            a3: {"name": "Sara", "balance": 50000, "type": "currentAccount" , "pin": a1},
            a2: {"name": "awais", "balance": 50000, "type": "currentAccount" , "pin": a2},
            a4: {"name": "sami", "balance": 50000, "type": "currentAccount" , "pin": a3},
            a1: {"name": "luffy", "balance": 50000, "type": "currentAccount" , "pin": a4},
            a5: {"name": "zoro", "balance": 50000, "type": "currentAccount" , "pin": a5}
        }
        
        
    def save_to_file(self, path):
        with open(path, "w") as file:
            json.dump(self.accounts, file, indent=5)

    def load_from_file(self, path):
        with open(path, "r") as file:
            self.accounts = json.load(file)

class sign_up(Data_base):
    def sign_up(self,accounts):
        acc_no = input("Enter new account number: ")

    # check if already exists
        if acc_no in accounts:
            print("❌ Account number already exists. Try login instead.")
            return accounts

        name = input("Enter your full name: ")
        acc_type = input("Enter account type (saving/current): ")
        balance = float(input("Enter opening balance: "))

    # add new account
        accounts[acc_no] = {
            "name": name,
            "type": acc_type,
            "balance": balance
        }

        print(f"✅ Account for {name} created successfully!")
        return accounts

class login(Data_base):
    def login(self,accounts):
        print(Fore.LIGHTBLUE_EX + "--welcome--")
        print(Style.RESET_ALL)
        
        max_attempts = 3
        attempts = 0

        while attempts < max_attempts:
            acc_no = input("Enter your account name: ")

            if acc_no in accounts:
                print(f"✅ {accounts[acc_no]['name']}!")
                max_attempts2 = 3
                attempts2 = 0
                while attempts < max_attempts:
                    pin = input("Enter your account pin:")
                    if pin in accounts:
                        print(f"✅  {accounts[pin]['name']}!")
                        print(Fore.LIGHTGREEN_EX + "Main menu")
                        print(Style.RESET_ALL)
                        print(Fore.LIGHTBLUE_EX + "For Deposit press  1:")
                        print("For withdraw press 2:")
                        print("For Status press   3:")
                        print("For Exit press     1:")
                        print(Style.RESET_ALL)

                        while True:
                            option = int(input("Enter your desire option:"))
                            if option == 1 :
                                amount = int(input("Enter your amount:"))
                                if amount > 0 :
                                    self.accounts[acc_no]["balance"] += amount
                                    print(f"✅ Deposit successful! New balance: {self.data[acc_no]['balance']} PKR")
                                    print("For Exit press      1:")
                                    print("For Main menu press 2:")
                                    option2 = input("Enter your option:")
                                    if option2 == 1:
                                        break
                                    else:
                                        print("Thanks")
                                    break
                                else:
                                    print("Invalid amount")
                            elif option == 2:
                                amount = int(input("Enter your amount:"))
                                if 0 < amount <= self.data[acc_no]["balance"]:
                                    self.accounts[acc_no]["balance"] -= amount
                                    print(f"✅ Withdraw successful! New balance: {self.accounts[acc_no]['balance']} PKR")
                                    option2 = input("Enter your option:")
                                    if option2 == 1:
                                        break
                                    else:
                                        print("Thanks")
                                    break
                                else:
                                    print("Insuificent balance")
                                    break
                            elif option == 3:
                                    print(f"🏦 Account Holder: {self.accounts[acc_no]['name']}")
                                    print(f"💰 Balance: {self.accounts[acc_no]['balance']} PKR")
                                    if option2 == 1:
                                        break
                                    else:
                                        print("Thanks")
                                    break
                            else:
                                print("Thanks for you Assists")
                                break
                else:
                    attempts2 += 1
                    print(f"❌ Invalid pin. Attempts left: {max_attempts - attempts}")

                if attempts2 == max_attempts2:
                    print("🚫 Too many failed attempts. Try later.")
                break
            else:
                attempts += 1
                print(f"❌ Invalid account. Attempts left: {max_attempts - attempts}")

        if attempts == max_attempts:
            print("🚫 Too many failed attempts. Try later.")

if __name__ == "__main__":
    print("For login press   1:")
    print("For sign up press 2:")
    option = int(input("Enter your option: "))
    l  = login()
    s = sign_up()
    if option == 1:
        l.login(accounts="1234")

        



