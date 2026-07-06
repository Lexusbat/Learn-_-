print("Hello! Welcome to the Quiz Game!")

class User: #Creation of a Class
    def __init__(self,user_id,username): 
     """Initialise attributes (Method)
     (self) is the actual object that's being initialised"""
     #NOTE: Everytime user = User() is created, the following happens
     print("New user being created...")
     #object.attribute = parameter
     self.id = user_id
     self.username = username
     self.followers =0
     self.following =0

     pass #Close Class Block. Can be done with Functions too.

    def follow(self,user): #Must always have a self param first
     user.followers += 1
     self.following += 1

#Object = Class (created above)
user_1 = User("001","skye")
print(user_1.username)
print(user_1.id)
#Must provide parameter attributes for __init__ Method
user_2 = User("002","Rhode")
user_2.follow(user_1)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
user_3 = User("003","Conner")
"""
Output:
New user being created...
New user being created...
New user being created...
"""