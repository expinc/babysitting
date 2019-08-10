import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')


import pygame.locals
from Environment import *
from engine.Game import *
from game.scenes.SceneType import *

Environment.init()
game = Game(SceneType.Welcome)
while True:
    event = Environment.getEvent()
    if event.type == pygame.locals.QUIT:
        sys.exit()
    game.handleEvent(event)
