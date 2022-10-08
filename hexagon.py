import turtle

colors = ["Red", "orange", "yellow", "green", "blue", "indigo", "violet"]

p = turtle.Pen()
turtle.bgcolor("black")

for i in range(300):
    p.pencolor(colors[i%7])
    p.width(i/100+2)
    p.forward(i)
    p.left(59)