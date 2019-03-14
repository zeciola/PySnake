import pygame
from pygame.locals import *
from game.snake import rand_snake_start_location as rand_snake
from game.snake import snake_style, snake_collision
from game.apple import rand_apple_pos, apple_style, apple_collision
from game.display import Display

UP = 0
DOWN = 1
RIGHT = 2
LEFT = 3


def edge_game(snake, display_sise):

    print(f"x:{snake[0][0]} y:{snake[0][1]}")

    if snake[0][0] < 0:
        print("borda esquerda")
        snake[0] = (display_sise[0] - 10, snake[0][1])

    if snake[0][1] < 0:
        print("borda topo")
        snake[0] = (snake[0][0], display_sise[1] - 10)

    if snake[0][0] >= display_sise[0]:
        print("borda direita")
        snake[0] = (0, snake[0][1])

    if snake[0][1] >= display_sise[1]:
        print("borda baixo")
        snake[0] = (snake[0][0], 0)

    return snake


def controls(snake, snake_direction=LEFT):
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:

            if event.key == K_ESCAPE:
                pygame.quit()
                exit()

            if event.key == K_UP and not snake_direction == DOWN:
                snake_direction = UP
            if event.key == K_DOWN and not snake_direction == UP:
                snake_direction = DOWN
            if event.key == K_RIGHT and not snake_direction == LEFT:
                snake_direction = RIGHT
            if event.key == K_LEFT and not snake_direction == RIGHT:
                snake_direction = LEFT

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i - 1][0], snake[i - 1][1])

    if snake_direction == UP:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if snake_direction == DOWN:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if snake_direction == RIGHT:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if snake_direction == LEFT:
        snake[0] = (snake[0][0] - 10, snake[0][1])

    return snake, snake_direction
    ...


def run_time_game():

    display_sise = (800, 600)

    screen = Display.format(display_sise)
    pygame.display.set_caption("PySnake")
    clock = pygame.time.Clock()

    snake = rand_snake(lifes=5)
    snake_skin = snake_style()
    snake_direction = LEFT

    apple = rand_apple_pos()
    apple_skin = apple_style()

    try:
        pygame.init()
    except Exception as e:
        print("Há algo de errado com o pygame! \n", e)
        exit()

    while True:

        # dificuldade
        clock.tick(10)

        apple = apple_collision(snake, apple)

        # controles

        snake = edge_game(snake, display_sise)

        snake, snake_direction = controls(snake, snake_direction)

        snake_collision(snake)

        screen.fill((0, 0, 0))

        screen.blit(apple_skin, apple)

        for pos in snake:
            screen.blit(snake_skin, pos)

        pygame.display.update()
