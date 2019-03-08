import pygame , random
from pygame.locals import *

def snake_style():
    skin = pygame.Surface((10,10))
    skin.fill((255,255,255))
    return skin

def rand_snake_start_location(lifes=3):
    snake = [(random.randrange(start = 10, stop = 590),random.randrange(start = 10, stop = 590))]

    for life in range(0, lifes - 1):

        snake.append((snake[life][0] + 10,snake[0][1]))

    return snake