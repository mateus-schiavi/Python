# Import the functions from the Draw 2-D library
# so that they can be used in this program.
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing

# Define your functions such as
# draw_sky and draw_ground here.
def draw_horizon(canvas):
    draw_line(canvas, 0, 300, 800, 300 )

def draw_road(canvas):
    draw_line(canvas, 0, 0, 400, 300)
    draw_line(canvas, 800, 0, 400, 300)
    draw_rectangle(canvas, 400, 0, 400, 50, width=30)
    draw_rectangle(canvas, 400, 115, 400, 150, width=20)
    draw_rectangle(canvas, 400, 200, 400, 225, width=10)
    draw_rectangle(canvas, 400, 260, 400, 275, width=5)

def draw_mountains(canvas):
    draw_line(canvas, 50, 300, 100, 350)
    draw_line(canvas, 100, 350, 125, 325)
    draw_line(canvas, 125, 325, 175, 375)
    draw_line(canvas, 175, 375, 225, 325)
    draw_line(canvas, 225, 325, 275, 350)
    draw_line(canvas, 275, 350, 325, 325)
    draw_line(canvas, 325, 325, 375, 375)
    draw_line(canvas, 375, 375, 400, 350)
    draw_line(canvas, 400, 350, 450, 400)
    draw_line(canvas, 450, 400, 500, 325)
    draw_line(canvas, 500, 325, 560, 360)
    draw_line(canvas, 560, 360, 615, 325)
    draw_line(canvas, 615, 325, 650, 350)
    draw_line(canvas, 650, 350, 700, 315)
    draw_line(canvas, 700, 315, 750, 365)
    draw_line(canvas, 750, 365, 800, 300)


def draw_sun(canvas):
    draw_arc(canvas, 250, 300, 550, 300, start=-180, extent=-180)
    

def draw_clouds(canvas):
    draw_oval(canvas, 100, 450, 300, 450, width=50, fill="ghostWhite")
    draw_oval(canvas, 550, 400, 750, 450, width=50, fill="ghostWhite")

def draw_grid(canvas, width, height, interval):
# draw vertical lines
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height)
        draw_text(canvas, x, label_y, f'{x}')

# draw horizontal lines
    label_x = 15
    for y  in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y)
        draw_text(canvas, label_x, y, f'{y}')

def main():
    # Width and height of the scene in pixels
    scene_width = 800
    scene_height = 500

    # Call the start_drawing function in the draw2d.py library
    # which will open a window and create a canvas.
    canvas = start_drawing("Scene", scene_width, scene_height)

    # Call your drawing functions such
    # as draw_sky and draw_ground here.
    # draw_grid(canvas, scene_width, scene_height, 50)
    draw_horizon(canvas)
    draw_road(canvas)
    draw_sun(canvas)
    draw_clouds(canvas)
    draw_mountains(canvas)
    
    

    # Call the finish_drawing function
    # in the draw2d.py library.
    finish_drawing(canvas)

# Call the main function so that
# this program will start executing.
main()