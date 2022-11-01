import turtle

t = turtle.Turtle()
t.speed(1)
t.color('red', 'green')

for i in range(1, 200):
    t.forward(10)
    t.right(10+i)


turtle.mainloop()