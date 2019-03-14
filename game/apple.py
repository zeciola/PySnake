import pygame, random
from pygame.locals import *


def rand_apple_pos():
    apple = (
        random.randrange(start=10, stop=590, step=10),
        random.randrange(start=10, stop=590, step=10),
    )
    return apple


def apple_style():
    apple_skin = pygame.Surface((10, 10))
    apple_skin.fill((0, 250, 0))
    return apple_skin


def apple_collision(snake, apple):

    if snake[0] == apple:
        snake.append(apple)
        apple = rand_apple_pos()
    return apple
    ...
