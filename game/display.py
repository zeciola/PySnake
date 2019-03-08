import pygame

class Display():

    def format(X,Y):
        screen = pygame.display.set_mode((800, 600))
        return screen

    def set_name(name):
        pygame.display.set_caption(name)

    def frame_clock(frame_speed):

        ...