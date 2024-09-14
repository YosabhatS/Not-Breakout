from setting import *

class Paddle:
    def __init__(self):
        self.reset()  # Initialize with default values

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= PADDLE_SPEED
        elif direction == 'right':
            self.rect.x += PADDLE_SPEED

        # Ensure paddle stays within the screen boundaries
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        pygame.draw.rect(screen, BLUE, self.rect)

    def enlarge(self):
        self.rect.width *= 1.5

    def reset_size(self):
        self.rect.width = PADDLE_WIDTH

    def reset(self):
        # Set initial position and size of the paddle
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PADDLE_WIDTH // 2, SCREEN_HEIGHT - PADDLE_HEIGHT - 10, PADDLE_WIDTH, PADDLE_HEIGHT)