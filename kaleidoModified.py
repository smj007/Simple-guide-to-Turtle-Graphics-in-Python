import time
import turtle as t
from itertools import cycle

colors = cycle(['blue', 'red', 'orange', 'yellow', 'green', 'white', 'purple'])

def draw_shape(size, angle, shift, shape):
    t.pencolor(next(colors))
    next_shape = ' '
    if shape == 'circle':
        t.circle(size)
        next_shape = 'square'
    elif shape == 'square':
        for i in range(4):
            t.forward(size * 2)
            t.left(90)
        next_shape = 'circle'
    t.right(angle)
    t.forward(shift)
    draw_shape(size + 5, angle + 1, shift + 1, next_shape)

t.bgcolor('black')
t.speed('fastest') #modify to fast for easier interpretation
t.pensize(5)

draw_shape(40, 0, 1, 'circle')

time.sleep(5)
t.hideturtle()
