import turtle, pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"

screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")

while True:
    answer_state = screen.textinput("Guess the State", "What's another state's name?").title()

    states = data.state

    if answer_state in states.values:
        print("It does exsist")
        state = turtle.Turtle()
        state.penup()
        x_cor = data[data.state == answer_state].x
        y_cor = data[data.state == answer_state].y
        print(f"{x_cor} {y_cor}")
        # state.goto(x_cor, y_cor)
        # state.write(answer_state, font=("Arial", 16, "normal"))
    else:
        print("Does not exsist")

turtle.mainloop()