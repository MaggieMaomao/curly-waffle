import turtle

class Solution:

    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("slow")
        my_pen.color("black")


#coordinates
        self.__draw(my_pen, -130, 170, 8, "white", False)
        self.__draw(my_pen, -90, 270, 8, "white", True)
        self.__draw(my_pen, 5, 140, 7, "white", True)
        self.__draw(my_pen, -20, -15, 2, "white", True)
        self.__draw(my_pen, 5, 140, 7, "white", False)
        self.__draw(my_pen, -130, 170, 8, "white", True)
        self.__draw(my_pen, -130, -50, 3, "white", True)
        self.__draw(my_pen, -140, -60, 4, "white", True)
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
        pen.goto(x, y - radius)
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

    turtle.done()
    turtle.Screen().exitonclick()

