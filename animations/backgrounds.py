from pygame import Surface, draw,gfxdraw
import numpy as np
import numpy.random as random
from colors  import color



def squares(screen, SIZE, color_variance = 0, color_min = 0, color_max = 127, N=100):
    bg = Surface(SIZE)
    for i in range(100):
        (X,Y) = SIZE
        r = random.normal(size=4).reshape((2,2))
        SIZE_2 = np.array(SIZE) / 2
        r *= SIZE_2 
        r += SIZE_2
         
        r = r.T.astype(int)
        col = np.ones(3,float) * random.randint(color_min,color_max) # gray
        if color_variance:
            col += random.normal(0,color_variance, size=3)
        col = col.astype(int)
        col[col>color_max] = color_max  
        col[col<color_min] = color_min

        dr = draw.rect(bg,col, r.T.astype(int)) 
    return bg


def clouds(screen, SIZE, color_variance = 0, color_min = 0, color_max = 127, N=100):
    bg = Surface(SIZE)
    bg.fill(color("MidnightBlue"))
    (X,Y) = SIZE

    for i in range(N):
        center = random.random(size=2)
        center *= SIZE 
        center = center.astype(int)      

        r = int(random.random()*min(SIZE)/10)

        col = np.ones(3,float) * random.randint(color_min,color_max) # gray
        if color_variance:
            col += random.normal(0,color_variance, size=3)
        col[col>color_max] = color_max  
        col[col<color_min] = color_min
        col = col.astype(int)
        dr = draw.circle(bg,col,center, r) 
    return bg

def starfield(screen,SIZE,N=600, color_min=127,color_max=255):
    bg = Surface(SIZE)
    bg.fill(color("MidnightBlue"))
    for i in range(N):
        center = random.random(size=2)
        center *= SIZE 
        center = center.astype(int)      
        col = np.ones(3,int) * random.randint(color_min,color_max) # gray
        (x,y)=center
        dr = gfxdraw.pixel(bg,x,y,col) 
    return bg
        
    
class Starfield():
    def __init__(self,screen,SIZE,N=600,color_min=127, color_max = 255):
        stars = random.random(N*4).reshape((N,4))
        stars[:,3]*=(color_max - color_min)
        stars[:,3]+= color_min
        stars[:,2] **= 2 # make positive
        stars[:,(0,1)] *= SIZE
        self.N = N
        self.SIZE = SIZE
        self.stars = stars
        self.bg = Surface(self.SIZE) 
        self.colors = (stars[:,3] * np.ones((N,3),int).T).T.astype(int)
        


    def render(self,coords):
        self.bg.fill(color("MidnightBlue"))
        c = np.array(coords)
        v = np.zeros((self.N,2)) + c
        
        v = (v.T * self.stars[:,2]).T
        xy = ((self.stars[:,(0,1)] + v) % self.SIZE).astype(int)
        for i in range(self.N):
            (x,y) = xy[i]
            dr = gfxdraw.pixel(self.bg,x,y,self.colors[i]) 
        return self.bg
            
            
            
