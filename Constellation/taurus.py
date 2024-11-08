import turtle

class Solution:
    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("fastest")
        my_pen.color("black")

#coordinates
        self.__draw(my_pen, -269, 120, 5, "white", False)
        self.__draw(my_pen, -90, 30, 2, "white", True)
        self.__draw(my_pen, -55, 20, 2, "white", True)
        self.__draw(my_pen, 20, -40, 5, "white", True)
        self.__draw(my_pen, -40, -100, 3, "white", True)
        self.__draw(my_pen, 0, -140, 3, "white", True)
        self.__draw(my_pen, -200, 190, 5, "white", False)
        self.__draw(my_pen, -90, 100, 5, "white", True)
        self.__draw(my_pen, -60, 40, 2, "white", True)
        self.__draw(my_pen, -55, 20, 2, "white", True)
        self.__draw(my_pen, 20, -40, 5, "white", True)
        self.__draw(my_pen, 140, -30, 3, "white", True)
        self.__draw(my_pen, 150, -70, 3, "white", True)
        self.__draw(my_pen, 190, -110, 3, "white", True)
        #self.__draw(my_pen, -200, 160, 8, "white", False)


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
        pen.goto(x, y- radius)
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




