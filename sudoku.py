import pygame
import sys
from board import Board


def draw_game_start(screen):
    screen.fill((255, 255, 255))
    title_font = pygame.font.Font(None, 40)
    title_surface = title_font.render('Welcome to Sudoku', True, (0, 0, 0))
    title_rect = title_surface.get_rect(center = (270, 100))
    screen.blit(title_surface, title_rect)

    subtitle_surface = title_font.render("Select Game Mode:", True, (0, 0, 0))
    subtitle_rect = subtitle_surface.get_rect(center=(270, 200))
    screen.blit(subtitle_surface, subtitle_rect)

    button_font = pygame.font.Font(None, 30)

    easy_text_surf = button_font.render('Easy', True, (255, 255, 255))
    easy_button = pygame.Rect(70, 300, 100, 50)
    pygame.draw.rect(screen, (255, 165, 0), easy_button)

    easy_text_rect = easy_text_surf.get_rect(center = easy_button.center)
    screen.blit(easy_text_surf, easy_text_rect)

    medium_text_surf = button_font.render('Medium', True, (255, 255, 255))
    medium_button = pygame.Rect(220, 300, 100, 50)
    pygame.draw.rect(screen, (255, 165, 0), medium_button)

    medium_text_rect = medium_text_surf.get_rect(center = medium_button.center)
    screen.blit(medium_text_surf, medium_text_rect)

    hard_text_surf = button_font.render('Hard', True, (255, 255, 255))
    hard_button = pygame.Rect(370, 300, 100, 50)
    pygame.draw.rect(screen, (255, 165, 0), hard_button)

    hard_text_rect = hard_text_surf.get_rect(center=hard_button.center)
    screen.blit(hard_text_surf, hard_text_rect)

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')

    draw_game_start(screen)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.update()