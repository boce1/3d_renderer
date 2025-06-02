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


#p1 = Point(0, 10, 30, RED)
#p2 = Point(10, 30, 0, GREEN)
#p3 = Point(10, 10, 30, BLUE)

#center = Point(0,0,0, BLACK)
#
#p1 = Point(0, 10, 0, RED)
#p2 = Point(10, 0, 0, GREEN)
p3 = Point(20, 0, 0, RED)
#
#t1 = Triangle(p1, p2, p3)
#

c1 = Cube(p3, 10, 10, 10)
c2 = Cube(Point(-20, 15, -5, GREEN), 10,10,10)
c3 = Cube(Point(-20, -20, 15, BLUE), 20, 10, 5)

angle = pi / 180

#t2 = Triangle(Point(), Point(), Point())

def draw(win):
    win.fill(WHITE)
    # center.draw(win)
    # p1.draw(win)
    # p2.draw(win)
    #t1.draw(win, True)
    c1.draw(win)
    c2.draw(win)
    c3.draw(win)
    pg.display.update()

run = True
clock = pg.time.Clock()
while run:
    clock.tick(FPS)
    draw(window)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    #rotate_x(t1, angle)
    #rotate_y(t1, angle)
    #rotate_z(t1, angle)

    rotate_x(c1, angle, True)
    rotate_y(c1, angle, True)
    rotate_z(c1, angle, True)

    rotate_x(c2, angle, True)
    rotate_y(c2, angle, False)
    rotate_z(c2, angle, True)

    rotate_x(c3, angle, False)
    rotate_y(c3, angle, False)
    rotate_z(c3, angle, False)
    #angle += 0.1
pg.quit()
