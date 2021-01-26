import pygame
import os

def load_image(filename, use_color_key=False):

    # Check if the path exists
    if os.path.isfile(filename):

        # Load the image and convert to alpha
        image = pygame.image.load(filename)
        image = image.convert_alpha()

        # Return the image
        return image

    # Else, raise an error
    else:
        raise Exception("Error loading image: {} - Check filename and path?".format(filename))
