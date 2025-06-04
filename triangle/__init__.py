import pygame as pg
from constants import *
from math3d import projection_cords

class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.points = [self.p1, self.p2, self.p3]
        self.outline_color = BLACK
        self.segments_num = 5

    def draw(self, win, drawPoints=False):
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

        # top point
        heightest_point = self.p1
        for p in self.points:
            if p.y > heightest_point.y:
                heightest_point = p
        
        bottom_points = [p for p in self.points]
        bottom_points.remove(heightest_point)
        x_highest, y_hightest = projection_cords(heightest_point)

        # middle point
        middle_point = bottom_points[0]
        if bottom_points[1].y > middle_point.y:
            middle_point = bottom_points[1]
        bottom_points.remove(middle_point)
        x_middle, y_middle = projection_cords(middle_point)
     
        # bottom point
        x_bottom, y_bottom = projection_cords(bottom_points[0])

        # draw top to middle
        slope_top_p1 = (x_highest - x_middle) / (y_hightest - y_middle)
        slope_top_p2 = (x_highest - x_bottom) / (y_hightest - y_bottom)
        
        current_x1 = x_highest
        current_x2 = x_highest
        n = int(y_hightest - x_middle)
        for y in range(int(y_hightest), int(y_middle)):
            pg.draw.line(win, BLACK, (current_x1, y), (current_x2, y), 1)
            current_x1 += slope_top_p1
            current_x2 += slope_top_p2

        # current_x2 is the point where its equal to x_middle but for seconds line

        # draw middle to bottom
        if y_bottom != y_middle:
            slope_middle_p1 = (x_bottom - x_middle) / (y_bottom - y_middle)
            slope_middle_p2 = (x_bottom - current_x2) / (y_bottom - y_middle)

            current_x1_bottom = x_bottom
            current_x2_bottom = x_bottom
            for y in range(int(y_bottom), int(y_middle) - 1, -1):
                pg.draw.line(win, BLACK, (current_x1_bottom, y), (current_x2_bottom, y), 1)
                current_x1_bottom -= slope_middle_p1
                current_x2_bottom -= slope_middle_p2  