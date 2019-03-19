import pygame, random
from pygame.locals import *


def rand_apple_pos(snake):
    
    apple_list = []

    good_apple = True

    i = len(snake)

    while good_apple:
        apple = (
            random.randrange(start=10, stop=590, step=10),
            random.randrange(start=10, stop=590, step=10),
        )

        for part in range(1, len(snake)):
            if part == apple:
                apple_list.append(part == apple)
            else:
                apple_list.append(part == apple)
        good_apple_set = set(apple_list)

        if len(good_apple_set) == 1:
            if good_apple_set == {False}:
                good_apple = False
        #import ipdb; ipdb.set_trace()
        

    return apple


def apple_style():
    apple_skin = pygame.Surface((10, 10))
    apple_skin.fill((0, 250, 0))
    return apple_skin


def apple_collision(snake, apple):

    if snake[0] == apple:
        snake.append(apple)
        apple = rand_apple_pos(snake)
    return apple
    ...
