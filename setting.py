import pygame
import sys
import random

# Define constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BRICK_ROWS = 5
BRICK_COLS = 8
BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLS
BRICK_HEIGHT = 25
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 16
PADDLE_SPEED = 10
BALL_RADIUS = 10
BALL_SPEED = 4
BRICK_EDGE_THICKNESS = 2
POWERUP_SIZE = 20
POWERUP_SPEED = 3
POWERUP_EFFECT_TIME = 5000 # ms
POWERUP_DROP_CHANCE = 0.2  # 20% chance a power-up will drop
FPS = 60


# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
PURPLE = (128, 0, 128)
ORANGE = (255, 165, 0)
PINK = (255, 140, 247)