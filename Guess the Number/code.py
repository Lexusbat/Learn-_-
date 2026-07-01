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
           print("You have {attempts} attempts to guess the number")
           guess = input("Make a gues: ")
           if num > guess :
              
           







    else: flag = True