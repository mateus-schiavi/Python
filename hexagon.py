import turtle

colors = ["white","beige","yellow","orange","red","pink","purple","blue","green","brown","grey"]

p = turtle.Pen()
turtle.bgcolor("black")

for i in range(300):
    p.pencolor(colors[i%11])
    p.width(i/100+2)
    p.forward(i)
    p.left(75)