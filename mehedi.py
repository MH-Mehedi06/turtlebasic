import turtle
import time

# Set up the screen
screen = turtle.Screen()
screen.title("Mehedi Name Drawing")
screen.bgcolor("white")

# Create and set up the turtle
pen = turtle.Turtle()
pen.speed(3)
pen.color("blue")
pen.pensize(5)
pen.penup()
pen.goto(-150, 0)  # Starting position
pen.pendown()

# Function to draw "Mehedi"
def write_mehedi():
    # Draw M
    pen.setheading(90)
    pen.forward(100)
    pen.setheading(-45)
    pen.forward(50)
    pen.setheading(45)
    pen.forward(50)
    pen.setheading(-90)
    pen.forward(100)
    
    # Move to position for e
    pen.penup()
    pen.forward(-100)
    pen.setheading(0)
    pen.forward(30)
    pen.pendown()
    
    # Draw e
    pen.setheading(0)
    pen.forward(50)
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(180)
    pen.forward(50)
    pen.setheading(-90)
    pen.forward(50)
    pen.setheading(0)
    pen.forward(50)
    
    # Draw h
    pen.penup()
    pen.setheading(90)
    pen.forward(100)
    pen.setheading(180)
    pen.forward(50)
    pen.pendown()
    pen.setheading(-90)
    pen.forward(100)
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(0)
    pen.forward(50)
    pen.setheading(-90)
    pen.forward(50)
    
    # Draw e
    pen.penup()
    pen.setheading(0)
    pen.forward(30)
    pen.pendown()
    pen.setheading(0)
    pen.forward(50)
    pen.setheading(90)
    pen.forward(50)
    pen.setheading(180)
    pen.forward(50)
    pen.setheading(-90)
    pen.forward(50)
    pen.setheading(0)
    pen.forward(50)
    
    # Draw d
    pen.penup()
    pen.setheading(90)
    pen.forward(50)
    pen.pendown()
    pen.circle(-25, 180)
    pen.setheading(90)
    pen.forward(50)
    
    # Draw i
    pen.penup()
    pen.setheading(0)
    pen.forward(30)
    pen.pendown()
    pen.setheading(-90)
    pen.forward(50)
    
    # Draw dot for i
    pen.penup()
    pen.setheading(90)
    pen.forward(70)
    pen.pendown()
    pen.dot(10)

# Call the function to write
write_mehedi()

# Hide the turtle and keep the window open
pen.hideturtle()
screen.mainloop()
