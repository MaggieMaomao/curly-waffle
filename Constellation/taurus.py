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
        my_pen.color("white")

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

    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()



