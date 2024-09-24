from pico2d import *
import math

open_canvas()

# fill here
grass = load_image("grass.png")
boy = load_image("character.png")

def draw(x, y):
    clear_canvas_now()
    boy.draw_now(x, y)
    grass.draw_now(400, 30)
    delay(0.001)

def run_top():
    print('TOP')
        draw(x, 550)
    pass
def run_right():
    print('RIGHT')
    for y in range(550, 90, -10):
        draw(780, y)
    pass
def run_bottom():
    print('BOTTOM')
    for x in range(780, 20, -10):
        draw(x, 90)
    pass
def run_left():
    print('LEFT')
    for y in range(90, 550, 10):
        draw(20, y)
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

    r, cx, cy = 230, (800//2)+20, (600//2)+20

    for d in range(-90, 270):
        x = r * math.cos(math.radians(d)) + cx
        y = r * math.sin(math.radians(d)) + cy
        draw(x, y)
    pass

while True:
    run_rectangle()
    run_circle()
    break

close_canvas()
