import pygame


class Font:
    def __init__(self, size, color = (0,0,0), typeface = "arial", italic = False, bold = False):
        bold = (0 if False == bold else 1)
        italic = (0 if False == italic else 1)
        self.internalFont = pygame.font.SysFont(typeface, size, bold, italic)
        self.color = color