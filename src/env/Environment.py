import pygame


class Environment:
    # directories:
    workDir = "./"
    resourceDir = workDir + "rc/"

    # display attributes:
    screenWidth = 800
    screenHeight = 600
    screen = None


    @staticmethod
    def init():
        pygame.init()
        Environment.screen = pygame.display.set_mode((Environment.screenWidth,Environment.screenHeight))
        pygame.display.set_caption("Babysitting")

    
    @staticmethod
    def getEvent():
        return pygame.event.poll()


    @staticmethod
    def flushDisplay():
        pygame.display.update()
