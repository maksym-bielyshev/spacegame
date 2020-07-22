import pygame

# Set the width and height of the screen.
screen_size = [360, 600]

# Create a screen to display a game.
screen = pygame.display.set_mode(screen_size)

# Set the background image.
background = pygame.image.load('background.png')

# Load the planet image.
planet = pygame.image.load('p_one.png')

# Load the spaceship image.
spaceship = pygame.image.load('spaceship.png')

# Load the bullet image.
bullet = pygame.image.load('bullet.png')

# Set the default condition for loop.
keep_alive = True

while keep_alive:
    # Access keyboard events.
    pygame.event.get()

    # Returns a list of all the keys.
    # The value of every key will be False.
    # Only the button user pressed will be True.
    keys = pygame.key.get_pressed()

    # Set the top side of the image to align with the top of the screen.
    # And the left side of the image aligns with the left side of the screen.
    # (blit - block image transfer)
    screen.blit(background, [0, 0])

    # Display planet image.
    screen.blit(planet, [140, 50])

    # Display bullet image.
    screen.blit(bullet, [180, 500])

    # Display spaceship image.
    screen.blit(spaceship, [160, 500])

    # Update the display at each iteration to change image positions.
    pygame.display.update()
