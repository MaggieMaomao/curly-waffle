import turtle

class Solution:
  def drawTimetable(self):
    my_window = turtle.Screen()
    my_window.bgcolor("blue4")
    my_pen = turtle.Turtle()
    my_pen.color("yellow2")
    
    my_pen.up()
    my_pen.left(90)
    my_pen.forward(300)

    my_pen.left(90)
    my_pen.forward(300)

    my_pen.right(180)
    my_pen.down()

    my_pen.write("Timetable", font=("Arial", 16, "normal"))

    my_pen.forward(500)
    my_pen.backward(500)

#   going to print numbers
    my_pen.up()
    my_pen.right(90)
    my_pen.forward(30)
    my_pen.left(90)
    my_pen.forward(20)
    my_pen.down()

    for i in range(1, 11):
      for j in range(1, 11):
        my_pen.write(i * j, move=False, align='left', font=("Arial", 16, "normal"))
        my_pen.up()
        my_pen.forward(50)
        my_pen.down()

      my_pen.up()
      my_pen.backward(20) 

      my_pen.right(90)
      my_pen.forward(14)
      my_pen.left(90)
      my_pen.down()
      my_pen.backward(500)
      my_pen.forward(20)
      my_pen.right(90)
      my_pen.up()
      my_pen.forward(30)
      my_pen.down()
      my_pen.left(90)

    my_pen.up()
    my_pen.right(180)
    my_pen.forward(20)
    my_pen.right(90)
    my_pen.forward(30)
    my_pen.down()
    my_pen.forward(450)
  # for i in range:
      # my_pen.up()



if __name__ == '__main__':
  solution = Solution()
  solution.drawTimetable()

  turtle.done
  turtle.Screen().exitonclick()