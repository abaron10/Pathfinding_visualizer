from queue import PriorityQueue
import pygame

class Astar():
    def implementation(self,draw, grid, start, end,win):
        count,origin,open_set_hash = 0 ,{}, {start}
        open_set = PriorityQueue()
        open_set.put((0, count, start))
        g_score , f_score = {node: float("inf") for row in grid for node in row},{node: float("inf") for row in grid for node in row}
        g_score[start],f_score[start] = 0, self.height(start.get_pos(), end.get_pos())

        while not open_set.empty():
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current = open_set.get()[2]
            open_set_hash.remove(current)

            if current == end:
                self.reversePath(origin,start, end, draw,win)
                end.make_end()
                return True

            for neighbor in current.neighbors:
                temp_g_score = g_score[current] + 1

                if temp_g_score < g_score[neighbor]:
                    origin[neighbor],g_score[neighbor],f_score[neighbor] = current,temp_g_score,temp_g_score + self.height(neighbor.get_pos(), end.get_pos())
                    if neighbor not in open_set_hash:
                        count += 1
                        open_set.put((f_score[neighbor], count, neighbor))
                        open_set_hash.add(neighbor)
                        neighbor.make_open()

            draw()

            if current != start:
                current.make_closed()

        return False
    def height(self,p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return abs(x1 - x2) + abs(y1 - y2)


    def reversePath(self,origin,start, current, draw,win):
        counter = 0
        
        while current in origin:
            current = origin[current]
            if current != start:
                current.make_patheight(win)
                
            else:
                current.make_start()
            counter += 1
            
            draw()
        
            
        
