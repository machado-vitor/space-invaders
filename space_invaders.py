import sys

import pygame


class Invader:
    def __init__(self, x, y):
        self.image = pygame.image.load("alien1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

class Player:
    def __init__(self):
        self.image = pygame.image.load("spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.speed = 5
        self.bullets = []
        self.bullet_speed = 10
        self.life = 100
        self.bullet_cooldown = 15  # Frames between shots
        self.cooldown_timer = 0    # Current cooldown timer

    def setup(self, screen):
        self.rect.x = (screen.get_width() - self.rect.width) // 2
        self.rect.y = screen.get_height() - self.rect.height - 10

    def update(self, screen):
        # Handle player movement with keyboard
        keys = pygame.key.get_pressed()

        # Move left with left arrow or A key
        if (keys[pygame.K_LEFT] or keys[pygame.K_a]) and self.rect.left > 0:
            self.rect.x -= self.speed

        # Move right with right arrow or D key
        if (keys[pygame.K_RIGHT] or keys[pygame.K_d]) and self.rect.right < screen.get_width():
            self.rect.x += self.speed

        # Handle bullet cooldown
        if self.cooldown_timer > 0:
            self.cooldown_timer -= 1

        # Fire bullet with spacebar
        if keys[pygame.K_SPACE] and self.cooldown_timer == 0:
            self.shoot()
            self.cooldown_timer = self.bullet_cooldown

        # Update bullets
        for bullet in self.bullets[:]:
            bullet.y -= self.bullet_speed
            if bullet.y < 0:  # Remove bullet if it goes off screen
                self.bullets.remove(bullet)

    def shoot(self):
        # Create a bullet (simple rect) at the player's position
        bullet = pygame.Rect(
            self.rect.centerx - 2,  # Center the bullet on the ship
            self.rect.top,          # Start at the top of the ship
            4,                      # Bullet width
            10                      # Bullet height
        )
        self.bullets.append(bullet)

    def draw(self, screen):
        # Draw the player
        screen.blit(self.image, self.rect)

        # Draw bullets
        for bullet in self.bullets:
            pygame.draw.rect(screen, (255, 255, 255), bullet)

class InvaderGroup:
    def __init__(self):
        self.invaders = []
        self.movement_direction = 1  # 1 for right, -1 for left
        self.horizontal_step = 5      # Horizontal movement speed
        self.vertical_step = 3  # Vertical drop amount
        self.movement_interval = 30  # Frames between horizontal movements
        self.movement_timer = 0
        self.drop_interval = 360  # Frames between periodic drops
        self.drop_timer = 0

    def setup(self, screen, rows, cols):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        invader = pygame.image.load("alien1.png").convert_alpha()
        invader_height = invader.get_height()

        # Calculate spacing with margins
        horizontal_margin = screen_width * 0.15 # 15% of margin on each side
        top_margin = screen_height * 0.10 # 10% of margin on top
        available_width = screen_width - (2 * horizontal_margin) # The width left after subtracting the left and right margins.
        x_spacing = available_width / cols # Divide the available width by the number of columns.
        y_spacing = invader_height * 1.5 # Prevent overlap by multiplying the height of the invader by 1.5.

        # Create invaders
        for row in range(rows):
            for col in range(cols):
                x = horizontal_margin + col * x_spacing
                y = top_margin + row * y_spacing
                invader = Invader(x, y)
                invader.row = row  # Store row information
                self.invaders.append(invader)

    def update(self):
        # Check if it's time to move
        self.movement_timer += 1
        if self.movement_timer >= self.movement_interval:
            self.movement_timer = 0

            # Move invaders horizontally based on row (even/odd)
            for invader in self.invaders:
                if invader.row % 2 == 0:  # Even rows
                    invader.rect.x += self.horizontal_step * self.movement_direction
                else:  # Odd rows
                    invader.rect.x += self.horizontal_step * -self.movement_direction

        # Periodic drop check
        self.drop_timer += 1
        if self.drop_timer >= self.drop_interval:
            self.drop_timer = 0
            self.movement_direction *= -1 # change the direction when dropping
            for invader in self.invaders:
                invader.rect.y += self.vertical_step


    def draw(self, screen):
        for invader in self.invaders:
            screen.blit(invader.image, invader.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()

    player = Player()
    player.setup(screen)
    invader_group = InvaderGroup()
    invader_group.setup(screen, rows=5, cols=10)

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update player (movement and shooting)
        player.update(screen)

        # Update invaders
        invader_group.update()

        # Draw player and invaders
        player.draw(screen)
        invader_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

