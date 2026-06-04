import math

logo = ''''''

Flag = False
bidders = {}



while Flag == False:
    print("\n" * 100)
    name = input("PLease enter your name:\n")
    amount = int(input("Enter amount you'd like to bid.\n R"))
    choice = input("Is there some one else who'd like to bid too? y/n").lower()
    

    bidders[name] = amount
    
    if choice == 'n':
        Flag = True

max = 0
for bid in bidders:
    if bidders[bid] > max:
        max = bidders[bid] 
        bid_name = bid


print(f"The highest bidder was {bid_name} with : R {max}")
