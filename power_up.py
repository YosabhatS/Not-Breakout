from setting import *
import pygame

class PowerUp:
    def __init__(self, x, y, power_type):
        self.rect = pygame.Rect(x, y, POWERUP_SIZE, POWERUP_SIZE)
        self.power_type = power_type  # 'enlarge', 'slow', or 'multiply'
        self.speed = POWERUP_SPEED

        # Load the images
        self.slow_image = pygame.image.load('assets/slow.png')
        self.enlarge_image = pygame.image.load('assets/expand.png')
        self.multiply_image = pygame.image.load('assets/increase.png')  # Load the new multiply power-up image

        # Scale the images to fit the power-up size if needed
        self.slow_image = pygame.transform.scale(self.slow_image, (POWERUP_SIZE, POWERUP_SIZE))
        self.enlarge_image = pygame.transform.scale(self.enlarge_image, (POWERUP_SIZE, POWERUP_SIZE))
        self.multiply_image = pygame.transform.scale(self.multiply_image, (POWERUP_SIZE, POWERUP_SIZE))  # Scale the new image

    def move(self):
        self.rect.y += self.speed

    def draw(self, screen):
        if self.power_type == 'enlarge':
            screen.blit(self.enlarge_image, (self.rect.x, self.rect.y))
        elif self.power_type == 'slow':
            screen.blit(self.slow_image, (self.rect.x, self.rect.y))
        elif self.power_type == 'multiply':
            screen.blit(self.multiply_image, (self.rect.x, self.rect.y))  # Draw the new image
