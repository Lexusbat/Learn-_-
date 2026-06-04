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

symbols = [
    '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.',
    '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    '{', '|', '}', '~'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
#lipps asvph
print(logo)
print("Welcome to Ceasar Cipher")




def encrypt(text,shift):
    string ='' 
    position = 0

    for char in text:
        if (char == " ") or (char in numbers) or (char in symbols):
             string = string + char

        if char in alph:
            position = alph.index(char) + shift 
            position %= len(alph)
            string = string + alph[position]
      
    return print(string)
        

def decrypt(text,shift):
    string ='' 
    position = 0

    for char in text:
        if (char == " ") or (char in numbers) or (char in symbols):
             string = string + char

        elif char in alph:
            position = alph.index(char) - shift 
            position %= len(alph)
            string = string + alph[position] # 0 - 24  mod 3 
    

      
    return print(string)

flag = False 

while flag == False :
     
 direction = input("Type 'E' to encrypt or 'D' to decode a text \n")
 text = str(input("Type your message here \n"))
 shift = int(input("Type in a shift number for encrypting/decoding \n"))
 if (direction == 'E') or (direction == 'e' ):
       print("Here is the messages encoded: ")
       encrypt(text,shift)
       choice = input("Would you like to continue? y/n\n").lower()
       if choice == 'n':
           flag = True
       else:
           flag = False 
        
       
            
 elif (direction == 'D') or (direction == 'd' ):
       print("Here is the messages decoded: ")
       decrypt(text,shift)
       choice = input("Would you like to continue? y/n").lower()
       if choice == 'n':
           flag = True
       else:
           flag = False       

 else:
     print("invalid")

