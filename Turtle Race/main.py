from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win? Bet on it! Choose a colour: ")

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


screen.exitonclick()