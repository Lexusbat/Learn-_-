import random
import math
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

card_values = {
    "A": [1, 11],
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10
}
your_cards = []
flag = False

def pc_play():
   
    pc_cards = []
    for i in range(2):
     card = random.choice(tuple(card_values.keys()))
     pc_cards.append(card)


    return print(f"{pc_cards[0]} hello") 
#Need to find a way to hide 2 and 3 card for next plays

if play == "y":
 pc_play()

