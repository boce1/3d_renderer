from math import sin, cos
from point import *

def multiply_matrices(point, rotation_matrix):
    out = []
    for row in rotation_matrix:
        comp1 = point.x * row[0]
        comp2 = point.y * row[1]
        comp3 = point.z * row[2]
        out.append(comp1 + comp2 + comp3)

    return out


# user watches the monitor from x, y plane where z=0, so
# rotating y from the ordinary coordinating system is like rotating z
# rotating z from the ordinary coordinating system is like rotating y

# if rotate_around_center==Fals , entity rotate around (0,0,0)

def rotate_x(entity, angle, rotate_around_center=True):
    rotate_x_matrix = [[1, 0, 0],
                       [0, cos(angle), -sin(angle)],
                       [0, sin(angle), cos(angle)]]
    
    for point in entity.points:
        if rotate_around_center:
            temp_point = Point(point.x - entity.center.x, point.y - entity.center.y, point.z - entity.center.z, BLACK)
            new_cords = multiply_matrices(temp_point, rotate_x_matrix)
            new_cords = update_cord_list(new_cords, entity.center)
        else:
            new_cords = multiply_matrices(point, rotate_x_matrix)

        point.update_cords(new_cords)

def rotate_y(entity, angle, rotate_around_center=True):
    rotate_y_matrix = [[cos(angle), 0, sin(angle)],
                       [0, 1, 0],
                       [-sin(angle), 0, cos(angle)]]
    
    for point in entity.points:
        if rotate_around_center:
            temp_point = Point(point.x - entity.center.x, point.y - entity.center.y, point.z - entity.center.z, BLACK)
            new_cords = multiply_matrices(temp_point, rotate_y_matrix)
            new_cords = update_cord_list(new_cords, entity.center)
        else:
            new_cords = multiply_matrices(point, rotate_y_matrix)

        point.update_cords(new_cords)


def rotate_z(entity, angle, rotate_around_center=True):
    rotate_z_matrix = [[cos(angle), -sin(angle), 0],
                       [sin(angle), cos(angle), 0],
                       [0, 0, 1]]
    
    for point in entity.points:
        if rotate_around_center:
            temp_point = Point(point.x - entity.center.x, point.y - entity.center.y, point.z - entity.center.z, BLACK)
            new_cords = multiply_matrices(temp_point, rotate_z_matrix)
            new_cords = update_cord_list(new_cords, entity.center)
        else:
            new_cords = multiply_matrices(point, rotate_z_matrix)

        point.update_cords(new_cords)

def center_of_mass(points):
    # each point has a mass of 1 unit
    n = len(points)
    x = sum([p.x for p in points]) // n
    y = sum([p.y  for p in points]) // n
    z = sum([p.z for p in points]) // n

    return Point(x, y, z, BLACK)

def update_cord_list(cord_list, point):
    return [cord_list[0] + point.x,
            cord_list[1] + point.y,
            cord_list[2] + point.z]