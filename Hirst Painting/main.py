import colorgram
from turtle import Turtle, Screen, colormode

colormode(255)

# Extract 6 colors from the image
colors = colorgram.extract("Skeleton.jpg", 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_colour = (r,g,b)
    rgb_colors.append(new_colour)
print(rgb_colors)

dot = Turtle()
dot.penup()
dot.left(180)
dot.forward(300)
dot.left(180)
dot.pendown()
dot.shape("circle")
dot.speed(0)
print(dot.position())
next = 0 
next2 = -50
for rows in range(0,12): # 6 rows
    dot.penup()
    dot.goto(-300, next2)
    dot.pendown()
    next2 -= 50

    for dots in range(0,10): # 5 dots
        dot.begin_fill()
        dot.pencolor(rgb_colors[next])
        dot.fillcolor((rgb_colors[next]))  # Integers, not floats
        dot.circle(15)
        dot.end_fill()
        dot.penup()
        dot.forward(60)
        dot.pendown()
        next = (next + 1) % len(rgb_colors)












my_screen = Screen()
my_screen.exitonclick()