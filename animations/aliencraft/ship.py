from pygame.sprite import Sprite
import pygame
from colors import color
import os.path
import numpy.random as random

class Ship(Sprite):
    """all aspects of the player ship"""
    # maximum y:horizontal and x:vertical speed 
    vy_max = 10
    vx_max = 10
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
        self.animation = None
        self.status = "flying"

    def update(self):
        # add current x speed (negative or positive) to position
        if self.rect.left + self.vx <0 or self.rect.right + self.vx > self.X:
            self.vx = 0 
        self.rect.x += self.vx
        if self.animation:
            self.animation()

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

    def crash(self):
        self.animation = self.explosion

    def explosion(self):
        if self.status != "exploding":
            self.status = "exploding"
            self.explosion_time = 0
            explosion_image = pygame.Surface((150,150))
            (x,y) = self.rect.center
            self.image = explosion_image
            self.image.fill(pygame.color.Color("white"))
            self.image.set_colorkey(pygame.color.Color("white"))
    
            self.rect = explosion_image.get_rect()
            self.rect.center = (x,y)
        explosion_color = (random.randint(100,255),0,0,random.randint(100,150))
        explosion_radius = random.randint(0, 30) + 2
        explosion_position = (random.randint(0,30) + 75 // 2 , random.randint(0,30) + 75)
        pygame.draw.circle(self.image, explosion_color, explosion_position, explosion_radius)
        self.explosion_time += 1
        if self.explosion_time > 300:
            self.status = False

    def handle_events(self,e):
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_a:
                self.left()
            elif e.key == pygame.K_d:
                self.right()
            elif e.key == pygame.K_SPACE:
                self.stop()
            elif e.key == pygame.K_F1:
                self.crash()




