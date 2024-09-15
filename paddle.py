import pygame
from setting import *

class Paddle:
    def __init__(self):
        self.image = pygame.image.load('assets/paddle.png')  # Load the paddle image
        self.rect = self.image.get_rect()  # Get the rectangle of the image for positioning
        self.reset()  # Set the initial position of the paddle

    def move(self, direction):
        if direction == 'left':
            self.rect.x -= PADDLE_SPEED
            if self.rect.left < 0:
                self.rect.left = 0
        elif direction == 'right':
            self.rect.x += PADDLE_SPEED
            if self.rect.right > SCREEN_WIDTH:
                self.rect.right = SCREEN_WIDTH

    def draw(self, screen):
        screen.blit(self.image, self.rect)  # Draw the paddle image on the screen

    def enlarge(self):
        # Enlarge the paddle by scaling the image and updating the rectangle
        new_width = int(self.rect.width * 1.5)
        self.image = pygame.transform.scale(self.image, (new_width, self.rect.height))
        self.rect = self.image.get_rect(center=self.rect.center)  # Keep the paddle's position centered

    def reset_size(self):
        # Reset the paddle size to its original size
        self.image = pygame.image.load('assets/paddle.png')  # Reload the original image
        self.rect = self.image.get_rect(center=self.rect.center)  # Keep the position centered

    def reset(self):
        # Set the initial paddle position at the bottom of the screen
        self.rect.midbottom = (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 30)
