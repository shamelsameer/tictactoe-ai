import pygame
import minimax
import time


class Grid:
    def __init__(self):
        self.grid_lines = [((0,200), (600,200)),
                            ((0,400),(600,400)),
                            ((200,0),(200,600)),
                            ((400,0),(400,600))]
        self.matrix = [[0,0,0],[0,0,0],[0,0,0]]
                
    def draw(self,surface):
        
            
       
        

        
        for line in self.grid_lines:
            pygame.draw.line(surface, (200,200,200), line[0], line[1],2)
        for x in range(3):
            for y in range(3):
                if self.matrix[x][y] == "X":
                    pygame.draw.line(surface, (200,200,200), (x*200,y*200),(x*200+200,y*200+200),2)
                    pygame.draw.line(surface, (200,200,200), (x*200+200, y*200), (x*200, y*200+200),2)
                elif self.matrix[x][y] == "O":
                    pygame.draw.circle(surface, (200,200,200), (x*200+100,y*200+100), 100, 2)
        if minimax.terminal(self.matrix):
            pygame.font.init() 
            myfont = pygame.font.SysFont('Comic Sans MS', 100)
            textsurface1 = myfont.render('Game Over :\(', False, (200, 0, 200))
            surface.blit(textsurface1,(100,225))
            if  minimax.utility(self.matrix) == -1:    
                textsurface2 = myfont.render('AI Wins!', False, (200,0,200))
                surface.blit(textsurface2,(150,325))
            else:
                textsurface2= myfont.render("Tie!", False, (200,0,200))
                surface.blit(textsurface2,(220,325))
            
        

    def play(self, x, y, player):
        self.matrix[x][y] = player
        print(self.matrix)


