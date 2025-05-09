import pygame, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()
# Blit (Block Image Transfer)
# Create an off‑screen surface (50×50) once, then convert it for fast blits
box = pygame.Surface((50, 50)).convert() # the gold square
box.fill("gold")
box_rect = box.get_rect(center=(320, 240))
speed = pygame.Vector2(120, 90)    # px per second
# The box will move 120 px per second on x-axis
# and 90 px per second on y-axis

while True:
    # tick limits the frame rate to 60 FPS, and returns in milliseconds
    dt = clock.tick(60) / 1000     # seconds since last frame
    for e in pygame.event.get(): # Get all events from the event queue.
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    box_rect.move_ip(speed * dt)   # move the box, ip stands for in place
    if not screen.get_rect().contains(box_rect):
        speed *= -1                # simple bounce

    screen.fill("black")
    screen.blit(box, box_rect) # Blit the box on the screen
    # it takes the source surface and the destination rectangle
    pygame.display.flip()
