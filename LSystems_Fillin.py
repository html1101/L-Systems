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
