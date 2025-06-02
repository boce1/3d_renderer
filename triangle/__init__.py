import pygame as pg
from constants import *

class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.points = [self.p1, self.p2, self.p3]
        self.outline_color = BLACK
        self.segments_num = 5

    def draw(self, win, drawPoints):
        self.draw_lines(win)
        cords_list = [(self.p1.projection_x, self.p1.projection_y), 
                      (self.p2.projection_x, self.p2.projection_y), 
                      (self.p3.projection_x, self.p3.projection_y)]
        pg.draw.polygon(win, self.outline_color, cords_list, width=2)
        if drawPoints:
            self.p1.draw(win)
            self.p2.draw(win)
            self.p3.draw(win)

    def draw_lines(self, win):
        self.p1.update_color()
        self.p2.update_color()
        self.p3.update_color()

        # add rasterazation