import random
cards = ["11","2","3","4","5","6","7","8","9","10","10","10","10"]
pc_cards = []
user_cards = []
Ace = False # Stays 11, if True value is 1

global answer 

def game_stand(Ace):
    total_pc = 0
    total_user =0
    answer = ""
    remainder_pc = 0 
    remainder_user = 0 
# Stand
    for k in range(2):
     if user_cards[k] == "11":
      if Ace == True: 
        user_cards[k] = "1"
      else: 
        Ace == False

# Add 2 cards fro user together and add 3 cards from dealer. 
    for i in range(3):
      total_pc += int(pc_cards[i])
    for k in range(2):
      total_user += int(user_cards[i])

# Check who has the closest to 21 or bust

    
    if (total_pc <= 21) and (total_user <= 21) :
      remainder_pc = 21 - total_pc
      remainder_user = 21 - total_user
      min( remainder_user,  remainder_pc)
      if total_pc == min( remainder_user,  remainder_pc):
        answer = "PC wins"
      else: answer = "You win"
    elif (total_pc > 21) and (total_user <= 21):
      answer = "PC BUSTED. You win "
    elif (total_user > 21) and (total_pc <= 21):
      answer = "YOU BUSTED. PC wins "
    elif (total_user > 21) and (total_pc > 21):
      answer = "YOU BUSTED. PC BUSTED. DRAW " 
 
    return print(answer)

def game_hit(Ace):
    total_pc = 0
    total_user = 0
    answer = ""
    remainder_pc = 0 
    remainder_user = 0 

# Stand
    for k in range(3):
     if user_cards[k] == "11":  
      if Ace == True: 
        user_cards[k] = "1"
      else: 
        Ace == False

# Add 2 cards fro user together and add 3 cards from dealer. 
    for i in range(3):
      total_pc += int(pc_cards[i])
    for k in range(2):
      total_user += int(user_cards[i])

# Check who has the closest to 21 or bust

    if (total_pc <= 21) and (total_user <= 21) :
      remainder_pc = 21 - total_pc
      remainder_user = 21 - total_user
      min( remainder_user,  remainder_pc)
      if total_pc == min( remainder_user,  remainder_pc):
        answer = "PC wins"
      else: answer = "You win"
    elif (total_pc > 21) and (total_user <= 21):
      answer = "PC BUSTED. You win "
    elif (total_user > 21) and (total_pc <= 21):
      answer = "YOU BUSTED. PC wins "
    elif (total_user > 21) and (total_pc > 21):
      answer = "YOU BUSTED. PC BUSTED. DRAW " 
 

    return print(answer)
  
  
flag = False  
while flag == False:
 choice = input("Would you like to play Black Jack? y/n").lower()
 if choice == 'y':
  for i in range(3):
   hand_pc = random.choice(cards)  # Generates a set of 3 random cards for the cards list above
   pc_cards.append(hand_pc)

  for i in range(3):
   hand_user = random.choice(cards)   # Generates a set of 3 random cards for the cards list above
   user_cards.append(hand_user)

 # Shows the user both 2 of their and the pc/dealers cards
  print(f"The computer got: [ {pc_cards[0]} , {pc_cards[1]}]")        
  print(f"You got: [ {user_cards[0]} , {user_cards[1]}]")     

 # If within user cards a card valued 11 if found, they will be asked whether to change the value of that card to an ace/jack
  if (user_cards[0] == "11") or  (user_cards[1] == "11"):  
    ace_choice = input("Would you like to change the value to an ace or keep it as a jack? a/j").lower()
    if ace_choice == 'a':
      Ace = True
    else:
      Ace = False


 choice2 = input("Would you like to hit or stand? h/s").lower() # Ask to hit or stand
 if choice2 == "s":                                   #if to hit, an additional card would be visible for both parties -> game() function will calc who busted/loss
    print(f"You got: [ {pc_cards[0]} , {pc_cards[1]} , {pc_cards[2]}]")  
    print(f"You got: [ {user_cards[0]} , {user_cards[1]} ]")  

    game_stand(Ace)

 if choice2 == "h":                                   #if to hit, an additional card would be visible for both parties -> game() function will calc who busted/loss
    print(f"You got: [ {pc_cards[0]} , {pc_cards[1]} , {pc_cards[2]}]")  
    print(f"You got: [ {user_cards[0]} , {user_cards[1]} , {user_cards[2]}]")  
    if (user_cards[2] == "11") :  
     ace_choice= input("Would you like to change the value to an ace or keep it as a jack? a/j").lower()
     if ace_choice == 'a':
      Ace = True
     else:
      Ace = False

    game_hit(Ace)

else:
     flag = True