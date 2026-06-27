import os
file_name = "activity_logs.txt"

if os.path.exists(file_name):
    print("Haaye! File mil gayi, ab ise read kar sakte hain.")
else:
    print("Oops! File nahi mili,safe exit.")