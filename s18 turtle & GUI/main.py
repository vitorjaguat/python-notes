# import heroes 
# python3 -m pip install "Heroes"
# print(heroes.gen())

from turtle import Turtle, Screen
import turtle
import random

timmy = Turtle()
timmy.shape('arrow')
timmy.color('red')
turtle.colormode(255)

# draw a square
# for _ in range(4):
#     timmy.left(90)
#     timmy.forward(100)

# draw a dashed line
# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

# square inside of a pentagon inside if a hexagen etc.:
# colors = ['CornflowerBlue', 'DarkOrchid', 'IndianRed', 'DeepSkyBlue', 'LightSeaGreen', 'wheat', 'SlateGray', 'red', 'blue', 'green', 'yellow', 'pink']

# def make_shape(sides_number):
#     angle = 360 / sides_number
#     for _ in range(sides_number):
#         timmy.forward(50)
#         timmy.right(angle)

# for _ in range(3,14):
#     timmy.color(random.choice(colors))
#     make_shape(_)



# random walk:
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return (r, g, b)


# directions = [0, 90, 180, 270]


# for _ in range(100):
#     # timmy.width(random.randint(1,8))
#     timmy.width(7)
#     timmy.speed('fastest')
#     timmy.color(random_color())
#     timmy.forward(random.randint(5,40))
#     timmy.setheading(random.choice(directions))
    

# spirograph:
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.speed(0)

def spirograph(gap):
    for n in range(int(360 / gap)):
        timmy.color(random_color())
        timmy.circle(80)
        timmy.setheading(timmy.heading() + gap)

spirograph(5)




screen = Screen()
screen.exitonclick()