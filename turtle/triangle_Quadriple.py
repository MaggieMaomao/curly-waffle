import turtle

class Solution:
  def drawTriangle(self):
    my_window = turtle.Screen()
    my_window.bgcolor("blue4")
    my_pen = turtle.Turtle()
    my_pen.color("yellow2")

    my_pen.forward(200)
    my_pen.right(135)
    my_pen.forward(283)
    my_pen.right(135)
    my_pen.forward(200)
    my_pen.up()
    my_pen.forward(40)
    my_pen.down()
    my_pen.forward(200)
    my_pen.right(135)
    my_pen.forward(283)
    my_pen.right(135)
    my_pen.forward(200)
    my_pen.up()
    my_pen.forward(40)
    my_pen.down()
    my_pen.forward(200)
    my_pen.right(135)
    my_pen.forward(283)
    my_pen.right(135)
    my_pen.forward(200)
    my_pen.up()
    my_pen.forward(40)
    my_pen.down()
    my_pen.forward(200)
    my_pen.right(135)
    my_pen.forward(283)
    my_pen.right(135)
    my_pen.forward(200)


if __name__ == '__main__':
  solution = Solution()
  solution.drawTriangle()

  turtle.done
  turtle.Screen().exitonclick()
