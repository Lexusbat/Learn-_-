import colorgram
colors = colorgram.extract("Skeleton.jpg", 6)
first_color = colors[0]
rgb = first_color.rgb
hsl = first_color.hsl 
proportion  = first_color.proportion
red = rgb[0]
red = rgb.r
saturation = hsl[1]
saturation = hsl.s

colorgram.Color
sorted(colors, key=lambda c: c.hsl.h)