import turtle
s=turtle.Screen().bgcolor("black")
t=turtle.Turtle()
t.speed(0)
t.width(12)
def curve():
    for i in range(200):
        t.right(1)
        t.forward(1)

def heart():
    t.color("red","red")
    t.begin_fill()
    t.left(140)
    t.forward(113)
    curve()
    t.left(120)
    curve()
    t.forward(112)
    t.end_fill()
heart()
t.penup()
t.goto(-260,-20)
t.pencolor("red")
t.write("I",align="left",font=("courier",150,"bold","italic"))
t.goto(100,-20)
t.write("You",align="left",font=("courier",150,"bold","italic"))
