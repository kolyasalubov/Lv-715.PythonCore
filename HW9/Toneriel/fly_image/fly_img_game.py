import pygame
import os

# Get the current working directory

cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create an 800x800 sized screen
screen = pygame.display.set_mode([WINDOW_HEIGHT, WINDOW_WIDTH])

# This sets the name of the window
pygame.display.set_caption('Fly')

clock = pygame.time.Clock()

# Restore the screen
pygame.display.update()

# Set positions of graphics
background_position = [0, 0]

# Load and set up graphics.
background_image = pygame.image.load("fly_image/cheese.png").convert()
player_image = pygame.image.load('fly_image/tiny_mouse.jpg').convert_alpha()
# Set player image size
player_image = pygame.transform.smoothscale(player_image, (150, 150))
player_image.set_colorkey(WHITE)

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.blit(background_image, (0, 0))


# Get the current mouse position. This returns the position
# as a list of two numbers.
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]

    # Copy image to screen:
    screen.blit(player_image, [x, y])

    pygame.display.flip()

    clock.tick(60)
    # Check player is on-screen


screen.blit(background_image, (0, 0))
screen.blit(player_image, (x, y))


# Restore the screen

pygame.quit()
