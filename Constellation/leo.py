import turtle

class Solution:
    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("fastest")
        my_pen.color("white")

    # Coordinates
        self.__draw(my_pen, -200, 0, 3, "white", False)

        self.__draw(my_pen, -130, 100, 3, "white", True)

        self.__draw(my_pen, 200, 250, 3, "white", True)

        self.__draw(my_pen, 150, 270, 3, "white", True)

        self.__draw(my_pen, 270, 400, 3, "white", True)

        self.__draw(my_pen, 300, 390, 3, "white", True)

        self.__draw(my_pen, 200, 250, 3, "white", True)

        self.__draw(my_pen, 300, 230, 3, "white", True)

        self.__draw(my_pen, 320, 190, 3, "white", True)

        self.__draw(my_pen, -100, 70, 3, "white", True)

        self.__draw(my_pen, -200, 0, 3, "white", True)


    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.moveTo(pen, x, y, color, line)
        self.drawCircle(pen, x, y, radius, color)
    def moveTo(self, pen, x, y, color, track) -> None:
      if track:
          pen.down()
      else:
          pen.up()
      pen.color(color)
      pen.goto(x, y)

    def drawCircle(self, pen, x, y, radius, color) -> None:
        pen.up()
        pen.goto(x, y)
        pen.down()
        pen.fillcolor("white")
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.up()
        pen.goto(x, y)
        pen.down()


if __name__ == '__main__':
  solution = Solution()
  solution.draw()

  turtle.done
  turtle.Screen().exitonclick()
