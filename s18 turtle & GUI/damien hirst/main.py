# python3 -m pip install colorgram.py
import colorgram as c
import turtle as t
import random
# import os

# print(os.getcwd())

t.colormode(255)
tim = t.Turtle()
tim.hideturtle()

print(t.screensize()) 
# 400 x 300


colors = c.extract('./s18 turtle & GUI/damien hirst/painting.jpg', 30)

colors_rgb = []
for color in colors:
    # append only the values of the named tuples, not the key:
    colors_rgb.append(color.rgb[:])
print(colors_rgb)

colors_rgb = [(249, 232, 19), (199, 12, 31), (195, 67, 21), (213, 13, 9), (32, 91, 188), (234, 151, 39), (232, 229, 5), (48, 219, 59), (35, 33, 154), (14, 205, 222), (18, 27, 60), (244, 42, 159), (71, 8, 51), (55, 24, 11), (228, 165, 9), (61, 200, 232), (16, 153, 16), (226, 19, 118), (98, 75, 9), (244, 44, 17), (66, 241, 159), (223, 140, 207), (248, 11, 9), (10, 97, 61), (5, 38, 33), (65, 221, 153)]

tim.penup()
tim.setposition(-240, 240)

for y in range(10):
    for n in range(10):
        tim.dot(20, random.choice(colors_rgb))
        tim.forward(50)
    tim.left(180)
    tim.forward(500)
    tim.left(90)
    tim.forward(50)
    tim.left(90)

screen = t.Screen()
screen.exitonclick()