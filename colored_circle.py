import turtle
 
ninja = turtle.Turtle()

ninja.speed(576)

for i in range(180):
    turtle.bgcolor("black")
    ninja.color("green")
    ninja.forward(100)
    ninja.right(30)
    ninja.color("yellow")
    ninja.forward(20)
    ninja.left(60)
    ninja.color("blue")
    ninja.forward(50)
    ninja.color("white")
    ninja.right(30)

    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()

    ninja.right(2)

turtle.done()
