import random

alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = ["apple", "aardvark", "strawberry"]
correct = 0
chosen_word = random.choice(word_list)
print(chosen_word)
 

user_letter = input("Type a letter to guess word").lower()
if user_letter not in alph_list:
    print("That is not a valid letter.")
    user_letter = input("Type a letter to guess word").lower()
else: 
    for char in chosen_word:
        if user_letter == char:
            print("Right")
        else:
            print("Wrong")


    