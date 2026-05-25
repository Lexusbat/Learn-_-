#Loops and Lists
import random
string = ' '
let_part = ' '
num_part = ' '
sym_part =' '
password = " "

print("Welcome to the password generator")
letters = int(input("How many letters would you like?"))
print(str(letters)) # string
symbols = int(input("How many symbols would you like?"))
print(str(symbols)) # string
numbers = int(input("How many numbers would you like"))
print(str(numbers)) # string


letters_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols_list = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
    '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~']

numbers_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
password_list =[]
for letter in range(0, letters) :
    password_list.append(random.choice(letters_list))

  
for symbols in range(0, symbols) :
    password_list.append(random.choice(symbols_list))

for letter in range(0, numbers) :
    password_list.append(random.choice(numbers_list))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f"This is your generated password: {password}")

    

