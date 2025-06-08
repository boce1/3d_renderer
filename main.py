import pygame as pg
from math import pi, sin
from math3d import *
from point import *
from constants import *
from triangle import *
from body import *

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Renderer")


c1 = Cube(Point(20, 0, 0, RED), 10, 10, 10)
c2 = Cube(Point(-20, 15, -5, GREEN), 10,10,10)
c3 = Cube(Point(-20, -20, 15, BLUE), 20, 10, 5)

angle = pi / 90
camera_vector = (0, 0, -1)


t1 = Triangle(Point(0 ,0, 0, RED), Point(-10, 5, 0, GREEN), Point(10, 5, 0, BLUE))

def draw(win):
    win.fill(WHITE)

    c1.draw(win)
    c2.draw(win)
    #c3.draw(win)

    t1.draw(win)

    pg.display.update()

run = True
clock = pg.time.Clock()
while run:
    clock.tick(FPS)
    draw(window)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False



    rotate_x(t1, angle, False)
    rotate_y(t1, angle, False)
    #rotate_z(t1, angle, True)

    rotate_x(c1, angle, True)
    rotate_y(c1, angle, True)
    rotate_z(c1, angle, True)
#
    rotate_x(c2, angle, True)
    rotate_y(c2, angle, False)
    rotate_z(c2, angle, True)
#
    rotate_x(c3, angle, False)
    rotate_y(c3, angle, False)
    #rotate_z(c3, angle, False)
    
pg.quit()

