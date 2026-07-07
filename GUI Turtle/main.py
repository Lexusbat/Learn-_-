from turtle import Turtle, Screen, colormode
import random
la_turtle = Turtle()
colormode(255)


for i in range(10):
 la_turtle.forward(10)
 la_turtle.penup()
 la_turtle.forward(10)
 la_turtle.pendown()
 la_turtle.forward(10)
la

def move(degree,increase):
  for i in range(increase):
    la_turtle.left(degree)
    la_turtle.forward(100)

def random_color():
 r = random.randint(0,255)
 g = random.randint(0,255)
 b = random.randint(0,255)
 random_colour = (r,g,b)

 return random_colour

colours = ["red","OrangeRed","gold1","chartreuse1","DodgerBlue","purple3","VioletRed3","black"]

la_turtle.left(90)
la_turtle.penup()
la_turtle.forward(200)
la_turtle.pendown()
la_turtle.left(90)

full = 360
count_corners = 3
next = 0

for shapes in range(9):
    degree = full / count_corners
    la_turtle.pencolor(colours[next])
    move(degree,count_corners)
    count_corners += 1
    next += 1


flag = False
left = ".left(90)"
right = ".left(180)"
la_turtle.pensize(5) 
la_turtle.speed(0)


while flag == False:
  """ colour = random.choice(colours)
  la_turtle.pencolor(colour)"""
  random_colour = random_color()
  la_turtle.pencolor(random_colour)
  move = random.randrange(1, 5)  # 1, 2, 3, or 4
  if move == 1:
   la_turtle.left(90)
   la_turtle.forward(20)
  elif move == 2:
   la_turtle.left(180)
   la_turtle.forward(20)  
  elif move == 3:
   la_turtle.left(270)
   la_turtle.forward(20)  
  elif move == 4:
   la_turtle.left(360)
   la_turtle.forward(20)  
  



my_screen = Screen()
my_screen.exitonclick()

