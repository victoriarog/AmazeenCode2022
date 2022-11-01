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
screen.bgcolor('pink')  # set screen background to black

t.hideturtle()  # do not show the turtle itself
t.color('gray')


def drawFigure(x, y):
    t.up()  # pen up - no drawing while moving...
    t.setpos(x, y)  # move to the point (x,y)
    t.down()  # pen down - while moving, the turtle will draw a line

    t.color('gray')
    t.begin_fill()
    t.circle(15)
    t.end_fill()

# two variables for coordinates
current_x = 0
current_y = 0

speed = 0.3

moving_left = False
moving_right = False
moving_up = False
moving_down = False

def onKeyUp():
    global moving_up
    moving_up = True

def onKeyUpRelease():
    global moving_up
    moving_up = False

def onKeyDown():
    global moving_down
    moving_down = True

def onKeyDownRelease():
    global moving_down
    moving_down = False


def onKeyLeft():
    global moving_left
    moving_left = True

def onKeyLeftRelease():
    global moving_left
    moving_left = False


def onKeyRight():
    global moving_right
    moving_right = True

def onKeyRightRelease():
    global moving_right
    moving_right = False

turtle.listen()  # start listening for keyboard events

turtle.onkeypress(onKeyUp, "Up")
turtle.onkeyrelease(onKeyUpRelease, "Up")  # If user has pressed up arrow, call our function onKeyUp

turtle.onkeypress(onKeyDown, "Down") # ....
turtle.onkeyrelease(onKeyDownRelease, "Down")

turtle.onkeypress(onKeyLeft, "Left") 
turtle.onkeyrelease(onKeyLeftRelease, "Left")# ....

turtle.onkeypress(onKeyRight, "Right") # ....
turtle.onkeyrelease(onKeyRightRelease, "Right")

# infinite loop which draws constantly (calls drawFigure again and again)
# actually, that's bad :-)


while True:
    if moving_left:
        current_x = current_x - speed
        if current_x < x_left: 
            current_x = x_left
    elif moving_right:
        current_x = current_x + speed
        if current_x > x_right: 
            current_x = x_right
    elif moving_up:
        current_y = current_y + speed
        if current_y > y_top: 
            current_y = y_top
    elif moving_down:
        current_y = current_y - speed
        if current_y < y_bottom: 
            current_y = y_bottom

    drawFigure(current_x, current_y)
    screen.update()
    t.clear()