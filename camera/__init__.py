from constants import *
from body import *
import pygame as pg

class Camera:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.z = 0

        self.possition = Point(self.x, self.y, self.z, BLACK)

        self.speed = 3

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

        if key_pressed[pg.K_a]:
            self.x += self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x+self.speed, p.y, p.z))

        if key_pressed[pg.K_d]:
            self.x -= self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x-self.speed, p.y, p.z))

        if key_pressed[pg.K_SPACE]:
            self.y -= self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x, p.y-self.speed, p.z))
        
        if key_pressed[pg.K_LSHIFT]:
            self.y += self.speed
            self.update_possition()

            for b in bodies:
                for p in b.points:
                    p.update_cords((p.x, p.y+self.speed, p.z)) 

    def update_possition(self):
        self.possition = Point(self.x, self.y, self.z, BLACK)
