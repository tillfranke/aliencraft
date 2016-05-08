from pygame.sprite import Sprite
import pygame
import os.path
import numpy.random as random

class SpaceObject(Sprite):
    """description of class"""



    @classmethod
    def init(cls,SIZE):
        cls.SIZE = SIZE
        (cls.X, cls.Y) = SIZE


    def __init__(self):
        Sprite.__init__(self)

        # we start just outside the top of the screen (y=0)
        self.y = 0.0 - self.rect.height    
        # make sure we stay within the screen in x direction. 
        # our x coordinate is on the center of the rectangle, so we compute the half
        # of the rectangle width   
        halfwidth = self.rect.width / 2
        self.x = halfwidth + float(random.randint(self.X - halfwidth))
    def update(self,ship_vy):
        pass