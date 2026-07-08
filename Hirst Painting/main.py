import colorgram

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
