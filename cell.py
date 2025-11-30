import pygame

class Cell:
    def  __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False
        self.original = value != 0

    def set_cell_value(self, value):
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value

    def draw(self):
        x = self.col * 60
        y = self.row * 60
        pygame.draw.rect(self.screen, (0,0,0), (x, y, 60, 60), 1)

        if self.value != 0:
            value_font = pygame.font.Font(None, 40)
            value_surf = value_font.render(str(self.value), True, (0,0,0))
            value_rect = value_surf.get_rect(center = (x + 30, y + 30))
            self.screen.blit(value_surf, value_rect)

        if self.value == 0 and self.sketched_value != 0:
            value_font = pygame.font.Font(None, 40)
            value_surf = value_font.render(str(self.sketched_value), True, (128, 128, 128))
            value_rect = value_surf.get_rect(topleft = (x + 23, y + 18))
            self.screen.blit(value_surf, value_rect)

        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0), (x, y, 60, 60), 3)

