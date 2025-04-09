import pygame,sys
from grid import Grid
from particle import SandParticle,RockParticle

class Simulation:
    def __init__(self,width,height,cell_size):
        self.grid = Grid(width,height,cell_size)
        self.cell_size = cell_size
        self.mode = "sand"

    def draw(self,window):
        self.grid.draw(window)

    def restart(self):
        self.grid.clear()

    def set_particle(self,mode):
        if mode == "sand":
            return 1
        if mode == "rock":
            return 2
        if mode == "eraser":
            return 0

    def add_particle(self,row,column):
        if self.mode == "sand":
            particle = SandParticle
        if self.mode == "rock":
            particle = RockParticle
        
        self.grid.add_particle(row,column,particle)
    
    def remove_particle(self,row,column):
        self.grid.remove_particle(row,column)
    
    def update(self):
        for row in range(self.grid.rows-2,-1,-1):
            for column in range(self.grid.cols):
                particle = self.grid.get_cell(row,column)
                if isinstance(particle,SandParticle):
                    new_pos = particle.update(self.grid,row,column)
                    if new_pos != (row,column):
                        self.grid.set_cell(new_pos[0],new_pos[1],particle)
                        self.grid.remove_particle(row,column)

    def handle_controls(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                self.handle_key(event)
        
        self.handle_mouse()
    
    def handle_key(self,event):
        if event.key == pygame.K_SPACE:
            self.restart()
        if event.key == pygame.K_r:
            self.mode = "rock"
        if event.key == pygame.K_s:
            self.mode = "sand"
        if event.key == pygame.K_e:
            self.mode = "eraser"
    
    def handle_mouse(self):
        buttons = pygame.mouse.get_pressed()

        if buttons[0]:
            pos = pygame.mouse.get_pos()
            row = pos[1] // self.cell_size # x coordinate
            col = pos[0] // self.cell_size # y coordinate
            
            if self.mode == "eraser":
                self.remove_particle(row,col)
            else:
                self.add_particle(row,col)
