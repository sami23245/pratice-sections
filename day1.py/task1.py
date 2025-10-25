"""1. Banking System (Refresher)
Design classes for `Account`, `SavingsAccount`, `CurrentAccount`.
Requirements:
- Implement deposit/withdraw, monthly interest calculation for SavingsAccount, and overdraft for CurrentAccount.
- Provide a CLI interface for adding accounts and performing transactions. Use simple JSON file persistence."""

class Accounts:
    bank_name = "bank of punjab"
    def __init__(self,account_no, name , balance):
        self.account_no = account_no
        self.name = name
        self.balance = balance
    def Deposit(amount):
        pass
    def withdraw(amount):
        pass
    def show_balance():
        pass
class SavingAccounts(Accounts):
    def __init__(self, interst_rate):
        self.interst_rate = interst_rate
    def apply_interst(self):
        self.balance += self.balance * (self.interst_rate / 100)
class current_account(Accounts):
    def __init__(self, overdraft_limit):
        self.ammount = int(input("enter your ammount: "))
        self.overdraft_limit = overdraft_limit
        if self.balance - self.amount >= -self.overdraft_limit:
            print("herrea")
        