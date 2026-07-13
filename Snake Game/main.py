from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake_parts = [] #List of all snake part (3)- will be able tc control form this list
start_pos =  [(0,0),(-20,0),(-40,0)] # Start pos Tuple 0,1,2
for  positions in start_pos:
  snake_part = Turtle("square")
  snake_part.color("white")
  snake_part.penup()
  snake_part.goto(positions)
  snake_parts.append(snake_part)


 



is_game_on = True


while is_game_on:
 screen.update()
 time.sleep(0.05)
 for snake_num in range(start= 2,stop= 0, step= -1 ): # start= 1,stop= 3 , step= 1 BUT Check above tuple (backwards)
  new_x = snake_parts[snake_num - 1].xcor()
  new_y = snake_parts[snake_num - 1].xcor()
  snake_parts[snake_num].goto(new_x, new_y)










screen.exitonclick()