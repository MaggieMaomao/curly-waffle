# File: aquarius.py
from turtle_drawer import TurtleDrawer
import turtle
import tkinter as tk
from tkinter import simpledialog

class Solution:
    """
    A class for drawing a specific pattern using the Turtle graphics library.
    """
    def __init__(self):
        self.drawer = TurtleDrawer()

    def draw_aquarius(self):
        """
        Draws the Aquarius constellation pattern.
        """
        screen = turtle.Screen()
        screen.bgcolor("black")

        # Coordinates and drawing instructions
        coordinates = [
            (-180, 50, 3, "white", False),
            (-89, 101, 3, "white", True),
            (40, 170, 3, "white", True),
            (-180, 50, 3, "white", False),
            (-80, 0, 3, "white", True),
            (-40, 0, 3, "white", True),
            (-180, 50, 3, "white", False),
            (-180, 0, 3, "white", True),
            (-200, 0, 3, "white", True),
            (-205, -20, 3, "white", True),
            (-140, -140, 3, "white", True),
            (-110, -90, 3, "white", True),
            (-70, -87, 3, "white", True),
            (-20, -137, 3, "white", True)
        ]

        # Draw the pattern
        for x, y, radius, color, draw_line in coordinates:
            self.drawer.move_to(x, y, color, draw_line)
            self.drawer.draw_circle(x, y, radius, color)

        # Keep the window open until clicked
        turtle.done()
        turtle.Screen().exitonclick()

class ConstellationApp:
    """
    A GUI application to select and draw constellations.
    """
    def __init__(self):
        self.solution = Solution()
        self.root = tk.Tk()
        self.root.title("Constellation Drawer")

        # Add menu
        menu = tk.Menu(self.root)
        self.root.config(menu=menu)

        constellation_menu = tk.Menu(menu, tearoff=0)
        menu.add_cascade(label="Constellations", menu=constellation_menu)
        constellation_menu.add_command(label="Aquarius", command=self.solution.draw_aquarius)
        constellation_menu.add_separator()
        constellation_menu.add_command(label="Exit", command=self.root.quit)

    def run(self):
        """
        Runs the main application loop.
        """
        self.root.mainloop()

if __name__ == '__main__':
    app = ConstellationApp()
    app.run()
