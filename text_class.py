import pygame
import random
import os
import numpy as np
from helper_functions import *
from settings import *
import pickle

class Timer:

    def __init__(self):

        self.font = pygame.font.SysFont(opening_screen_font_name, opening_screen_text_size)
        self.text_color = pacman_orange
        self.start_time = 0
        self.time = self.start_time
        self.message = "Time: {}".format((self.time / 1000))
        self.pos = (20, 10)
        self.running = False

        with open('highscore.data', 'rb') as filehandle:
            # read the data as binary data stream
            self.high_score = pickle.load(filehandle)

        self.score = None

        pass

    def draw(self, surface):

        surface.blit(self.font.render(self.message, True, self.text_color), self.pos)

    def update(self, time):

        if self.score:
            self.time = time - self.start_time
            if self.high_score:
                self.message = "Time: {}\nBest time: {}".format((self.time / 1000), self.high_score/1000)
            else:
                self.message = "Time: {}".format((self.time / 1000))
            self.running = True
