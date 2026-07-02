import random #Import random module
from logo import load_logo, load_vs #Imports imagaes from logo.py
from data import celebrities #Imports data from data.py
global right_option_celeb


load_logo()


def get_random_celebrity():
    comparison_celebrityA_info = ""
    comparison_celebrityA_followers = 0
    """Returns a random celebrity from the data list."""
    comparison_celebrityA = random.choice(celebrities)
    comparison_celebrityA_info = f"{comparison_celebrityA['name']}, a {comparison_celebrityA['profession']} from {comparison_celebrityA['country']} "
    comparison_celebrityA_followers = comparison_celebrityA['followers_millions']

    return comparison_celebrityA_info,comparison_celebrityA_followers
    
def get_random_celebrity2():
    comparison_celebrityB_info = ""
    comparison_celebrityB_followers = 0
    """Returns a random celebrity from the data list."""
    # Ensure that the second celebrity is not the same as the first one
    comparison_celebrityB = random.choice(celebrities)
    comparison_celebrityB_info = f"{comparison_celebrityB['name']}, a {comparison_celebrityB['profession']} from {comparison_celebrityB['country']} "
    comparison_celebrityB_followers = comparison_celebrityB['followers_millions']

    return comparison_celebrityB_info, comparison_celebrityB_followers
    


print("Welcome to Higher vs Lower game!")
print("The goal is to compare celebs Instagram followers. Guess the one with the moste followers and lets see how many point you can score!")
choice = input("Are you ready to play? Type 'y' for yes or 'n' for no: ").lower()
flag = False
flag_game = False
end_game = 0
if choice not in ['y', 'n']:
    print("Invalid input. Please enter 'y' or 'n'.")
elif choice == 'y':
   print("Great! Let's get started!")

   while flag_game == False:

    # Continue with the game logic here
    comparison_celebrityA_info, comparison_celebrityA_followers = get_random_celebrity()
    comparison_celebrityB_info, comparison_celebrityB_followers = get_random_celebrity2()
    max_followers = 0
    score = 0
    print("Comparison A: ") 
    print(comparison_celebrityA_info)
    load_vs()
    print("Comparison B: ")
    
    if get_random_celebrity2() == get_random_celebrity():
        print(comparison_celebrityB_info)
        flag = True
    else: print(comparison_celebrityB_info)
      
    """ Max variable checks which A/B option has most followers, then compare it with the option chosen from user -
        If max_followers == followers amount == option chosen via guess variable, then increase score variable, else end game.
    """
    max_followers = max(comparison_celebrityA_followers,comparison_celebrityB_followers)
    guess = input("Guess, who has more followers? A/B").lower()
    if guess not in ["a","b"]:
       print("Invalid Answer, remember 'A' or 'B'")
       guess = input("Guess, who has more followers? A/B").lower()
    elif guess == 'a':
       if max_followers != comparison_celebrityA_followers:
        print(f"Wrong answer! That's game! \n Your Final Score is: {score}")
        end_game += 1
       elif max_followers == comparison_celebrityA_followers:
          print("Lots of followers! You are correct!")
          score += 1
          print(f"Your Score is: {score}")

    elif guess == 'b':
       if max_followers != comparison_celebrityB_followers:
        print(f"Wrong answer! That's game! \n Your Final Score is: {score}")
        end_game += 1
       elif max_followers == comparison_celebrityB_followers:
          print("Lots of followers! You are correct!")
          score += 1
          print(f"Your Score is: {score}")

elif choice == 'n':
    print("No worries! Come back when you're ready. Goodbye!")
    exit()

