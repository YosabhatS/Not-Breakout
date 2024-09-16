import pygame
import random
import math
from setting import *

class Ball:
    def __init__(self):
        pygame.mixer.init()  # Initialize the mixer module
        self.hit_sound = pygame.mixer.Sound('assets/hit.wav')  # Load hit sound
        self.hit_sound.set_volume(0.2)
        self.break_sound = pygame.mixer.Sound('assets/break.wav')  # Load break sound
        self.reset()  # Initialize with default values

    def move(self, paddle):
        # Move the ball
        self.rect.x += self.x_speed
        self.rect.y += self.y_speed

        # Ball bounce on walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.x_speed = -self.x_speed
            self.hit_sound.play()  # Play hit sound on wall collision
        if self.rect.top <= 0:
            self.y_speed = -self.y_speed
            self.hit_sound.play()  # Play hit sound on wall collision

        # Check if the ball collides with the paddle
        if self.rect.colliderect(paddle.rect):
            self.reflect_from_paddle(paddle)
            self.hit_sound.play()  # Play hit sound on paddle collision

        # Normalize speed to maintain stability
        self.normalize_speed()

    def draw(self, screen):
        pygame.draw.circle(screen, WHITE, self.rect.center, BALL_RADIUS)

    def slow_down(self):
        # Slow down the ball, but keep the speed proportional
        self.x_speed *= 0.5
        self.y_speed *= 0.5
        self.normalize_speed()

    def reset_speed(self):
        # Reset the ball's horizontal speed to a fixed constant
        self.x_speed = BALL_SPEED if self.x_speed >= 0 else -BALL_SPEED
        
        # Keep the ball's current vertical direction, but set its speed to BALL_SPEED
        # Maintain the current direction (upward or downward) without resetting it
        if self.y_speed != 0:
            speed = math.sqrt(self.x_speed ** 2 + self.y_speed ** 2)
            self.y_speed = (self.y_speed / abs(self.y_speed)) * (speed * BALL_SPEED / abs(speed))
        
        # Normalize the speed to ensure consistency
        self.normalize_speed()

    def reset(self):
        # Reset ball position and speed
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - BALL_RADIUS, SCREEN_HEIGHT // 2 - BALL_RADIUS, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.x_speed = random.choice([-BALL_SPEED, BALL_SPEED])
        self.y_speed = -BALL_SPEED
        self.normalize_speed()

    def reflect_from_paddle(self, paddle):
        # Calculate reflection based on paddle hit position
        hit_pos = (self.rect.centerx - paddle.rect.centerx) / (paddle.rect.width / 2)
        max_angle = 75  # Maximum reflection angle
        angle = hit_pos * max_angle
        angle_radians = math.radians(angle)

        # Calculate speed to maintain constant overall speed
        speed = math.sqrt(self.x_speed ** 2 + self.y_speed ** 2)
        self.x_speed = speed * math.sin(angle_radians)
        self.y_speed = -abs(speed * math.cos(angle_radians))

        # Normalize speed after reflection
        self.normalize_speed()

    def normalize_speed(self):
        # Ensure the ball speed is constant
        speed = math.sqrt(self.x_speed ** 2 + self.y_speed ** 2)
        if speed != 0:
            speed = BALL_SPEED
            self.x_speed = (self.x_speed / speed) * BALL_SPEED
            self.y_speed = (self.y_speed / speed) * BALL_SPEED
    def check_ball_brick_collision(self, bricks):
        for brick in bricks:
            if self.rect.colliderect(brick.rect):
                self.break_sound.play()  # Play break sound on brick collision
                # Handle brick destruction and ball behavior
                # ...
