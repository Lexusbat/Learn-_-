import random 

image = """
  _______  ____  ____   _______   ________  ________      ___________  __    __    _______      _____  ___   ____  ____  ___      ___  _______    _______   _______   
 /" _   "|("  _||_ " | /"     "| /"       )/"       )    ("     _   ")/" |  | "\  /"     "|    (\"   \|"  \ ("  _||_ " ||"  \    /"  ||   _  "\  /"     "| /"      \  
(: ( \___)|   (  ) : |(: ______)(:   \___/(:   \___/      )__/  \\__/(:  (__)  :)(: ______)    |.\\   \    ||   (  ) : | \   \  //   |(. |_)  :)(: ______)|:        | 
 \/ \     (:  |  | . ) \/    |   \___  \   \___  \           \\_ /    \/      \/  \/    |      |: \.   \\  |(:  |  | . ) /\\  \/.    ||:     \/  \/    |  |_____/   ) 
 //  \ ___ \\ \__/ //  // ___)_   __/  \\   __/  \\          |.  |    //  __  \\  // ___)_     |.  \    \. | \\ \__/ // |: \.        |(|  _  \\  // ___)_  //      /  
(:   _(  _|/\\ __ //\ (:      "| /" \   :) /" \   :)         \:  |   (:  (  )  :)(:      "|    |    \    \ | /\\ __ //\ |.  \    /:  ||: |_)  :)(:      "||:  __   \  
 \_______)(__________) \_______)(_______/ (_______/           \__|    \__|  |__/  \_______)     \___|\____\)(__________)|___|\__/|___|(_______/  \_______)|__|  \___) 
                                                                                                                                                                     
                                                                                                                                                                      
 """

print("Welcome to the Guess te Number Game!!")

def low(remainder):
   answer = ""
   if remainder <= 10:
      answer = "Quite Low...close"
   elif remainder in range(11, 26):
      answer = "Too Low...almost"
   elif remainder in range(26, 51):
      answer = "Very Low...try again"
   elif remainder in range(51,101):
      answer = "Hella Low...boi up!"

   return print(answer)

def high(remainder):
   answer = ""
   if remainder <= 10:
      answer = "Quite High...close"
   elif remainder in range(11, 26):
      answer = "Too High...almost"
   elif remainder in range(26, 51):
      answer = "Very High...try again"
   elif remainder in range(51,101):
      answer = "Hella High...boi down!"

   return print(answer)

flag = False
while flag == False:
    num = random.randint(0, 101)
    remainder = 0

    choice = input("Would you like to play? y/n").lower()
    if choice not in ["y","n"]:
        print("invalid input")
    elif choice == "y":
        print("Im guessing a number between 1 to 100")
        Dif = input("Choose a difficulty. 'e' for easy or 'h' for hard").lower()
        if Dif not in ["e","h"]:
         print("invalid input")
        elif Dif == "e":
           attempts = 10
           flag2 = False
           while flag2 == False :
            print(f"You have {attempts} attempts to guess the number. ")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if num == guess :
              print("Wow you got it right!")
              flag2 = True
            elif attempts == 0:
               print("You Lose! Guess better!!")
               flag2 = True

            if num > guess :
              remainder = num - guess
              low(remainder)
            elif num < guess :
              remainder = guess - num
              high(remainder)
            
        elif Dif == "h":
           attempts = 5
           flag2 = False
           while flag2 == False :
            print(f"You have {attempts} attempts to guess the number. ")
            guess = int(input("Make a guess: "))
            attempts -= 1
            if num == guess :
              print("Wow you got it right!")
              flag2 = True
            elif attempts == 0:
               print("You Lose! Guess better!!")
               flag2 = True

            if num > guess :
              remainder = num - guess
              low(remainder)
            elif num < guess :
              remainder = guess - num
              high(remainder)
              
            
    else: flag = True