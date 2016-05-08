import pygame
from colors import color
from backgrounds import Starfield
from aliencraft.ship import Ship
from aliencraft.asteroid import Asteroid
from aliencraft.aliencoin import AlienCoin
from pygame.sprite import RenderUpdates, spritecollideany
import numpy.random as random

import time

X=800
Y=600
SIZE=(X,Y)
CLOCK = None
SCREEN = None

FPS=30

START_ASTEROIDS = 5
START_COINS = 1




        
def main():
    pygame.init()
    global SCREEN
    #SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #SIZE=pygame.display.get_surface().get_size()
    SCREEN = pygame.display.set_mode(SIZE)

    background = Starfield(SCREEN,SIZE)

    ship = Ship(SIZE)
    player = RenderUpdates(ship)

    Asteroid.initialize(SIZE)
    AlienCoin.initialize(SIZE)
    asteroids = RenderUpdates()
    coins = RenderUpdates()

    for i in range(START_ASTEROIDS):
        asteroids.add(Asteroid())    

    for i in range(START_COINS):
        coins.add(AlienCoin())
    
    # aliens = RenderUpdates(coins)
    CLOCK = pygame.time.Clock()
    pygame.key.set_repeat(10,10)
    y = 0.0

    running = True
    while running and ship.status:
        for e in  pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                ship.handle_events(e)

        y += ship.vy
        if y  > 10*len(asteroids.sprites()) and random.random() < 0.5:
            asteroids.add(Asteroid())     

        if y  > 10*len(coins.sprites()) and random.random() < 0.1:
            coins.add(AlienCoin())     
        
        SCREEN.blit(background.render((0,y)),(0,0))
        player.update()
        asteroids.update(ship.vy)
        coins.update(ship.vy)
        # aliens.update()
        player.draw(SCREEN)
        asteroids.draw(SCREEN)
        coins.draw(SCREEN)
        # aliens.draw(SCREEN)
        pygame.display.flip()
        dt = CLOCK.tick(FPS)
        if spritecollideany(ship, asteroids):
            ship.crash()
        coins_caught = spritecollideany(ship, coins)
        if coins_caught:
            ship.vy *= 1.1
            coins.remove(coins_caught)
    pygame.display.quit()
        


if __name__ == "__main__":
    main()
