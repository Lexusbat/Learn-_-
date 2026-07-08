import colorgram

# Extract 6 colors from the image
colors = colorgram.extract("Skeleton.jpg", 30)

for color in colors:
    print(color.rgb)