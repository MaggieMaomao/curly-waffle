import turtle

class TurtleDrawer:
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.speed("fastest")

    def move_to(self, x, y, color="black", draw_line=False):
        if draw_line:
            self.pen.down()
        else:
            self.pen.up()

        self.pen.color(color)
        self.pen.goto(x, y)

    def draw_circle(self, x, y, radius, color="white"):
        self.pen.up()
        self.pen.goto(x, y - radius)
        self.pen.down()
        self.pen.fillcolor(color)
        self.pen.begin_fill()
        self.pen.circle(radius)
        self.pen.end_fill()
        self.pen.up()
        self.pen.goto(x, y)
        self.pen.down()
