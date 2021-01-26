import pygame
import random
import os
import numpy as np
from helper_functions import *
from settings import *

class Track(pygame.sprite.Sprite):

    def __init__(self, pos):

        # Run the init from pygame.sprite.Sprite
        super().__init__()

        self.start_pos = pos

        # Get a random crate size
        self.size = np.random.randint(75, 150)

        # Load the image and get it's rectangle
        self.image = pygame.transform.scale(load_image(os.getcwd() + "\\track2.jpg"), (display_width, display_height))
        self.mask = pygame.mask.from_threshold(self.image, (0, 0, 0), (1, 1, 1, 255))
        # self.mask = pygame.mask.from_threshold(self.image, (109, 110, 113), (1, 1, 1, 255))
        self.rect = self.image.get_rect()

    # Add this draw function so we can draw individual sprites
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass


class Finish(pygame.sprite.Sprite):

    def __init__(self, pos):

        # Run the init from pygame.sprite.Sprite
        super().__init__()

        self.start_pos = pos

        # Load the image and get it's rectangle
        self.image = pygame.transform.scale(load_image(os.getcwd() + "\\finish_line.png"), (20, 78))
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.midleft = pos

    # Add this draw function so we can draw individual sprites
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass