from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

def snake():
 xpos = 0.00
 ypos = 0.00
 for  snake in range(3):
  sam = Turtle()
  sam.color("white")
  sam.shape("square")
  sam.setpos(xpos,ypos)
  xpos += 20.00



snake()







screen.exitonclick()