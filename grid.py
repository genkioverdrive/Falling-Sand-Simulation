import pygame

class Grid:
    def __init__(self, width = 800, height = 600, cell_size = 20):
        self.rows = height // cell_size
        self.cols = width // cell_size
        self.cell_size = cell_size
        self.cells = [[None for _ in range(self.cols)] for _ in range(self.rows)]
    
    def draw(self,window):
        for row in range(self.rows):
            for column in range(self.cols):
                part = self.cells[row][column]
                if part is not None:
                    color = part.color
                    pygame.draw.rect(window,color,(column * self.cell_size, row * self.cell_size,self.cell_size,self.cell_size))

    def clear(self):
        for row in range(self.rows):
            for column in range(self.cols):
                self.remove_particle(row,column)

    def add_particle(self,row,column,particle_type):
        if 0 <= row < self.rows and 0 <= column < self.cols and self.is_empty(row,column):
            self.cells[row][column] = particle_type()

    def remove_particle(self,row,column):
        if 0 <= row < self.rows and 0 <= column < self.cols:
            self.cells[row][column] = None
    
    def is_empty(self,row,column):
        if (0 <= row < self.rows and 0 <= column < self.cols):
            if (self.cells[row][column] == None):
                return True
        return False
    
    def set_cell(self,row,column,particle):
        if not (0 <= row < self.rows and 0 <= column < self.cols):
            return
        self.cells[row][column] = particle

    def get_cell(self,row,column):
        if (0 <= row < self.rows and 0 <= column < self.cols):
            return self.cells[row][column]
        return None