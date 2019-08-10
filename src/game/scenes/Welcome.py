from .SceneType import *
from engine.Scene import *
from engine.Engine import *
from Meta import *


class Welcome(Scene):
    def refreshPressStartText(self):
        self.pressStartText = Engine.createText("Press space to start", self.pressStartFonts[self.pressStartFontIndex])


    def __init__(self):
        super().__init__()

        self.resources = {"background" : Engine.loadImage("welcome.png")}

        self.pressStartFonts = []
        pressStartFontSize = 40
        pressStartFontTypeface = "calibri"
        self.pressStartFonts.append(Engine.createFont(pressStartFontSize, (255,1,1), pressStartFontTypeface, True))
        self.pressStartFonts.append(Engine.createFont(pressStartFontSize, (1,255,1), pressStartFontTypeface, True))
        self.pressStartFonts.append(Engine.createFont(pressStartFontSize, (1,1,255), pressStartFontTypeface, True))
        self.pressStartFontIndex = 0
        self.refreshPressStartText()
        self.pressStartColorChangeInterval = 500
        self.lastPressStartColorChangeTick = Engine.getTick()

        versionFont = Engine.createFont(20)
        self.resources["version"] = Engine.createText("Version " + Meta.version, versionFont)


    def handleEvent(self, event, currentTick):
        nextSceneType = SceneType.Welcome
        if (pygame.KEYUP == event.type and pygame.K_SPACE == event.key):
            nextSceneType = SceneType.Play

        lastPressStartColorChangeDuration = currentTick - self.lastPressStartColorChangeTick
        if (lastPressStartColorChangeDuration > self.pressStartColorChangeInterval):
            self.pressStartFontIndex = (self.pressStartFontIndex + 1) % 3
            self.refreshPressStartText()
            self.lastPressStartColorChangeTick = currentTick

        return nextSceneType


    def draw(self):
        Engine.draw(self.resources["background"], (0,0))
        Engine.draw(self.pressStartText, (240,380))
        
        versionText = self.resources["version"]
        versionSize = versionText.size()
        versionPosition = (
            Environment.screenWidth - versionSize[0] - 1,
            Environment.screenHeight - versionSize[1] - 1)
        Engine.draw(versionText, versionPosition)