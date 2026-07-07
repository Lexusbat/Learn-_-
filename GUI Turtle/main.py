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
flag = False
left = ".left(90)"
right = ".left(180)"
while flag == False:
  move = random.randrange(1, 5)  # 1, 2, 3, or 4
  if move == 1:
   la_turtle.left(90)
   la_turtle.forward()
  elif move == 2:
   la_turtle.left(180)
   la_turtle.forward()  
  elif move == 3:
   la_turtle.left(270)
   la_turtle.forward()  
  elif move == 4:
   la_turtle.left(360)
   la_turtle.forward()  



my_screen = Screen()
my_screen.exitonclick()