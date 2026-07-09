from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")
colors = ["black","red","blue","purple","yellow","green"] # 6 color turtles
y_pos = [-70,-40,-10,20,50,80]
all_turtles =[]

def Turtle_pos(index,spaces_sam):
    sam = Turtle()
    sam.penup()
    sam.shape("turtle")
    sam.color(colors[index])
    sam.goto(-200,y_pos[index])
    sam.forward(spaces_sam)
    
is_race_on = False

"""
def race():
    spaces_sam  = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)
    sam.speed(1)
    sam.forward(spaces_sam)
    spaces_tim = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)

sam = Turtle()
tim = Turtle()
sam.penup()
sam.goto(x=-200,y=0)
tim.penup()
tim.goto(x=-200,y=-50)
"""



while is_race_on ==  False:
    spaces_sam  = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)
    for index in range(6):
      Turtle_pos(index,spaces_sam)





screen.exitonclick()