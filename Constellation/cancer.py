import turtle

class Solution:

    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("slow")
        my_pen.color("yellow")



        self.__draw(my_pen, -130, 170, 4, "turquoise", False)

        self.__draw(my_pen, 70, 110, 5, "turquoise", True)

        self.__draw(my_pen, 130, 70, 6, "turquoise", True)

        self.__draw(my_pen, 130, -35, 8, "yellow", True)

        self.__draw(my_pen, 130, 70, 6, "yellow", True)

        self.__draw(my_pen, 150, 65, 2, "yellow", True)

        self.__draw(my_pen, 290, 30, 7, "yellow", True)

    def __draw(self, pen, x, y, radius, color, leaveTrace) -> None:
        self.moveTo(pen, x, y, color, leaveTrace)
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
        pen.goto(x, y - radius)
        pen.down()
        pen.fillcolor("yellow")
        pen.begin_fill()
        pen.circle(radius)
        pen.end_fill()
        pen.up()
        pen.goto(x, y)
        pen.down()


if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()
