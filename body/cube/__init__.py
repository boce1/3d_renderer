from triangle import *
from point import *
from constants import *
import pygame as pg

class Cube:
    def __init__(self, bottom_left_point, width, height, depth):
        self.bottom_left_front_point = bottom_left_point
        self.width = width
        self.height = height
        self.depth = depth

        x, y, z, color = self.bottom_left_front_point.x, self.bottom_left_front_point.y, self.bottom_left_front_point.z, self.bottom_left_front_point.color # reffrence cords, for visual purpose
        self.bottom_right_front_point = Point(x + width, y, z, color)
        self.bottom_left_back_point = Point(x, y, z + depth, color)
        self.top_left_front_point = Point(x, y + height, z, color)
        
        self.top_right_front_point = Point(x + width, y + height, z, color)
        self.top_right_back_point = Point(x + width, y + height, z + depth, color)
        self.top_left_back_point = Point(x, y + height, z + depth, color)
        self.bottom_right_back_point = Point(x + width, y, z + depth, color)

        self.points = [ self.bottom_left_front_point,
                        self.bottom_right_front_point,
                        self.top_left_front_point,
                        self.top_right_front_point,

                        self.bottom_left_back_point,
                        self.top_right_back_point,
                        self.top_left_back_point,
                        self.bottom_right_back_point]

    def draw(self, win, draw_countuor=True):
        for p in self.points:
            p.draw(win)
        
        if draw_countuor:
            self.draw_countuor(win)

    def draw_countuor(self, win): 
        # bottom side
        pg.draw.line(win, BLACK, self.bottom_left_front_point.projection_cords, self.bottom_right_front_point.projection_cords)
        pg.draw.line(win, BLACK, self.bottom_left_front_point.projection_cords, self.bottom_left_back_point.projection_cords)
        pg.draw.line(win, BLACK, self.bottom_left_back_point.projection_cords, self.bottom_right_back_point.projection_cords)
        pg.draw.line(win, BLACK, self.bottom_right_front_point.projection_cords, self.bottom_right_back_point.projection_cords)
        
        # top side
        pg.draw.line(win, BLACK, self.top_left_front_point.projection_cords, self.top_right_front_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_left_front_point.projection_cords, self.top_left_back_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_left_back_point.projection_cords, self.top_right_back_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_right_front_point.projection_cords, self.top_right_back_point.projection_cords)

        # sides
        pg.draw.line(win, BLACK, self.top_left_front_point.projection_cords, self.bottom_left_front_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_right_front_point.projection_cords, self.bottom_right_front_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_left_back_point.projection_cords, self.bottom_left_back_point.projection_cords)
        pg.draw.line(win, BLACK, self.top_right_back_point.projection_cords, self.bottom_right_back_point.projection_cords)
        