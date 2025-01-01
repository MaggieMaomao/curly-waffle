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
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()