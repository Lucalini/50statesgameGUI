import turtle
import pandas
import csv
screen = turtle.Screen()

screen.title("U.S. States Game")
image = "blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

states_data = pandas.read_csv("50_states.csv")

states_list = states_data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f" {len(guessed_states)}/50 States Correct Guess the State",
                                    prompt="What's another State's name?").title()
    user_guess_data = states_data[states_data["state"] == answer_state]
    if answer_state == "Exit":
        break
    if answer_state in states_list:
        user_x = int(user_guess_data["x"])
        user_y = int(user_guess_data["y"])

        t = turtle.Turtle()
        t.ht()
        t.penup()
        t.speed("fastest")
        t.goto(user_x,user_y)
        t.write(answer_state, False, 'center', ('Arial', 8, 'normal') )
        guessed_states.append(answer_state)
for state in states_list:
    if state in guessed_states:
        states_list.remove(state)
states_to_know = pandas.DataFrame(states_list)
states_to_know.to_csv("states_to_know")

screen.exitonclick()