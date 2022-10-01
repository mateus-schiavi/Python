# Example 3

from draw2d import start_drawing, draw_oval, finish_drawing

def main():
    # Call the start_drawing function in the draw2d.py
    # library which will open a window and create a canvas.
    canvas = start_drawing("Repeated Shapes", 600, 375)

    diameter = 15
    space = 5
    interval = diameter + space

    # Draw a row of 20 circles.
    x = 100
    y = 100
    for i in range(20):
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="royalBlue1")
        x += interval

    # Draw a column of 10 circles.
    x = 100
    y = 120
    for i in range(10):
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="indianRed1")
        y += interval

    # Draw a diagonal of 10 circles.
    x = 120
    y = 300
    for i in range(10):
        draw_oval(canvas, x, y, x + diameter, y + diameter,
                fill="mediumPurple1")
        x += interval
        y -= interval

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)


# Call the main function so that
# this program will start executing.
main()