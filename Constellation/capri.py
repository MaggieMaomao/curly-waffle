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
        my_pen.color("black")

        self.__draw(my_pen, -130, 170, 8, "white", False)

      
        self.__draw(my_pen, 10, 120, 5, "white", True)

     
        self.__draw(my_pen, 160, 100, 7, "white", True)

     
        self.__draw(my_pen, 10, -50, 10, "white", True)

     
        self.__draw(my_pen, -120, 70, 6,  "white", True)

       
        self.__draw(my_pen, -130, 170, 9, "white", True)

    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius, color)

if __name__ == '__main__':
        solution = Solution()
        solution.draw()

        turtle.done()
        turtle.Screen().exitonclick()

        # Do spaces/enter buttons in text matter?
       # what do the "" mean?
