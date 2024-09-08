import turtle

class Solution:
  def trianglePrism(self):
    my_window = turtle.Screen()
    my_window.bgcolor("darkolivegreen1")
    my_pen = turtle.Turtle()
    my_pen.left (60)
    my_pen.forward(200)
    my_pen.right(60)
    
if __name__ == '__main__':
  solution = Solution()
  solution.trianglePrism()

  turtle.done
  turtle.Screen().exitonclick() 