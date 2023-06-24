import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f'{len(guessed_states)}/50 States Correct', prompt="What's another state's name?").title()

    if answer_state == 'Exit':
        break

    if answer_state in all_states:
        if answer_state not in guessed_states:
            guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        state_name = state_data.state.item()
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_name, font=('Arial', 12, 'normal'))

failed_states = []
for state in all_states:
    if state not in guessed_states:
        failed_states.append(state)
failed_dataframe = pandas.DataFrame(failed_states)
failed_dataframe.to_csv('failed_states.csv')

    # if len(data[data['state'] == answer_state]):
    #     state_row = data[data['state'] == answer_state]
    #     state_name = data[data['state'] == answer_state].state.to_string()
    #     state_x = data[data['state'] == answer_state].x.to_numpy
    #     state_y = data[data['state'] == answer_state].y.to_numpy
    #     print(state_x, state_y)
    #     new_write = turtle.Turtle()
    #     # new_write.hideturtle()
    #     # new_write.goto()
    #     new_write.write(state_name, font=('Arial', 12, 'normal'))






# turtle.mainloop()
# screen.exitonclick()