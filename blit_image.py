import pygame, sys, pathlib; pygame.init()
screen = pygame.display.set_mode((512, 512))
clock  = pygame.time.Clock()

img = pygame.image.load(pathlib.Path(__file__).with_name("ship.png")).convert()
# img.set_colorkey((0, 0, 0))        # treat pure black as transparent
rect = img.get_rect(center=(256, 256))

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
    screen.fill("navy")
    screen.blit(img, rect)
    pygame.display.flip()
    clock.tick(60)
