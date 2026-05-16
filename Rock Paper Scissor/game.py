choice = input("Enter your choice (rock, paper, scissors): ")
for stages in choice:
    if stages == "rock":
        print("You chose rock!")
    elif stages == "paper":
        print("You chose paper!")
    elif stages == "scissors":
        print("You chose scissors!")
else:
    print("Invalid choice. Please choose rock, paper, or scissors.")