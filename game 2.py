choices = ["rock","paper","scissor"]
computer_choice = choices[1]
user = input("Enter rock,paper,scissor:")
if computer_choice == user:
    print("match Tie 🤝")
elif (user == "paper" and computer_choice == "rock") or\
      (user == "rock" and computer_choice == "scissor") or\
      (user == "scissor" and computer_choice == "paper"):

    print("user wins 🎉")
else :
    print("computer wins 🎊")