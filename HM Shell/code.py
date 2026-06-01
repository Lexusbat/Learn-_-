import random


stage1 = '''

      _______
     |/      |
     |      
     |      
     |       
     |      
     |
    _|___

'''
stage2= '''

      _______
     |/      |
     |      ( )
     |      
     |       
     |      
     |
    _|___

'''
stage3= '''

      _______
     |/      |
     |      (_)
     |       
     |       
     |      
     |
    _|___

'''
stage4 = '''

      _______
     |/      |
     |      (_)
     |       |
     |       
     |      
     |
    _|___

'''
stage5= '''

      _______
     |/      |
     |      (_)
     |       |
     |       |
     |      
     |
    _|___

'''
stage6= '''

      _______
     |/      |
     |      (_)
     |      \|
     |       |
     |      
     |
    _|___

'''
stage7= '''

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      
     |
    _|___

'''
stage8= '''

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / 
     |
    _|___

'''
stage9 = '''

      _______
     |/      |
     |      (_)
     |      \|/
     |       |
     |      / \\
     |
    _|___


'''
hang = '''

██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝
'''
stage_list = [
    stage1,
    stage2,
    stage3,
    stage4,
    stage5,
    stage6,
    stage7,
    stage8,
    stage9
]

alph_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_list = [
    "apple",
    "aardvark",
    "strawberry",
    "banana",
    "orange",
    "computer",
    "keyboard",
    "python",
    "elephant",
    "mountain",
    "diamond",
    "library",
    "football",
    "chocolate",
    "umbrella",
    "garden",
    "window",
    "bottle",
    "pencil",
    "school",
    "teacher",
    "student",
    "picture",
    "camera",
    "guitar",
    "piano",
    "violin",
    "airport",
    "planet",
    "rocket",
    "galaxy",
    "island",
    "desert",
    "forest",
    "jungle",
    "river",
    "ocean",
    "castle",
    "dragon",
    "pirate",
    "treasure",
    "monkey",
    "giraffe",
    "zebra",
    "kangaroo",
    "penguin",
    "dolphin",
    "turtle",
    "rabbit",
    "hamster",
    "butterfly",
    "spider",
    "flower",
    "sunshine",
    "rainbow",
    "thunder",
    "lightning",
    "weather",
    "winter",
    "summer",
    "autumn",
    "spring",
    "holiday",
    "birthday",
    "kitchen",
    "bedroom",
    "bathroom",
    "garage",
    "mirror",
    "blanket",
    "pillow",
    "candle",
    "basket",
    "wallet",
    "jacket",
    "trousers",
    "sweater",
    "sandals",
    "necklace",
    "bracelet",
    "diamond",
    "silver",
    "golden",
    "market",
    "doctor",
    "nurse",
    "hospital",
    "medicine",
    "bicycle",
    "scooter",
    "airplane",
    "traffic",
    "station",
    "engine",
    "bridge",
    "tunnel",
    "village",
    "country",
    "capital",
    "museum",
    "theater",
    "stadium",
    "restaurant",
    "sandwich",
    "popcorn",
    "pancake",
    "cupcake",
    "cookie",
    "cheese",
    "carrot",
    "potato",
    "pumpkin",
    "lettuce",
    "pepper",
    "onion",
    "garlic",
    "chicken",
    "sausage",
    "noodle",
    "butter",
    "honey",
    "coffee",
    "lemonade",
    "coconut",
    "avocado",
    "peach",
    "cherry",
    "grapes",
    "melon",
    "papaya",
    "mango",
    "apricot",
    "walnut",
    "almond",
    "cereal",
    "planet",
    "comet",
    "meteor",
    "satellite",
    "astronaut",
    "telescope",
    "volcano",
    "earthquake",
    "waterfall",
    "cliff",
    "valley",
    "meadow",
    "harbor",
    "compass",
    "lantern",
    "backpack",
    "notebook",
    "calendar",
    "envelope",
    "message",
    "printer",
    "monitor",
    "speaker",
    "charger",
    "battery",
    "button",
    "pocket",
    "ladder",
    "hammer",
    "shovel",
    "blanket"
]
string_list = []
string = ""
chosen_word = random.choice(word_list)
print(chosen_word)
for underscore in range(0,len(chosen_word)):
    string_list.append("_")

for underrscore in string_list:
    string += "_"
print(string)

stage_count = 0
def add(user_letter):
    global stage_count
    count = 0
    flag = False
    if user_letter not in alph_list:
     print("That is not a valid letter.")
     user_letter = input("Type a letter to guess word: ").lower()
    else: 
     for char in chosen_word: 
        count += 1
        if user_letter == char:
             flag = True
             string_list[count-1] = user_letter   
     
     if flag == False:
         print("Incorrect try again")
         stage_count += 1
       
            
    return  print(stage_list[stage_count])

print(hang)

while string != chosen_word:
 user_letter = input("Type a letter to guess word: ").lower()
 add(user_letter)
         
 #print(string_list) 
 string =""
 for char in string_list:
  string += char


 print(string)
 if stage_count == 8:
    print("+++++++++You Lost+++++++++")
 if (stage_count < 9) and (string == chosen_word):
    print("+++++++++You won++++++++++")

 
 
        