import random

choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()
options = ["rock", "paper", "scissors"]
            # 1        2       3
choice_pc = random.choice(options)

for count in range(3):
    print("Rock...")
    print("Paper...")
    print("Scissors...")
print("Shoot!")
if choice == choice_pc:
    print('It"s a tie')
elif choice == 'rock':
    if choice_pc == 'scissors':
        print("You win! Rock crushes scissors.")
    else :
        print("You lose! Paper covers rock.")
elif choice == 'paper':
    if choice_pc == 'rock':paper
        print("You win! Paper covers rock.")
    else :
        print("You lose! Scissors cut paper.")
elif choice == 'scissors':
    if choice_pc == 'paper':
        print("You win! Scissors cut paper.")
    else :
        print("You lose! Rock crushes scissors.")

breakpoint()
print("Would you like to play the game again? Y/N")