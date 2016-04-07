from pygame.sprite import Sprite
import pygame
from colors import color
import os.path

class Ship(Sprite):
    """all aspects of the player ship"""
    # maximum y:horizontal and x:vertical speed 
    vy_max = 10
    vx_max = 5
    def __init__(self, SIZE):
        Sprite.__init__(self)
        # total screen size
        (X,Y) = SIZE
        self.X = X
        self.Y = Y
        image = pygame.image.load(os.path.dirname(__file__)+"/SHIP.PNG").convert()
        self.image = pygame.transform.scale(image, (X/40,Y/30))
        # set transparent color
        self.image.set_colorkey(color("White"))
        self.rect = self.image.get_rect()
        self.rect.center = ( X/2, 4*Y/5)
        # speed horizontal
        self.vx = 0
        # speed vertical
        self.vy = 0.1

    def update(self):
        # add current x speed (negative or positive) to position
        if self.rect.left + self.vx <0 or self.rect.right + self.vx > self.X:
            self.vx = 0 
        self.rect.x += self.vx

    def left(self):
        # check for maximum speed left (negative)
        if self.vx > - self.vx_max:
            self.vx -= 1
    def right(self):
        # check for maximum speed right (positive)
        if self.vx < self.vx_max:
            self.vx += 1
    def stop(self):
        self.vx = 0

    def handle_events(self,e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                self.left()
            elif e.key == pygame.K_d:
                self.right()
            elif e.key == pygame.K_SPACE:
                self.stop()
