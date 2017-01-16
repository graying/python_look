"""Draw a circle or a rectangle when key pressed"""
import random

import pygame

pygame.init()
screen = pygame.display.set_mode([1440, 900])
screen.fill([0, 0, 0])
draw_command = 1


# draw_command = 1 circle, 0 rectangle


def draw_rect(screen):
    rectcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    rectsize = [random.randint(0, 1300), random.randint(0, 900), random.randint(1, 256), random.randint(1, 256)]
    pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0, 5))
    pygame.display.update()


def draw_circle(screen):
    circle_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle_location = [random.randint(0, 1300), random.randint(0, 900)]
    circle_radius = random.randint(5, 256)
    circle_line = random.randint(1, 5)
    pygame.draw.circle(screen, circle_color, circle_location, circle_radius, circle_line)
    pygame.display.update()


for i in range(1):
    draw_rect(screen)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                screen.fill([0, 0, 0])
                pygame.display.update()
            elif event.key == pygame.K_RETURN:
                if draw_command == 1:
                    draw_command = 0
                else:
                    draw_command = 1
            else:
                for i in range(1):
                    if draw_command == 1:
                        draw_circle(screen)
                    else:
                        draw_rect(screen)
                    # draw_rect(screen)

pygame.quit()
