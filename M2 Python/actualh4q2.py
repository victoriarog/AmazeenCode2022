import turtle

t = turtle.Turtle()
t.width(3)

screen = turtle.Screen()

windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth/2
x_right = windowWidth/2
y_top = windowHeight/2
y_bottom = -windowHeight/2

f = open("hw4-path.txt", "r") 
text = f.read()
commands = text.splitlines(0)
# print(commands)
# TODO: split the text by line breaks

step = 20 # length of "forward" step
forw = 'F'
leftie = 'L'
rightie = 'R'

for i in commands:
    
    if i == forw:
        t.forward(step)
    elif i == leftie:
        t.left(45)
    elif i == rightie:
        t.right(45)

turtle.mainloop()