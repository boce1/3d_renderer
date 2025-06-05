import pygame as pg
from constants import *
from math3d import projection_cords, center_of_mass
from math import ceil, floor

class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.points = [self.p1, self.p2, self.p3]
        self.outline_color = BLACK

        self.center = center_of_mass(self.points)
        self.points.append(self.center)

    def draw(self, win, draw_points=False):
        self.draw_lines(win)

        if draw_points:
            cords_list = [(self.p1.projection_x, self.p1.projection_y), 
                          (self.p2.projection_x, self.p2.projection_y), 
                          (self.p3.projection_x, self.p3.projection_y)]
            pg.draw.polygon(win, self.outline_color, cords_list, width=2)
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
        bottom_point = bottom_points[0]
        x_bottom, y_bottom = projection_cords(bottom_point)

        # colors
        n_top_mid = int(floor(y_middle - y_hightest)) + 1
        colors_top_middle = self.calculate_colors_on_lines(heightest_point, middle_point, n_top_mid)
        
        n_top_bottom = int(floor(y_bottom - y_hightest)) + 1
        colors_top_bottom = self.calculate_colors_on_lines(heightest_point, bottom_point, n_top_bottom)

        n_middle_bottom = int(floor(y_bottom - y_middle)) + 1
        colors_middle_bottom = self.calculate_colors_on_lines(bottom_point, middle_point, n_middle_bottom)
    
        # # #
        # draw top to middle
        current_x1 = None
        current_x2 = None
        color_index = None

        if abs(y_hightest - y_middle) > PIXEL_LIMIT_DISTANCE and abs(y_hightest - y_bottom) > PIXEL_LIMIT_DISTANCE:
            slope_top_p1 = (x_highest - x_middle) / (y_hightest - y_middle)
            slope_top_p2 = (x_highest - x_bottom) / (y_hightest - y_bottom)
            current_x1 = x_highest
            current_x2 = x_highest
            color_index = 0
            for y in range(int(y_hightest), int(y_middle)):
                line_width = int(ceil(abs(current_x1 - current_x2)))
                if 0 <= color_index < len(colors_top_middle):
                    color1 = colors_top_middle[color_index]
                else:
                    color1 = BLACK
                if color_index < len(colors_top_bottom):
                    color2 = colors_top_bottom[color_index]
                else:
                    color2 = BLACK
                color_index += 1
                if x_middle < x_bottom:
                    line_colors = self.calculate_color_inside(color1, color2, line_width)
                else:
                    line_colors = self.calculate_color_inside(color2, color1, line_width)


                line_x_min = int(min(current_x1, current_x2))
                for i in range(line_width):
                    pg.draw.rect(win, line_colors[i], (line_x_min + i, y, 1, 1)) 
                current_x1 += slope_top_p1
                current_x2 += slope_top_p2

    # current_x2 is the point where its equal to x_middle but for seconds line

    # draw middle to bottom
        if abs(y_bottom - y_middle) > PIXEL_LIMIT_DISTANCE:

            if not current_x2:
                current_x2 = x_highest
            if not color_index:
                color_index = 0

            slope_middle_p1 = (x_bottom - x_middle) / (y_bottom - y_middle)
            slope_middle_p2 = (x_bottom - current_x2) / (y_bottom - y_middle)
        
            current_x1_bottom = x_bottom
            current_x2_bottom = x_bottom
            color_index_bottom = 0
            
            for y in range(int(y_bottom), int(y_middle)-1, -1):

                line_width = int(ceil(abs(current_x1_bottom - current_x2_bottom)))
                #print(n_top_bottom - color_index_bottom, len(colors_top_bottom))
                if 0 <= n_top_bottom - color_index_bottom < len(colors_top_bottom):
                    color1 = colors_top_bottom[n_top_bottom - color_index_bottom]
                else:
                    color1 = BLACK
                if color_index_bottom < len(colors_middle_bottom):
                    color2 = colors_middle_bottom[color_index_bottom]
                else:
                    color2 = BLACK
                color_index -= 1
                color_index_bottom += 1
                if x_middle > x_bottom:
                    line_colors = self.calculate_color_inside(color1, color2, line_width)
                else:
                    line_colors = self.calculate_color_inside(color2, color1, line_width)

                line_x_min = int(min(current_x1_bottom, current_x2_bottom))
                for i in range(line_width):
                    pg.draw.rect(win, line_colors[i], (line_x_min + i, y, 1, 1)) 
                # color2 above is for top to bottom, color_index is the last visited color and thats where it starts coloring for the bottom triable
                current_x1_bottom -= slope_middle_p1
                current_x2_bottom -= slope_middle_p2 


    def calculate_colors_on_lines(self, point1, point2, n):
        colors = []
        if n > 0:
            for i in range(n+1):
                red = int(point1.render_color[0] * (n - i) / n + point2.render_color[0] * i / n) % 256
                green = int(point1.render_color[1] * (n - i) / n + point2.render_color[1] * i / n) % 256
                blue = int(point1.render_color[2] * (n - i) / n + point2.render_color[2] * i / n) % 256

                colors.append((red, green, blue))
        return colors
    
    def calculate_color_inside(self, color_tuple1, color_tuple2, x):
        colors = []
        if x > 0:
            for i in range(x):
                red = int(color_tuple1[0] * (x - i) / x + color_tuple2[0] * i / x) % 256
                green = int(color_tuple1[1] * (x - i) / x + color_tuple2[1] * i / x) % 256
                blue = int(color_tuple1[2] * (x - i) / x + color_tuple2[2] * i / x) % 256

                colors.append((red, green, blue))
        return colors

