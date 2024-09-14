from setting import *

class Brick:
    def __init__(self, x, y, width, height, brick_type='normal'):
        self.rect = pygame.Rect(x, y, width, height)
        self.brick_type = brick_type

    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, BRICK_EDGE_THICKNESS)

    @staticmethod
    def get_brick_width(screen_width, brick_margin, num_columns):
        # Define SCOREBOARD_MARGIN here, or import it from setting
        SCOREBOARD_MARGIN = 50  # Adjust if needed

        # Adjust brick width to fit the screen width
        brick_width = (screen_width - (num_columns + 1) * brick_margin) / num_columns
        return brick_width

    @staticmethod
    def create_bricks(level, screen_width, screen_height, brick_margin):
        num_columns = BRICK_COLS + level - 1  # Increase columns with each level
        num_rows = BRICK_ROWS
        bricks = []
        brick_width = Brick.get_brick_width(screen_width, brick_margin, num_columns)
        brick_height = BRICK_HEIGHT  # Keep the fixed height

        for row in range(num_rows):
            for col in range(num_columns):
                brick_x = col * (brick_width + brick_margin) + brick_margin
                brick_y = 50 + row * (brick_height + brick_margin) + brick_margin  # Include margin for the scoreboard
                brick = Brick(brick_x, brick_y, brick_width, brick_height)
                bricks.append(brick)

        return bricks
