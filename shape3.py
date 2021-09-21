import turtle

turtle.bgcolor('black')
turtle.pensize(2)
turtle.speed(0)
for i in range(100):
    for colors in ['red','blue']:
        turtle.color(colors)
        turtle.circle(i)
        turtle.forward(i)
        turtle.left(15)






