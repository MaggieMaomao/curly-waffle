import turtle

class Solution:

    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("fastest")
        my_pen.color("black")

        self.__draw(my_pen, 20, 200, 3, "white", False)

        self.__draw(my_pen, 25, 130, 3, "white", True)
        self.__draw(my_pen, 50, 40, 3, "white", True)
        self.__draw(my_pen, -70, -10, 3, "white", True)
        self.__draw(my_pen, -120, -70, 5, "white", True)
        self.__draw(my_pen, -140, 60, 3, "white", True)
        self.__draw(my_pen, 25, 130, 3, "white", True)

        self.__draw(my_pen, 50, 40, 3, "white", True)
        self.__draw(my_pen, 120, 50, 3, "white", True)
        self.__draw(my_pen, 190, 80, 3, "white", True)
        self.__draw(my_pen, 210, 130, 3, "white", True)

        self.__draw(my_pen, -120, -70, 5, "white", False)
        self.__draw(my_pen, -220, -70, 3, "white", True)
        
        self.__draw(my_pen, -140, 60, 3, "white", False)
        self.__draw(my_pen, -200, 80, 3, "white", True)
        self.__draw(my_pen, -280, 80, 3, "white")

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
    