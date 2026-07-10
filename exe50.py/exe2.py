import os
current_folder = os.getcwd()
print("AAp abhi is folder mein ho:",current_folder)

files = os.listdir()
print("\n is mein yeh sarri files h :")

for file in files:
    print("-",file)
# naya folder banana
folder_name = "kritika_hacking_lab"

if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Mubarak ho! '{folder_name}' naam ka naya folder ban gya.")
else:
    print("Yeh folder toh phele sa hi bna hua h!")