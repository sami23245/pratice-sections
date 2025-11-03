import json

path = "accounts.json"

# Step 1: Load data
try:
    with open(path, "r") as f:
        data = json.load(f)
except FileNotFoundError:
    data = {}  # empty if file doesn’t exist

# Step 2: Take input
acc_no = input("Enter new account number: ")
name = input("Enter account holder name: ")
balance = float(input("Enter opening balance: "))
acc_type = input("Enter account type (saving/current): ")

# Step 3: Add to data
data[acc_no] = {
    "name": name,
    "balance": balance,
    "type": acc_type
}

# Step 4: Save back
with open(path, "w") as f:
    json.dump(data, f, indent=4)

print("✅ New account added successfully!")
