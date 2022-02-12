import pygame
import GfxContext
import Logger


# density = 30
# width = density * 40
# height= density * 24
# window = pygame.display.set_mode((width, height))


# def draw(denx, deny):
#     
#     colour = (232, 226, 225)
#         
#     for n in range(denx, width, denx):
#         line = pygame.draw.line(window, colour, (n, 0), (n, height), 1) 
#         if pygame.mouse.get_pos()[0] == n + denx:
#             colour = (255, 0, 0)
#         else:
#             colour = (232, 226, 225)
#             
#     for n in range(deny, height, deny):
#         line = pygame.draw.line(window, colour, (0, n), (width, n), 1)   
#         if pygame.mouse.get_pos()[1] == n + deny:
#             colour = (255, 0, 0)
#         else:
#             colour = (232, 226, 225)
# 
# def gridToSurface(gridCoord):
#     return (surfaceStartX + gridWidth * gridCoord[0], surfaceStartY + gridHeight * gridCoord[1])
#             
def main():
    
    g = GfxContext.GfxContext((1500, 800), (20, 20), (20, 20), (73, 38))  
    g.drawRaster()
    
    fonts = pygame.font.get_fonts()
    Logger.info(fonts)
    
    myfont = pygame.font.SysFont('lucidasans', 30)
    textsurface = myfont.render('Some Text', False, (0, 255, 0))
    g.getWindow().blit(textsurface,(0,0))
    
    
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

#         window.fill((0,0,0))
#         draw(int(width/density), int(width/density))
#         draw(density, density)
        
        pygame.display.update()
    
    
main()