import pygame


class Display:
    def format(size=(800, 600)):
        screen = pygame.display.set_mode((size[0], size[1]))
        return screen

    def set_name(name):
        pygame.display.set_caption(name)

    def frame_clock(frame_speed):

        ...
