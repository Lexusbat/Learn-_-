from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")

def race():
    speed = random.randint(range(0,11))
    sam.speed(speed)
    sam.forward(10)


sam = Turtle()
sam.penup()
sam.goto(x=-200,y=0)



screen.exitonclick()