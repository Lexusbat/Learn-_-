print("Hello! Welcome to the Quiz Game!")

class User: #Creation of a Class
    def __init__(self): #Initialise attributes (Method)
     #NOTE: Everytime user = User() is created, the following happens
     print("New user being created...")

     pass #Close Class Block. Can be done with Functions too.

#Object = Class (created above)
user_1 = User()
user_2 = User()
user_3 = User()
"""
Output:
New user being created...
New user being created...
New user being created...
"""