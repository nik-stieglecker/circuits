
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


def createSimpleTestBoard():
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 10), "Power", Rotate.ROTATE180))
    c1 = board.addComponent(Connector.Connector((8, 7), "c1"))
    c2 = board.addComponent(Connector.Connector((20, 13), "c2"))

    board.connect(powerSource, c1)
    board.connect(c1, c2)
    board.connect(c2, powerSource) 

    board.resetVolt()

    rasterCount = (39, 19)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount

def createTestBoard():
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 10), "Power", Rotate.ROTATE180))
    c1 = board.addComponent(Connector.Connector((8, 7), "c1"))
    s1 = board.addComponent(Switch12.Switch12((10, 7), "s1", Rotate.ROTATE90))


    s2 = board.addComponent(Switch21.Switch21((20, 7), "s2", Rotate.ROTATE90)) 

    c_b = board.addComponent(Connector.Connector((26, 13), "c_b"))
     
    lamp = board.addComponent(Lamp.Lamp((24, 7), "result", Rotate.ROTATE90))

    board.connect(powerSource, c1)
    
    board.connect(c1, s1) 

    board.connect(s1, s2) 
    board.connect(s1, s2)
     
    board.connect(s2, lamp)
    
    board.connect(lamp, c_b)
    board.connect(c_b, powerSource)  
    
    board.resetVolt()
    
    rasterCount = (39, 19)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount

def createNotBoard():
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 4), "Power", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((8, 4), "c1"))
    s1 = board.addComponent(Switch.Switch((10, 4), "s1", Rotate.ROTATE90))
    n1 = board.addComponent(NotGate.NotGate((15, 4), "NOT", Rotate.ROTATE90))
    c3 = board.addComponent(Connector.Connector((18, 4), "c3"))
    c4 = board.addComponent(Connector.Connector((18, 8), "c4"))
    c5 = board.addComponent(Connector.Connector((1, 8), "c5"))

    board.connect(powerSource, c1)
    board.connect(c1, s1)
    board.connect(s1, n1)
    board.connect(n1, c3)
    board.connect(c3, c4)
    board.connect(c4, c5)
    board.connect(c5, powerSource)

    rasterCount = (40, 20)
    rasterSize = 20
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
    board, printSize, rasterCount = createTestBoard()
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
