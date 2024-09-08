import turtle

#test file.
class Solution:
  def draw(self):
    my_window = turtle.Screen()
    my_window.bgcolor("DimGray")
    my_pen = turtle.Turtle()
    my_pen.speed("fastest")
    #define a few colors
    color1 = "DeepPink1"
    color2 = "Yellow"
    color3 = "blue"
    my_pen.up()
    #pick a starting point
    my_pen.goto(-60,-90)
    my_pen.down()

    #draw a little spirograph donut
    #do this sixty times to make a fun pattern
    for i in range(100):
      my_pen.color(color1)
      my_pen.right(10)
      my_pen.forward(90)
      my_pen.color(color2)
      my_pen.right(10)
      my_pen.forward(65)
      my_pen.color(color3)
      my_pen.left(73)
      my_pen.forward(75)

    my_pen.hideturtle()

if __name__ == '__main__':
  solution = Solution()
  solution.draw()

  turtle.done
  turtle.Screen().exitonclick()
