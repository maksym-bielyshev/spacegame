import pygame

# Set the width and height of the screen.
screen_size = [360, 600]

# Create a screen to display a game.
screen = pygame.display.set_mode(screen_size)

# Set the background image.
background = pygame.image.load('background.png')

# Load the planet image.
planet = pygame.image.load('p_one.png')

# Set the default condition for loop.
keep_alive = True

while keep_alive:
    # Set the top side of the image to align with the top of the screen.
    # And the left side of the image aligns with the left side of the screen.
    # (blit - block image transfer)
    screen.blit(background, [0, 0])

    # Display planet image.
    screen.blit(planet, [140, 50])

    # Update the display at each iteration to change image positions.
    pygame.display.update()
