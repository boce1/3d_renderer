from triangle import *
from point import *
from constants import *
from math3d import center_of_mass
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

        self.center = center_of_mass(self.points)
        self.points.append(self.center)

    def draw(self, win, draw_countuor=True):
        self.draw_triangles(win)
        
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
        

    def draw_triangles(self, win):
        t1_front = Triangle(self.bottom_left_front_point, self.bottom_right_front_point, self.top_left_front_point)
        t2_front = Triangle(self.top_left_front_point, self.top_right_front_point, self.bottom_right_front_point)

        t1_top = Triangle(self.top_left_front_point, self.top_right_front_point, self.top_right_back_point)
        t2_top = Triangle(self.top_right_back_point, self.top_left_back_point, self.top_left_front_point)

        t1_left = Triangle(self.bottom_left_front_point, self.bottom_left_back_point, self.top_left_back_point)
        t2_left = Triangle(self.top_left_back_point, self.top_left_front_point, self.bottom_left_front_point)

        t1_right = Triangle(self.bottom_right_front_point, self.bottom_right_back_point, self.top_right_back_point)
        t2_right = Triangle(self.top_right_back_point, self.top_right_front_point, self.bottom_right_front_point)

        t1_bottom = Triangle(self.bottom_left_front_point, self.bottom_right_front_point, self.bottom_left_back_point)
        t2_bottom = Triangle(self.bottom_left_back_point, self.bottom_right_back_point, self.bottom_right_front_point)

        t1_top = Triangle(self.top_left_front_point, self.top_right_front_point, self.top_left_back_point)
        t2_top = Triangle(self.top_left_back_point, self.top_right_back_point, self.top_right_front_point)

        t1_front.draw(win)
        t2_front.draw(win)
        t1_top.draw(win)
        t2_top.draw(win)
        t1_left.draw(win)
        t2_left.draw(win)
        t1_right.draw(win)
        t2_right.draw(win)
        t1_bottom.draw(win)
        t2_bottom.draw(win)
        t1_top.draw(win)
        t2_top.draw(win)

        # TO DO: optimaze rasterization, add threads

