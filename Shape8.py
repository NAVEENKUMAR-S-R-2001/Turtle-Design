import turtle
colors=['red','yellow','blue','green','orange','pink']
turtle.bgcolor('black')
for x in range(100):
    turtle.pencolor(colors[x%6])
    turtle.forward(x)
    turtle.width(x/100+1)
    turtle.left(61)
