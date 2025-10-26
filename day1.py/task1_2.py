import json
import os

path = r"/workspaces/pratice-sections/day1.py/accounts.json"

class Data:
    def __init__(self):
        self.accounts = {
            "1234": {"name": "Ali", "balance": 20000, "type": "savingAccount"},
            "5678": {"name": "Sara", "balance": 50000, "type": "currentAccount"}
        }

    def save_to_file(self, path):
        with open(path, "w") as file:
            json.dump(self.accounts, file, indent=4)

    def load_from_file(self, path):
        with open(path, "r") as file:
            self.accounts = json.load(file)


class Accounts(Data):
    bank_name = "Bank of Punjab"

    def __init__(self):
        super().__init__()
        self.data = self.accounts

    def deposit(self):
        acc_no = input("Enter your account number: ")
        amount = float(input("Enter amount to deposit: "))

        if acc_no in self.data:
            if amount > 0:
                self.data[acc_no]["balance"] += amount
                print(f"✅ Deposit successful! New balance: {self.data[acc_no]['balance']} PKR")
            else:
                print("❌ Invalid deposit amount.")
        else:
            print("❌ Account not found.")

    def withdraw(self):
        acc_no = input("Enter your account number: ")
        amount = float(input("Enter amount to withdraw: "))

        if acc_no in self.data:
            if 0 < amount <= self.data[acc_no]["balance"]:
                self.data[acc_no]["balance"] -= amount
                print(f"✅ Withdraw successful! New balance: {self.data[acc_no]['balance']} PKR")
            else:
                print("❌ Insufficient balance or invalid amount.")
        else:
            print("❌ Account not found.")

    def show_balance(self):
        acc_no = input("Enter your account number: ")
        if acc_no in self.data:
            print(f"🏦 Account Holder: {self.data[acc_no]['name']}")
            print(f"💰 Balance: {self.data[acc_no]['balance']} PKR")
        else:
            print("❌ Account not found.")


if __name__ == "__main__":
    a = Accounts()
    while True:
        print("\n--- BANK MENU ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            a.deposit()
        elif choice == "2":
            a.withdraw()
        elif choice == "3":
            a.show_balance()
        elif choice == "4":
            a.save_to_file(path)
            print("✅ Data saved. Goodbye!")
            break
        else:
            print("❌ Invalid choice.")
