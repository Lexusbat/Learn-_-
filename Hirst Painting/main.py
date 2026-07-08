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

for rows in range(0,5): # 6 rows

    for dots in range(0,4): # 5 dots
        dot.pencolor(rgb_colors[dots])
        dot.circle(15)
        dot.fillcolor(rgb_colors[dots])
        dot.penup()
        dot.forward(60)
        dot.pendown()










my_screen = Screen()
my_screen.exitonclick()