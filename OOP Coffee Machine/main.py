from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

flag = False
money = 0 
while flag == False:
    request = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if request not in ["e","l","c","report","exit"]:
        print("Invalid input.Try again")
        print("Type in either 'e'/'l'/'c' please: \n")
    elif request == "report":
     money_machine.report()
     money_machine.money_received()
    elif request == "e":
       request = "espresso"
       check = coffee_maker.is_resource_sufficient(request)
       if check == True:
        print("Please insert coins: ")
        money_machine.make_payment()
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

       
