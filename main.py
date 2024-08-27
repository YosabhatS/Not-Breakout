from paddle import *
from ball import *
from brick import *
from power_up import *
from screen import *

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not Breakout")
S = Screen(screen)

# Main game loop
def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    bricks = Brick.create_bricks()
    powerups = []
    running = True
    game_over = False
    won = False
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

            # Ball movement
            ball.move()

            # Ball and paddle collision
            if ball.rect.colliderect(paddle.rect):
                ball.y_speed = -ball.y_speed

            # Ball and brick collision
            for brick in bricks[:]:
                if ball.rect.colliderect(brick.rect):
                    bricks.remove(brick)
                    ball.y_speed = -ball.y_speed

                    # Randomly drop a power-up
                    if random.random() < POWERUP_DROP_CHANCE:
                        power_type = random.choice(['enlarge', 'slow'])
                        powerup = PowerUp(brick.rect.x, brick.rect.y, power_type)
                        powerups.append(powerup)
                    break

            # Ball out of bounds (lose condition)
            if ball.rect.bottom >= SCREEN_HEIGHT:
                game_over = True
                S.show_retry_screen("Game Over")

            # Win condition
            if not bricks:
                won = True
                game_over = True
                S.show_retry_screen("You Win!")

            # Power-up movement and collision with paddle
            for powerup in powerups[:]:
                powerup.move()
                if powerup.rect.colliderect(paddle.rect):
                    if powerup.power_type == 'enlarge':
                        paddle.enlarge()
                        powerup_effect_time = pygame.time.get_ticks()
                    elif powerup.power_type == 'slow':
                        ball.slow_down()
                        powerup_effect_time = pygame.time.get_ticks()
                    powerups.remove(powerup)

            # Reset power-up effects after a few seconds
            if powerup_effect_time and pygame.time.get_ticks() - powerup_effect_time > POWERUP_EFFECT_TIME:
                paddle.reset_size()
                ball.reset_speed()
                powerup_effect_time = 0

            # Drawing
            paddle.draw(screen)
            ball.draw(screen)
            for brick in bricks:
                brick.draw(screen)
            for powerup in powerups:
                powerup.draw(screen)

        # Update display
        pygame.display.flip()
        clock.tick(FPS)

        # Reset the game if player presses space to retry
        if game_over:
            paddle = Paddle()
            ball = Ball()
            bricks = Brick.create_bricks()
            powerups = []
            game_over = False
            won = False

if __name__ == "__main__":
    S.start_screen()
    main()