from engine.Actor import *
from engine.Engine import *
from geo2d.Rectangle import *
from game.Util import *


class Mom(Actor):
    def directTo(self, direction):
        if Direction4.Left == direction:
            drawableIndex = "left"
        elif Direction4.Up == direction:
            drawableIndex = "up"
        elif Direction4.Right == direction:
            drawableIndex = "right"
        else:
            drawableIndex = "down"
        
        self.drawable = self.drawables[drawableIndex]
        self.direction = direction
        

    def __init__(self, center):
        self.drawables = {}
        self.drawables["left"] = Engine.loadImage("mom-left.png")
        self.drawables["up"] = Engine.loadImage("mom-up.png")
        self.drawables["right"] = Engine.loadImage("mom-right.png")
        self.drawables["down"] = Engine.loadImage("mom-down.png")

        size = self.drawables["down"].size()
        self.geo = Rectangle(center, size)
        self.dimension = self.geo.dimension
        self.directTo(Direction4.Down)