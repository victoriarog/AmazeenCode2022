import turtle

class Ball:
    def __init__(self, *, initial_x = 0, initial_y = 0, initial_vx = 0.3, initial_vy = 0.3, initial_color = "blue", initial_size =15):
        self.x = initial_x
        self.y = initial_y
        self.vx = initial_vx
        self.vy = initial_vy
        self.color = initial_color
        self.size = initial_size

    def move(self, min_x, max_x, min_y, max_y):
        self.x = self.x + self.vx
        self.y = self.y + self.vy

        if self.x <= min_x or self.x >= max_x:
            self.vx = - self.vx
        if self.y <= min_y or self.y >= max_y:
            self.vy = - self.vy

    def draw(self): #current obj = self
        t.up()
        t.setpos(self.x, self.y) 
        t.down()  

        t.color(self.color)
        t.begin_fill()
        t.circle(self.size)
        t.end_fill()


b = Ball() 
b.color = "gray"
b.size = 10

balls = [Ball(initial_x=10, initial_y=20, initial_color="red"), 
        Ball(initial_vx=0.5, initial_vy=0.3), 
        Ball(initial_size=20, initial_color="green", initial_vx=0.6),
        Ball(initial_size=5, initial_color="purple", initial_vx=0.7, initial_vy=0.6)]

t = turtle.Turtle()

screen = turtle.Screen()
screen.setup(600, 600)

windowWidth = screen.window_width()
windowHeight = screen.window_height()

x_left = -windowWidth // 2
x_right = windowWidth // 2
y_top = windowHeight // 2
y_bottom = -windowHeight // 2

t.speed(0)
turtle.tracer(0)
screen.bgcolor('gray')

t.hideturtle()

speed = 0.5

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

turtle.listen()

turtle.onkeypress(onKeyUp, "Up")
turtle.onkeyrelease(onKeyUpRelease, "Up") 

turtle.onkeypress(onKeyDown, "Down") # ....
turtle.onkeyrelease(onKeyDownRelease, "Down")

turtle.onkeypress(onKeyLeft, "Left") 
turtle.onkeyrelease(onKeyLeftRelease, "Left")# ....

turtle.onkeypress(onKeyRight, "Right") # ....
turtle.onkeyrelease(onKeyRightRelease, "Right")

while True:
    if moving_left:
        b.x = b.x - speed
        if b.x < x_left: 
            b.x = x_left
    elif moving_right:
        b.x = b.x + speed
        if b.x > x_right: 
            b.x = x_right
    elif moving_up:
        b.y = b.y + speed
        if b.y > y_top: 
            b.y = y_top
    elif moving_down:
        b.y = b.y - speed
        if b.y < y_bottom: 
            b.y = y_bottom

    for movingBall in balls:
        movingBall.move(x_left, x_right, y_bottom, y_top)
        movingBall.draw()

    screen.update()
    t.clear()