import pygame as pg
from math3d import projection_cords
from constants import *

class Point:
    def __init__(self, x, y, z, color):
        self.x = x
        self.y = y
        self.z = z
        self.color = color
        self.render_color = [x for x in self.color]

        self.projection_x, self.projection_y = projection_cords(self)
        self.projection_cords = (self.projection_x, self.projection_y)

    def draw(self, win):
        pg.draw.circle(win, self.render_color, (self.projection_x , self.projection_y), 7)
        self.update_color()

    def update_cords(self, new_cords):
        self.x = new_cords[0]
        self.y = new_cords[1]
        self.z = new_cords[2]

        self.projection_x, self.projection_y = projection_cords(self)
        self.projection_cords = (self.projection_x, self.projection_y)

    def update_color(self):
        if self.z <= 0:
            coef = 1
        else:
            coef = FOV / (FOV + DARK_COLOR_INTENSITY * self.z)

        for i in range(3):
            self.render_color[i] = int(self.color[i] * coef)


