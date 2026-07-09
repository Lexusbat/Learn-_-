from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")
colors = ["black","red","blue","purple","yellow","green"] # 6 color turtles
y_pos = [-70,-40,-10,20,50,80]



def Turtle_pos(index):
    sam = Turtle()
    sam.penup()
    sam.shape("turtle")
    sam.color(colors[index])
    sam.goto(-200,y_pos[index])

"""

def race():
    spaces_sam  = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)
    sam.speed(1)
    sam.forward(spaces_sam)
    spaces_tim = random.randint(5, 20)   # Returns an integer from 0 to 10 (inclusive)
    tim.speed(1)
    tim.forward(spaces_tim)


sam = Turtle()
tim = Turtle()
sam.penup()
sam.goto(x=-200,y=0)
tim.penup()
tim.goto(x=-200,y=-50)
while (sam.position() != (250.00, 0.00)) and (tim.position() != (250.00, -50.00)) :
    race()

"""
for index in range(6):
    Turtle_pos(index)



screen.exitonclick()