import pygame
import time


class Animation:
    def __init__(self):
        self.font = pygame.font.Font('freesansbold.ttf', 72)
        self.small_font = pygame.font.Font('freesansbold.ttf', 48)

    def show_checkmate(self, screen):
        text = self.font.render("CHECKMATE!", True, (255, 0, 0))
        text_rect = text.get_rect(center=(400, 300))

        for alpha in range(0, 256, 5):
            text.set_alpha(alpha)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(30)

        pygame.time.delay(1000)

        for alpha in range(255, -1, -5):
            text.set_alpha(alpha)
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(30)

    def show_win(self, winner, screen):
        for size in range(20, 73, 2):
            temp_font = pygame.font.Font('freesansbold.ttf', size)
            text = temp_font.render(f"{winner} WINS!", True, (0, 255, 0))
            text_rect = text.get_rect(center=(400, 250))
            screen.blit(text, text_rect)
            pygame.display.update()
            pygame.time.delay(50)

        pygame.time.delay(2000)
