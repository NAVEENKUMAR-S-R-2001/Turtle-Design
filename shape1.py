import turtle
colors=['red','yellow','blue','green']
turtle.bgcolor('black')
for x in range(100):
    turtle.pencolor(colors[x%4])
    turtle.forward(x)
    turtle.left(91)
