import turtle

colors = ["white"]

p = turtle.Pen()
turtle.bgcolor("black")

for i in range(256):
    p.pencolor(colors[i%1])
    p.width(i/100+2)
    p.forward(i)
    p.left(64)