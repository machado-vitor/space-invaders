import pygame, sys; pygame.init()
screen = pygame.display.set_mode((300, 200))
clock  = pygame.time.Clock()
font   = pygame.font.SysFont(None, 48)

while True:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            print("SPACE via event queue")

    keys = pygame.key.get_pressed()
    text = "←→ wasd pressed" if keys[pygame.K_a] else ""
    screen.fill("gray15")
    screen.blit(font.render(text, True, "white"), (10, 80))
    pygame.display.flip()
    clock.tick(60)
