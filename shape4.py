import turtle as t

t.pensize(2)
t.bgcolor('black')
t.speed(2)
def pat1():
    for i in range(8):
        for colors in ['cyan']:
            t.color(colors)
            t.left(135)
            t.forward(300)



def pat2():
    for i in range(4):
        for colors in ['cyan']:
            t.color(colors)
            t.left(81)
            t.forward(100)
            
            
pat1()
