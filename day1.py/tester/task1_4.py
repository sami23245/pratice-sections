# Existing database (could also be loaded from a file)
data = {
    "1001": {"name": "Ali", "balance": 5000, "type": "saving"},
    "1002": {"name": "Sara", "balance": 8000, "type": "current"}
}

def sign_up(data):
    acc_no = input("Enter new account number: ")

    # check if already exists
    if acc_no in data:
        print("❌ Account number already exists. Try login instead.")
        return data

    name = input("Enter your full name: ")
    acc_type = input("Enter account type (saving/current): ")
    balance = float(input("Enter opening balance: "))

    # add new account
    data[acc_no] = {
        "name": name,
        "type": acc_type,
        "balance": balance
    }

    print(f"✅ Account for {name} created successfully!")
    return data

# Example use
# data = sign_up(data)
# print(data)print(f"✅ Deposit successful! New balance: {self.data[acc_no]['balance']} PKR")
# while True:
#     password = input("Enter your password: ")
#     if password == "1234":
#         print("✅ Access granted")
#         break  # exits the loop
#     else:
#         print("❌ Wrong password, try again")
while True:
    option = int(input("Enter your desire option:"))
    if option == 1 :
        amount = int(input("Enter your amount:"))
        if amount > 0 :
            
            print(f"✅ Deposit successful! New balance:  PKR")
            option2 = input("Enter")
            if option2 == 1:
                break
            else:
                print("thanks")
            break
                
            
        else:
            print("Invalid amount")
             
