from pygame.sprite import Sprite
from aliencraft.space_object import SpaceObject
import pygame
import os.path
import numpy.random as random





class AlienCoin(SpaceObject):
    """description of class"""



    @classmethod
    def initialize(cls,SIZE):
        SpaceObject.init(SIZE)
        image = pygame.image.load(os.path.dirname(__file__)+"/COIN.PNG").convert()
        image = pygame.transform.scale(image, (image.get_width()* cls.X/4000, image.get_height() * cls.Y/3000))
        # set transparent color
        image.set_colorkey(pygame.color.Color("white"))
        
        cls.image = image

    def __init__(self):

        self.image = AlienCoin.image
        self.rect = self.image.get_rect()

        SpaceObject.__init__(self)
        
    def update(self,ship_vy):

        # total speed on screen is ship speed
        dy = 5* ship_vy
        self.y += dy
        self.rect.center = (self.x, self.y)
        
        # when coin disappears at the bottom of the  screen, re-appear at the top  
        if self.rect.top > self.Y:
            self.y = 0.0 - self.rect.height     
