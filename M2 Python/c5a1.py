import turtle

turtle.tracer(0)

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(600,600)


windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth/2
x_right = windowWidth/2
y_top = windowHeight/2
y_bottom = -windowHeight/2

t.speed(0)

screen.bgcolor('black')
screen.tracer(0)

t.hideturtle()
t.color('green')

t.width(5)

def draw_person(x, y):
    t.up()
    t.setpos(x, y)
    t.down()

    t.begin_fill()
    t.circle(20)
    t.end_fill()
    t.goto(x, y - 55)
    t.goto(x + 25, y - 110)
    t.up()
    t.goto(x, y - 55)
    t.down()
    t.goto(x - 25, y - 110)
    t.up()
    t.goto(x, y - 20)
    t.down()
    t.goto(x - 20, y - 50)
    t.up()
    t.goto(x, y - 20)
    t.down()
    t.goto(x + 20, y - 50)

current_x = 0
current_y = 0

x_direction = 0.4
y_direction = 0.5


while True:
    draw_person(current_x, current_y)
    screen.update()
    t.clear()
    
    current_x = current_x + x_direction
    current_y = current_y + y_direction

    if current_x >= x_right or current_x <= x_left: 
        x_direction = -x_direction
    elif current_y >= y_top or current_y <= y_bottom:
        y_direction = -y_direction

turtle.mainloop()