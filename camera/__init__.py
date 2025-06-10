from constants import *
from body import *
import pygame as pg

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.possition = Point(self.x, self.y, self.z, BLACK)

        self.speed = 1

    def move(self, key_pressed, bodies):
        if key_pressed[pg.K_w]:
            self.z -= self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x, p.y, p.z-self.speed))

        if key_pressed[pg.K_s]:
            self.z += self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x, p.y, p.z+self.speed))

    def update_possition(self):
        self.possition = Point(self.x, self.y, self.z, BLACK)
