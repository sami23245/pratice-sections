"""1. Banking System (Refresher)
Design classes for `Account`, `SavingsAccount`, `CurrentAccount`.
Requirements:
- Implement deposit/withdraw, monthly interest calculation for SavingsAccount, and overdraft for CurrentAccount.
- Provide a CLI interface for adding accounts and performing transactions. Use simple JSON file persistence."""

import json
import os

path = r"/workspaces/pratice-sections/day1.py/accounts.json"

import json

class Data:
    def __init__(self):
        self.accounts = {
            "1234": {
                "name": "Ali",
                "balance": 20000,
                "type": "savingAccount"
            },
            "5678": {
                "name": "Sara",
                "balance": 50000,
                "type": "currentAccount"
            }
        }

    def save_to_file(self, path):
        with open(path, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def load_from_file(self, path):
        with open(path, "r") as file:
            self.accounts = json.load(file)

    def get_account(self, acc_no):
        return self.accounts.get(acc_no, None)

class Accounts(Data):
    bank_name = "bank of punjab"
    #def __init__(self,account_no = None, name= None , balance = None,data = None):
        #self.account_no = account_no
        #self.balace = balance
        # self.name = name
        # self.data = data
    def Deposit(self):
    # Ask for account and amount
        self.account_no = input("Enter your account number: ")
        self.amount = float(input("Enter amount to deposit: "))

    # Check if account exists
        if self.account_no in self.data:
            print("✅ Your account is available.")

        # Deposit should only accept positive amounts
            if self.amount <= 0:
                print("❌ Invalid amount. Please enter a positive number.")
                return

        # Add amount to balance
            self.data[self.account_no]["balance"] += self.amount
            print(f"💰 Deposit successful! New balance: {self.data[self.account_no]['balance']}")

            # Optional: Ask for slip
            slip_gen = input("Do you want a slip? (yes/no): ").lower()
            if slip_gen == "yes":
                print("🧾 Generating slip...")
                print(f"Account: {self.account_no}")
                print(f"Deposited: {self.amount}")
                print(f"New Balance: {self.data[self.account_no]['balance']}")
            else:
                print("😊 Happy to assist you!")

        else:
            print("❌ Account not found.")
        #new section start
    def withdraw(self):
    # Ask for account and amount
        self.account_no = input("Enter your account number: ")
        self.amount = float(input("Enter amount to deposit: "))

    # Check if account exists
        if self.account_no in self.data:
            print("✅ Your account is available.")

            # Deposit should only accept positive amounts
            if self.amount <= 0:
                print("❌ Invalid amount. Please enter a positive number.")
                return

            # Add amount to balance
            self.data[self.account_no]["balance"] -= self.amount
            print(f"💰 withdraw successful! New balance: {self.data[self.account_no]['balance']}")

            # Optional: Ask for slip
            slip_gen = input("Do you want a slip? (yes/no): ").lower()
            if slip_gen == "yes":
                print("🧾 Generating slip...")
                print(f"Account: {self.account_no}")
                print(f"Deposited: {self.amount}")
                print(f"New Balance: {self.data[self.account_no]['balance']}")
            else:
                print("😊 Happy to assist you!")

        else:
            print("❌ Account not found.")

    def show_balance(self):
        self.account_no = input("Enter your account number: ")
        self.amount = float(input("Enter amount to deposit: "))

        if self.account_no in self.data:
            print(f"your account num is {self.data[self.balance]}")
        else:
            print ("invalid")

class SavingAccounts(Accounts):
    def __init__(self, account_no, name , balance,interst_rate):
        super().__init__(account_no, name , balance, interst_rate)
        
    def apply_interst(self):
        self.balance += self.balance * (self.interst_rate / 100)
class current_account(Accounts):
    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance, overdraft_limit)

        self.ammount = int(input("enter your ammount: "))

#making objects
a = __main__.Accounts()
print(a.withdraw)
