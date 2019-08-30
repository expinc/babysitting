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