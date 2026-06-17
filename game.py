secret_number = 2
for attempt in range (1,6):
    num = int (input("Enter your number:"))
    
    if num == secret_number  :
        print("You Win🎉")
        break

    elif num < secret_number:
        print ("Think the Bigger number")

    elif num > secret_number :
        print ("Think the Smaller number")
    
   
