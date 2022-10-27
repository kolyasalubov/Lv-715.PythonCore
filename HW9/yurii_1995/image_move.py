# homework #9 - practice with pygame library

import pygame

# Define some colors
WHITE = (255, 255, 255)
BROWN = (102, 51, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()

# Create a 800x600 sized screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])

# This sets the name of the window
pygame.display.set_caption('Bird Fly')

# Load and set up graphics
bird_start_position = pygame.image.load("bird_start:end.png").convert()
bird_fly1 = pygame.image.load("bird_fly1.png").convert()
bird_fly2 = pygame.image.load("bird_fly2.png").convert()
bird_fly3 = pygame.image.load("bird_fly3.png").convert()

# Change the sizes of the images
bird_start_position = pygame.transform.scale(bird_start_position, (90, 70))
bird_fly1 = pygame.transform.scale(bird_fly1, (110, 130))
bird_fly2 = pygame.transform.scale(bird_fly2, (100, 120))
bird_fly3 = pygame.transform.scale(bird_fly3, (100, 120))

# Additional parameters
done = False
bird_step = 2
bird_fly_point = 90
bird_fly_height = 2

line_x = (0, screen_height - 50)
line_y = (screen_width, screen_height - 50)
line_size = 10

# Additional bird's parameters
bird_start_position_x = 5
bird_start_position_y = 475

bird_fly1_x = 220
bird_fly1_y = bird_start_position_y - bird_fly_point

bird_fly2_x = 420
bird_fly2_y = bird_fly1_y - (bird_fly_point * 2)

bird_fly3_x = 540
bird_fly3_y = bird_fly2_y - (bird_fly_point * 2)

while not done:
    pygame.time.delay(20)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(WHITE)

    # Copy image to screen and draw a line
    line = pygame.draw.line(screen, BROWN, line_x, line_y, line_size)
    screen.blit(bird_start_position, (bird_start_position_x, bird_start_position_y))

    if bird_start_position_x <= 200:
        bird_start_position_x += bird_step
    if bird_start_position_x >= 200:
        bird_start_position.fill(WHITE)
        screen.blit(bird_fly1, (bird_fly1_x, bird_fly1_y))
        bird_fly1_x += bird_step
        bird_fly1_y -= bird_fly_height
        line_x = (0, screen_height)
    if bird_fly1_y <= 250:
        bird_fly1.fill(WHITE)
        screen.blit(bird_fly2, (bird_fly2_x, bird_fly2_y))
        bird_fly2_x += bird_step
        bird_fly2_y -= bird_fly_height
    if bird_fly2_y <= 120:
        bird_fly2.fill(WHITE)
        screen.blit(bird_fly3, (bird_fly3_x, bird_fly3_y))
        bird_fly3_x += bird_step
        bird_fly3_y -= bird_fly_height
    if bird_fly3_y <= 0:
        bird_fly3_x += bird_step
        bird_fly3_y += bird_fly_height

    # update the screen
    pygame.display.flip()

pygame.quit()
