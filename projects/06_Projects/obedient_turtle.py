"""
Make an obedient turtle that will obey commands to draw shapes.
"""

import turtle
from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import simpledialog, messagebox



# TODO)
#   1. Create a turtle.
t = turtle.Turtle()
#   2. Write 3 function definitions for drawing a square, triangle, and
#      circle.
def square():
    for i in range(4):
        t.forward(45)
        t.left(90)
def triangle():
    for i in range(3):
        t.left(60)
        t.forward(50)
def circle():
    t.circle(50)
#   3. Ask the user for the for a shape to draw.
shape = simpledialog.askstring(title="Shape", prompt="Choose either square, triangle, or circle")
if shape == "square":
    square()
elif shape == "triangle":
    triangle()
elif shape == "circle":
    circle()
else:
    messagebox.showinfo(title="Invalid Input", message="Invalid Input")
    
#   4. Draw the appropriate shape depending on their answer (call the right
#      function)
turtle.exitonclick()
