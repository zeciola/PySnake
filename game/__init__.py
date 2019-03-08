import pygame
from pygame.locals import *
#from game.display import display_format
from game.snake import rand_snake_start_location as rand_snake
from game.snake import snake_style

screen = pygame.display.set_mode((800,600))
pygame.display.set_caption('PySnake')

snake = rand_snake()
snake_skin = snake_style()

def run_time_game():
    try:
        pygame.init()
    except Exception as e:
        print('Há algo de errado com o pygame')
        exit()

    while True:

        for event in pygame.event.get():

            if event.type == QUIT:
                pygame.quit()
                exit()

        pygame.display.update()

        screen.fill((0,0,0))

        for pos in snake:
            screen.blit(snake_skin, pos)