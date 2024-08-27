from setting import *
class Screen:
  def __init__(self, screen):
    self.screen = screen

  # Display game over or win message
  def show_retry_screen(self, message):
      text = pygame.font.SysFont(None, 48).render(message, True, WHITE)
      retry_text = pygame.font.SysFont(None, 36).render("Press SPACE to Retry", True, WHITE)
      
      self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - text.get_height() // 2))
      self.screen.blit(retry_text, (SCREEN_WIDTH // 2 - retry_text.get_width() // 2, SCREEN_HEIGHT // 2 + 40))
      
      pygame.display.flip()
      self.wait("retry")

  def start_screen(self):
      game_name_text = pygame.font.SysFont(None, 60).render("NOT BREAKOUT", True, WHITE)
      play_text = pygame.font.SysFont(None, 36).render("Press ENTER to Start", True, WHITE)

      self.screen.blit(game_name_text, (SCREEN_WIDTH // 2 - game_name_text.get_width() // 2, SCREEN_HEIGHT // 4))
      self.screen.blit(play_text, (SCREEN_WIDTH // 2 - play_text.get_width() // 2, SCREEN_HEIGHT // 3 + 40))

      pygame.display.flip()
      self.wait("start")

  # Wait for the player to press space to retry or press enter to start
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
