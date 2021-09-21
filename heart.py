import turtle as t
t.bgcolor("black")
pen=t.Turtle()
pen.pencolor('red')

def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)
    curve()
    pen.forward(112)
    pen.end_fill()

def text():
    pen.up()
    pen.setpos(-68,95)
    pen.down()
    pen.color('black')
    pen.write('I LOVE PYTHON',font=('Verdana',13,'bold'))

heart()
text()
pen.ht()
