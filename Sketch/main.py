from turtle import Turtle, Screen

sam = Turtle()
screen = Screen()

def move_forward():
    sam.forward(10)

def clockwise_turn(increase):
    sam.setheading(increase)

def move_backwards():
    sam.backward(10)

screen.listen()
screen.onkey(key="w",fun=move_forward,)

screen.onkey(key="s",fun=move_backwards,)

screen.exitonclick()