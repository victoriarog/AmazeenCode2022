import turtle

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
turtle.tracer(0)  # disable automatic drawing - the picture will be shown only after a call to screen.update()
screen.bgcolor('black')  # set screen background to black

t.hideturtle()  # do not show the turtle itself
t.color('green')


def drawFigure(x, y):
    t.up()  # pen up - no drawing while moving...
    t.setpos(x, y)  # move to the point (x,y)
    t.down()  # pen down - while moving, the turtle will draw a line

    t.color('green')
    # draw filled circle
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# two variables for coordinates
current_x = 0
current_y = 0

speed = 10

def onKeyUp():
    global current_y # global variable current_y can be accessed and changed inside the function
    current_y = current_y + speed
    if current_y > y_top: 
        current_y = y_top - 30

def onKeyDown():
    global current_y # global variable current_y can be accessed and changed inside the function
    current_y = current_y - speed
    if current_y < y_bottom: 
        current_y = y_bottom + 20


def onKeyLeft():
    global current_x # global variable current_x can be accessed and changed inside the function
    current_x = current_x - speed
    if current_x < x_left: 
        current_x = x_left + 20


def onKeyRight():
    global current_x # global variable current_x can be accessed and changed inside the function
    current_x = current_x + speed
    if current_x > x_right: 
        current_x = x_right - 20

turtle.listen()  # start listening for keyboard events

turtle.onkey(onKeyUp, "Up")  # If user has pressed up arrow, call our function onKeyUp
turtle.onkey(onKeyDown, "Down") # ....
turtle.onkey(onKeyLeft, "Left") # ....
turtle.onkey(onKeyRight, "Right") # ....

# infinite loop which draws constantly (calls drawFigure again and again)
# actually, that's bad :-)

while True:
    drawFigure(current_x, current_y)
    screen.update()
    t.clear()