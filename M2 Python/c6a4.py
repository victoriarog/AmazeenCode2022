import turtle

t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()
screen.setup(600,600)

windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth/2
x_right = windowWidth/2
y_top = windowHeight/2
y_bottom = -windowHeight/2

def square():
    for i in range(4):
        t.forward(75)
        t.left(90)
    t.forward(75)


for i in range(8):
    t.up()
    t.setpos(x_left, y_bottom + 75*i)
    t.down()

    t.fillcolor()
    t.fillcolor("black")
    square()
    t.end_fill()

