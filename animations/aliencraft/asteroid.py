from pygame.sprite import Sprite
import pygame
import os.path
import numpy.random as random



class Asteroid(Sprite):
    """description of class"""
    vy_max = 20
    

    @classmethod
    def init(cls,SIZE):
        """load the asteroid images"""
        cls.SIZE = SIZE
        (cls.X, cls.Y) = SIZE
        cls.images = []
        for i in (1,2,3):
            image = pygame.image.load(os.path.dirname(__file__)+"/ASTEROID{}.PNG".format(i)).convert()
            image = pygame.transform.scale(image, (image.get_width()* cls.X/4000, image.get_height() * cls.Y/3000))
            # set transparent color
            image.set_colorkey(pygame.color.Color("white"))
            cls.images.append(image)

    def __init__(self):
        Sprite.__init__(self)
        self.asteroid_type = random.randint(3)
        self.image = Asteroid.images[self.asteroid_type]
        self.rect = self.image.get_rect()
        self.y = 0.0 - self.rect.height        
        halfwidth = self.rect.width / 2
        self.x = halfwidth + float(random.randint(self.X - halfwidth))
        self.vy = random.random() * self.vy_max + 4.0
        print("new asteroid, type is {}, center is {}, speed is {}".format(self.asteroid_type,self.rect.center, self.vy))

    def update(self,ship_vy):
        dy = ship_vy * self.vy
        self.y += dy
        self.rect.center = (self.x, self.y)
        if self.rect.top > self.Y:
            self.y = 0.0 - self.rect.height     
        #print("moving asteroid, type is {}, center is {}, dy is {}".format(self.asteroid_type, self.rect.center, dy))
