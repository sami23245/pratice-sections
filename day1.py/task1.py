"""1. Banking System (Refresher)
Design classes for `Account`, `SavingsAccount`, `CurrentAccount`.
Requirements:
- Implement deposit/withdraw, monthly interest calculation for SavingsAccount, and overdraft for CurrentAccount.
- Provide a CLI interface for adding accounts and performing transactions. Use simple JSON file persistence."""

import json
import os

path = r"/workspaces/pratice-sections/day1.py/accounts.json"

class Accounts:
    bank_name = "bank of punjab"
    def __init__(self,account_no, name , balance):
        super().__init__(account_no, name , balance)
    def Deposit(self,amount):
        pass
    def withdraw(self, amount):
        pass
    def show_balance(self):
        pass
class SavingAccounts(Accounts):
    def __init__(self, account_no, name , balance,interst_rate):
        super().__init__(account_no, name , balance, interst_rate)
        
    def apply_interst(self):
        self.balance += self.balance * (self.interst_rate / 100)
class current_account(Accounts):
    def __init__(self, account_no, name, balance, overdraft_limit):
        super().__init__(account_no, name, balance, overdraft_limit)

        self.ammount = int(input("enter your ammount: "))
        
        
    

Account_name = {
    "1234": {
        "name": "ali",
        "balance": 20000,
        "type": "savingAccount"
    }
}

json_data = json.dumps(Account_name, indent=4)
print(json_data)

with open(path, "w") as f:
    json.dump(Account_name, f, indent=4)

option = str(input("plz enter yes if you want to delete this file:"))

if option == "yes":
    
    os.remove(path)
else:
    print ("okkkk")


#print(json.dumps({"name": "John", "age": 30}),type(y))


