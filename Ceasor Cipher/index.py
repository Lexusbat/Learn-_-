import math
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

print(logo)
print("Welcome to Ceasar Cipher")
direction = input("Type 'E' to encrypt or 'D' to decode a text ")
text = input("Type your message here ")
shift = int(input("Type in a shift number for encrypting/decoding "))
text_list = []

def encrypt(text,shift):
    string ='' 
    position = 0

    for char in text:
        if char in alph:
            position = alph.index(char)
            string = string + alph[position + shift ]
        elif char == " ":
             string = string + " "

    return print(string)
        

def decrypt(text,shift):
    string ='' 
    position = 0

    for char in text:
        if char in alph:
            position = alph.index(char)
            string = string + alph[position - shift ]
        elif char == " ":
             string = string + " "

      
    return print(string)
        


if (direction == 'E') or (direction == 'e' ):
       print("Here is the messages encoded: ")
       encrypt(text,shift)
elif (direction == 'D') or (direction == 'd' ):
       print("Here is the messages decoded: ")
       decrypt(text,shift)

else:
     print("invalid")

