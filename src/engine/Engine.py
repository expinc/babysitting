from .resource.Drawable import *
from .resource.Font import *
from Environment import *
from pygame import time


class Engine:
    transparentColorKey = (0,0,0)


    @staticmethod
    def getTick():
        return time.get_ticks()


    @staticmethod
    def createRect(size, color = (1,1,1)):
        drawable = Drawable(pygame.Surface(size))
        drawable.surface.set_colorkey(Engine.transparentColorKey)
        pygameRect = pygame.Rect((0,0), size)
        pygame.draw.rect(drawable.surface, color, pygameRect)
        return drawable


    @staticmethod
    def loadImage(file):
        result = Image()
        result.surface = pygame.image.load(Environment.resourceDir + file)
        return result


    @staticmethod
    def createFont(size, color = (1,1,1), typeface = "arial", italic = False, bold = False):
        return Font(size, color, typeface, italic, bold)


    @staticmethod
    def createText(content, font):
        return Text(font.internalFont.render(content, True, font.color))


    @staticmethod
    def draw(drawable, position):
        Environment.screen.blit(drawable.surface, position)


    @staticmethod
    def flushDisplay():
        Environment.flushDisplay()