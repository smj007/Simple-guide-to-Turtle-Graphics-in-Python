import time
import turtle as t
from itertools import cycle

colors = cycle(['blue', 'red', 'orange', 'yellow', 'green', 'white', 'purple'])

def draw_circle(size, angle, shift):
    t.pencolor(next(colors))
    t.circle(size)
    t.right(angle)
    t.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

t.bgcolor('black')
t.speed('fastest') #modify to fast for easier interpretation
t.pensize(5)

draw_circle(40, 0, 1)

time.sleep(5)
t.hideturtle()
