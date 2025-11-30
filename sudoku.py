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

    return easy_button, medium_button, hard_button

def draw_game_buttons(screen):
    button_font = pygame.font.Font(None, 30)

    reset_text = button_font.render('Reset', True, (255, 255, 255))
    reset_btn = pygame.Rect(50, 550, 100, 40)
    pygame.draw.rect(screen, (255, 165, 0), reset_btn)
    screen.blit(reset_text, (reset_btn.x + 20, reset_btn.y + 10))

    restart_text = button_font.render("Restart", True, (255, 255, 255))
    restart_btn = pygame.Rect(220, 550, 100, 40)
    pygame.draw.rect(screen, (255, 165, 0), restart_btn)
    screen.blit(restart_text, (restart_btn.x + 10, restart_btn.y + 10))

    exit_text = button_font.render("Exit", True, (255, 255, 255))
    exit_btn = pygame.Rect(390, 550, 100, 40)
    pygame.draw.rect(screen, (255, 165, 0), exit_btn)
    screen.blit(exit_text, (exit_btn.x + 30, exit_btn.y + 10))

    return reset_btn, restart_btn, exit_btn

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((540, 600))
    pygame.display.set_caption('Sudoku')

    easy_button, medium_button, hard_button = draw_game_start(screen)

    draw_game_start(screen)

    board = None
    reset_btn = None
    restart_btn = None
    exit_btn = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if board is None:
                    if easy_button.collidepoint(event.pos):
                        board = Board(9,9, screen, 'Easy')
                    elif medium_button.collidepoint(event.pos):
                        board = Board(9,9, screen, 'Medium')
                    elif hard_button.collidepoint(event.pos):
                        board = Board(9,9,screen, 'Hard')

                else:
                    clicked_cell = board.click(event.pos[0], event.pos[1])
                    if clicked_cell:
                        board.select(clicked_cell[0], clicked_cell[1])

                    if reset_btn and reset_btn.collidepoint(event.pos):
                        board.reset_to_original()
                    elif restart_btn and restart_btn.collidepoint(event.pos):
                        board = None
                    elif exit_btn and exit_btn.collidepoint(event.pos):
                        sys.exit()
                        
            if event.type == pygame.KEYDOWN and board:
                if not hasattr(board, 'selected_row') or board.selected_row is None:
                    board.selected_row = 0
                if not hasattr(board, 'selected_col') or board.selected_col is None:
                    board.selected_col = 0
                row, col = board.selected_row, board.selected_col
                
                if event.unicode.isdigit() and event.unicode != "0":
                    board.sketch(int(event.unicode))
                elif event.key == pygame.K_RETURN:
                    val = board.cells[row][col].sketched_value
                    if val != 0:
                        board.place_number(val)
                elif event.key == pygame.K_BACKSPACE:
                        board.clear()
                elif event.key == pygame.K_UP:
                    board.selected_row = max(0, board.selected_row - 1)
                    board.select(board.selected_row, board.selected_col)
                elif event.key == pygame.K_DOWN:
                    board.selected_row = min(8, board.selected_row + 1)
                    board.select(board.selected_row, board.selected_col)
                elif event.key == pygame.K_LEFT:
                    board.selected_col = max(0, board.selected_col - 1)
                    board.select(board.selected_row, board.selected_col)
                elif event.key == pygame.K_RIGHT:
                    board.selected_col = min(8, board.selected_col + 1)
                    board.select(board.selected_row, board.selected_col)
                

        screen.fill((255, 255, 255))

        if board is None:
            easy_button, medium_button, hard_button = draw_game_start(screen)
        else:
            board.draw()
            reset_btn, restart_btn, exit_btn = draw_game_buttons(screen)

        pygame.display.update()
