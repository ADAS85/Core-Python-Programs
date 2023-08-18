"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
turtle.Screen().bgcolor("violet")
"""
for c in ['red', 'green', 'blue', 'yellow']:
    t.color(c)
    t.forward(75)
    t.left(90)
"""
t.speed(2)
t.pendown()
t.pencolor("white")

num_sides = int(input("Enter no. of sides: "))
side_length = 100
angle = 360.0/num_sides

for i in range(num_sides):
  t.forward(side_length)
  t.right(angle)

#turtle.done()



