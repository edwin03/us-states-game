import turtle, pandas, csv

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_states = []
states2learn = []

states = data.state # Or do all_states = data.state.to_list()

while len(correct_states) < 50:
    answer_state = screen.textinput(f"{len(correct_states)}/{len(states.values)} States Correct", "What's another state's name?").title()

    if answer_state == "Exit":
        break
    if answer_state in states.values:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data.state == answer_state].y.item()
        state.goto(x_cor, y_cor)
        state.write(answer_state, font=("Arial", 12, "normal"))
        correct_states.append(answer_state)

for state in states.values:
    if state not in correct_states:
        states2learn.append(state)

pandas.Series(states2learn).to_csv('states_to_learn.csv', header=False, sep=" ", lineterminator="\n")