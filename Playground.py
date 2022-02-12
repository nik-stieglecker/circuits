
import pygame

import AndGate
import Board
import Connector
import GfxContext
import Lamp
import Logger
import NotGate
import PowerSource
from Rotate import Rotate
import Switch
import Switch12
import Switch21


def createSimpleBoard():
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 4), "Power", Rotate.ROTATE90))
    
    lamp = board.addComponent(Lamp.Lamp((5, 8), "out", Rotate.ROTATE270))    
    c1 = board.addComponent(Connector.Connector((1, 8), ""))

    board.connect(powerSource, lamp)
    board.connect(lamp, c1)
    board.connect(c1, powerSource)
    
    rasterCount = (18, 9)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
 
    return board, printSize, rasterCount

def createPrintContext(printSize, rasterCount):
    printSurface = pygame.Surface(printSize)
    printContext = GfxContext.GfxContext(printSurface, rasterCount)
    printContext.setBackgroundColour((255, 255, 255))
    printContext.setRasterColour((255, 255, 255))
    printContext.setRasterColourHigh((255, 255, 255))
    printContext.setConnectorLineWidth(4)
    printContext.setConnectorColour((50, 50, 50))
    printContext.setComponentColour((50, 50, 50))
    printContext.setLampColour((50, 50, 50))
    printContext.setActiveConnectorLineWidth(8)
    printContext.setActiveConnectorColour((0, 0, 0))
    printContext.setActiveComponentColour((0, 0, 0))
    printContext.setActiveLampColour((0, 0, 0))
    
    return printContext



def main():
    
    pygame.init()
    pygame.font.init()
    
    Logger.setLogLevel(3)
    
    # board, printSize, rasterCount = createSimpleTestBoard()
    board, printSize, rasterCount = createSimpleBoard()
    #board, printSize, rasterCount = createNotBoard()
    
    
    
    printContext = createPrintContext(printSize, rasterCount)

    screenRasterFactor = 1500 / printContext.getSurfaceSize()[0]
    surface = pygame.display.set_mode((round(printContext.getSurfaceSize()[0]*screenRasterFactor), round(printContext.getSurfaceSize()[1]*screenRasterFactor)))
    screenContext = GfxContext.GfxContext(surface, printContext.getRasterCount())  
    
    Logger.info("creating test board...")
    board.switchOn()
    Logger.info("finished.")
    
    draw(screenContext, board)
    
    run = True
    while run:
        for event in pygame.event.get():
#            print (event)
            if event.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                globalRaster = screenContext.surfaceToRaster(pos)
                Logger.debug(event)
            
                clicked = board.getClicked(globalRaster)
                
                if clicked:
                    #Logger.info(clicked)
                
                    clicked.handleClicked(globalRaster) 
                
                    draw(screenContext, board)
            elif event.type == pygame.QUIT:
                run = False
                
            elif event.type == pygame.TEXTINPUT:
                if event.text == "p":
                    print ("saving image")
                    draw(printContext, board)
                    printContext.save(r"C:\Users\nikst\ws\test2.jpeg")
                

                
        pygame.display.update()


def draw(g, board):
    board.switchOn()
    g.clear()
    g.drawRaster()
    board.draw(g)    

    
main()
