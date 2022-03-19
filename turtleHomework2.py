import turtle
tao = turtle.Pen() #ดึงความสามารถการใช้ปากกา
tao.shape('turtle') #แปลงร่างเป็นเต่า
tao.speed(100) # ปรับความเร็วเต่าขยับ

def Grass():
    Go(-400,50)
    tao.fillcolor("limegreen")
    tao.begin_fill()
    for i in range(2):
        tao.forward(850)
        tao.right(90)
        tao.forward(400)
        tao.right(90)
    tao.end_fill()
    tao.color('black')

def Sky():
    Go(-400,50)
    tao.fillcolor('DeepSkyBlue')
    tao.begin_fill()
    for i in range(2):
        tao.forward(850)
        tao.left(90)
        tao.forward(400)
        tao.left(90)
    tao.end_fill()
    tao.color('black')

def Go(x,y):
    tao.penup()
    tao.goto(x,y)
    tao.pendown()

def SunCircle():
    Go(10,200)
    colors = ['RED', 'ORANGE', 'YELLOW']
    for i in range(50):
        tao.pencolor(colors[i%3])
        tao.circle(i,45*i)
        tao.circle(i)
    tao.left(180)
    
def Mountain():
    global a,b
    Go(-400,50)
    tao.fillcolor('burlywood3')
    tao.begin_fill()
    for i in range(4):
        if i == 2:
            (a,b) = tao.pos()
        if i%2 == 0:
            tao.left(45)
            tao.forward(300)
            tao.right(45)
        if i%2 == 1:
            tao.right(45)
            tao.forward(300)
            tao.left(45)
    tao.goto(-400,50)
    tao.end_fill()
    tao.color('black')

def tree():
    tao.setheading(270)
    # Tree trunk
    tao.fillcolor("saddlebrown")
    tao.begin_fill()
    for i in range(2):
        tao.forward(40)
        tao.left(90)
        tao.forward(10)
        tao.left(90)
    tao.end_fill()
    tao.color('black')
    # Turn the turtle around
    tao.forward(10)
    tao.left(90)
    tao.forward(5)
    # Leaves on tree
    tao.fillcolor("forestgreen")
    tao.begin_fill()
    tao.circle(25)
    tao.end_fill()
    tao.right(90)
    tao.color('black')

def RiverLine():
    tao.setheading(0)
    tao.right(160)
    tao.circle(100,120)
    tao.right(180)
    tao.circle(50,-120)
    tao.left(190)
    tao.circle(100,120)

def River():
    Go(a-20,b)
    RiverLine()
    tao.pencolor('blue')
    for i in range(38):
        Go(a-20+i,b)
        RiverLine()
    tao.pencolor('black')
    Go(a+20,b)
    RiverLine()

def AllTree():
    Go(-300,20)
    tree()
    Go(-220,-30)
    tree()
    Go(-150,-100)
    tree()
    Go(-250,-200)
    tree()
    Go(240,30)
    tree()
    Go(300,-50)
    tree()
    Go(100,-100)
    tree()
    Go(150,-250)
    tree()

Sky()
Grass()
Mountain()
SunCircle()
River()
AllTree()
Go(-30,-10)





