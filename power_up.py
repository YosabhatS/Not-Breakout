from setting import *
class PowerUp:
    def __init__(self, x, y, power_type):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.power_type = power_type  # 'enlarge' or 'slow'
        self.speed = POWERUP_SPEED

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        if self.power_type == 'enlarge':
            pygame.draw.rect(screen, PURPLE, self.rect)
        elif self.power_type == 'slow':
            pygame.draw.rect(screen, ORANGE, self.rect)