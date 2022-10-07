import random
import math
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
        scene_width = 1280
        scene_height = 720

        canvas = start_drawing("Scene", scene_width, scene_height)
        draw_sky(canvas, scene_width, scene_height)
        draw_sun(canvas, 125, 250)
        draw_bird(canvas, 250, 125)
        draw_ground(canvas, scene_width,scene_height)
        for a in range(2500):
            x = random.randint(0, scene_width)
            y = random.randint(0, math.ceil(scene_height / 2))
            draw_grass(canvas, x, y)
            draw_pine_tree(canvas, 100, 150, 200)
            draw_pine_tree(canvas, 125, 150, 175)
            draw_pine_tree(canvas, 150, 150, 150)
            draw_pine_tree(canvas, 130, 150, 170)
            draw_pine_tree(canvas, 90, 120, 90)
            draw_pine_tree(canvas, 115, 115, 115) 
        finish_drawing(canvas)
        
    
def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 4,
        scene_width, scene_height, width=0, fill="gray")

def draw_sun(canvas, x, y):
    draw_oval(canvas, x, y, x+150, y+150, outline="green", fill="yellow")

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="green")
    
def draw_grass(canvas, x, y):
    draw_rectangle(canvas,x,y,x+2,y+3, outline="green", fill="darkblue")

def draw_pine_tree(canvas, center_x, buttom, height):
    # Draw the trunk of the tree
    trunk_width = height / 4
    trunk_height = height / 16
    left_trunk = center_x - trunk_width / 12
    buttom_trunk = buttom
    right_trunk = center_x + trunk_width / 8
    trunk_top = buttom + trunk_height
    draw_rectangle(canvas, left_trunk, buttom_trunk, right_trunk, trunk_top, fill = 'tan4')
    
    # Draw the skirt of the tree
    skirt_width = height / 2
    skirt_left = center_x - skirt_width / 4
    skirt_buttom = trunk_top
    peak_x = center_x
    peak_y = buttom + height
    skirt_right = center_x + skirt_width / 8
    draw_polygon(canvas, skirt_left, skirt_buttom, peak_x, peak_y, skirt_right, skirt_buttom, fill = 'forestGreen')

def draw_cloud(canvas, x, y):
    draw_oval(canvas, x, y, x+100, y+50, outline="white", fill="white")
    
def draw_grid(canvas, width, height, interval, color= 'blue'):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)


# Calling the main function
main()
