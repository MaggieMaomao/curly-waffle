import turtle
maggie = turtle.Turtle()
    
maggie.penup()
maggie.right(40)
maggie.backward(500)
maggie.pendown()

r = 30
maggie.circle(r) 

maggie.penup()
maggie.forward(300)
maggie.pendown()

for i in range(10):
  maggie.circle(r + i, 45)

maggie.penup()
maggie.forward(200)
maggie.pendown()
r = 10
n = 10

for i in range(1, n + 1, 1):
  maggie.circle(r * i)

turtle.exitonclick()
