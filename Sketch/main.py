from turtle import Turtle, Screen

sam = Turtle()
screen = Screen()

def move_forward():
    sam.forward(10)

screen.listen()
screen.onkey(key="space",fun=move_forward,)
screen.exitonclick()