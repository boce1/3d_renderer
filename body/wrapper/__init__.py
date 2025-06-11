from math3d import rotate_x, rotate_y, rotate_z

class Wrapper:
    def __init__(self):
        self.bodies_atributes = dict()
        self.bodies = list()

    def add(self, body, angle_x=0, center_x=True, angle_y=0, center_y=True, angle_z=0, center_z=True):
        self.bodies_atributes[body] = [[angle_x, center_x], [angle_y, center_y], [angle_z, center_z]]
        self.bodies.append(body)

    def sort(self):
        nearest_points = dict()
        for b in self.bodies:
            min_point = b.points[0]
            for p in b.points:
                if p.z < min_point.z:
                    min_point = p
            nearest_points[b] = min_point

        self.bodies = sorted(self.bodies, key=lambda body : nearest_points[body].z, reverse=True) # reserse the list
        # the closest one need to be rendered the last

    def draw(self, win, camera_position):
        self.sort()

        for b in self.bodies:
            rotate_x(b, self.bodies_atributes[b][0][0], self.bodies_atributes[b][0][1], camera_position)
            rotate_y(b, self.bodies_atributes[b][1][0], self.bodies_atributes[b][1][1], camera_position)
            rotate_z(b, self.bodies_atributes[b][2][0], self.bodies_atributes[b][2][1], camera_position)

            b.draw(win)