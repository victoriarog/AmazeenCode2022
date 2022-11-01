import turtle
import random

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(600, 600)

windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth // 2
x_right = windowWidth // 2
y_top = windowHeight // 2
y_bottom = -windowHeight // 2

t.speed(0)  # Set turtle speed to maximum
screen.bgcolor('black')  # set screen background to black

t.hideturtle()  # do not show the turtle itself
t.color('green')

def drawRect(x, y, width, height, color):
    t.up()
    t.goto(x, y)
    t.down()

    t.color(color)

    t.begin_fill()
    t.setheading(0)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.right(90)
    t.forward(width)
    t.right(90)
    t.forward(height)
    t.end_fill()

colours = ['#1abc9c', '#2ecc71', '#3498db', '#9b59b6', '#34495e', '#16a085', '#27ae60', '#2980b9', '#8e44ad', '#2c3e50',
          '#f1c40f', '#e67e22', '#e74c3c', '#ecf0f1', '#95a5a6', '#f39c12', '#d35400', '#c0392b', '#bdc3c7']

numRows = int(input("How many rows of rectangles?"))
numColumns = int(input("How many rectangles in a row?"))

newHeight = 600 / numRows
newWidth = 600 /numColumns 

for j in range(0, numRows):
    for i in range(0, numColumns):
        drawRect(x_left + i*newWidth, y_top - j*newHeight, newWidth, newHeight, colours[random.randint(0,len(colours)-1)])

turtle.mainloop() 

