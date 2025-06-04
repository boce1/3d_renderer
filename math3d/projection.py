from constants import *

def projection_cords(point):
    x = (point.x * FOV) / (FOV + point.z) # prjection matrix
    y = (point.y * FOV) / (FOV + point.z)

    x *= UNIT
    y *= UNIT
    
    x += WIDTH // 2 # move it to center
    y = HEIGHT // 2 - y # move it to center and  multiply to (1, -1) vector to rotate it

    return (int(x), int(y))