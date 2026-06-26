# 1. Pehle "w" mode se file khud generate karein aur data likhein
with open("secret_flag.txt", "w") as file:
    file.write("FLAG{file_handling_mastered}")

# 2. Ab aapka purana code (Read Mode) perfectly chalega!
with open("secret_flag.txt", "r") as file:
    flag_data = file.read()
    print(flag_data)