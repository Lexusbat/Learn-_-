from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

def snake():
 xpos = 0
 ypos = 0
 for  snake in range(3):
  sam = Turtle()
  sam.shape("square")
  sam.pos(xpos,ypos)
  xpos += 20



snake()







screen.exitonclick()