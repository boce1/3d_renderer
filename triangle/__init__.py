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
            if p.projection_y < heightest_point.projection_y:
                heightest_point = p
        
        bottom_points = [p for p in self.points]
        bottom_points.remove(heightest_point)
        x_highest, y_hightest = projection_cords(heightest_point)

        # middle point
        middle_point = bottom_points[0]
        if bottom_points[1].projection_y < middle_point.projection_y:
            middle_point = bottom_points[1]
        bottom_points.remove(middle_point)
        x_middle, y_middle = projection_cords(middle_point)
    
        # bottom point
        bottom_point = bottom_points[0]
        x_bottom, y_bottom = projection_cords(bottom_point)
        
        # colors
        n_top_mid = y_middle - y_hightest
        colors_top_middle = self.calculate_colors_on_lines(heightest_point, middle_point, n_top_mid)
        
        n_top_bottom = y_bottom - y_hightest
        colors_top_bottom = self.calculate_colors_on_lines(heightest_point, bottom_point, n_top_bottom)

        n_middle_bottom = y_bottom - y_middle
        colors_middle_bottom = self.calculate_colors_on_lines(bottom_point, middle_point, n_middle_bottom)
    
        # # #
        # draw top to middle
        slope_top_p1 = 0
        slope_top_p2 = 0

        if y_hightest != y_middle:
            slope_top_p1 = (x_highest - x_middle) / (y_hightest - y_middle)
        if y_hightest != y_bottom:
            slope_top_p2 = (x_highest - x_bottom) / (y_hightest - y_bottom)
        current_x1 = x_highest
        current_x2 = x_highest
        color_index = 0

        for y in range(y_hightest, y_middle):
            line_width = ceil(abs(current_x1 - current_x2))
  
            #print(color_index // (n_top_mid // COLOR_SEGMENTS), len(colors_top_middle))
            if n_top_mid > COLOR_SEGMENTS:
                color1 = colors_top_middle[color_index // ((n_top_mid + COLOR_SEGMENTS - 1) // COLOR_SEGMENTS)]
            else:
                color1 = heightest_point.render_color
            
            if n_top_bottom > COLOR_SEGMENTS:
                color2 = colors_top_bottom[color_index // ((n_top_bottom + COLOR_SEGMENTS - 1) // COLOR_SEGMENTS)]
            else:
                color2 = heightest_point.render_color

            color_index += 1

            if x_middle < x_bottom:
                line_colors = self.calculate_color_inside(color1, color2, line_width)
            else:
                line_colors = self.calculate_color_inside(color2, color1, line_width)


            line_x_min = int(min(current_x1, current_x2))
            self.draw_line(win, line_colors, line_x_min, line_width, y) 
            
            current_x1 += slope_top_p1
            current_x2 += slope_top_p2

        # current_x2 is the point where its equal to x_middle but for seconds line

        # draw middle to bottom
        slope_middle_p1 = 0
        slope_middle_p2 = 0

        if y_bottom != y_middle:
            slope_middle_p1 = (x_bottom - x_middle) / (y_bottom - y_middle)
            slope_middle_p2 = (x_bottom - current_x2) / (y_bottom - y_middle)
        
        current_x1_bottom = x_bottom
        current_x2_bottom = x_bottom
        color_index_bottom = 0
         
        for y in range(y_bottom, y_middle - 1, -1):

            line_width = ceil(abs(current_x1_bottom - current_x2_bottom))
            if n_top_bottom > COLOR_SEGMENTS:
                color1 = colors_top_bottom[(n_top_bottom - color_index_bottom) // ((n_top_bottom + COLOR_SEGMENTS - 1) // COLOR_SEGMENTS)]
                #color1 = heightest_point.render_color

            else:
                color1 = heightest_point.render_color

            if n_middle_bottom > COLOR_SEGMENTS:
                color2 = colors_middle_bottom[color_index_bottom // ((n_middle_bottom + COLOR_SEGMENTS - 1) // COLOR_SEGMENTS)] # +2 for color on 0-th place and +1 for index border
            else:
                color2 = middle_point.render_color
            #print(color_index_bottom // COLOR_SEGMENTS % COLOR_SEGMENTS)
            
            color_index -= 1
            color_index_bottom += 1

            if x_middle > x_bottom:
                line_colors = self.calculate_color_inside(color1, color2, line_width)
            else:
                line_colors = self.calculate_color_inside(color2, color1, line_width)

            line_x_min = int(min(current_x1_bottom, current_x2_bottom))
            self.draw_line(win, line_colors, line_x_min, line_width, y)

            # color2 above is for top to bottom, color_index is the last visited color and thats where it starts coloring for the bottom triable
            current_x1_bottom -= slope_middle_p1
            current_x2_bottom -= slope_middle_p2 


    def calculate_colors_on_lines(self, point1, point2, n):
        colors = []
        if n > 0: # if levels are equal dont calcualte lines
            for i in range(COLOR_SEGMENTS + 1):
                red = int(point1.render_color[0] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + point2.render_color[0] * i / COLOR_SEGMENTS) % 256
                green = int(point1.render_color[1] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + point2.render_color[1] * i / COLOR_SEGMENTS) % 256
                blue = int(point1.render_color[2] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + point2.render_color[2] * i / COLOR_SEGMENTS) % 256

                colors.append((red, green, blue))
        else:
            colors.append(point2.render_color)
        
        return colors 
    
    def calculate_color_inside(self, color_tuple1, color_tuple2, line_width):
        colors = []
        for i in range(COLOR_SEGMENTS):
            red = int(color_tuple1[0] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + color_tuple2[0] * i / COLOR_SEGMENTS) % 256
            green = int(color_tuple1[1] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + color_tuple2[1] * i / COLOR_SEGMENTS) % 256
            blue = int(color_tuple1[2] * (COLOR_SEGMENTS - i) / COLOR_SEGMENTS + color_tuple2[2] * i / COLOR_SEGMENTS) % 256
            colors.append((red, green, blue))
        return colors
    
    def draw_line(self, win, line_colors, line_x_min, line_width, y):
        for i in range(line_width):
            if line_width > COLOR_SEGMENTS:
                pg.draw.rect(win, line_colors[i // ((line_width + COLOR_SEGMENTS - 1) // COLOR_SEGMENTS)], (line_x_min + i, y, 1, 1)) 
            else:
                pg.draw.rect(win, line_colors[i % COLOR_SEGMENTS], (line_x_min + i, y, 1, 1)) 
