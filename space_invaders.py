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

    def setup(self, screen):
        self.rect.x = (screen.get_width() - self.rect.width) // 2
        self.rect.y = screen.get_height() - self.rect.height - 10

class InvaderGroup:
    def __init__(self):
        self.invaders = []
        self.direction = 1  # 1 for right, -1 for left
        self.speed = 5      # Horizontal movement speed
        self.drop_speed = 3  # Vertical drop amount
        self.move_time = 30  # Frames between horizontal movements
        self.current_move_time = 0
        self.drop_time = 360  # Frames between periodic drops
        self.current_drop_time = 0

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

    def update(self, screen):
        # Check if it's time to move
        self.current_move_time += 1
        if self.current_move_time >= self.move_time:
            self.current_move_time = 0

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
