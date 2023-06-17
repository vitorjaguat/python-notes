# from turtle import Turtle, Screen
# # https://docs.python.org/3/library/turtle.html

# timmy = Turtle()

# print(timmy)
# timmy.shape('turtle')
# timmy.color('DarkOrange4')
# timmy.forward(100)
# timmy.color('red', 'yellow')
# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break
# timmy.end_fill()
# timmy.done()

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()
table.add_column('Pokemon Name', ['Pikachu', 'Squirtle', 'Charmander'])
table.add_column('Type', ['Electric', 'Water', 'Fire'])
table.align = 'l'
print(table)