"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"

# Change the Turtle Image

Here is an example of how you can change the look of the turtle to an image. 
You can copy the ``set_turtle_image()`` function into your own programs. 

Important:
* The image file must be a GIF. ( The file name ends in `.gif` )
* The image file must be in the `image` directory, and the  `image` directory
  must be in the same directory as your program. 

"""

import turtle


def set_turtle_image(turtle, image_name):
    """Set the turtle's shape to a custom image."""

    from pathlib import Path
    image_dir = Path(__file__).parent / "images"
    image_path = str(image_dir / image_name)

    screen = turtle.getscreen()
    screen.addshape(image_path)
    turtle.shape(image_path)

# Set up the screen
screen = turtle.Screen()
screen.setup(width=600, height=600)

# Create a turtle and set its shape to the custom GIF
t = turtle.Turtle()

set_turtle_image(t, "pikachu.gif")

t.penup()
t.speed(3)

for i in range(4):
    t.goto(200, 200)
    t.goto(-200, -200)


turtle.exitonclick()     

#Then change the code so that the turtle has a different image ( look in the 'images'
#directory ) and moves to the corners of the screen in a square pattern. 

