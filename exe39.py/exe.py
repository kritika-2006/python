with open ("activity_logs.txt","a") as file:
    file.write("Log: System running normally.\n")

with open ("activity_logs.txt","a") as file:
    file.write("Log: New login detected from user root.\n")

with open ("activity_logs.txt","r") as file:
    print(file.read())


