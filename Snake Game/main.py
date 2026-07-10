from turtle import Turtle, Screen, Time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("My Snake Game")

snake_parts = [(0.00,0.00),(-20.00,0.00),(-40.00,0.00)]

def snake_body():
 for  positions in snake_parts:
  snake_part = Turtle()
  snake_part.penup()
  snake_part.color("white")
  snake_part.shape("square")
  snake_part.goto(positions)

 

snake_body()

is_game_on = True


while is_game_on == True:
 screen.update()
 time.sleep(-1)

 for snake in snake_parts:







screen.exitonclick()