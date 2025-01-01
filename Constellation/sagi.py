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

        # Twisty thingy
        self.__draw(my_pen, 180, 200, 5, "white", False)
        self.__draw(my_pen, 160, 170, 3, "white", True)
        self.__draw(my_pen, 180, 150, 3.5, "white", True)

        # Main body
        self.__draw(my_pen, 80, 140, 8, "white", True)
        self.__draw(my_pen, 60, 115, 4, "white", True)
        self.__draw(my_pen, 80, 45, 4, "white", True)
        self.__draw(my_pen, -50, 20, 4, "white", True)

        # Back leg/extention of main body
        self.__draw(my_pen, -70, -50, 4, "white", True)

        # Front leg
        self.__draw(my_pen, 80, 45, 4, "white", False)
        self.__draw(my_pen, 180, -10, 3, "white", True)

        # Is that a tail?
        self.__draw(my_pen, -50, 20, 4, "white", False)
        self.__draw(my_pen, -120, 35, 5, "white", True)
        self.__draw(my_pen, -170, 20, 3, "white", True)

        # Dangling limb/half decapitated head
        self.__draw(my_pen, 80, 140, 8, "white", False)
        self.__draw(my_pen, 70, 185, 3, "white", True)
        self.__draw(my_pen, 30, 160, 3, "white", True)

    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()