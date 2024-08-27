from paddle import *
from ball import *
from brick import *
from power_up import *

pygame.init()

# Create screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Not Breakout")

# Display game over or win message
def show_retry_screen(message):
    text = pygame.font.SysFont(None, 48).render(message, True, WHITE)
    retry_text = pygame.font.SysFont(None, 36).render("Press SPACE to Retry", True, WHITE)
    
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
    screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
    
    pygame.display.flip()
    wait("retry")

def start_screen():
    game_name_text = pygame.font.SysFont(None, 60).render("NOT BREAKOUT", True, WHITE)
    play_text = pygame.font.SysFont(None, 36).render("Press ENTER to Start", True, WHITE)

    screen.blit(game_name_text, (SCREEN_WIDTH // 2 - game_name_text.get_width() // 2, SCREEN_HEIGHT // 4))
    screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, SCREEN_HEIGHT // 3 + 40))

    pygame.display.flip()
    wait("start")

# Wait for the player to press space to retry or press enter to start
def wait(type):
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if type == "retry":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    waiting = False
            elif type == "start":
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    waiting = False

# Main game loop
def main():
    clock = pygame.time.Clock()
    paddle = Paddle()
    ball = Ball()
    bricks = brick.create_bricks()
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
                show_retry_screen("Game Over")

            # Win condition
            if not bricks:
                won = True
                game_over = True
                show_retry_screen("You Win!")

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
            bricks = brick.create_bricks()
            powerups = []
            game_over = False
            won = False

if __name__ == "__main__":
    start_screen()
    main()