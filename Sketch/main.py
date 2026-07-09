from turtle import Turtle, Screen

sam = Turtle()
screen = Screen()

def move_forward():
    sam.forward(10)

def clockwise_turn():
   new_heading = sam.heading() - 10
   sam.setheading(new_heading)

def anti_clockwise_turn():
   new_heading = sam.heading() + 10
   sam.setheading(new_heading)

def move_backwards():
    sam.backward(10)

def clear():
    sam.clear()
    sam.penup()
    sam.home()
    sam.pendown()

screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="d",fun=clockwise_turn)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=anti_clockwise_turn)
screen.onkey(key="c",fun=clear)

screen.exitonclick()