import turtle

class Solution:

    def draw(self) -> None:
    my_window = turtle.Screen()
    my_window.bgcolor("black")
    my_pen = turtle.Turtle()
    my_pen.speed("slow")
    my_pen.color("black")

    #print("Capricorn")


#cordinates
        self.__draw(my_pen, -130, 170, 8, "white", False)

        #print("step 1")
        self.__draw(my_pen, 10, 120, 5, "white", True)

       #print("step 2")
        self.__draw(my_pen, 160, 100, 7, "white", True)

        #print("step 3")
        self.__draw(my_pen, 10, -50, 10, "white", True)

       #print("step 4")
        self.__draw(my_pen, -120, 70, 6,  "white", True)

        #print("step 5")
        self.__draw(my_pen, -130, 170, 9, "white", True)

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
        turtle.Screen().exitonclick()

        # Do spaces/enter buttons in text matter?
       # what do the "" mean?
