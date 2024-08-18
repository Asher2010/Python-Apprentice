"""
Write a Python program that asks the user for two numbers. The program should
display the sum of the two numbers.

In this program we will just give you the comments for what you need to do. Look
at the comments and the code snippets in the previous lessons, like
03_My_Ages.py, to figure out how to complete the program.


"""

# Import the required modules
from tkinter import messagebox, simpledialog, Tk # import required modules

window = Tk()     # Create a window object
window.withdraw()
# Create a window object

# Hide the window, hint: use the withdraw method

# Ask the user for the first number   
number1 = simpledialog.askfloat(title="First Number", prompt="Input a number")
number2 = simpledialog.askfloat(title="Second Number", prompt="Input another number")
# Ask the user for the second number

# Display the sum of the two numbers 
number3 = number1+number2
messagebox.showinfo(title="sum", message=number3)
# Keep the window open
5
