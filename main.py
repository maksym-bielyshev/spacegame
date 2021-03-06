import pygame

# Set the width and height of the screen.
screen_size = [360, 600]

# Create a screen to display a game.
screen = pygame.display.set_mode(screen_size)

# Set the background image.
background = pygame.image.load('background.png')

# Load the spaceship image.
spaceship = pygame.image.load('spaceship.png')

# Load the bullet image.
bullet = pygame.image.load('bullet.png')

# Add bullet_y and fired value.
bullet_y = 500
fired = False

# Add planets list and planet index.
planets = ['p_one.png', 'p_two.png', 'p_three.png']
p_index = 0

# Load the planet image.
planet = pygame.image.load(planets[p_index])

# Add planet_x and move direction.
planet_x = 140
move_direction = 'right'

# Set the default condition for loop.
keep_alive = True

clock = pygame.time.Clock()

while keep_alive:
    # Access keyboard events.
    pygame.event.get()

    # Returns a list of all the keys.
    # The value of every key will be False.
    # Only the button user pressed will be True.
    keys = pygame.key.get_pressed()

    # If the value of the space key is True, the user pressed that keyboard
    # key. It would be False for every other key in the keyboard.
    if keys[pygame.K_SPACE] == True:
        fired = True
        print("Space key pressed")

    if fired is True:
        bullet_y = bullet_y - 5
        if bullet_y == 50:
            fired = False
            bullet_y = 500

    # Set the top side of the image to align with the top of the screen.
    # And the left side of the image aligns with the left side of the screen.
    # (blit - block image transfer)
    screen.blit(background, [0, 0])

    # Display bullet image.
    screen.blit(bullet, [180, bullet_y])

    # Display spaceship image.
    screen.blit(spaceship, [160, 500])

    if move_direction == 'right':
        planet_x = planet_x + 5
        if planet_x == 300:
            move_direction = 'left'
    else:
        planet_x = planet_x - 5
        if planet_x == 0:
            move_direction = 'right'

    # Display planet image.
    screen.blit(planet, [planet_x, 50])

    # React to a bullet and a planet collision.
    if bullet_y < 80 and planet_x > 120 and planet_x < 180:
        p_index = p_index + 1
        if p_index < len(planets):
            planet = pygame.image.load(planets[p_index])
            planet_x = 10
        else:
            print('YOU WIN')
            keep_alive = False
        print('BOOM')

    # Update the display at each iteration to change image positions.
    pygame.display.update()

    # Set 60 frames per second.
    clock.tick(60)
