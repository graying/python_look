import pygame
import time
import random

pygame.init()
screen = pygame.display.set_mode([1440, 900])
screen.fill([2,255,2])

rectcolor = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
rectsize = [random.randint(0,1000), random.randint(0,900), random.randint(0,256), random.randint(0, 256)]
pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0,5))
pygame.display.flip()

for i in range(100):
    rectcolor = [random.randint(0,255), random.randint(0,255), random.randint(0, 255)]
    rectsize = [random.randint(0,1000), random.randint(0,900), random.randint(0,256), random.randint(0, 256)]
    pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0,5))
    pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False

pygame.quit()
