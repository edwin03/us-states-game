import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

correct_states = []

while True:
    states = data.state # Or do all_states = data.state.to_list()
    answer_state = screen.textinput(f"{len(correct_states)}/{len(states.values)} States Correct", "What's another state's name?").title()

    if answer_state in states.values:
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        x_cor = data[data.state == answer_state].x.item()
        y_cor = data[data.state == answer_state].y.item()
        state.goto(x_cor, y_cor)
        state.write(answer_state, font=("Arial", 12, "normal"))
        correct_states.append(answer_state)