import pygame
import random
import math
from setting import *

class Ball:
    def __init__(self):
        self.reset()  # Initialize with default values

    def move(self, paddle):
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball bounce on walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_speed = -self.x_speed
        if self.rect.top <= 0:
            self.y_speed = -self.y_speed

        # Check if the ball collides with the paddle
        if self.rect.colliderect(paddle.rect):
            self.reflect_from_paddle(paddle)  # Reflect the ball when it hits the paddle

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)

    def slow_down(self):
        self.x_speed *= 0.5
        self.y_speed *= 0.5

    def reset_speed(self):
        self.x_speed = -BALL_SPEED if self.x_speed < 0 else BALL_SPEED
        self.y_speed = -BALL_SPEED if self.y_speed < 0 else BALL_SPEED

    def reset(self):
        # Reset ball position to the center of the screen
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        # Reset ball speed to initial values
        self.x_speed = random.choice([-4, 4])
        self.y_speed = -BALL_SPEED

    def reflect_from_paddle(self, paddle):
        # Calculate the difference between the ball's center and the paddle's center
        hit_pos = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)

        # Adjust the angle of reflection based on the hit position
        max_angle = 75  # Maximum reflection angle
        angle = hit_pos * max_angle  # Proportion of the max angle based on hit position

        # Convert angle to radians for calculations
        angle_radians = math.radians(angle)

        # Adjust ball speed based on angle
        speed = math.sqrt(self.x_speed ** 2 + self.y_speed ** 2)  # Keep the total speed constant
        self.x_speed = speed * math.sin(angle_radians)  # Adjust x speed
        self.y_speed = -abs(speed * math.cos(angle_radians))  # Adjust y speed (upward)
