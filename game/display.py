import pygame

class Display():

    def format(x,y):
        screen = pygame.display.set_mode((x, y))
        return screen

    def set_name(name):
        pygame.display.set_caption(name)

    def frame_clock(frame_speed):

        ...