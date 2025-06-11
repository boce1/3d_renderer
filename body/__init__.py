from .cube import *
from .pyramid import *
from .wrapper import *

def rainbow_body(entity, color_list):
    for i in range(len(entity.points)):
        entity.points[i].color = color_list[i % len(color_list)]