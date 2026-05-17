import random


options = ["rock", "paper", "scissors"]
            # 1        2       3

choice_pc = random.choice(options)
count = 0
point = 0
invalid = 0
pc_point = 0

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
        point += 1
       else :
        print("You lose! Paper covers rock.")
        pc_point += 1
    elif choice == 'paper':
        print(f"Computer chose {choice_pc}")
        if choice_pc == 'rock':
          print("You win! Paper covers rock.")
          point += 1
        else :
          print("You lose! Scissors cut paper.")
          pc_point += 1
    elif choice == 'scissors':
        print(f"Computer chose {choice_pc}")
        if choice_pc == 'paper':
          print("You win! Scissors cut paper.")
          point += 1
        else :
           print("You lose! Rock crushes scissors.")
           pc_point += 1
    else:
      print("Invalid choice. Please choose rock, paper, or scissors.")
      invalid += 1
  
if pc_point > point:
   print("HAHA. YOU LOST AGAINTS A COMPUTER!")
   #print(pc_point + " >" + point)
elif pc_point < point:
   print("WOW YOU WON AGAINST A COMPUTER. MUST FEEL GREAT FOR YOU DOESN'T IT??")
   #print(pc_point + " <" + point)
elif invalid > point:
   print("Invalid game play. Start over")
  

