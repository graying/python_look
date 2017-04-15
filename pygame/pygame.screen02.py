"""Draw a circle or a rectangle when key pressed"""
import random

import pygame

pygame.init()
screen = pygame.display.set_mode([1440, 900])
screen.fill([0, 0, 0])
draw_command = 1

FPS = 30  # frames per second setting
fpsClock = pygame.time.Clock()

# draw_command = 1 circle, 0 rectangle


def draw_rect(screen):
    rectcolor = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    rectsize = [random.randint(0, 1300), random.randint(0, 900), random.randint(1, 256), random.randint(1, 256)]
    pygame.draw.rect(screen, rectcolor, rectsize, random.randint(0, 5))
    pygame.display.update()
    fpsClock.tick(FPS)


def draw_circle(screen):
    circle_color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    circle_location = [random.randint(0, 1300), random.randint(0, 900)]
    circle_radius = random.randint(5, 256)
    circle_line = random.randint(1, 5)
    pygame.draw.circle(screen, circle_color, circle_location, circle_radius, circle_line)
    pygame.display.update()
    fpsClock.tick(FPS)


def draw_triangle(screen):
    color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
    line_width = random.randint(1, 5)
    point1 = [random.randint(0, 1300), random.randint(0, 900)]
    point2 = [random.randint(0, 1300), random.randint(0, 900)]
    point3 = [random.randint(0, 1300), random.randint(0, 900)]
    pygame.draw.lines(screen, color, True, [point1, point2, point3, point1], line_width)
    pygame.display.update()
    fpsClock.tick(FPS)


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
                        draw_triangle(screen)
                        draw_rect(screen)
                        # draw_rect(screen)

pygame.quit()
