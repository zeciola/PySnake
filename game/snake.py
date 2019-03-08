import pygame , random
from pygame.locals import *

def snake_style():
    snake_skin = pygame.Surface((10,10))
    snake_skin.fill((255,255,255))
    return snake_skin

def rand_snake_start_location(lifes=3):
    snake = [(random.randrange(start=10, stop=590, step=10),random.randrange(start=10, stop=590, step=10))]

    for life in range(0, lifes - 1):

        snake.append((snake[life][0] + 10,snake[0][1]))

    return snake