import turtle  # Use turtle module

t = turtle.Turtle()  # Create a turtle and save it to variable 't'

t.speed(0)  # set turtle speed to maximum

screen = turtle.Screen()  # Get Screen object from turtle

windowWidth = screen.window_width()  # Get window width
windowHeight = screen.window_height()  # Get window height

x_left = -windowWidth // 2  # Minimal x coordinate
x_right = windowWidth // 2  # Maximal x coordinate
y_bottom = -windowHeight // 2  # Minimal y coordinate
y_top = windowHeight // 2  # Maximal y coordinate

line = 2
# Define function to draw coordinate grid (need to be implemented)
def drawCoordinateGrid():
    t.up()
    t.goto(x_left, 0)
    t.up()
    # t.goto()
    # t.down
    t.down()
    t.goto(x_right, 0)
    # To be continued
    t.up()
    t.goto(0, x_right)
    t.down()
    t.goto(0, x_left)

x_lines = x_left
y_lines = y_bottom

for i in range(0, 15):
    t.up()
    t.goto(x_lines + i*55, 10)
    t.down()
    t.goto(x_lines + i*55, -10)
    
    t.up()
    t.goto(10, y_lines + i*50)
    t.down()
    t.goto(-10, y_lines + i*50)


drawCoordinateGrid() # Call the function

turtle.mainloop()  # Start main loop inside the turtle module - to prevent window from closing automatically