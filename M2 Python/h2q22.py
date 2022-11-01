import turtle

def showSquare(x, y, edge_length, fill_color,line_color, t):
    t.up()
    t.setpos(x, y)
    t.down()

    t.color(line_color)
    t.fillcolor(fill_color)


    t.begin_fill()
    t.forward(edge_length)
    t.right(90)
    t.forward(edge_length)
    t.right(90)
    t.forward(edge_length)
    t.right(90)
    t.forward(edge_length)
    t.right(90)
    t.end_fill()

t = turtle.Turtle()
t.speed(3) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest

showSquare(218, 295, 40, 'green','red' , t)

showSquare(-258, 295, 40, 'green','red', t)

showSquare(-20, 20, 40, 'green','red', t)

showSquare(218, -255, 40, 'green','red' , t)

showSquare(-258, -255, 40, 'green','red', t)