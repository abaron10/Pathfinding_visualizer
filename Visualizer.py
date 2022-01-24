import pygame
import math
from queue import PriorityQueue
from ui_complements.Constants import Colors
from algorithm.Node import Node
from ui_complements.Grid import Grid
from algorithm.Astar import  Astar

pygame.font.init()
WIDTH = 700
WIN = pygame.display.set_mode((1200, WIDTH))
pygame.display.set_caption("A star Path Finding Algorithm")

def main(win, width):
	ROWS = 50
	gridObject = Grid()	
	astar = Astar()
	grid = gridObject.make_grid(ROWS, width)
	start,end,run = None,None,True
	def current_click(pos, rows, width):
		gap = width // rows
		return pos[0] // gap, pos[1] // gap

	while run:
		
		gridObject.draw(win, grid, ROWS, width)
		for event in pygame.event.get():
			
			if event.type == pygame.QUIT:
				run = False

			if pygame.mouse.get_pressed()[0]:
				pos = pygame.mouse.get_pos()
				row, col = current_click(pos, ROWS, width)
				node = grid[row][col]
				if not start and node != end:
					start = node
					start.make_start()

				elif not end and node != start:
					end = node
					end.make_end()

				elif node != end and node != start:
					node.make_barrier()
			elif pygame.mouse.get_pressed()[1]:
				for row in grid:
					for node in row:
						x,y = node.get_pos()
						grid[x][y].reset()
				start, end = None , None

			elif pygame.mouse.get_pressed()[2]: # RIGHT
				pos = pygame.mouse.get_pos()
				row, col = current_click(pos, ROWS, width)
				node = grid[row][col]
				node.reset()
				if Node == start:
					start = None
				elif node == end:
					end = None

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_SPACE and start and end:
					for row in grid:
						for node in row:
							node.update_neighbors(grid)

					astar.implementation(lambda: gridObject.draw(win, grid, ROWS, width), grid, start, end,win)

				if event.key == pygame.K_c:
					start = None
					end = None
					grid = gridObject.make_grid(ROWS, width)
		
	
	pygame.quit()

main(WIN, 1200)