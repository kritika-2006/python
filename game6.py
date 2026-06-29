import  random
user_choice = input("Enter your choice:('Rock','Paper','scissor'):")
options = ("Rock","Paper","scissor")
computer_choice = random.choice(options)
print(f"computer choose : {computer_choice}")

if user_choice == computer_choice:
    print("It's a Tie! ")

elif user_choice == "Paper":
    if computer_choice == "Rock":
        print("You win !")
    else:
        print("computer wins!")

elif user_choice == "scissor":
   if computer_choice == "paper":
      print("You win !")
   else:
      print("computer wins!")

    
elif user_choice == "Rock":
   if computer_choice == "scissor":
    print("You win! ")
   else:
    print("computer wins!")
