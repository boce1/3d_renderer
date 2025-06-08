from point import *
from triangle import *
from constants import *
from math3d import *

class Pyramid:
    def __init__(self, top_point, height, width, depth):
        self.top_point = top_point
        self.height = height
        self.width = width
        self.depth = depth

        x, y, z, color = self.top_point.x, self.top_point.y, self.top_point.z, self.top_point.color

        self.left_front_point = Point(x - self.width // 2, y - self.height, z - self.depth // 2, color)
        self.right_front_point = Point(x + self.width // 2, y - self.height, z - self.depth // 2, color)
        self.left_back_point = Point(x - self.width // 2, y - self.height, z + self.depth // 2, color)
        self.right_back_point = Point(x + self.width // 2, y - self.height, z + self.depth // 2, color)

        self.points = [self.top_point, self.left_front_point, self.right_front_point, self.left_back_point, self.right_back_point]
        self.center = center_of_mass(self.points)
        self.points.append(self.center)

    def draw(self, win):
        self.draw_triangles(win)

    def draw_triangles(self, win):
        t1 = Triangle(self.top_point, self.left_front_point, self.right_front_point)
        t2 = Triangle(self.top_point, self.right_front_point, self.right_back_point)
        t3 = Triangle(self.top_point, self.right_back_point, self.left_back_point)
        t4 = Triangle(self.top_point, self.left_back_point,  self.left_front_point)

        t1_bottom = Triangle(self.left_front_point, self.right_back_point, self.right_front_point)
        t2_bottom = Triangle(self.left_front_point, self.left_back_point, self.right_back_point)

        triagnles = [t1, t2, t3, t4, t1_bottom, t2_bottom] 

        #for p in self.points:
        #    p.draw(win)

        for i in range(len(triagnles)):
            if not is_facing_away(normal_vector(triagnles[i])):
                triagnles[i].draw(win)
                if i < 4: # t1, t2, t3, t4
                    pg.draw.line(win, BLACK, triagnles[i].p1.projection_cords, triagnles[i].p2.projection_cords, 3)
                    pg.draw.line(win, BLACK, triagnles[i].p1.projection_cords, triagnles[i].p3.projection_cords, 3)
                    pg.draw.line(win, BLACK, triagnles[i].p2.projection_cords, triagnles[i].p3.projection_cords, 3)
                if i == 4:
                    pg.draw.line(win, BLACK, triagnles[i].p2.projection_cords, triagnles[i].p3.projection_cords, 3)
                    pg.draw.line(win, BLACK, triagnles[i].p1.projection_cords, triagnles[i].p3.projection_cords, 3)

                if i == 5:
                    pg.draw.line(win, BLACK, triagnles[i].p3.projection_cords, triagnles[i].p2.projection_cords, 3)
                    pg.draw.line(win, BLACK, triagnles[i].p1.projection_cords, triagnles[i].p2.projection_cords, 3)


