import turtle

class Solution:
  def draw(self):
    my_window = turtle.Screen()
    my_window.bgcolor("black")
    my_pen = turtle.Turtle()
    my_pen.speed("fastest")
    my_pen.color("yellow")
    my_pen.hideturtle()
    use_guide = False


    if use_guide:
      self.drawCircle(my_pen,0,0,2,"blue")

      self.drawCircle(my_pen,300,0,2,"blue")
      self.drawCircle(my_pen,0,300,2,"blue")
      self.drawCircle(my_pen,-300,0,2,"blue")
      self.drawCircle(my_pen,0,-300,2,"blue")


    # Draw Leo constellation
    # x, y, radius, color, if connect to previous star
    stars = [
      (-150, 150, 6, "turquoise", 0),
      (50, 50, 3, "turquoise", 1),
      (145, -30, 3, "turquoise", 1),
      (145, -130, 6, "turquoise", 1),

    ]

    for i, (x, y, r, color, isConnected) in enumerate(stars):
      self.drawCircle(my_pen, x, y, r, color)
      my_pen.penup()
      my_pen.goto(x, y)

      if isConnected == 1:
        my_pen.pendown()
        my_pen.goto(stars[i - 1][0], stars[i - 1][1])
      else:
        my_pen.goto(stars[i - 1][0], stars[i - 1][1])
        my_pen.pendown()

  def drawCircle(self, pen, x, y, radius, color):
    pen.up()
    pen.goto(x, y)
    pen.down()

    pen.color(color)
    pen.begin_fill()
    pen.circle(radius)
    pen.end_fill()

  def drawGuide():
    self.drawCircle(my_pen,0,0,2,"blue")
    self.drawCircle(my_pen,100,0,2,"blue")
    self.drawCircle(my_pen,0,100,2,"blue")
    self.drawCircle(my_pen,-100,0,2,"blue")
    self.drawCircle(my_pen,0,-100,2,"blue")

if __name__ == '__main__':
  solution = Solution()
  solution.draw()

  turtle.done
  turtle.Screen().exitonclick()
