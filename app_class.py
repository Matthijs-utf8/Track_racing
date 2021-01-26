import pygame
import sys
from settings import *
from player_class import *
from track_class import *
from finish_line_class import *
from text_class import *
import numpy as np
from map import *
import pickle

# Initialize all pygame modules
pygame.init()

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()


class App:

    def __init__(self):

        # Initialize a window and clock
        self.screen = pygame.display.set_mode((display_width, display_height))
        self.clock = pygame.time.Clock()
        self.dt = clock.tick(FPS)

        # Create a running variable
        self.running = True

        # Load a player instance from the Player class and ad it to the players group
        self.player = Player(start_pos=[start_pos_x, start_pos_y])
        # self.player = pygame.sprite.Group().add(player)

        # Load a box instance from the Player class and ad it to the boxes group
        self.map = Map()
        self.map.add(Track((0, 0)))
        self.finish = Finish(finish_pos)

        self.timer = Timer()

    def run(self):

        pressed_left = pressed_right = pressed_up = pressed_down = None
        finished = False
        cant_cross = False
        start_time = None

        # While the game is running, check the state and update the game according to the current state
        while self.running:

            # Get all the events that happened since the last time pygame.event.get() was called.
            for event in pygame.event.get():

                # If the player presses the cross in the top right corner, quit the game
                if event.type == pygame.QUIT:
                    self.running = False

            # Get a list of all the keys pressed since last time
            keys_pressed = pygame.key.get_pressed()

            # Check if escape is pressed, then exit
            if keys_pressed[pygame.K_ESCAPE]:
                self.running = False

            # Check all the movement keys and change the angular- and linear speed accordingly
            if keys_pressed[pygame.K_a]:
                self.player.angular_velocity -= player_angular_speed
            elif keys_pressed[pygame.K_d]:
                self.player.angular_velocity += player_angular_speed
            if keys_pressed[pygame.K_w]:
                self.player.velocity += player_speed
            elif keys_pressed[pygame.K_s]:
                self.player.velocity -= backwards_driving_speed_penalty * player_speed

            # Draw the background and finish
            self.screen.fill(pacman_blue)

            # Update the sprites
            self.map.update()
            self.timer.update(pygame.time.get_ticks())
            self.player.update()

            # Draw the sprites
            self.map.draw(self.screen)
            self.finish.draw(self.screen)
            self.timer.draw(self.screen)
            self.player.draw(self.screen)

            # Check collisions
            if pygame.sprite.spritecollide(self.player, self.map, False, pygame.sprite.collide_mask):
                self.player.pos = self.player.start_pos
                self.player.velocity = self.player.angular_velocity = self.player.angle = 0
                cant_cross = False
                finished = False
                self.timer.score = None

            #################################### FINISH LINE HANDLING #######################################

            # Check if the car collides with the finish line
            if pygame.sprite.collide_rect(self.player, self.finish):

                # If the car collides, but the center is not over the left side of the finish line yet,
                # then it is allowed to cross (cant_cross = False)
                if self.player.rect.centerx < finish_pos[0]:
                    cant_cross = False

                # If the car is not allowed to cross, break
                if cant_cross:
                    self.player.pos = self.player.start_pos
                    self.player.velocity = self.player.angular_velocity = self.player.angle = 0
                    cant_cross = False
                    finished = False
                    self.timer.score = None

                # Set finished to True
                else:
                    finished = True

            else:

                # If the car and finish dont collide anymore but finished is still set to True,
                if finished:

                    # If the player crossed the finish line from left to right,
                    # we finish and we cant cross again till we race around the track once
                    if self.player.rect.left > (finish_pos[0] + 25):

                        if self.timer.score:

                            self.timer.score = self.timer.time

                            if self.timer.high_score:

                                if self.timer.score < self.timer.high_score:

                                    self.timer.high_score = self.timer.score

                                    with open('highscore.data', 'wb') as filehandle:
                                        # store the data as binary data stream
                                        pickle.dump(self.timer.high_score, filehandle)


                            else:
                                self.timer.high_score = self.timer.score

                        self.timer.start_time = pygame.time.get_ticks()

                        finished = False
                        self.timer.score = True
                        cant_cross = True

            # Flip to the next frame
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()
        sys.exit()