import turtle

# Set up the screen with a background
screen = turtle.Screen()
screen.bgcolor("lightblue")  # Set the background color to light blue
screen.title("Stick Figure Drawing with Green Grass")  # Set the title of the window

# Set up the turtle
pen = turtle.Turtle()
pen.speed(3)  # Set drawing speed
pen.pensize(3)  # Thicker lines

# Function to move the turtle without drawing
def move(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

# Draw the ground (green grass)
pen.color("green")  # Set pen color to green for the grass
pen.begin_fill()
move(-200, -200)  # Move to the bottom-left corner of the screen
pen.setheading(0)  # Point the turtle to the right
pen.forward(400)  # Draw the bottom edge of the rectangle
pen.setheading(90)  # Point the turtle upward
pen.forward(50)  # Draw the right edge
pen.setheading(180)  # Point the turtle to the left
pen.forward(400)  # Draw the top edge
pen.setheading(270)  # Point the turtle downward
pen.forward(50)  # Draw the left edge and close the rectangle
pen.end_fill()

# Reset pen color to black for the stick figure
pen.color("black")

# Draw the head
move(0, 100)  # Correct position for the head, centered above the body
pen.circle(30)  # Draw a circle with radius 30

# Draw the body
move(0, 100)  # Start from the bottom of the head
pen.setheading(270)  # Point the turtle downward
pen.forward(100)  # Draw a line for the body

# Draw the arms
move(0, 50)  # Move to the middle of the body
angles = [225, 315]  # Angles for left and right arms
for angle in angles:
    pen.setheading(angle)  # Set the turtle's direction
    pen.forward(50)  # Draw the arm
    pen.backward(50)  # Move back to the middle of the body

# Draw the legs
move(0, 0)  # Move to the bottom of the body
angles = [225, 315]  # Angles for left and right legs
for angle in angles:
    pen.setheading(angle)  # Set the turtle's direction
    pen.forward(50)  # Draw the leg
    pen.backward(50)  # Move back to the bottom of the body

# Hide the turtle and display the drawing
pen.hideturtle()
turtle.done()
