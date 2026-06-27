import os
target_file = "activity_logs.txt"

if os.path.exists(target_file):
   with open(target_file,"r") as file:
    print(file.read())
else:
   print("Warning: Backup log file is missing!")