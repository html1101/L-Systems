# Import Turtle
from turtle import *

# Establish variables
axiom = "F++F++F"
angle = 60
length = 5
iterations = 4
rules = {
    "F": "F-F++F-F"
}

# Set speed of turtle
speed(0)

stack = []
# Create function to draw out the final string we're given.
def parseString(string):
    # 1) Go through each letter of the string we're given
    for i in string:
        # 2) Check if those letters match the letters the parser understands.
        if i == "F":
            pendown()
            forward(length)
        elif i == "f":
            penup()
            forward(length)
        elif i == "-":
            right(angle)
        elif i == "+":
            left(angle)
        elif i == "[":
            stack = [heading(), pos()]
        elif i == "]":
            home()
            goto(*stack[1])
            left(stack[0])

# Start replacing values in axiom
final_str = axiom
for i in range(iterations):
    for rule in rules:
        if rule in final_str:
            # Replace rule in final_str
            final_str = final_str.replace(rule, rules[rule])

parseString(final_str)
done()