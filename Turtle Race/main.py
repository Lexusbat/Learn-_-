from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")

def race():
    speed = random.randint(0, 10)   # Returns an integer from 0 to 10 (inclusive)
    sam.speed(speed)
    sam.forward(10)


sam = Turtle()
sam.penup()
sam.goto(x=-200,y=0)
while sam.position() != (250.00, 0.00):
    race()


screen.exitonclick()