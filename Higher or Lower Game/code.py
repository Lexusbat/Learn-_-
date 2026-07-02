import random #Import random module
from logo import load_logo, load_vs #Imports imagaes from logo.py
from data import celebrities #Imports data from data.py
global comparison_celebrityA


load_logo()
#load_vs()

def get_random_celebrity():
    comparison_celebrityA_info = ""
    """Returns a random celebrity from the data list."""
    comparison_celebrityA = random.choice(celebrities)
    comparison_celebrityA_info = f"{comparison_celebrityA['name']}, a {comparison_celebrityA['profession']} from {comparison_celebrityA['country']} "

    return comparison_celebrityA_info
    
def get_random_celebrity2():
    comparison_celebrityB_info = ""
    """Returns a random celebrity from the data list."""
    # Ensure that the second celebrity is not the same as the first one
    comparison_celebrityB = random.choice(celebrities)
    comparison_celebrityB_info = f"{comparison_celebrityB['name']}, a {comparison_celebrityB['profession']} from {comparison_celebrityB['country']} "

    return comparison_celebrityB_info
    


print("Welcome to Higher vs Lower game!")
print("The goal is to compare celebs Instagram followers. Guess the one with the moste followers and lets see how many point you can score!")
choice = input("Are you ready to play? Type 'y' for yes or 'n' for no: ").lower()
flag = False

if choice not in ['y', 'n']:
    print("Invalid input. Please enter 'y' or 'n'.")
elif choice == 'y':
    print("Great! Let's get started!")
    # Continue with the game logic here
    print("Comparison A: ") 
    print(get_random_celebrity())
    load_vs()
    print("Comparison B: ")
    while flag == False:
     if get_random_celebrity2() == get_random_celebrity():
        print(get_random_celebrity2())
        flag = True
     else: print(get_random_celebrity2())
     exit()






    ''' if comparison_celebrityB := random.choice(celebrities) == comparison_celebrityA:
        comparison_celebrityB = random.choice(celebrities)'''













elif choice == 'n':
    print("No worries! Come back when you're ready. Goodbye!")
    exit()

