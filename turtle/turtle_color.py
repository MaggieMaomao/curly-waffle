import turtle

class Solution:
  def colorTest(self):

    # turtle.bgcolor("blue")

    # t = turtle.Turtle()
    # t.circle(60)

    import turtle
    my_window = turtle.Screen ()
    my_window.bgcolor("darkseagreen1")
    my_pen = turtle.Turtle()
    my_pen.pencolor("blue")
    my_pen.forward(200)
    my_pen.left(90)
    my_pen.forward(350)
    my_pen.color("lavender")
    my_pen.pensize(12)

    turtle.done
    turtle.Screen().exitonclick()
  



if __name__ == '__main__':
  solution = Solution()
  solution.colorTest()
