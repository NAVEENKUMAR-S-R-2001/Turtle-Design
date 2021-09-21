import turtle
colors = ['red','blue','green']
t=turtle.pen()
turtle.bgcolor('black')
for x in range(180):
    turtle.pencolor(colors[x%3])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.left(120)
