from pygame.sprite import Sprite
import pygame
import os.path
import numpy.random as random



class Asteroid(Sprite):
    """Asteroid: a rock hurling through space"""
    vy_max = 20
    

    @classmethod
    def init(cls,SIZE):
        """load the asteroid images"""
        cls.SIZE = SIZE
        (cls.X, cls.Y) = SIZE

        # load three sizes of asteroids and scale to a good size
        cls.images = []
        for i in (1,2,3):
            image = pygame.image.load(os.path.dirname(__file__)+"/ASTEROID{}.PNG".format(i)).convert()
            image = pygame.transform.scale(image, (image.get_width()* cls.X/4000, image.get_height() * cls.Y/3000))
            # set transparent color
            image.set_colorkey(pygame.color.Color("white"))
            cls.images.append(image)

    def __init__(self):
        Sprite.__init__(self)

        # 3 sizes of asteroids, load the right image
        self.asteroid_type = random.randint(3)
        self.image = Asteroid.images[self.asteroid_type]
        self.rect = self.image.get_rect()

        # we start just outside the top of the screen (y=0)
        self.y = 0.0 - self.rect.height    
        
        # make sure we stay within the screen in x direction. 
        # our x coordinate is on the center of the rectangle, so we compute the half
        # of the rectangle width   
        halfwidth = self.rect.width / 2
        self.x = halfwidth + float(random.randint(self.X - halfwidth))
        
        # take a random number for the vertical speed
        self.vy = random.random() * self.vy_max + 4.0
        print("new asteroid, type is {}, center is {}, speed is {}".format(self.asteroid_type,self.rect.center, self.vy))

    def update(self,ship_vy):

        # total speed on screen is asteroid speed + ship speed
        dy = ship_vy * self.vy
        self.y += dy
        self.rect.center = (self.x, self.y)
        
        # when asteroid disappears at the bottom of the  screen, re-appear at the top  
        if self.rect.top > self.Y:
            self.y = 0.0 - self.rect.height     
        #print("moving asteroid, type is {}, center is {}, dy is {}".format(self.asteroid_type, self.rect.center, dy))
