import pygame


class Display:
    def format(xy=(800, 600)):
        screen = pygame.display.set_mode((xy[0], xy[1]))
        return screen

    def set_name(name):
        pygame.display.set_caption(name)

    def frame_clock(frame_speed):

        ...
