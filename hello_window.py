# hello_window.py
import pygame, sys
pygame.init() # Initialize all imported pygame modules

SCREEN_W, SCREEN_H = 1280, 800
screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock  = pygame.time.Clock()       # FPS limiter

while True:
    # Process player inputs.
    for event in pygame.event.get(): # Get all events from the event queue.
        if event.type == pygame.QUIT: # if the windows close button is pressed
            pygame.quit(); sys.exit()

    # Do logical updates here.
    # ...
    screen.fill("purple") # Fill the display with a solid color
    pygame.display.flip() # Refresh on-screen display
    clock.tick(60) # wait until next frame (at 60 FPS)
