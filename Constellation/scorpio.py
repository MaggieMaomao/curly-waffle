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

        self.__draw(my_pen, 230, 210, 3, "white", False)
        self.__draw(my_pen, 190, 170, 3, "white", True)
        self.__draw(my_pen, 230, 170, 3, "white", True)
        self.__draw(my_pen, 190, 170, 3, "white", True)
        self.__draw(my_pen, 220, 130, 3, "white", True)
        
        self.__draw(my_pen, 190, 170, 3, "white", True)
        self.__draw(my_pen, 175, 165, 5, "white", True)
        self.__draw(my_pen, 150, 150, 3, "white", True)
        self.__draw(my_pen, 90, 100, 3, "white", True)
        self.__draw(my_pen, 60, 20, 3, "white", True)

        self.__draw(my_pen, 40, 23, 3, "white", True)
        self.__draw(my_pen, 10, 30, 3, "white", True)
        self.__draw(my_pen, 0, 60, 3, "white", True)
        self.__draw(my_pen, 25, 80, 3, "white", True)

def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()
    