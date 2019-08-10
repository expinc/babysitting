from .Engine import *
from .Scene import *
from game.scenes.SceneType import *
from game.scenes.Welcome import *
from game.scenes.Play import *


class Game:
    def goToScene(self, sceneType):
        self.sceneType = sceneType

        if SceneType.Welcome == sceneType:
            self.scene = Welcome()
        elif SceneType.Play == sceneType:
            self.scene = Play()


    def __init__(self, initScene):
        super().__init__()
        self.goToScene(initScene)
        self.fps = 20
        self.lastFlushedTick = Engine.getTick()


    def handleEvent(self, event):
        currentTick = Engine.getTick()
        tickTnterval = currentTick - self.lastFlushedTick

        nextSceneType = self.scene.handleEvent(event, currentTick)
        if nextSceneType != self.sceneType:
            self.goToScene(nextSceneType)

        if (tickTnterval > (1 / self.fps * 1000)):
            self.scene.draw()
            self.lastFlushedTick = currentTick
            Engine.flushDisplay()
