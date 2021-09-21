import turtle
colors = ['red','blue','green','orange']
t=turtle.pen()
turtle.bgcolor('black')
for x in range(180):
    turtle.pencolor(colors[x%4])
    turtle.width(x/100+1)
    turtle.forward(x)
    turtle.right(75)
    
    
