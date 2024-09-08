
import turtle

class Solution:
  def jackInABox(self):
    my_window = turtle.Screen()
    my_window.bgcolor("skyblue1")
    my_pen = turtle.Turtle()
    my_pen.forward(150)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.left(90)
    my_pen.forward(150)
    my_pen.up()
    my_pen.forward(50)
    my_pen.down()
    my_pen.left(90)
    my_pen.pencolor("blue")
    for i in range(4):
      my_pen.forward(150)
      my_pen.left(90)
    my_pen.right(90)
    my_pen.up()
    my_pen.forward(50)
    my_pen.down()
    my_pen.left(90)
    my_pen.pencolor("red")
    for i in range(4):
     my_pen.forward(150)
     my_pen.left(90) 
if __name__ == '__main__':
  solution = Solution()
  solution.jackInABox()

  turtle.done
  turtle.Screen().exitonclick()