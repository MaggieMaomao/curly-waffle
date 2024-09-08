# importing package
import turtle

screen = turtle.getscreen()

# help(screen.tracer)

# The first parameter of tracer is actually only two options: 0 or 1
# 0 means turn off tracer so the screen update will be happened right away, 
#   the whole circle will be drawn on the screen in one screen update
# 1 means turn on tracer so the screen update will depend on the 2nd parameter, which is the delay seconds,
#   the screen will be updated step by step

screen.tracer(1, 25)
dist = 2
for i in range(10):
	turtle.fd(dist)
	turtle.rt(90)
	dist += 2

screen.tracer(2, 25)
for i in range(11, 20):
	turtle.fd(dist)
	turtle.rt(90)
	dist += 2

screen.tracer(1, 25)
for i in range(21, 30):
	turtle.fd(dist)
	turtle.rt(90)
	dist += 2

turtle.exitonclick()