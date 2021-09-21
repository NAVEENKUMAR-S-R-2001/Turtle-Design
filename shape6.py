import turtle as tr
sc=tr.Screen()
sc.setup(600,600)
spiral=tr.Turtle()
spiral.speed(10)
sc.bgcolor('black')
cl=['yellow','blue','white','green','orange']
c=0
for i in range(70):
    spiral.forward(i*10)
    spiral.right(144)
    spiral.color(cl[c])
    if c==4:
        c=0
    else:
        c+=1
