import turtle

def drawRandom(x, y, line_color, t):
    t.up()
    t.setpos(x, y)
    t.down()

    t.color(line_color)

    for i in range(5):
        t.right(144)
        t.forward(100)


t = turtle.Turtle()
t.speed(5) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

drawRandom(0, 0, 'purple', t)
drawRandom(100, 100, 'purple', t)
drawRandom(200, -100, 'purple', t)
drawRandom(-200, 100, 'purple', t)
drawRandom(-100, -200, 'purple', t)
drawRandom(300, 200, 'purple', t)


# screen.window_height + width for the square hw 
