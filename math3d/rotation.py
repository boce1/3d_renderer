from math import sin, cos

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

def rotate_x(entity, angle):
    rotate_x_matrix = [[1, 0, 0],
                       [0, cos(angle), -sin(angle)],
                       [0, sin(angle), cos(angle)]]
    
    for point in entity.points:
        new_cords = multiply_matrices(point, rotate_x_matrix)
        point.update_cords(new_cords)

def rotate_y(entity, angle):
    rotate_y_matrix = [[cos(angle), 0, sin(angle)],
                       [0, 1, 0],
                       [-sin(angle), 0, cos(angle)]]
    
    for point in entity.points:
        new_cords = multiply_matrices(point, rotate_y_matrix)
        point.update_cords(new_cords)

def rotate_z(entity, angle):
    rotate_z_matrix = [[cos(angle), -sin(angle), 0],
                       [sin(angle), cos(angle), 0],
                       [0, 0, 1]]
    
    for point in entity.points:
        new_cords = multiply_matrices(point, rotate_z_matrix)
        point.update_cords(new_cords)