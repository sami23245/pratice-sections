import os

for i in range(2,11):
    folder_name = f"Day_{i}"
    os.makedirs(folder_name, exist_ok=True)
    print(f"✅ Created folder: {folder_name}")