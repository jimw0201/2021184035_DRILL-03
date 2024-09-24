from pico2d import *
import math

open_canvas()

# fill here
grass = load_image("grass.png")
boy = load_image("character.png")

def run_top():
    print('TOP')
    pass
def run_right():
    print('RIGHT')
    pass
def run_bottom():
    print('BOTTOM')
    pass
def run_left():
    print('LEFT')
    pass

def run_rectangle():
    print('RECTANGLE')
    run_top()
    run_right()
    run_bottom()
    run_left()
    pass

def run_circle():
    print('CIRCLE')

    r, cx, cy = 300, 800//2, 600//2

    for d in range(0, 360):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
    
        clear_canvas_now()
        boy.draw_now(x, y)
        delay(0.1)
    pass

while True:
    run_rectangle()
    # run_circle()
    break

close_canvas()
