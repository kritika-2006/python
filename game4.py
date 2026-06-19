students = ["kritika","manvi","anjali","Rahul","gurleen"]
while True:
    print("\n 1. view students.")
    print("2. add students.")
    print("3. remove students.")
    print("4. checkout and exit.")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(" Present student:",students)
    elif choice == 2:
        name = input("add students in the list,who are present")
        students.append(name)
        print(name,"added")
    elif choice == 3:
        name = input("remove students in the list , who are not present")
        students.remove(name)
        print(name,"remove")
    elif choice == 4:
        print("attendance complete!")
        print("total students present",len (students))
        break