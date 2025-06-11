import pygame as pg
from math import pi
from math3d import *
from point import *
from constants import *
from triangle import *
from body import *
from camera import *

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Renderer")

angle1 = pi / 90
angle2 = -pi / 45
angle3 = pi / 60

c1 = Cube(Point(30, 10, 0, RED), 5, 5, 5)
c2 = Cube(Point(-20, -20, 15, GREEN), 7,7,7)
c3 = Cube(Point(0, -10, 5, BLUE), 8, 8, 8)
p1 = Pyramid(Point(0, 30, 5, YELLOW), 15, 8, 8)
rainbow_body(c1, (RED, BLUE, GREEN, YELLOW))
rainbow_body(p1, (RED, YELLOW))

wrapper = Wrapper()
wrapper.add(c1, angle1, False, angle1, True, angle1, True)
wrapper.add(c2, angle1, True, angle1, False, angle3, True)
wrapper.add(c3, angle1, False, angle2, True)
wrapper.add(p1, angle2, True, angle1, True, angle3, True)

camera = Camera()

#t1 = Triangle(Point(-5 , -10, 0, RED), Point(-10, 5, 0, GREEN), Point(10, 5, 0, BLUE))

def draw(win, camera_position):
    win.fill(WHITE)

    wrapper.draw(win, camera_position)

    pg.display.update()

run = True
clock = pg.time.Clock()
while run:
    key_pressed = pg.key.get_pressed()
    camera.move(key_pressed, (c1, c2, c3, p1))

    clock.tick(FPS)
    draw(window, camera.possition)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False 

pg.quit()

