from ..actors.Mom import *
from ..actors.Wall import *
from .SceneType import *
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
        self.walls.append(Wall((250, 200, 349, 209)))
        self.walls.append(Wall((450, 200, 549, 209)))
        # right door
        self.walls.append(Wall((540, 200, 549, 259)))
        self.walls.append(Wall((540, 340, 549, 399)))
        # bottom door
        self.walls.append(Wall((250, 390, 349, 399)))
        self.walls.append(Wall((450, 390, 549, 399)))


    def __init__(self):
        super().__init__()
        self.buildWalls()
        initPos = [Environment.screenWidth / 2, Environment.screenHeight / 2]
        self.mom = Mom(initPos)
        self.lastMomMoveTick = Engine.getTick()
        self.momMoveHandleInterval = 100
        self.directionKeys = (
            pygame.K_LEFT,
            pygame.K_UP,
            pygame.K_RIGHT,
            pygame.K_DOWN
        )


    def draw(self):
        Engine.draw(self.background, (0,0))

        for wall in self.walls:
            Engine.draw(wall.drawable, wall.getPosition())

        Engine.draw(self.mom.drawable, self.mom.getLTCorner())


    def handleEvent(self, event, currentTick):
        nextSceneType = SceneType.Play
        if (pygame.KEYDOWN == event.type and event.key in self.directionKeys):
            if (pygame.K_LEFT == event.key):
                self.mom.moveDirection = Direction4.Left
            elif (pygame.K_UP == event.key):
                self.mom.moveDirection = Direction4.Up
            elif (pygame.K_RIGHT == event.key):
                self.mom.moveDirection = Direction4.Right
            else:
                self.mom.moveDirection = Direction4.Down
        elif (pygame.KEYUP == event.type and event.key in self.directionKeys):
            self.mom.moveDirection = None

        if (None != self.mom.moveDirection and currentTick - self.lastMomMoveTick > self.momMoveHandleInterval):
            self.lastMomMoveTick = currentTick
            self.mom.move()

        return nextSceneType
