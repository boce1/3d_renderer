from math import acos, pi

def cross_product(v1_tuple, v2_tuple):
    prod = []
    prod.append(v1_tuple[1] * v2_tuple[2] - v2_tuple[1] * v1_tuple[2])
    prod.append(v1_tuple[0] * v2_tuple[2] - v2_tuple[0] * v1_tuple[2])
    prod.append(v1_tuple[0] * v2_tuple[1] - v2_tuple[0] * v1_tuple[1])

    return tuple(prod)

def normal_vector(triangle): 
    vector_p1_p2 = (triangle.p2.x - triangle.p1.x, triangle.p2.y - triangle.p1.y, triangle.p2.z - triangle.p1.z) # y and z swaped
    vector_p1_p3 = (triangle.p3.x - triangle.p1.x,  triangle.p3.y - triangle.p1.y, triangle.p3.z - triangle.p1.z) # bacause x, y are projection axes

    return cross_product(vector_p1_p2, vector_p1_p3)

def magnitude(vector):
    x, y, z = vector
    return (x**2 + y**2 + z**2)**0.5

def angle_y(normal_vector_tuple):
    m = magnitude(normal_vector_tuple)
    if m == 0:
        return 0
    return acos(normal_vector_tuple[1] / m) 

def angle_x(normal_vector_tuple):
    m = magnitude(normal_vector_tuple)
    if m == 0:
        return 0
    return acos(normal_vector_tuple[0] / m) 

def is_facing_away(normal_vector_tuple, view_direction = (0,0,1)):
    dot_product = (
        normal_vector_tuple[0] * view_direction[0] +
        normal_vector_tuple[1] * view_direction[1] +
        normal_vector_tuple[2] * view_direction[2]
    )

    return dot_product < 0