from pico2d import *

open_canvas()

# fill here
grass = load_image("grass.png")
boy = load_image("character.png")

def run_rectangle():
    print('RECTANGLE')
    pass

def run_circle():
    print('CIRCLE')
    pass

while True:
    run_rectangle()
    run_circle()

close_canvas()
