import turtle as t
import time
def draw_smile(loc):
    if(loc<200):
        t.color('yellow')
        t.penup()
        t.goto(300-loc,0)
        t.dot(30,'red')

    t.seth(0)
    t.goto(0,-100)
    t.begin_fill()
    t.circle(100)
    t.end_fill()

    if(loc<200):
        t.color('black')
        t.goto(87,-51)
        t.pendown()
        t.seth(60)
        t.begin_fill()
        t.circle(100,60)
        t.goto(0,0)
        t.end_fill()

t.tracer(False) 
t.screensize(800,600,'black')
t.color('yellow')
t.speed(1)

for r in range(0,200,10):
    t.tracer(False)
    t.clear()
    draw_smile(r)
    time.sleep(1)
    t.hideturtle()
    t.tracer(True)

t.clear()
t.tracer(0)
draw_smile(0)