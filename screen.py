import csv
import os
from setting import *

class Screen:
    def __init__(self, screen):
        self.screen = screen

    # Show the game over screen and prompt for player name
    def show_retry_screen(self, message, score):
        # Extract the status message
        status_message = message.split(":")[0]  # "Game Over" or "You Win"
        
        # Render the status message
        status_text = pygame.font.SysFont(None, 48).render(status_message, True, WHITE)
        self.screen.blit(status_text, (SCREEN_WIDTH // 2 - status_text.get_width() // 2, SCREEN_HEIGHT // 3))

        # Render the score
        score_text = pygame.font.SysFont(None, 48).render(f"Score: {score}", True, WHITE)
        self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2))

        # Render the retry instruction
        retry_text = pygame.font.SysFont(None, 36).render("Press SPACE to Retry", True, WHITE)
        self.screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 60))

        pygame.display.flip()

        # Get player name
        player_name = self.get_player_name()

        # Save the score with player name
        self.save_score(player_name, score)

        # Show high scores
        self.show_high_scores()

        self.wait("retry")

    # Capture player's name input
    def get_player_name(self):
        player_name = ""
        font = pygame.font.SysFont(None, 36)
        input_active = True

        while input_active:
            self.screen.fill(BLACK)
            prompt = font.render("Enter your name: " + player_name, True, WHITE)
            self.screen.blit(prompt, (SCREEN_WIDTH // 2 - prompt.get_width() // 2, SCREEN_HEIGHT // 3))
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and player_name:
                        input_active = False
                    elif event.key == pygame.K_BACKSPACE:
                        player_name = player_name[:-1]
                    else:
                        player_name += event.unicode

        return player_name

    # Save the score to a CSV file
    def save_score(self, player_name, score):
        filename = 'high_scores.csv'
        file_exists = os.path.isfile(filename)

        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            if not file_exists:
                writer.writerow(['Name', 'Score'])  # Write header if file doesn't exist
            writer.writerow([player_name, score])

    # Display top 10 high scores
    def show_high_scores(self):
        filename = 'high_scores.csv'
        scores = []

        # Read the CSV file
        if os.path.isfile(filename):
            with open(filename, mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    scores.append((row['Name'], int(row['Score'])))

        # Sort the scores and keep the top 10
        top_scores = sorted(scores, key=lambda x: x[1], reverse=True)[:10]

        # Render the high scores
        self.screen.fill(BLACK)
        font = pygame.font.SysFont(None, 36)
        title = font.render("Top 10 High Scores", True, WHITE)
        self.screen.blit(title, (SCREEN_WIDTH // 2 - title.get_width() // 2, SCREEN_HEIGHT // 4))

        for i, (name, score) in enumerate(top_scores):
            score_text = font.render(f"{i + 1}. {name} - {score}", True, WHITE)
            self.screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 3 + (i + 1) * 30))

        pygame.display.flip()

        self.wait("retry")

    def start_screen(self):
        game_name_text = pygame.font.SysFont(None, 60).render("NOT BREAKOUT", True, WHITE)
        play_text = pygame.font.SysFont(None, 36).render("Press ENTER to Start", True, WHITE)

        self.screen.blit(game_name_text, (SCREEN_WIDTH // 2 - game_name_text.get_width() // 2, SCREEN_HEIGHT // 4))
        self.screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, SCREEN_HEIGHT // 3 + 40))

        pygame.display.flip()
        self.wait("start")

    def wait(self, type):
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
