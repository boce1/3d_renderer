import pygame as pg
from math import pi, sin
from math3d import *
from point import *
from constants import *
from triangle import *
from body import *
from camera import *

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Renderer")


c1 = Cube(Point(30, 10, 0, RED), 5, 5, 5)
c2 = Cube(Point(-20, -20, 15, GREEN), 7,7,7)
c3 = Cube(Point(0, -5, 5, BLUE), 8, 8, 8)
p1 = Pyramid(Point(0, 30, 5, YELLOW), 15, 8, 8)

rainbow_body(c1, (RED, BLUE, GREEN, YELLOW))
rainbow_body(p1, (RED, YELLOW))

camera = Camera()

angle1 = pi / 90
angle2 = -pi / 45
angle3 = pi / 60

#t1 = Triangle(Point(-5 , -10, 0, RED), Point(-10, 5, 0, GREEN), Point(10, 5, 0, BLUE))

def draw(win):
    win.fill(WHITE)

    #c1.draw(win)
    #c2.draw(win)
    c3.draw(win)
    #p1.draw(win)
    #t1.draw(win)

    pg.display.update()

run = True
clock = pg.time.Clock()
while run:
    key_pressed = pg.key.get_pressed()
    camera.move(key_pressed, (c1, c2, c3, p1))

    clock.tick(FPS)
    draw(window)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #rotate_x(c1, angle1, False, camera.possition)
    #rotate_y(c1, angle1, True)
    #rotate_z(c1, angle1, True)
#
    #rotate_x(c2, angle1, False, camera.possition)
    #rotate_y(c2, angle2, False)
    #rotate_z(c2, angle3, True)
#
    rotate_x(c3, angle1, False, camera.possition)
    #rotate_y(c3, angle2, True)
#
    #rotate_y(p1, angle2, True)
    #rotate_x(p1, angle1, True)
    #rotate_z(p1, angle3, True)

pg.quit()

