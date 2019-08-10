from ..actors.Wall import *
from engine.Engine import *
from engine.Scene import *
from Environment import *


class Play(Scene):
    def buildWalls(self):
        screenSize = (Environment.screenWidth, Environment.screenHeight)
        self.background = Engine.createRect(screenSize, (255,255,255))

        self.walls = []
        # left room
        self.walls.append(Wall((0, 390, 249, 399)))
        self.walls.append(Wall((0, 200, 9, 399)))
        self.walls.append(Wall((0, 200, 249, 209)))
        # top room
        self.walls.append(Wall((250, 0, 259, 199)))
        self.walls.append(Wall((250, 0, 549, 9)))
        self.walls.append(Wall((540, 0, 549, 199)))
        # right room
        self.walls.append(Wall((550, 200, 799, 209)))
        self.walls.append(Wall((790, 200, 799, 399)))
        self.walls.append(Wall((550, 390, 799, 399)))
        # bottom room
        self.walls.append(Wall((540, 400, 549, 599)))
        self.walls.append(Wall((250, 590, 549, 599)))
        self.walls.append(Wall((250, 400, 259, 599)))
        # left door
        self.walls.append(Wall((250, 200, 259, 259)))
        self.walls.append(Wall((250, 340, 259, 399)))
        # top door
        self.walls.append(Wall((250, 200, 309, 209)))
        self.walls.append(Wall((490, 200, 549, 209)))
        # right door
        self.walls.append(Wall((540, 200, 549, 259)))
        self.walls.append(Wall((540, 340, 549, 399)))
        # bottom door
        self.walls.append(Wall((250, 390, 309, 399)))
        self.walls.append(Wall((490, 390, 549, 399)))


    def __init__(self):
        super().__init__()
        self.buildWalls()


    def draw(self):
        Engine.draw(self.background, (0,0))

        for wall in self.walls:
            Engine.draw(wall.drawable, wall.getPosition())