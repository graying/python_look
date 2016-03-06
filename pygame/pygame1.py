import pygame, sys
from pygame.locals import *

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE = (  0,   0, 255)


pygame.init()
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('Hello World!')
DISPLAYSURF.fill(GREEN)
while True: # main game loop
    for event in pygame.event.get():
        if event.type == QUIT:
             pygame.quit()
             sys.exit()
        pygame.display.update()
