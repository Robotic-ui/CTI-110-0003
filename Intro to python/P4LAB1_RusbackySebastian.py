import turtle

window = turtle.Screen()
turtle.bgcolor("orange")

# draw square
squareTurtle = turtle.Turtle()

for square_line in range(4):
    squareTurtle.forward(100)
    squareTurtle.left(90)

triangleTurtle = turtle.Turtle()

# draw   triangle
for triangle_line in range(3):
    triangleTurtle.forward(100)
    triangleTurtle.left(120)

turtle.done()