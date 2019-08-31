from .Direction4 import *


class Rectangle:
    def __init__(self, dimension):
        self.dimension = dimension
    
    
    def __init__(self, center, size):
        self.dimension = [
            center[0] - (size[0] / 2),
            center[1] - (size[1] / 2),
            center[0] + (size[0] / 2),
            center[1] + (size[1] / 2)
        ]


    def move(self, direction, distance):
        if Direction4.Left == direction:
            self.dimension[0] -= distance
            self.dimension[2] -= distance
        elif Direction4.Up == direction:
            self.dimension[1] -= distance
            self.dimension[3] -= distance
        elif Direction4.Right == direction:
            self.dimension[0] += distance
            self.dimension[2] += distance
        else:
            self.dimension[1] += distance
            self.dimension[3] += distance
