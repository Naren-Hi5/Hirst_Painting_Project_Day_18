'''
                                              Hirst Painting Project

                  colorgram.py is a Python Library that lets you extract colors from images.
                  Compared to other libraries, the colorgram algorithm's results are more intense.

first_color = colors[0]
rgb = first_color.rgb

print(rgb)

red = rgb[0]
red = rgb.r

print(red)

len_of_colors = len(colors)

color_tuple = ()
color_list = []

for color in range(0, len_of_colors):
    colour = colors[color]
    RGB = colour.rgb
    red = RGB[0]
    red = RGB.r
    green = RGB[1]
    green = RGB.g
    blue = RGB[2]
    blue = RGB.b
    color_list.e


print(color_list)


[(244, 243, 240), (3, 2, 1), (241, 212, 2), (252, 248, 251), (245, 252, 247), (249, 249, 253), (240, 213, 47), (211, 9, 4), (218, 6, 14), (176, 155, 146), (146, 68, 62), (195, 40, 50), (4, 4, 10), (222, 54, 65), (1, 12, 3), (20, 5, 13), (213, 78, 70), (248, 165, 154), (214, 128, 134), (253, 144, 152), (202, 184, 40), (246, 11, 23), (82, 81, 87), (175, 180, 174), (65, 64, 62), (158, 156, 167), (191, 193, 190)]
'''
''' 
import colorgram

# TODO 1: Extracts RGB Values From Images
colors = colorgram.extract('hirst_image.jpg', 30)
print(colors)

rgb_color_list = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_color_list.append(new_color)

print(rgb_color_list)

'''
import turtle as turtle_module
import random


turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(0)
tim.penup()
tim.hideturtle()

colors_list = [(3, 2, 1), (241, 212, 2), (240, 213, 47), (211, 9, 4), (218, 6, 14), (176, 155, 146), (146, 68, 62),
               (195, 40, 50), (4, 4, 10), (222, 54, 65), (1, 12, 3), (20, 5, 13), (213, 78, 70), (248, 165, 154),
               (214, 128, 134), (253, 144, 152), (202, 184, 40), (246, 11, 23), (82, 81, 87), (175, 180, 174),
               (65, 64, 62), (158, 156, 167), (191, 193, 190)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(colors_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
