import sys
import os
sys.path.append(os.path.dirname(__file__) + os.sep + '../')

import pygame.locals
from env.Environment import Environment


Environment.init()
while True:
    event = Environment.getEvent()
    if event.type == pygame.locals.QUIT:
        sys.exit()
