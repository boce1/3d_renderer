import pygame as pg

class Triangle:
    def __init__(self, point1, point2, point3):
        self.p1 = point1
        self.p2 = point2
        self.p3 = point3
        self.points = [self.p1, self.p2, self.p3]
    

    def draw(self, win, drawPoints):
        cords_list = [(self.p1.projection_x, self.p1.projection_y), 
                      (self.p2.projection_x, self.p2.projection_y), 
                      (self.p3.projection_x, self.p3.projection_y)]
        pg.draw.polygon(win, (255,255,255), cords_list, width=2)
        if drawPoints:
            self.p1.draw(win)
            self.p2.draw(win)
            self.p3.draw(win)
        