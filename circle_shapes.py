import turtle as t

t.bgcolor('black')
t.pensize(3)
t.speed(0)

for i in range(5):
    for colors in ['red','magenta','blue','cyan','green','yellow','white']:
        t.color(colors)
        t.circle(100)
        t.left(10)

t.hideturtle()
