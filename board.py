import pygame
from cell import Cell
from sudoku_generator import generate_sudoku

def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self. difficulty = difficulty

    if self.difficulty == 'Easy':
        num_removed = 30
    elif self.difficulty == 'Medium':
        num_removed = 40
    elif self.difficulty == 'Hard':
        num_removed = 50

    def draw(self):

    def select(self, row, col):

    def click(self, x, y):

    def clear(self):

    def sketch(sketch, value):

    def place_number(self, value):

    def reset_to_original(self):

    def is_full(self):

    def update_board(self):

    def find_empty(self):

    def check_board(self):