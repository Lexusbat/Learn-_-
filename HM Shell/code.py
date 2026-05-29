import random

alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = ["apple", "aardvark", "strawberry"]
string_list = []
string = ""
count = 0
flag = 0
chosen_word = random.choice(word_list)
print(chosen_word)
for underscore in range(0,len(chosen_word)):
    string_list.append("_")

for underrscore in string_list:
    string += "_"
print(string)



user_letter = input("Type a letter to guess word").lower()
if user_letter not in alph_list:
    print("That is not a valid letter.")
    user_letter = input("Type a letter to guess word").lower()
else: 
    for char in chosen_word:
        count += 1
        if user_letter == char:
             flag += 0
             string_list.insert(count-1,user_letter)       
             for remove in range(flag + 1):
                 string_list.pop()
        

#print(string_list) 
string =""
for char in string_list:
    string += char
print(string)

