import turtle
turtle.Screen().bgcolor("yellow")
turtle.Screen().setup(500,500)

polygon = turtle.Turtle()
sides = 6
angles = 360/sides
length = 70

for i in range(sides):
    polygon.forward(length)
    polygon.right(angles)

turtle.done()