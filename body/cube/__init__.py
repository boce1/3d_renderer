from triangle import *
from point import *
from constants import *
from math3d import *
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

    def draw(self, win):
        self.draw_triangles(win)

    def draw_triangles(self, win):
        t1_front = Triangle(self.top_left_front_point, self.bottom_right_front_point, self.bottom_left_front_point) # front
        t2_front = Triangle(self.top_left_front_point, self.top_right_front_point, self.bottom_right_front_point)

        t1_top = Triangle(self.top_left_front_point, self.top_right_back_point, self.top_right_front_point) # top
        t2_top = Triangle(self.top_left_front_point, self.top_left_back_point, self.top_right_back_point) 

        t1_left = Triangle(self.top_left_back_point, self.bottom_left_front_point, self.bottom_left_back_point) # left
        t2_left = Triangle(self.top_left_back_point, self.top_left_front_point, self.bottom_left_front_point)

        t1_right = Triangle(self.bottom_right_front_point, self.top_right_back_point, self.bottom_right_back_point) # right
        t2_right = Triangle(self.bottom_right_front_point, self.top_right_front_point, self.top_right_back_point) 
            

        t1_bottom = Triangle(self.bottom_right_front_point, self.bottom_left_back_point, self.bottom_left_front_point) # bottom
        t2_bottom = Triangle(self.bottom_right_front_point, self.bottom_right_back_point, self.bottom_left_back_point)

        t1_back = Triangle(self.bottom_right_back_point, self.top_left_back_point, self.bottom_left_back_point) # back
        t2_back = Triangle(self.bottom_right_back_point, self.top_right_back_point, self.top_left_back_point)

        triangles = [
            t1_top, t2_top,
            t1_bottom, t2_bottom,
            t1_back, t2_back,
            t1_left, t2_left,
            t1_right, t2_right,
            t1_front, t2_front ] 

        n = len(triangles)
        for i in range(n):
            if not is_facing_away(normal_vector(triangles[i])):
                triangles[i].draw(win)
                if i % 2 == 0:
                    pg.draw.line(win, BLACK, triangles[i].p1.projection_cords, triangles[i].p3.projection_cords, 3)
                    pg.draw.line(win, BLACK, triangles[i].p2.projection_cords, triangles[i].p3.projection_cords, 3)
                else:
                    pg.draw.line(win, BLACK, triangles[i].p1.projection_cords, triangles[i].p2.projection_cords, 3)
                    pg.draw.line(win, BLACK, triangles[i].p2.projection_cords, triangles[i].p3.projection_cords, 3)

