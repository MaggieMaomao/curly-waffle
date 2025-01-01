from turtle_drawer import TurtleDrawer

import turtle

class Solution:

    def __init__(self):
         self.drawer = TurtleDrawer()

    def draw(self) -> None:
        my_window = turtle.Screen()
        my_window.bgcolor("black")
        my_pen = turtle.Turtle()
        my_pen.speed("fastest")
        my_pen.color("black")

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
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()