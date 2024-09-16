import pygame
from setting import *

class Brick:
    def __init__(self, x, y, width, height, color=PINK):  # Pass the color you want for the overlay
        self.rect = pygame.Rect(x, y, width, height)
        self.image = pygame.image.load('assets/brick.png')  # Load the brick image
        self.image = pygame.transform.scale(self.image, (width, height))  # Scale the image to fit the brick size
        
        # Create a surface for the color overlay
        self.overlay = pygame.Surface((width, height), pygame.SRCALPHA)  # Create a transparent surface
        self.overlay.fill((*color, 128))  # Set color with 50% opacity (128 is 50% in the alpha channel)

    def draw(self, screen):
        # Draw the brick image on the screen
        screen.blit(self.image, (self.rect.x, self.rect.y))
        # Draw the 50% opacity color overlay on top of the brick image
        screen.blit(self.overlay, (self.rect.x, self.rect.y))

    @staticmethod
    def create_bricks(level, screen_width, screen_height, brick_margin):
        bricks = []
        num_cols = 5 + level  # Increase the number of columns with each level
        brick_width = (screen_width - (num_cols + 1) * brick_margin) // num_cols
        brick_height = 30
        num_rows = 5  # You can adjust this based on the difficulty/level
        
        # Define a list of colors for each row
        row_colors = [(255, 0, 0),   # Red
                      (255, 165, 0), # Orange
                      (255, 255, 0), # Yellow
                      (0, 255, 0),   # Green
                      (0, 0, 255)]   # Blue

        for row in range(num_rows):
            color = row_colors[row % len(row_colors)]  # Cycle through colors for each row
            for col in range(num_cols):
                x = col * (brick_width + brick_margin) + brick_margin
                y = row * (brick_height + brick_margin) + brick_margin + 50  # Adding 50 pixels margin from the top
                brick = Brick(x, y, brick_width, brick_height, color)
                bricks.append(brick)
        return bricks
