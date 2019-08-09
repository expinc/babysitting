from .Engine import *
from .Scene import *


class Game:
    def __init__(self, initScene):
        super().__init__()
        self.scene = initScene
        self.fps = 20
        self.lastFlushedTick = Engine.getTick()


    def handleEvent(self, event):
        currentTick = Engine.getTick()
        tickTnterval = currentTick - self.lastFlushedTick

        self.scene.handleEvent(event, currentTick)

        if (tickTnterval > (1 / self.fps * 1000)):
            self.scene.draw()
            self.lastFlushedTick = currentTick
            Engine.flushDisplay()
