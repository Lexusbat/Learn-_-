from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

snake_parts = []

def snake():
 xpos = 0.00
 ypos = 0.00
 for  snake in range(3):
  snake_part = Turtle()
  snake_part.color("white")
  snake_part.shape("square")
  snake_parts.append(snake_part)
  snake_part.setpos(xpos,ypos)
  xpos += 20.00




snake()







screen.exitonclick()