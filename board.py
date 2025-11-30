import pygame
from cell import Cell
from sudoku_generator import SudokuGenerator

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty

        # mapping empty cells to difficulty
        if self.difficulty == 'Easy':
            num_removed = 30
        elif self.difficulty == 'Medium':
            num_removed = 40
        elif self.difficulty == 'Hard':
            num_removed = 50
        else:
            num_removed = 30 # default to easy

        sudoku_gen = SudokuGenerator(9, num_removed)
        sudoku_gen.fill_values()
        self.solution = [row.copy() for row in sudoku_gen.get_board()]

        sudoku_gen.remove_cells()
        self.board_values = sudoku_gen.get_board()

        self.cells = []
        for row in range(9):
            row_data = []
            for col in range(9):
                current_val = self.board_values[row][col]
                new_cell = Cell(current_val, row, col, self.screen)
                new_cell.original = current_val != 0
                row_data.append(new_cell)
            self.cells.append(row_data)

        self.selected_row = 0
        self.selected_col = 0
        self.select(0, 0)

    def draw(self):
        for row in range(9):
            for col in range(9):
                current_cell = self.cells[row][col]
                current_cell.draw()

        for i in range(4):
            pos = i * 180
            # Vertical
            pygame.draw.line(self.screen, (0, 0, 0), (pos, 0), (pos, 540), 5)
            # Horizontal
            pygame.draw.line(self.screen, (0, 0, 0), (0, pos), (540, pos), 5)

    def select(self, row, col):
        # Reset cells
        for r in range(9):
            for c in range(9):
                self.cells[r][c].selected = False
        # User picks
        self.cells[row][col].selected = True
        self.selected_row = row
        self.selected_col = col

    def click(self, x, y):
        if x < 540 and y < 540:
            row = y // 60
            col = x // 60
            return (row, col)
        else:
            return None

    def clear(self):
        row = self.selected_row
        col = self.selected_col
        if not self.cells[row][col].original:
            self.cells[row][col].set_cell_value(0)
            self.cells[row][col].set_sketched_value(0)


    def sketch(self, value):
        row = self.selected_row
        col = self.selected_col
        if not self.cells[row][col].original:
            self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        row, col = self.selected_row, self.selected_col
        if self.cells[row][col].original:
            return False
        self.cells[row][col].value = value
        self.cells[row][col].sketched_value = 0

        if self.is_full():
            if self.check_board():
                self.show_game_won()
            else:
                self.show_game_over()
                
        return True
        
    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if not self.cells[row][col].original:
                    self.cells[row][col].set_cell_value(0)
                    self.cells[row][col].set_sketched_value(0)

    def is_full(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return False
        return True

    def update_board(self):
        for row in range(9):
            for col in range(9):
                self.board_values[row][col] = self.cells[row][col].value

    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.cells[row][col].value == 0:
                    return(row, col)
        return None

    def check_board(self):
        self.update_board()
        for row in range(9):
            for col in range(9):
                if self.board_values[row][col] != self.solution[row][col]:
                    return False

        return True
    
    def show_game_won(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 80)
        text = font.render("Game Won :)", True, (255, 255, 255))
        rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, rect)
        pygame.display.update()

    def show_game_over(self):
        self.screen.fill((0, 0, 0))
        font = pygame.font.SysFont(None, 80)
        text = font.render("Game Over :(", True, (255, 255, 255))
        rect = text.get_rect(center=(self.width // 2, self.height // 2))
        self.screen.blit(text, rect)
        pygame.display.update()
