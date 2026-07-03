MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },

    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },

    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}



coins = {
    "penny": 0.01,
    "nickel": 0.05,
    "dime": 0.10,
    "quarter": 0.25
}

def process_order(request):
   
   for ingredient in MENU[request]["ingredients"]:
    if MENU[request]["ingredients"][ingredient] <= resources[ingredient]:
        resources[ingredient] = resources[ingredient] -MENU[request]["ingredients"][ingredient] 
    else:
        print(f"Not enough {ingredient}")


   
def check_resources(request):
    for ingredient in MENU[request]["ingredients"]:
        if MENU[request]["ingredients"][ingredient] > resources[ingredient]:

            return False
    return True

def calc_transaction(request):
   change = 0
   money_add = 0
   coins_total = 0
   insufficient = 0 
   while True:
    try:
        quarter = int(input("How many quarters?: "))
        dime = int(input("How many dimes?: "))
        nickel = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        break  # All inputs were valid integers
    except ValueError:
        print("Please enter whole numbers only.")

   for money in coins:
    if money == "quarter": 
       coins_total=  coins_total + (coins[money] * quarter) 
    elif money== "dime": 
       coins_total= coins_total + (coins[money] * dime) 
    elif money== "nickel":
       coins_total= coins_total + (coins[money] * nickel) 
    elif money == "pennies": 
       coins_total= coins_total + (coins[money] * pennies) 

   if coins_total < MENU[request]["cost"]:  
      insufficient += 1
      print("Not enough coins inserted. Please try again")
   elif coins_total >= MENU[request]["cost"]:
      change = round(coins_total - MENU[request]["cost"],2)
      money_add = money_add + MENU[request]["cost"]
      print(f"Here is ${change} in change")
      print(f"Here is your {request}. Enjoy!\n")

       
   return money_add, insufficient


flag = False
money = 0 
while flag == False:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request not in ["e","l","c","report","exit"]:
        print("Invalid input.Try again")
        print("Type in either 'e'/'l'/'c' please: \n")
    elif request == "report":
     print(f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g")
     print(f"Money: ${money}")
    elif request == "e":
       request = "espresso"
       if check_resources(request) == True:
        print("Please insert coins: ")
        money_add, insufficient = calc_transaction(request)       
        money = money + money_add
        if insufficient == 0 :
         process_order(request)
        else:
         print("xxxxxxxxxxxxxxxxxxxxx")
           

    elif request == "l":
       request = "latte"
       if check_resources(request) == True:
        print("Please insert coins: ")
        money_add, insufficient = calc_transaction(request)       
        money = money + money_add
        if insufficient == 0 :
         process_order(request)
        else:
         print("xxxxxxxxxxxxxxxxxxxxx")
           

    elif request == "c":
       request = "cappuccino"
       if check_resources(request) == True:
        print("Please insert coins: ")
        money_add, insufficient = calc_transaction(request)       
        money = money + money_add
        if insufficient == 0 :
         process_order(request)
        else:
         print("xxxxxxxxxxxxxxxxxxxxx")
           

       
    elif request == "exit":
       flag = True

       



































