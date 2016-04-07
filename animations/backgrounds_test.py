import unittest
import backgrounds
import pygame
from math import pi,cos
import numpy as np
pygame.init()
X = 800
Y = 600
SIZE=(X,Y)
import time
WAIT=2
SCREEN = None


class Test_backgrounds_test(unittest.TestCase):
    def setUp(self):
        global SCREEN
        SCREEN = pygame.display.set_mode(SIZE)
    def tearDown(self):
        #pygame.display.quit()
        pygame.display.flip()
        time.sleep(WAIT)

    def utest_rect(self):
        bg = backgrounds.squares(SCREEN,SIZE)
        SCREEN.blit(bg,(0,0))

    def utest_rect_color(self):
        bg = backgrounds.squares(SCREEN,SIZE,color_variance=127,color_min = 0, color_max = 255, N=200)
        SCREEN.blit(bg,(0,0))
        
    def utest_clouds(self):
        bg = backgrounds.clouds(SCREEN,SIZE)
        SCREEN.blit(bg,(0,0))
    def utest_cloudscolor(self):
        bg = backgrounds.clouds(SCREEN,SIZE,color_variance=5, color_min=64, color_max = 240)
        SCREEN.blit(bg,(0,0))
    def utest_cloudsbw(self):
        bg = backgrounds.clouds(SCREEN,SIZE, color_min=100, color_max=240, N=400)
        SCREEN.blit(bg,(0,0))
    def utest_starfield(self):
        bg = backgrounds.starfield(SCREEN,SIZE)
        SCREEN.blit(bg,(0,0))
    def test_small_starfield(self):
        clock = pygame.time.Clock()
        FPS=60
        s = backgrounds.Starfield(SCREEN,SIZE,N=10)
        for x in range(400):
            bg = s.render((x*8,0))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            clock.tick(FPS)
        for x in range(400):
            bg = s.render((0,x*8))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            clock.tick(FPS)
        
    def test_moving_starfield(self):
        clock = pygame.time.Clock()
        FPS=60
        s = backgrounds.Starfield(SCREEN,SIZE,N=1000)
        clock.tick()
        for x in range(40):
            bg = s.render((x,0))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            clock.tick(FPS)
        for y in range(40):
            bg = s.render((x,y))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            clock.tick(FPS)
        for x in range(140):
            bg = s.render((30*x,40*x))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            clock.tick(FPS)
        for y in range(1000):
            bg = s.render((30*cos(y/20.0),3*y))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            dt = clock.tick(FPS)
            if ( dt > 1100/FPS):
                print("overload: {} > {}".format(dt, 1100/FPS))
    def test_starfield_speed(self):
        clock = pygame.time.Clock()
        steps=1000
        t = np.zeros(steps)
        s = backgrounds.Starfield(SCREEN,SIZE,N=4000)
        clock.tick()
        for y in range(steps):
            bg = s.render((2*y,y))
            SCREEN.blit(bg,(0,0))
            pygame.display.flip()
            t[y] = clock.tick(0)
        self.assertLess(t.mean(), 10, "mean tick time {} too large".format(t.mean()))




if __name__ == '__main__':
    unittest.main()
