import turtle

class Solution:
  def main(self, constellation: str) -> bool:
    print(constellation)
    screen = turtle.getscreen()
    t = turtle.Turtle()
    t.speed("fastest")
    turtle.done()
    turtle.exitonclick()

if __name__ == '__main__':
  solution = Solution()
  solution.main('constellation')
