import sys
import pygame
import math

class Invader:
    def __init__(self, x, y):
        self.image = pygame.image.load("alien1.png").convert_alpha()
        self.rect = self.image.get_rect(topleft=(x, y))

class Player:
    def __init__(self, screen, y):
        self.image = pygame.image.load("spaceship.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = (screen.get_width() - self.rect.width) // 2
        self.rect.y = y
        self.speed = 5
        self.bullets = []
        self.bullet_speed = 10

class InvaderGroup:
    def __init__(self, screen, rows, cols):
        self.invaders = []
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 5      # Horizontal movement speed
        self.drop_speed = 30  # Vertical drop amount
        self.move_time = 50  # Frames between horizontal movements
        self.current_move_time = 0
        self.drop_time = 360  # Frames between periodic drops
        self.current_drop_time = 0

        # Create the invaders grid
        self._create_invaders(screen, rows, cols)

    def _create_invaders(self, screen, rows, cols):
        screen_width = screen.get_width()
        screen_height = screen.get_height()

        invader = pygame.image.load("alien1.png").convert_alpha()
        invader_width = invader.get_width()
        invader_height = invader.get_height()

        # Calculate spacing with margins
        horizontal_margin = screen_width * 0.15
        top_margin = screen_height * 0.10
        available_width = screen_width - (2 * horizontal_margin)
        x_spacing = available_width / cols
        y_spacing = invader_height * 1.5

        # Create invaders
        for row in range(rows):
            row_invaders = []
            for col in range(cols):
                x = horizontal_margin + col * x_spacing
                y = top_margin + row * y_spacing
                invader = Invader(x, y)
                invader.row = row  # Store row information
                self.invaders.append(invader)
                row_invaders.append(invader)

    def update(self, screen):
        # Check if it's time to move
        self.current_move_time += 1
        if self.current_move_time >= self.move_time:
            self.current_move_time = 0

            # Check for edges
            screen_width = screen.get_width()

            # Find leftmost and rightmost invaders
            min_x = float('inf')
            max_x = float('-inf')
            for invader in self.invaders:
                if invader.rect.left < min_x:
                    min_x = invader.rect.left
                if invader.rect.right > max_x:
                    max_x = invader.rect.right

            # Move invaders horizontally based on row (even/odd)
            for invader in self.invaders:
                if invader.row % 2 == 0:  # Even rows
                    invader.rect.x += self.speed * self.direction
                else:  # Odd rows
                    invader.rect.x += self.speed * -self.direction

        # Periodic drop check
        self.current_drop_time += 1
        if self.current_drop_time >= self.drop_time:
            self.current_drop_time = 0
            self.direction *= -1
            for invader in self.invaders:
                invader.rect.y += self.drop_speed

    def draw(self, screen):
        for invader in self.invaders:
            screen.blit(invader.image, invader.rect)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")

    clock = pygame.time.Clock()

    player = Player(screen, 500)
    invader_group = InvaderGroup(screen, rows=5, cols=10)

    running = True
    while running:
        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Update invaders
        invader_group.update(screen)

        # Draw player and invaders
        screen.blit(player.image, player.rect)
        invader_group.draw(screen)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
