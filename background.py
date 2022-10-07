from draw2d import \
    start_drawing, draw_line, draw_oval, draw_arc, \
    draw_rectangle, draw_polygon, draw_text, finish_drawing


def main():
    scene_width = 800
    scene_height = 500


    canvas = start_drawing("Scene", scene_width, scene_height)

    draw_sky(canvas, scene_width, scene_height)
    draw_ground(canvas, scene_width, scene_height)
    draw_grid(canvas, scene_width, scene_height, 50)
    
    finish_drawing(canvas)


def draw_sky(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, scene_height / 3,
        scene_width, scene_height, width=0, fill="deepskyblue")

    def draw_clouds(canvas, cloud_center_x_offset):
        draw_oval(canvas, cloud_center_x_offset+50, 350, 200+cloud_center_x_offset, 450, width=1, outline="ghostwhite", fill="ghostwhite")
        draw_oval(canvas, cloud_center_x_offset+75, 385, 250+cloud_center_x_offset, 475, width=1, outline="ghostwhite", fill="ghostwhite")
        draw_oval(canvas, cloud_center_x_offset+100, 345, 270+cloud_center_x_offset, 425, width=1, outline="ghostwhite", fill="ghostwhite")
    
    x_start_sky = 100
    for n in range (0, 3 ):
        x_offset_sky = 200*n + x_start_sky
        draw_clouds(canvas, x_offset_sky)
        print('drawing clouds at ', x_offset_sky)

# group of trees
def draw_group_trees(tree_center_x_offset, canvas):
    # TODO adjust the X offsets
    tree_center_x = tree_center_x_offset + 20
    tree_bottom = 100
    tree_height = 200
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x = tree_center_x_offset - 20
    tree_bottom = 70
    tree_height = 220
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

    tree_center_x =  tree_center_x_offset + 25
    tree_bottom = 100
    tree_height = 50
    draw_pine_tree(canvas, tree_center_x,
            tree_bottom, tree_height)

def draw_ground(canvas, scene_width, scene_height):
    draw_rectangle(canvas, 0, 0,
        scene_width, scene_height / 3, width=0, fill="lawngreen")

    x_start_trees = 0
    for n in range(0, 17):
        x_offset = 75 * n + x_start_trees
        draw_group_trees(x_offset, canvas)
        print("Drawing trees at ", x_offset)




def draw_pine_tree(canvas, center_x, bottom, height):
    trunk_width = height / 10
    trunk_height = height / 8
    trunk_left = center_x - trunk_width / 2
    trunk_right = center_x + trunk_width / 2
    trunk_top = bottom + trunk_height

    draw_rectangle(canvas,
            trunk_left, trunk_top, trunk_right, bottom,
            outline="gray20", width=1, fill="tan3")

    skirt_width = height / 2
    skirt_height = height - trunk_height
    skirt_left = center_x - skirt_width / 2
    skirt_right = center_x + skirt_width / 2
    skirt_top = bottom + height

    draw_polygon(canvas, center_x, skirt_top,
            skirt_right, trunk_top,
            skirt_left, trunk_top,
            outline="gray20", width=1, fill="dark green")



def draw_grid(canvas, width, height, interval, color="blue"):
    label_y = 15
    for x in range(interval, width, interval):
        draw_line(canvas, x, 0, x, height, fill=color)
        draw_text(canvas, x, label_y, f"{x}", fill=color)

    label_x = 15
    for y in range(interval, height, interval):
        draw_line(canvas, 0, y, width, y, fill=color)
        draw_text(canvas, label_x, y, f"{y}", fill=color)



main()