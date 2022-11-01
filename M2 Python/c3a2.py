import turtle
import random

def drawCaterpillar(x, y, edge_length, line_color, t):
    t.up()
    t.setpos(x, y)
    t.down()

    t.color(line_color)
    # t.fillcolor(fill_color)


    # t.begin_fill()
    t.forward(edge_length)
    t.right(270)
    t.forward(edge_length)
    t.right(90)
    t.forward(edge_length)
    t.right(270)
    t.forward(edge_length)
    t.right(90)
    t.forward(edge_length)
    t.right(270)
    t.forward(edge_length)
    t.left(90)
    t.forward(edge_length)
    t.right(270)
    t.forward(edge_length)
    t.left(90)
    t.forward(edge_length)
    t.right(270)
    t.forward(edge_length)
    t.left(90)


    # t.end_fill()
    
def drawRandom(x, y, line_color, t):
    t.up()
    t.setpos(x, y)
    t.down()

    t.color(line_color)

    for i in range(5):
        t.right(144)
        t.forward(100)

def endless(x, y, edge_length, color, t):
    t.up()
    t.setpos(x, y)
    t.down()
    t.color(color)
    angle = 90

    # t.begin_fill()
    for i in range(1,100):
        t.forward(edge_length)
        t.right(angle + 2)
        edge_length =  edge_length + 2

def polygon(t, x, y, n, color, size):
    t.up()
    t.setpos(x, y)
    t.down()
    t.color(color)

    if n > 2:
        angle = 360/n
    for n in range(0, n):
            t.left(angle)
            t.forward(size)



t = turtle.Turtle()
t.speed(0)

screen = turtle.Screen()

windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth/2
x_right = windowWidth/2
y_top = windowHeight/2
y_bottom = -windowHeight/2

edge_len = 50

for i in range(500):
    x = random.randint(x_left, x_right - edge_len)
    y = random.randint(y_bottom, y_top - edge_len)

    fig_num = random.randint(1, 5)

    if fig_num == 1:
        drawCaterpillar(x,y,edge_len,'yellow', t)
    elif fig_num == 2:
        polygon(t, x, y, random.randint(3, 10), 'purple', 30)
    elif fig_num == 3:
        endless(x, y, 5, "orange", t)
    elif fig_num == 4:
        drawRandom(x, y, "red", t)
        
turtle.mainloop()