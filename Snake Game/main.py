from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_parts = [(0.00,0.00),(-20.00,0.00),(-40.00,0.00)]

def snake_body():
 xpos = 0.00
 ypos = 0.00
 for  snake in range(3):
  snake_part = Turtle()
  snake_part.penup()
  snake_part.color("white")
  snake_part.shape("square")
  snake_parts.append(snake_part)
  snake_part.setpos(xpos,ypos)
  xpos += 20.00
 

snake_body()

is_game_on = True


while is_game_on == True:

 for snake in snake_parts:
  snake.forward(10)
  snake.left(90)
  snake.penup()

 






screen.exitonclick()