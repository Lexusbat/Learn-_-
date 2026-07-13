from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake_parts = [(0,0),(-20,0),(-40,0)]


for  positions in snake_parts:
  snake_part = Turtle()
  snake_part.penup()
  snake_part.color("white")
  snake_part.shape("square")
  snake_part.goto(positions)

 



is_game_on = True


while is_game_on:
 screen.update()
 #time.sleep(-1)

 for snake in snake_parts:
  snake.forward(20)







screen.exitonclick()