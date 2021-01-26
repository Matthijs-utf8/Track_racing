import pygame
from helper_functions import *
import os
import math
import numpy as np
from settings import *


# A class for everything that the player does
class Player(pygame.sprite.Sprite):

    def __init__(self, start_pos, velocity=0, start_dir=[1, 0]):

        # Run the init from pygame.sprite.Sprite
        super().__init__()

        # Initialize state of the sprite
        self.start_pos = start_pos
        self.pos = pygame.math.Vector2(self.start_pos)
        self.movement = [0, 0]
        self.velocity = velocity
        self.angular_velocity = 0
        radius, self.angle = pygame.math.Vector2(start_dir).normalize().as_polar()

        # Load the image and get it's rectangle
        self.orig_image = pygame.transform.scale(load_image(os.getcwd() + "\\formula_one_car.png"), player_size)
        self.image = self.orig_image.copy()
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = start_pos

    # Add this draw function so we can draw individual sprites
    def draw(self, screen):
        screen.blit(self.image, self.rect)


    # Update the state of the sprite
    def update(self):

        # Update the position, angle and velocities of the sprite
        self.rotate()
        self.move()
        self.decay()

    def rotate(self):

        # Rotate the image and it's rectangle
        self.image = pygame.transform.rotate(self.orig_image, -self.angle)
        self.rect = self.image.get_rect(center=self.rect.midtop)

    def move(self):

        # Update the position of the sprite according to the velocity and it's angle
        self.movement = self.velocity * pygame.math.Vector2([np.cos(np.deg2rad(self.angle)),
                                                             np.sin(np.deg2rad(self.angle))]).normalize()
        self.pos += self.movement

        # Update the angle of the sprite according to it's angular velocity
        self.angle += self.angular_velocity

        # Update the rectangle
        self.rect.center = round(self.pos.x), round(self.pos.y)

    def decay(self):

        # Calculate the decayed velocities and update the current velocities
        if self.velocity > 0:
            self.velocity = min(self.velocity, top_speed) * speed_decay
        elif self.velocity < 0:
            self.velocity = max(self.velocity, -top_speed) * speed_decay
        if self.angular_velocity > 0:
            self.angular_velocity = min(self.angular_velocity, 10) * angular_speed_decay
        elif self.angular_velocity < 0:
            self.angular_velocity = max(self.angular_velocity, -10) * angular_speed_decay


