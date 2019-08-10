from engine.Actor import *
from engine.Engine import *


class Wall(Actor):
    def __init__(self, dimension):
        super().__init__(dimension)
        size = self.getSize()
        self.drawable = Engine.createRect(size)
