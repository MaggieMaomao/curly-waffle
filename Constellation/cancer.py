from turtle_drawer import TurtleDrawer

import turtle

class Solution:

    def __init__(self):
         self.drawer = TurtleDrawer()

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

    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()

