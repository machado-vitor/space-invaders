import pygame, sys
pygame.init()

screen = pygame.display.set_mode((640, 480))
clock  = pygame.time.Clock()

# Create an off‑screen surface (50×50) once, then convert it for fast blits
box = pygame.Surface((50, 50)).convert()
box.fill("gold")
box_rect = box.get_rect(center=(320, 240))
speed = pygame.Vector2(120, 90)    # px per second

while True:
    dt = clock.tick(60) / 1000     # seconds since last frame
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    box_rect.move_ip(speed * dt)
    if not screen.get_rect().contains(box_rect):
        speed *= -1                # simple bounce

    screen.fill("black")
    screen.blit(box, box_rect)
    pygame.display.flip()
