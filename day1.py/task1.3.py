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
            a2: {"name": "Sara", "balance": 50000, "type": "currentAccount" , "pin": a2},
            a4: {"name": "Sara", "balance": 50000, "type": "currentAccount" , "pin": a3},
            a1: {"name": "Sara", "balance": 50000, "type": "currentAccount" , "pin": a4},
            a5: {"name": "Sara", "balance": 50000, "type": "currentAccount" , "pin": a5}
        }
        
        print(a)
    def save_to_file(self, path):
        with open(path, "w") as file:
            json.dump(self.accounts, file, indent=5)

    def load_from_file(self, path):
        with open(path, "r") as file:
            self.accounts = json.load(file)

c = Data_base()
c.save_to_file(path)
c.load_from_file(path)

