from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake_parts = [] #List of all snake part (3)- will be able tc control form this list
start_pos =  [(0,0),(-20,0),(-40,0)] # Start pos Tuple
for  positions in start_pos:
  snake_part = Turtle("square")
  snake_part.color("white")
  snake_part.penup()
  snake_part.goto(positions)
  snake_parts.append(snake_part)


 



is_game_on = True


while is_game_on:
 screen.update()
 for snake in snake_parts:

  snake.forward(20)
  time.sleep(0.05)








screen.exitonclick()