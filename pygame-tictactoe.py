import pygame
from grid import Grid
import minimax

surface = pygame.display.set_mode((600,600))
pygame.display.set_caption("Tic-Tac-Toe")

grid = Grid()

player = "X"


    
def game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0] == 1:
                        x=pygame.mouse.get_pos()[0]//200
                        y=pygame.mouse.get_pos()[1]//200
                        grid.play(x,y, player)
                        if minimax.terminal(grid.matrix):
                            grid.draw(surface)
                        else:
                            act =  minimax.minimax(grid.matrix)
                            grid.matrix =  minimax.result(grid.matrix,act)
                            
        surface.fill((0,0,0))

        grid.draw(surface)
        pygame.display.flip()



def intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        surface.fill((200,200,200))
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 100)
        textsurface3 = myfont.render('Tic-Tac-Toe', False, (200, 0, 200))
        surface.blit(textsurface3,(125,225))
        
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 250+100 > mouse[0] > 250 and 350+50 > mouse[1] > 350:
            pygame.draw.rect(surface, (100,100,100), (250,350,100,50))
            if click[0] == 1:
                game_loop()
        else:
            pygame.draw.rect(surface, (0,0,0), (250,350,100,50))
        
        pygame.font.init() 
        myfont = pygame.font.SysFont('Comic Sans MS', 40)
        textsurface4 = myfont.render('Play', False, (200, 200, 200))
        surface.blit(textsurface4,(270,365))
        pygame.display.update()
        pygame.display.flip()

intro()
game_loop()
