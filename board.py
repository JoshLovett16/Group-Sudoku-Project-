import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

class Board:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.screen = screen
        self. difficulty = difficulty

        # mapping empty cells to difficulty
        if self.difficulty == 'Easy':
            num_removed = 30
        elif self.difficulty == 'Medium':
            num_removed = 40
        elif self.difficulty == 'Hard':
            num_removed = 50
        else:
            num_removed = 30 # default to easy

        self.cells = []
        self.board_values = generate_sudoku(9, num_removed)

        for row in range(9):
            row_data = []
            for col in range(9):
                current_val = self.board_values[row][col]
                new_cell = Cell(current_val, row, col, self.screen)
                row_data.append(new_cell)
            self.cells.append(row_data)

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
                current_cell = self.cells[r][c]
                current_cell.selected = False
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

        if row is not None and col is not None:
            if self.board_values[row][col] == 0:
                self.cells[row][col].set_cell_value(0)
                self.cells[row][col].set_sketched_value(0)


    def sketch(self, value):
        row = self.selected_row
        col = self.selected_col

        if row is not None and col is not None:
            if self.board_values[row][col] == 0:
                self.cells[row][col].set_sketched_value(value)

    def place_number(self, value):
        row = self.selected_row
        col = self.selected_col

        if row is not None and col is not None:
            if self.board_values[row][col] == 0:
                self.cells[row][col].set_cell_value(value)
                self.cells[row][col].set_sketched_value(0)

    def reset_to_original(self):
        for row in range(9):
            for col in range(9):
                if self.board_values[row][col] == 0:
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
            row_numbers = set(self.board_values[row])
            if len(row_numbers) != 9 or 0 in row_numbers:
                return False

        for col in range(9):
            col_numbers = [self.board_values[row][col] for row in range(9)]
            if len(set(col_numbers)) != 9 or 0 in set(col_numbers):
                return False

        return True