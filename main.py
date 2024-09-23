import pygame
import sys
import random
from paddle import Paddle
from ball import Ball
from brick import Brick
from power_up import PowerUp
from screen import Screen
from setting import *

# Initialize Pygame
pygame.init()

# Screen setup
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not Breakout")
S = Screen(screen)

# Initialize sound effects
pygame.mixer.init()
hit_sound = pygame.mixer.Sound('assets/hit.wav')
break_sound = pygame.mixer.Sound('assets/break.wav')

hit_sound.set_volume(0.1)
break_sound.set_volume(0.1)

# Variables to track player stats
score = 0
lives = 3
level = 1

# Function to draw the scoreboard
def draw_scoreboard(screen, score, lives, level):
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    # lives_text = font.render(f"Lives: {lives}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)

    # Position the scoreboard
    screen.blit(score_text, (10, 10))  # Score at top-left
    screen.blit(level_text, (SCREEN_WIDTH - 150, 10))  # Level at top-right
    # screen.blit(level_text, (SCREEN_WIDTH // 2 - 50, 10))  # Level in the center

# Main game loop
def main():
    global score, lives, level
    clock = pygame.time.Clock()
    paddle = Paddle()

    # Start with one ball
    balls = [Ball()]

    brick_margin = 5  # Margin between bricks
    bricks = Brick.create_bricks(level, SCREEN_WIDTH, SCREEN_HEIGHT, brick_margin)
    powerups = []
    running = True
    game_over = False
    powerup_effect_time = 0

    while running:
        screen.fill(BLACK)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        if not game_over:
            # Paddle movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                paddle.move('left')
            if keys[pygame.K_RIGHT]:
                paddle.move('right')

            # Move and draw all balls
            for ball in balls[:]:
                ball.move(paddle)  # Pass the paddle to the ball move function

                # Ball and paddle collision
                if ball.rect.colliderect(paddle.rect):
                    ball.reflect_from_paddle(paddle)  # Reflect based on paddle collision
                    hit_sound.play()  # Play hit sound on paddle collision

                # Ball and brick collision
                for brick in bricks[:]:
                    if ball.rect.colliderect(brick.rect):
                        bricks.remove(brick)
                        ball.y_speed = -ball.y_speed  # Reflect ball on brick collision
                        score += 500  # Increment score when a brick is destroyed
                        break_sound.play()  # Play break sound on brick collision

                        # Randomly drop a power-up
                        if random.random() < POWERUP_DROP_CHANCE:
                            power_type = random.choice(['enlarge', 'slow', 'multiply'])
                            powerup = PowerUp(brick.rect.x, brick.rect.y, power_type)
                            powerups.append(powerup)
                        break

                # Ball out of bounds (lose condition)
                if ball.rect.bottom >= SCREEN_HEIGHT:
                    balls.remove(ball)  # Remove the ball from the game
                    if not balls:
                        game_over = True
                        S.show_retry_screen("Game Over!", score)

            # Win condition - clear all bricks
            if not bricks:
                level += 1
                bricks = Brick.create_bricks(level, SCREEN_WIDTH, SCREEN_HEIGHT, brick_margin)
                for ball in balls:
                    ball.reset()
                paddle.reset()

            # Power-up movement and collision with paddle
            for powerup in powerups[:]:
                powerup.move()
                if powerup.rect.colliderect(paddle.rect):
                    if powerup.power_type == 'enlarge':
                        paddle.enlarge()
                        powerup_effect_time = pygame.time.get_ticks()
                    elif powerup.power_type == 'slow':
                        for ball in balls:
                            ball.slow_down()
                        powerup_effect_time = pygame.time.get_ticks()
                    elif powerup.power_type == 'multiply':
                        # Generate a new ball
                        new_ball = Ball()
                        new_ball.x_speed = random.choice([-4, 4])  # Random initial direction
                        new_ball.y_speed = -BALL_SPEED
                        balls.append(new_ball)
                    powerups.remove(powerup)

            # Reset power-up effects after a few seconds
            if powerup_effect_time and pygame.time.get_ticks() - powerup_effect_time > POWERUP_EFFECT_TIME:
                paddle.reset_size()
                for ball in balls:
                    ball.reset_speed()
                powerup_effect_time = 0

            # Drawing
            paddle.draw(screen)
            for ball in balls:
                ball.draw(screen)
            for brick in bricks:
                brick.draw(screen)
            for powerup in powerups:
                powerup.draw(screen)

            # Draw the scoreboard
            draw_scoreboard(screen, score, lives, level)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

        # If game is over, wait for space to return to start screen
        if game_over:
            score = 0
            keys = pygame.key.get_pressed()
            if keys[pygame.K_SPACE]:
                S.start_screen()  # Clears the screen and shows the main screen
                main()  # Restart the main game loop after the player presses enter


if __name__ == "__main__":
    S.start_screen()
    main()
