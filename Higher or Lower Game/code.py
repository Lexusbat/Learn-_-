import random #Import random module
from logo import load_logo, load_vs #Imports imagaes from logo.py
from data import celebrities #Imports data from data.py


load_logo()
#load_vs()

def get_random_celebrity():
    """Returns a random celebrity from the data list."""
    comparison_celebrityA = random.choice(celebrities)
    # Ensure that the second celebrity is not the same as the first one
    if comparison_celebrityB := random.choice(celebrities) == comparison_celebrityA:
        comparison_celebrityB = random.choice(celebrities)
    return comparison_celebrityA, comparison_celebrityB

print("Welcome to Higher vs Lower game!")
print("The goal is to compare celebs Instagram followers. Guess the one with the moste followers and lets see how many point you can score!")
choice = input("Are you ready to play? Type 'y' for yes or 'n' for no: ").lower()

if choice not in ['y', 'n']:
    print("Invalid input. Please enter 'y' or 'n'.")
elif choice == 'y':
    print("Great! Let's get started!")
    # Continue with the game logic here
    get_random_celebrity()


















elif choice == 'n':
    print("No worries! Come back when you're ready. Goodbye!")
    exit()

