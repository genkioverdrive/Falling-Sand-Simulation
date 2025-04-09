import pygame
import sys
from simulation import Simulation

pygame.init()

# window definitions
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600 
CELL_SIZE = 20


# bg color(grey)
BG_COLOR = (29,29,29)

#fps setting
FPS = 120

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Falling Sand Simulation")
clock = pygame.time.Clock()

sim = Simulation(WINDOW_WIDTH,WINDOW_HEIGHT,CELL_SIZE)

running = True
while running:
    sim.handle_controls()

    #draws stuff on the screen
    # window.fill((r,g,b))
    window.fill(BG_COLOR)

    sim.draw(window)
    sim.update()
    # grid.draw(window)

    pygame.display.flip()
    clock.tick(FPS)