#Building Conways Game of life using visual model
import pygame as py 
import sys

py.init()
c = ('white')
screen = py.display.set_mode((800, 800))
py.display.set_caption("Life Simulation")
running = True


while running: 
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
    #Creating your grids
    for x in range(0, 801, 40): #start - stop - step 
        py.draw.line(screen ,c, (0, x), (800, x), 1 )
        py.draw.line(screen, c,(x,0), (x, 800), 1)
      

    py.display.flip()
    

