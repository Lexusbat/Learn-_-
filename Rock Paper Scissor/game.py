import random


options = ["rock", "paper", "scissors"]
            # 1        2       3
choice_pc = random.choice(options)
count = 0
while count < 3:
    choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
    print("Rock...")
    print("Paper...")
    print("Scissors...")
    print("Shoot!")
    count += 1
    if choice == choice_pc:
       print('It"s a tie')
    elif choice == 'rock':
       print(f"Computer chose {choice_pc}")
       if choice_pc == 'scissors':
        print("You win! Rock crushes scissors.")
       else :
        print("You lose! Paper covers rock.")
    elif choice == 'paper':
        print(f"Computer chose {choice_pc}")
        if choice_pc == 'rock':
          print("You win! Paper covers rock.")
        else :
          print("You lose! Scissors cut paper.")
    elif choice == 'scissors':
        print(f"Computer chose {choice_pc}")
        if choice_pc == 'paper':
          print("You win! Scissors cut paper.")
        else :
           print("You lose! Rock crushes scissors.")
    else:
      print("Invalid choice. Please choose rock, paper, or scissors.")

#play_again = print("Would you like to play the game again? Y/N").lower()
#if play_again == 'y':
 #  count = 0

