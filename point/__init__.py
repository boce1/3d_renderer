import pygame as pg
from math3d import projection_cords

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

        self.projection_x, self.projection_y = projection_cords(self)

    def draw(self, win):
        x, y = projection_cords(self)
        pg.draw.circle(win, (255,255,255), (x , y), 2)

    def update_cords(self, new_cords):
        self.x = new_cords[0]
        self.y = new_cords[1]
        self.z = new_cords[2]

        self.projection_x, self.projection_y = projection_cords(self)
