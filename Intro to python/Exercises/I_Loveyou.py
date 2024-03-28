import turtle
import time
turtle.shape("turtle")
turtle.color("red")

# Set starting position
turtle.penup()
turtle.goto(0, -100)
turtle.pendown()
turtle.pensize(5)

# Heart shape
turtle.begin_fill()
turtle.left(140)
turtle.forward(224)
turtle.circle(-112, 200)
turtle.setheading(60)
turtle.circle(-112, 200)
turtle.forward(224)
turtle.end_fill()

# I love you below heart
turtle.penup()
turtle.goto(-120, -180)
turtle.pendown()
turtle.write("I love you!", font=("Times New Roman", 36, "normal"))

# Sets turtle Background
t = turtle.Turtle()
colors = ["purple", "maroon", "magenta", "light slate blue",  "violet", "black"]

for color in colors:
    t.screen.bgcolor(color)
    time.sleep(1)

turtle.done()