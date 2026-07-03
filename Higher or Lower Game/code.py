import random #Import random module
from logo import load_logo, load_vs #Imports imagaes from logo.py
from data import celebrities #Imports data from data.py
global right_option_celeb  
celeb_compare_info = {}



load_logo()


def get_random_celebrity():
    comparison_celebrity_info = ""
    comparison_celebrity_followers = 0
    """Returns a random celebrity from the data list."""
    comparison_celebrity = random.choice(celebrities)
    comparison_celebrity_info = f"{comparison_celebrity['name']}, a {comparison_celebrity['profession']} from {comparison_celebrity['country']} "
    comparison_celebrity_followers = comparison_celebrity['followers_millions']

    return comparison_celebrity_info,comparison_celebrity_followers

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
   right_option_celeb = ""
#CREATING 2 CELEB ACCOUNTS WITH ONE FUNCTION
   comparison_celebrity_info, comparison_celebrity_followers = get_random_celebrity()
   celebAinfo = comparison_celebrity_info
   celebAfollowers = comparison_celebrity_followers

   celeb_first_info = ''
   celeb_first_followers = 0

   """Returns a random celebrity from the data list."""
   comparison_celebrity = random.choice(celebrities)
   celeb_first_info = f"{comparison_celebrity['name']}, a {comparison_celebrity['profession']} from {comparison_celebrity['country']} "
   celeb_first_followers = comparison_celebrity['followers_millions']

   celeb_compare_info.append('celeb_first_info') = celeb_first_followers


   flag = False
   max_followers = 0
   score = 0
   print("Comparison A: ") 
   print(celebAinfo)
   load_vs() 
   print("Comparison B: ")
   print()


   max_followers = max(celebAfollowers,celeb_first_followers)
   while flag_game == False:


    """ Max variable checks which A/B option has most followers, then compare it with the option chosen from user -
        If max_followers == followers amount == option chosen via guess variable, then increase score variable, else end game.
    """
   guess = input("Guess, who has more followers? A/B").lower()
   if guess not in ["a","b"]:
       print("Invalid Answer, remember 'A' or 'B'")
       guess = input("Guess, who has more followers? A/B").lower()

   elif guess == 'a':
       if max_followers != celebAinfo:
        print(f"Wrong answer! That's game! \n++Your Final Score is: {score}++")
        end_game += 1
       elif max_followers == celebAinfo:
          print("Lots of followers! You are correct!")
          score += 1
          right_option_celeb = celebAinfo
          celeb_compare[0] = right_option_celeb
          celeb_compare[1] = ""
          print(f"Your Score is: {score}")
   elif guess == 'b':
       if max_followers != celeb_first_followers:
        print(f"Wrong answer! That's game! \n++Your Final Score is: {score}++")
        end_game += 1
       elif max_followers == celeb_first_followers:
          print("Lots of followers! You are correct!")
          score += 1
          right_option_celeb = celeb_first_followers
          print(f"Your Score is: {score}")
          
    
       if right_option_celeb== comparison_celebrity_info:
        print(right_option_celeb)
        flag = True
       else: print(right_option_celeb)
      
   elif end_game == 1:
        flag_game = True

elif choice == 'n':
    print("No worries! Come back when you're ready. Goodbye!")
    exit()

