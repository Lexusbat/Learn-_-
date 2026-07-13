from turtle import Turtle, Screen
import time
from snake import Snake

start_pos =  [(0,0),(-20,0),(-40,0)] # Start pos Tuple 0,1,2
snake_parts = [] #List of all snake part (3)- will be able tc control form this list

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

"""Creates Snake - __init__"""
snake = Snake(start_pos,snake_parts)

is_game_on = True

#TODO Snake, Food, Scoreboard Classes
while is_game_on:
 screen.update()
 time.sleep(0.05)      
 snake.move(snake_parts) 


 #screen.onkey(key="d",fun=clockwise_turn)
 #screen.onkey(key="a",fun=anti_clockwise_turn)







screen.exitonclick()