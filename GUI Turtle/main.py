from turtle import Turtle, Screen
import random
la_turtle = Turtle()


"""
for i in range(10):
 la_turtle.forward(10)
 la_turtle.penup()
 la_turtle.forward(10)
 la_turtle.pendown()
 la_turtle.forward(10)

"""
def move(degree,increase):
  for i in range(increase):
    la_turtle.left(degree)
    la_turtle.forward(100)

colours = ["red","OrangeRed","gold1","chartreuse1","DodgerBlue","purple3","VioletRed3","black"]

la_turtle.left(90)
la_turtle.penup()
la_turtle.forward(200)
la_turtle.pendown()
la_turtle.left(90)
"""
full = 360
count_corners = 3
next = 0

for shapes in range(9):
    degree = full / count_corners
    la_turtle.pencolor(colours[next])
    move(degree,count_corners)
    count_corners += 1
    next += 1

"""




my_screen = Screen()
my_screen.exitonclick()