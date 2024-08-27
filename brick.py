from setting import *
class Brick:
    def __init__(self, x, y, brick_type='normal'):
        self.rect = pygame.Rect(x, y, BRICK_WIDTH, BRICK_HEIGHT)

    def draw(self, screen):
        # Draw the filled rectangle (the brick itself)
        pygame.draw.rect(screen, WHITE, self.rect)

        # Draw the outline (the edge of the brick)
        pygame.draw.rect(screen, BLACK, self.rect, BRICK_EDGE_THICKNESS)

def create_bricks():
    bricks = []
    for row in range(BRICK_ROWS):
        for col in range(BRICK_COLS):
            brick = Brick(col * BRICK_WIDTH, row * BRICK_HEIGHT)
            bricks.append(brick)
    return bricks
