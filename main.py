import pygame as pg
from math import pi, sin
from math3d import *
from point import *
from constants import *
from triangle import *

pg.init()

window = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Renderer")


p1 = Point(0, 10, 20)
p2 = Point(10, 0, 0)

center = Point(0,0,0)

t1 = Triangle(p1, p2, center)
angle = pi / 180

#t2 = Triangle(Point(), Point(), Point())

def draw(win):
    win.fill((0,0,0))
    # center.draw(win)
    # p1.draw(win)
    # p2.draw(win)
    t1.draw(win, True)

    pg.display.update()

run = True
clock = pg.time.Clock()
while run:
    clock.tick(FPS)
    draw(window)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False

    rotate_x(t1, angle)
    rotate_y(t1, angle)
    rotate_z(t1, angle)

    #angle += 0.1
pg.quit()
