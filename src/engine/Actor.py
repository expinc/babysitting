class Actor:
    def __init__(self, dimension):
        # dimesion = (left, top, right, bottom)
        self.dimension = dimension
        self.drawable = None


    def getPosition(self):
        # (left, top)
        return self.dimension[0:2]


    def getSize(self):
        # (width, height)
        return (
            self.dimension[2] - self.dimension[0] + 1,
            self.dimension[3] - self.dimension[1] + 1)
        