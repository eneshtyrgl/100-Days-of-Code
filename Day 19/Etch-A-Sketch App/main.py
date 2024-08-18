from turtle import Turtle, Screen

pen = Turtle()
screen = Screen()
 
def move_forwards():
    pen.forward(10)

def move_backwards():
    pen.backward(10)

def move_right():
    new_heading = pen.heading() - 10
    pen.setheading(new_heading)

def move_left():
    new_heading = pen.heading() + 10
    pen.setheading(new_heading)

def clear():
    pen.clear()
    pen.penup()
    pen.home()
    pen.pendown()

screen.listen()
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(move_right, "d")
screen.onkey(move_left, "a")
screen.onkey(clear, "c")
screen.exitonclick()