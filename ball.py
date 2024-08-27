from setting import *
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.x_speed = random.choice([-4, 4])
        self.y_speed = -BALL_SPEED

    def move(self):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball bounce on walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_speed = -self.x_speed
        if self.rect.top <= 0:
            self.y_speed = -self.y_speed

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)

    def slow_down(self):
        self.x_speed *= 0.5
        self.y_speed *= 0.5

    def reset_speed(self):
        self.x_speed = -BALL_SPEED if self.x_speed < 0 else BALL_SPEED
        self.y_speed = -BALL_SPEED if self.y_speed < 0 else BALL_SPEED
