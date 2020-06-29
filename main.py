import pygame

# Set the width and height of the screen.
screen_size = [360, 600]

# Create a screen to display a game.
screen = pygame.display.set_mode(screen_size)

# Set the background image.
background = pygame.image.load('background.png')

# Set the top side of the image to align with the top of the screen.
# And the left side of the image aligns with the left side of the screen.
# (blit - block image transfer)
screen.blit(background, [0, 0])
