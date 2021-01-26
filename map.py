import pygame
import sys
from settings import *
from player_class import *
from track_class import *
import numpy as np


class Map(pygame.sprite.Group):

    def __init__(self):
        super().__init__()

    def draw(self, surface):

        sprites = self.sprites()
        surface_blit = surface.blit
        for spr in sprites:
            self.spritedict[spr] = surface_blit(spr.image, spr.rect)

    def update(self, *args):

        for s in self.sprites():
            s.update(*args)

# width_pixels = range(0, display_width, box_spacing)
# height_pixels = range(0, display_height, box_spacing)
# boxes_x, boxes_y = int(display_width / box_spacing + 1), int(display_height / box_spacing + 1)
# grd = np.array(np.meshgrid(width_pixels, height_pixels, indexing="xy"))

# for x in range(boxes_x):
#     for y in range(boxes_y):
#         self.map.add(Box(grd[:, y, x]))
