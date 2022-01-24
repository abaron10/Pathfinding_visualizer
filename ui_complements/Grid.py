
from ui_complements.Constants import Colors
from algorithm.Node import Node
import pygame
pygame.font.init()
class Grid():
    
    def make_grid(self,rows, width):
        grid = []
        gap = width // rows
        for i in range(rows):
            grid.append([])
            for j in range(rows):
                node = Node(i, j, gap, rows)
                grid[i].append(node)

        return grid
    

    def draw_grid(self,win, rows, width):
        gap = width // rows
        for i in range(rows):
            pygame.draw.line(win, Colors.GREY.value, (0, i * gap), (width, i * gap))
            for j in range(rows):
                pygame.draw.line(win, Colors.GREY.value, (j * gap, 0), (j * gap, width))
                


    def draw(self,win, grid, rows, width):
        win.fill(Colors.WHITE.value)

        for row in grid:
            for node in row:
                node.draw(win)
               

        self.draw_grid(win, rows, width)
        
        pygame.display.update()