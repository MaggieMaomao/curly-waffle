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

        self.__draw(my_pen, -90, 200, 5, "white", False)
        self.__draw(my_pen, -150, 140, 3, "white", True)
        self.__draw(my_pen, -145, 70, 3, "white", True)

        self.__draw(my_pen, -40, 10, 3, "white", True)
        self.__draw(my_pen, 40, -40, 3, "white", True)
        self.__draw(my_pen, 100, -100, 3, "white", True)
        self.__draw(my_pen, 70, -170, 3, "white", True)

        self.__draw(my_pen, -90, 200, 5, "white", False)
        self.__draw(my_pen, 0, 160, 3, "white", True)
        self.__draw(my_pen, 120, 50, 3, "white", True)
        self.__draw(my_pen, 190, 10, 2, "white", True)
        self.__draw(my_pen, 230, 20, 3, "white", True)

    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()
    
    
   