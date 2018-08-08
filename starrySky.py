import turtle as t
#from itertools import cycle
from random import randint, random

#size = 300
#points = 5
#bgdcolor = cycle(['red','light blue', 'orange', 'green', 'yellow', 'purple'])



def draw_star(points, size, col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    angle = 180 - (180 / points)
    t.color(col)
    t.begin_fill()
    for i in range(points):
        t.forward(size)
        t.right(angle)
    t.end_fill()

def draw_planet(col, x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(col)
    t.begin_fill()
    t.circle(40)
    t.end_fill()

t.Screen().bgcolor('dark blue')
draw_planet('red', 0, 10)

while True:
    ranPts = randint(2, 5) * 2 + 1
    ranSize = randint(10, 50)
    ranColor = (random(), random(), random())
    ranX = randint(-350, 300)
    ranY = randint(-250, 250)

    draw_star(ranPts, ranSize, ranColor, ranX, ranY)


#draw_star(5, 50, 'yellow', 0, 0)




