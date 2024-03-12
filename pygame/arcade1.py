import pygame
import numpy
pygame.init()

# Define colors and constants
BLACK    = (   0,   0,   0)
WHITE    = ( 255, 255, 255)
GREEN    = (   0, 255,   0)
RED      = ( 255,   0,   0)
BLUE     = (   0,   0, 255)
PI = numpy.pi

# Opening and setting the window size
size = (700, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Arcade Game lol")

# Loop until the user clicks close
done = False

# How fast the screen updates
clock = pygame.time.Clock()

# Main Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            print("Pressed a key")
        elif event.type == pygame.KEYUP:
            print("Oh?")
    # Game logic

    # Drawing code

    # Draw program
    screen.fill(WHITE)
    pygame.display.flip()

    # Limit to 60 fps
    clock.tick(60)

pygame.quit()
