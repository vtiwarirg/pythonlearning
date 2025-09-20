# import os
# import colorgram

# if not os.path.exists(r"D:\pythonlearning\PYthon100\hirst-painting\image.jpg"):
#     print("Error: image.jpg not found in the current directory.")
# else:
#     rgb_colors = []
#     colors = colorgram.extract(
#         r"D:\pythonlearning\PYthon100\hirst-painting\image.jpg", 30
#     )
#     for color in colors:
#         r = color.rgb.r
#         g = color.rgb.g
#         b = color.rgb.b
#         new_color = (r, g, b)
#         rgb_colors.append(new_color)
#     print(rgb_colors)

import turtle as t
import random

t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(205, 218, 239), (151, 162, 174), (180, 155, 138), (117, 100, 91), (94, 103, 113), (107, 95, 99), (174, 154, 159), (36, 43, 58), (91, 113, 106), (221, 203, 191), (180, 190, 208), (112, 127, 149), (134, 158, 153), (57, 46, 51), (148, 119, 113), (60, 45, 41), (212, 201, 207), (218, 190, 158), (53, 61, 81), (93, 146, 135), (151, 114, 120), (150, 128, 98), (203, 184, 188), (82, 55, 51), (45, 56, 53), (98, 141, 147), (77, 56, 61), (180, 195, 200), (207, 185, 179), (216, 229, 227)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
