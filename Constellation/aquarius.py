import turtle

class Solution:

    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("fastest")
        my_pen.color("black")


#coordinates
        self.__draw(my_pen, -180, 50, 3, "white", False)
        self.__draw(my_pen, -89, 101, 3, "white", True)
        self.__draw(my_pen, 40, 170, 3, "white", True)
        self.__draw(my_pen, -180, 50, 3, "white", False)
        self.__draw(my_pen, -80, 0, 3, "white", True)
        self.__draw(my_pen, -40, 0, 3, "white", True)
        self.__draw(my_pen, -180, 50, 3, "white", False)
        self.__draw(my_pen, -180, 0, 3, "white", True)
        self.__draw(my_pen, -200, 0, 3, "white", True)
        self.__draw(my_pen, -205, -20, 3, "white", True)
        self.__draw(my_pen, -140, -140, 3, "white", True)
        self.__draw(my_pen, -110, -90, 3, "white", True)
        self.__draw(my_pen, -70, -87, 3, "white", True)
        self.__draw(my_pen, -20, -137, 3, "white", True)

        

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