import os
current_folder = os.getcwd()
print("Aap abi is folder mein ho:",current_folder)

files = os.listdir()
print("\n Is folder meinyeh saari files hain:")

for file in files:
    print("-",file)