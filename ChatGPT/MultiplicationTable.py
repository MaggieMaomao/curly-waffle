import turtle

def draw_table(t, x, y, size, rows, columns):
    for i in range(rows + 1):
        t.penup()
        t.goto(x, y - i * size)
        t.pendown()
        t.goto(x + columns * size, y - i * size)
        
    for j in range(columns + 1):
        t.penup()
        t.goto(x + j * size, y)
        t.pendown()
        t.goto(x + j * size, y - rows * size)
        
    for i in range(rows):
        for j in range(columns):
            t.penup()
            t.goto(x + j * size, y - i * size)
            t.pendown()
            t.write(str((i + 1) * (j + 1)), align="center", font=("Arial", 12, "normal"))

def main():
    t = turtle.Turtle()
    t.speed("fastest")
    t.penup()
    draw_table(t, -100, 100, 50, 10, 10)
    turtle.done()

if __name__ == "__main__":
    main()
