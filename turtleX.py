import turtle as t
import time
import random

def inside_zone():
    left_limit = (-t.window_width()/2) + 100
    right_limit = (t.window_width()/2) - 100
    top_limit = (t.window_height()/2) - 100
    bottom_limit = (-t.window_height()/2) + 100
    (x, y) = t.pos()
    inside = (left_limit < x < right_limit) and (bottom_limit < y < top_limit)
    return inside


def move_turtle():
    if inside_zone():
        angle = random.randint(0, 180)
        shift = random.randint(50, 300)
        t.right(angle)
        t.forward(shift)
    else:
        t.backward(300)

t.shape('turtle')
t.fillcolor('green')
t.bgcolor('black')
t.speed('slow')


while True:
    move_turtle()
