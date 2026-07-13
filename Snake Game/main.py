from turtle import Turtle, Screen
import time
from snake import Snake


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

"""Creates Snake - __init__"""
snake = Snake()

is_game_on = True

#TODO Snake, Food, Scoreboard Classes
while is_game_on:
 screen.update()
 time.sleep(0.05)      
 snake.move() 


 #screen.onkey(key="d",fun=clockwise_turn)
 #screen.onkey(key="a",fun=anti_clockwise_turn)







screen.exitonclick()