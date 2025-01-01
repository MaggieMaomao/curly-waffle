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

#Coordinates
        self.__draw(my_pen, 20, 170, 3, "white", False)
        self.__draw(my_pen, -20, 150, 3, "white", True)
        self.__draw(my_pen, -50, 130, 3, "white", True)
        self.__draw(my_pen, -10, 90, 3, "white", True)
       
        self.__draw(my_pen, -10, 60, 3, "white", True)
        self.__draw(my_pen, -60, 0, 3, "white", True)
        self.__draw(my_pen, -120, -40, 3, "white", True)
        self.__draw(my_pen, -160, -80, 3, "white", True)
        
        self.__draw(my_pen, -140, -75, 3, "white", True)
        self.__draw(my_pen, -110, -60, 3, "white", True)
        self.__draw(my_pen, -100, -55, 3, "white", True)
        self.__draw(my_pen, -20, -50, 3, "white", True)
        self.__draw(my_pen, -10, -53, 3, "white", True)
        self.__draw(my_pen, 70, -62, 3, "white", True)

        self.__draw(my_pen, 90, -53, 3, "white", True)
        self.__draw(my_pen, 110, -80, 3, "white", True)
        self.__draw(my_pen, 125, -83, 4, "white", True)
        self.__draw(my_pen, 110, -80, 3, "white", True)
        self.__draw(my_pen, 93, -95, 3, "white", True)
        self.__draw(my_pen, 70, -95, 3, "white", True)
        self.__draw(my_pen, 70, -63, 3, "white", True)

    
    def __draw(self, pen, x, y, radius, color, line) -> None:
        self.drawer.move_to(x, y, color, line)
        self.drawer.draw_circle(x, y, radius)

if __name__ == '__main__':
    solution = Solution()
    solution.draw()

    turtle.done()
    turtle.Screen().exitonclick()



