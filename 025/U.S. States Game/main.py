import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = r"100 Days of Code\Day 25\U.S. States Game\blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

data = pandas.read_csv("100 Days of Code/Day 25/U.S. States Game/50_states.csv")
all_states = data["state"].to_list()
correct_guesses = []


while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        # missing_states = []
        # for state in missing_states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        missing_states = [state for state in all_states if state not in correct_guesses]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("100 Days of Code/Day 25/U.S. States Game/missing_states.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)
        state_data = data[data.state == answer_state]
        pen.goto(x=int(state_data.x), y=int(state_data.y))
        pen.write(answer_state)


def get_mouse_click_coor(x, y):
    print(x, y)
turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()