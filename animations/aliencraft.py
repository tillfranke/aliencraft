import pygame
from colors import color
from backgrounds import Starfield
from aliencraft.ship import Ship
from pygame.sprite import RenderUpdates

import time

X=800
Y=600
SIZE=(X,Y)
CLOCK = None
SCREEN = None

FPS=30




        
def main():
    pygame.init()
    global SCREEN
    #SCREEN = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
    #SIZE=pygame.display.get_surface().get_size()
    SCREEN = pygame.display.set_mode(SIZE)
    background = Starfield(SCREEN,SIZE)
    ship = Ship(SIZE)
    player = RenderUpdates(ship)
    # asteroids = RenderUpdates(rocks)
    # aliens = RenderUpdates(coins)
    CLOCK = pygame.time.Clock()
    pygame.key.set_repeat(10,10)
    y = 0

    running = True
    while running:
        for e in  pygame.event.get():
                if e.type == pygame.KEYDOWN:
                    if e.key == pygame.K_ESCAPE:
                        running = False
                ship.handle_events(e)
        y += ship.vy
        SCREEN.blit(background.render((0,y)),(0,0))
        player.update()
        # asteroids.update()
        # aliens.update()
        player.draw(SCREEN)
        # asteroids.draw(SCREEN)
        # aliens.draw(SCREEN)
        pygame.display.flip()
        dt = CLOCK.tick(FPS)
    pygame.display.quit()
        


if __name__ == "__main__":
    main()
