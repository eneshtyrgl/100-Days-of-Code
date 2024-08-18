import colorgram
import turtle
import random

rgb_colors = []
colors = colorgram.extract('100 Days of Code\Day 18\Damien Hirst Painting\image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

turtle.colormode(255)
pen = turtle.Turtle()
pen.speed('fastest')
pen.penup()
pen.hideturtle()

pen.setheading(225)
pen.forward(300)
pen.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    pen.dot(20, random.choice(rgb_colors))
    pen.forward(50)
    if dot_count % 10 == 0:
        pen.setheading(90)
        pen.forward(50)
        pen.setheading(180)
        pen.forward(500)
        pen.setheading(0)

screen = turtle.Screen()
screen.exitonclick()