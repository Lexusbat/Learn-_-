import random
cards = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
pc_cards = []
user_cards = []

def game():
    total_pc = 0
    total_user =0
    for i in range(3):
      total_pc += int(pc_cards[i])
    for k in range(3):
      total_user += int(user_cards[i])
    if (total_user > total_pc) and (total_user <= 21):
      answer =  print("You win")
    elif(total_user < total_pc) and (total_pc <= 21):
      answer = print("PC win")
    elif total_user > 21:
      answer =   print("Bust. You lose")
    elif total_pc > 21:
      answer =   print("Bust. You win")
      
    return answer 
  
flag = False  
while flag == False:
 choice = input("Would you like to play Black Jack? y/n").lower()
 if choice == 'y':
  for i in range(3):
   hand_pc = random.choice(cards)
   pc_cards.append(hand_pc)

  for i in range(3):
   hand_user = random.choice(cards)
   user_cards.append(hand_user)
  print(f"The computer got: [ {pc_cards[0]} , {pc_cards[1]}]")        
  print(f"You got: [ {pc_cards[0]} , {pc_cards[1]}]")  
  choice2 = print("Would you like to hit or stand? h/s")
  if choice2 == "h":
    print(f"You got: [ {pc_cards[0]} , {pc_cards[1]} , {pc_cards[2]}]")  
    print(f"You got: [ {user_cards[0]} , {user_cards[1]} , {user_cards[2]}]")  
    game()
 else:
     flag = False               
            
