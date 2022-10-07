import random
import math
from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
        scene_width = 1280
        scene_height = 720

canvas = star("Scene", scene_width, scene_height)

draw_sky(canvas, scene_width, scene_height)
draw_sun()   
               
