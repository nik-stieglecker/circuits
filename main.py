'''
Created on 12.12.2020

@author: nikst
'''

import pygame

import AndGate
import Board
import Connector
import GfxContext
import Lamp
import Logger
import OrGate
import PowerSource
from Rotate import Rotate
import Switch
import Switch12
import Switch21
import XnorGate
import XorGate


rasterInc = 10

rasterX = 0
rasterY = rasterInc

def nextPos():
    global rasterX
    global rasterY
    rasterX += rasterInc
    
    if rasterX > 73:
        rasterX = rasterInc
        rasterY += rasterInc
        
    return rasterX, rasterY

def createAndGateBoard():

    # AND gate made with 2 switches
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 3), "POWER", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((9, 3), "a", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((13, 3), "b", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((17, 3), ""))
    c2 = board.addComponent(Connector.Connector((17, 8), ""))       
    c3 = board.addComponent(Connector.Connector((1, 8), ""))
    out = board.addComponent(Lamp.Lamp((11 ,8 ), "out", Rotate.ROTATE270))        
    
    board.connect(powerSource, s1)    
    board.connect(s1, s2)
    board.connect(s2, c1)    
    board.connect(c1, c2)    
    board.connect(c2, out)
    board.connect(out, c3)    
    board.connect(c3, powerSource)
              
    rasterCount = (18, 10)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
 
    return board, printSize, rasterCount, (s1, s2)

def createOrGateBoard():

    # OR gate made with 2 switches
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 4), "POWER", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((8, 4), ""))
    s1 = board.addComponent(Switch.Switch((10, 2), "a", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((10, 6), "b", Rotate.ROTATE90))
    c2 = board.addComponent(Connector.Connector((12, 4), ""))
    c3 = board.addComponent(Connector.Connector((13, 4), ""))
    c4 = board.addComponent(Connector.Connector((13, 9), ""))
    c5 = board.addComponent(Connector.Connector((1, 9), ""))
    out = board.addComponent(Lamp.Lamp((7 , 9), "out", Rotate.ROTATE270))        

    board.connect(powerSource, c1)
    board.connect(c1, s1)
    board.connect(c1, s2)
    board.connect(s1, c2)
    board.connect(s2, c2)
    board.connect(c2, c3)
    board.connect(c3, c4)
    board.connect(c4, out)
    board.connect(out, c5)    
    board.connect(c5, powerSource)

    rasterCount = (14, 11)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
 
    return board, printSize, rasterCount, (s1, s2)

def createNotGateBoard():

    # NOT gate made with a switch
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 3), "POWER", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((10, 3), "a", Rotate.ROTATE90, True))
    c1 = board.addComponent(Connector.Connector((12, 8), ""))
    c2 = board.addComponent(Connector.Connector((1, 8), ""))
    out = board.addComponent(Lamp.Lamp((7 ,8 ), "out", Rotate.ROTATE270))        


    board.connect(powerSource, s1)
    board.connect(s1, c1)
    board.connect(c1, out)
    board.connect(out, c2)
    board.connect(c2, powerSource)
    
    
    rasterCount = (13, 10)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
 
    return board, printSize, rasterCount, s1   

def createSwitch12Board():

    # board made for presenting the toogle switch
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 10), "POWER", Rotate.ROTATE180))
    s1 = board.addComponent(Switch12.Switch12((3, 2), "a", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((1, 7), ""))
    c_weg1 = board.addComponent(Connector.Connector((5, 1), "1"))
    c_weg2 = board.addComponent(Connector.Connector((5, 3), "2"))
    
    c2 = board.addComponent(Connector.Connector((10, 1), "2"))
    c3 = board.addComponent(Connector.Connector((10, 3), "2"))
    
    c_b = board.addComponent(Connector.Connector((26, 13), ""))
     
    lamp = board.addComponent(Lamp.Lamp((24, 3), "out", Rotate.ROTATE90))

    board.connect(powerSource, c1)
    
    board.connect(c1, s1) 

    board.connect(s1, c_weg2) 
    board.connect(s1, c_weg1) 


    board.connect(c_weg2, c3)    
    board.connect(c_weg1, c2) 
    board.connect(c2, c3) 
     
    board.connect(c3, lamp)
    
    board.connect(lamp, c_b)
    board.connect(c_b, powerSource)  
    
    rasterCount = (7, 5)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, s1
    
def createXorGateBoard():

    # XOR gate made with toggle switches
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 5), "POWER", Rotate.ROTATE180))
    c1 = board.addComponent(Connector.Connector((8, 2), ""))
    s1 = board.addComponent(Switch12.Switch12((10, 2), "a", Rotate.ROTATE90))


    s2 = board.addComponent(Switch21.Switch21((20, 2), "b", Rotate.ROTATE90)) 

    c_b = board.addComponent(Connector.Connector((26, 8), ""))
     
    lamp = board.addComponent(Lamp.Lamp((24, 2), "out", Rotate.ROTATE90))

    board.connect(powerSource, c1)
    
    board.connect(c1, s1) 

    board.connect(s1, s2)
    board.connect(s1, s2) 
     
    board.connect(s2, lamp)
    
    board.connect(lamp, c_b)
    board.connect(c_b, powerSource)  
    
    
    rasterCount = (27, 9)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2)

def create2BitAddingBoard():
     
    # circuit for adding 2 bits
     
    board = Board.Board();
     
    powerSource = board.addComponent(PowerSource.PowerSource((3, 4), "POWER"))
    
    c1 = board.addComponent(Connector.Connector((3, 10), ""))
    c2 = board.addComponent(Connector.Connector((3, 16), ""))
    c3 = board.addComponent(Connector.Connector((38, 16), ""))
    c4 = board.addComponent(Connector.Connector((38, 10), ""))        
    c5 = board.addComponent(Connector.Connector((38, 1), ""))
    
    s1 = board.addComponent(Switch.Switch((7, 10), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((7, 16), "", Rotate.ROTATE90)) 
 
    andGate = board.addComponent(AndGate.AndGate((25, 16), "AND", Rotate.ROTATE90))
    xorGate = board.addComponent(XorGate.XorGate((25, 10), "XOR", Rotate.ROTATE90))

    # lamp for result
       
    lamp = board.addComponent(Lamp.Lamp((34, 10), "result", Rotate.ROTATE90))
    
    # lamp for carry bit
    
    lamp_c = board.addComponent(Lamp.Lamp((34, 16), "carry", Rotate.ROTATE90))
    
    # lamps to represent if the input is 1 or 0
    
    lamp1 = board.addComponent(Lamp.Lamp((13, 10), "a", Rotate.ROTATE90))
    lamp2 = board.addComponent(Lamp.Lamp((13, 16), "b", Rotate.ROTATE90))
 
    board.connect(powerSource, c1)
     
    board.connect(c1, s1)
    board.connect(c1, c2)
    board.connect(c2, s2)
     
    board.connect(s2, lamp2)
    board.connect(lamp2, xorGate)
     
    board.connect(s1, lamp1)
    board.connect(lamp1, xorGate)
     
    board.connect(lamp2, andGate) 
    board.connect(lamp1, andGate)         
 
    board.connect(andGate, lamp_c)
    board.connect(lamp_c, c3)
    board.connect(c3, c4)
    
    board.connect(c4, c5) 
    board.connect(xorGate, lamp)
    board.connect(lamp, c4)
    board.connect(c5, powerSource)
     
    rasterCount = (39, 19)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
 
    return board, printSize, rasterCount, (s1, s2)

def createResultBoard():

    # circuit that displays the result when adding 3 Bits.
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 6), "POWER", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((14, 2), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((14, 6), "", Rotate.ROTATE90))
    s3 = board.addComponent(Switch.Switch((14, 10), "", Rotate.ROTATE90))
    
    lamp_a = board.addComponent(Lamp.Lamp((18, 2), "a", Rotate.ROTATE90))
    lamp_b = board.addComponent(Lamp.Lamp((18, 6), "b", Rotate.ROTATE90))
    lamp_c = board.addComponent(Lamp.Lamp((18, 10), "c", Rotate.ROTATE90))

    xorGate1 = board.addComponent(XorGate.XorGate((24, 3), "XOR", Rotate.ROTATE90))
    xorGate2 = board.addComponent(XorGate.XorGate((32, 5), "XOR", Rotate.ROTATE90))
    
    out = board.addComponent(Lamp.Lamp((38, 5), "result", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((12, 2), ""))
    c2 = board.addComponent(Connector.Connector((12, 6), ""))
    c3 = board.addComponent(Connector.Connector((12, 10), ""))
    c4 = board.addComponent(Connector.Connector((27, 10), ""))
    c5 = board.addComponent(Connector.Connector((27, 6), ""))
    c6 = board.addComponent(Connector.Connector((40, 13), ""))
    c7 = board.addComponent(Connector.Connector((1, 13), ""))
    c_xnor1 = board.addComponent(Connector.Connector((20, 4), ""))
    c_xnor2 = board.addComponent(Connector.Connector((27, 4), ""))

    board.connect(powerSource, c2) 
    board.connect(c2, c1) 
    board.connect(c2, c3) 
    board.connect(c1, s1) 
    board.connect(c2, s2) 
    board.connect(c3, s3) 
    
    board.connect(s1, lamp_a)
    board.connect(s2, lamp_b)
    
    board.connect(s3, lamp_c)

    board.connect(lamp_b, c_xnor1)
    board.connect(c_xnor1, xorGate1) 
    
    board.connect(lamp_a, xorGate1)
    board.connect(lamp_c, c4)
    
    board.connect(c4, c5) 
    board.connect(c5, xorGate2)
    board.connect(xorGate1, c_xnor2)
    board.connect(c_xnor2, xorGate2) 
 
    board.connect(xorGate2, out)
    board.connect(out, c6) 
    board.connect(c6, c7)
    board.connect(c7, powerSource) 
 

    rasterCount = (42, 14)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2, s3)    

def createCarryBoard():
   
    # circuit that displays the carry bit when adding 3 Bits.
       
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 9), "POWER", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((11, 5), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((11, 9), "", Rotate.ROTATE90))
    s3 = board.addComponent(Switch.Switch((11, 13), "", Rotate.ROTATE90))
    
    lamp_a = board.addComponent(Lamp.Lamp((15, 5), "a", Rotate.ROTATE90))
    lamp_b = board.addComponent(Lamp.Lamp((15, 9), "b", Rotate.ROTATE90))
    lamp_c = board.addComponent(Lamp.Lamp((15, 13), "c", Rotate.ROTATE90))    
    
    AndGate1 = board.addComponent(AndGate.AndGate((26, 3), "AND", Rotate.ROTATE90))
    AndGate2 = board.addComponent(AndGate.AndGate((26, 9), "AND", Rotate.ROTATE90))
    AndGate3 = board.addComponent(AndGate.AndGate((26, 15), "AND", Rotate.ROTATE90))
    OrGate1 = board.addComponent(OrGate.OrGate((33, 4), "OR", Rotate.ROTATE90))
    OrGate2 = board.addComponent(OrGate.OrGate((40, 5), "OR", Rotate.ROTATE90))
    
    c_a = board.addComponent(Connector.Connector((9, 5), ""))
    c_b = board.addComponent(Connector.Connector((9, 9), ""))
    c_c = board.addComponent(Connector.Connector((9, 13), ""))
    c1 = board.addComponent(Connector.Connector((18, 5), ""))
    c2 = board.addComponent(Connector.Connector((18, 13), ""))
    c3 = board.addComponent(Connector.Connector((18, 2), ""))
    c4 = board.addComponent(Connector.Connector((18, 16), ""))
    c5 = board.addComponent(Connector.Connector((23, 5), ""))
    c6 = board.addComponent(Connector.Connector((23, 13), ""))

    c9 = board.addComponent(Connector.Connector((20, 9), ""))
    c10 = board.addComponent(Connector.Connector((20, 4), ""))    
    c11 = board.addComponent(Connector.Connector((20, 14), ""))    
    c12 = board.addComponent(Connector.Connector((36, 15), ""))    
    c13 = board.addComponent(Connector.Connector((29, 5), ""))    
    c14 = board.addComponent(Connector.Connector((36, 6), ""))    
    c15 = board.addComponent(Connector.Connector((43, 20), ""))    
    c16 = board.addComponent(Connector.Connector((1, 20), ""))    
    carry = board.addComponent(Lamp.Lamp((22, 20), "carry", Rotate.ROTATE270))

    board.connect(powerSource, c_b)
    board.connect(c_b, c_a)
    board.connect(c_b, c_c)
    board.connect(c_a, s1)
    board.connect(c_b, s2)
    board.connect(c_c, s3)
    
    board.connect(s1, lamp_a)
    board.connect(lamp_a, c1) 

    board.connect(c1, c3)
    board.connect(s3, lamp_c)
    board.connect(lamp_c, c2)
    board.connect(c2, c4)
    
    board.connect(c1, c5)
    board.connect(c2, c6)
    
    board.connect(s2, lamp_b) 
    board.connect(lamp_b, c9)
    board.connect(c9, c10)
    board.connect(c9, c11)
    
    board.connect(c10, AndGate1)
    board.connect(c3, AndGate1)
    
    board.connect(c6, AndGate2)
    board.connect(c5, AndGate2)
    
    board.connect(c4, AndGate3)
    board.connect(c11, AndGate3)

    board.connect(AndGate2, c13)
    board.connect(c13, OrGate1)    
    board.connect(AndGate1, OrGate1)

    
    board.connect(AndGate3, c12)
    board.connect(c12, c14)
    
    board.connect(c14, OrGate2)
    board.connect(OrGate1, OrGate2)
    
    board.connect(OrGate2, c15)
    board.connect(c15, carry)
    board.connect(carry, c16)
    board.connect(c16, powerSource)
    
        
    rasterCount = (44, 22)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2, s3)  

def create3BitAddingBoard():
    
    # circuit that adds 3 Bits (Combination of the circuit for the carry bit
    # and the result)
    
    board = Board.Board();

    # with addComponent() all the needed components are put on the board. 
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 24), "POWER", Rotate.ROTATE90))
    
    s1 = board.addComponent(Switch.Switch((11, 20), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((11, 24), "", Rotate.ROTATE90))
    s3 = board.addComponent(Switch.Switch((11, 28), "", Rotate.ROTATE90))
    
    AndGate1 = board.addComponent(AndGate.AndGate((33, 3), "AND", Rotate.ROTATE90))
    AndGate2 = board.addComponent(AndGate.AndGate((33, 9), "AND", Rotate.ROTATE90))
    AndGate3 = board.addComponent(AndGate.AndGate((33, 15), "AND", Rotate.ROTATE90))
    
    lamp_a = board.addComponent(Lamp.Lamp((15, 20), "a", Rotate.ROTATE90))
    lamp_b = board.addComponent(Lamp.Lamp((15, 24), "b", Rotate.ROTATE90))
    lamp_c = board.addComponent(Lamp.Lamp((15, 28), "c", Rotate.ROTATE90))
    
    
    OrGate1 = board.addComponent(OrGate.OrGate((40, 4), "OR", Rotate.ROTATE90))
    OrGate2 = board.addComponent(OrGate.OrGate((47, 5), "OR", Rotate.ROTATE90))
    
    XorGate1 = board.addComponent(XorGate.XorGate((26, 21), "XOR", Rotate.ROTATE90))
    XorGate2 = board.addComponent(XorGate.XorGate((33, 22), "XOR", Rotate.ROTATE90))

    carry = board.addComponent(Lamp.Lamp((30, 36), "carry", Rotate.ROTATE270))
    result = board.addComponent(Lamp.Lamp((30, 31), "result", Rotate.ROTATE270))

    # all the connectors used in this board are added below. 

    c_a = board.addComponent(Connector.Connector((9, 20), ""))
    c_b = board.addComponent(Connector.Connector((9, 24), ""))
    c_c = board.addComponent(Connector.Connector((9, 28), ""))

    c_x = board.addComponent(Connector.Connector((19, 22), ""))


    c1 = board.addComponent(Connector.Connector((17, 20), ""))
    c2 = board.addComponent(Connector.Connector((19, 24), ""))
    c3 = board.addComponent(Connector.Connector((21, 28), ""))
    c4 = board.addComponent(Connector.Connector((29, 28), ""))
    c5 = board.addComponent(Connector.Connector((29, 23), ""))
    c6 = board.addComponent(Connector.Connector((36, 31), ""))
    c7 = board.addComponent(Connector.Connector((22, 31), ""))
    c8 = board.addComponent(Connector.Connector((1, 31), ""))
    c9 = board.addComponent(Connector.Connector((17, 6), ""))
    c10 = board.addComponent(Connector.Connector((19, 9), ""))
    c11 = board.addComponent(Connector.Connector((21, 12), ""))
    c12 = board.addComponent(Connector.Connector((25, 6), ""))
    c13 = board.addComponent(Connector.Connector((28, 9), ""))
    c14 = board.addComponent(Connector.Connector((25, 12), ""))
    c15 = board.addComponent(Connector.Connector((30, 6), ""))
    c16 = board.addComponent(Connector.Connector((30, 12), ""))
    c17 = board.addComponent(Connector.Connector((25, 2), ""))
    c18 = board.addComponent(Connector.Connector((28, 4), ""))
    c19 = board.addComponent(Connector.Connector((25, 16), ""))
    c20 = board.addComponent(Connector.Connector((28, 14), ""))
    c21 = board.addComponent(Connector.Connector((36, 5), ""))
    c22 = board.addComponent(Connector.Connector((43, 15), ""))
    c23 = board.addComponent(Connector.Connector((43, 6), ""))
    c24 = board.addComponent(Connector.Connector((50, 36), ""))
    c25 = board.addComponent(Connector.Connector((22, 36), ""))
 
    # circuit for carry bit
    
    board.connect(powerSource, c_b)
    board.connect(c_b, c_a)
    board.connect(c_b, c_c)
    board.connect(c_a, s1)
    board.connect(c_b, s2)
    board.connect(c_c, s3)
    
    board.connect(s1, lamp_a) 
    board.connect(lamp_a, c1)
    
    board.connect(s2, lamp_b) 
    board.connect(lamp_b, c2)
    board.connect(c2, c_x)
    board.connect(c_x, c10)
    
    board.connect(s3, lamp_c)
    board.connect(lamp_c, c3)
    
    board.connect(c1, c9)
    board.connect(c3, c11)
    
    board.connect(c9, c12)
    board.connect(c12, c17)
    board.connect(c12, c15)
    
    board.connect(c10, c13)
    board.connect(c13, c18)
    board.connect(c13, c20)
    
    board.connect(c11, c14)
    board.connect(c14, c16)
    board.connect(c14, c19)

    board.connect(c18, AndGate1)    
    board.connect(c17, AndGate1)

    board.connect(c16, AndGate2)
    board.connect(c15, AndGate2)

    board.connect(c19, AndGate3)    
    board.connect(c20, AndGate3)

    board.connect(AndGate2, c21)
    board.connect(c21, OrGate1)    
    board.connect(AndGate1, OrGate1)

    
    board.connect(AndGate3, c22)
    board.connect(c22, c23)
    board.connect(c23, OrGate2)
    board.connect(OrGate1, OrGate2)
    board.connect(OrGate2, c24)
    board.connect(c24, carry)
    board.connect(carry, c25)
    board.connect(c25, c7)

    # circuit for result
    
    board.connect(c_x, XorGate1)
    board.connect(c1, XorGate1)
    board.connect(c3, c4)
    board.connect(c4, c5)
    board.connect(c5, XorGate2)
    board.connect(XorGate1, XorGate2)
    board.connect(XorGate2, c6)
    board.connect(c6, result)
    board.connect(result, c7)
    board.connect(c7, c8)
    board.connect(c8, powerSource)

    
    rasterCount = (51, 38)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2, s3)     
 
def createPrintContext(printSize, rasterCount):
    
    # This are the graphic settings used for all the images in my VWA that I
    # created. The interactive board uses different settings.
    
    printSurface = pygame.Surface(printSize)
    printContext = GfxContext.GfxContext(printSurface, rasterCount)
    printContext.setBackgroundColour((255, 255, 255))
    printContext.setRasterColour((255, 255, 255))
    printContext.setRasterColourHigh((255, 255, 255))
    printContext.setConnectorLineWidth(4)
    printContext.setConnectorColour((0, 0, 0))
    printContext.setComponentColour((0, 0, 0))
    printContext.setFontColour((0, 0, 0))
    printContext.setLampColour((0, 0, 0))
    printContext.setActiveConnectorLineWidth(4)
    printContext.setActiveConnectorColour((50, 200, 50))
    printContext.setActiveComponentColour((0, 0, 0))
    printContext.setActiveLampColour((50, 200, 50))
    
    return printContext

def main(path):
    
    pygame.init()
    pygame.font.init()
    
    Logger.setLogLevel(3)
    
    Logger.info("creating board...")

    # Here you can choose the board you want to have opened.
    
    # board, printSize, rasterCount, (s1) = createSimpleBoard()
    # board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    # board, printSize, rasterCount, s1 = createSwitch12Board()
    # board, printSize, rasterCount, () = createBitAddingBoard()
    # board, printSize, rasterCount, () = createCarryBitBoard()
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    # board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    
    printContext = createPrintContext(printSize, rasterCount)
    screenRasterFactor = 1200/printContext.getSurfaceSize()[0]
    surface = pygame.display.set_mode((round(printContext.getSurfaceSize()[0]*screenRasterFactor), round(printContext.getSurfaceSize()[1]*screenRasterFactor)))
    screenContext = GfxContext.GfxContext(surface, printContext.getRasterCount())  
    
    board.resetVolt()
    board.switchOn()
    Logger.info("finished.")
    

    
    draw(screenContext, board)
    
    # loop that executes all needed functions to open up, print, click, or close
    # a board  
    
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
                    printContext.save(path +"board.png")
                
                elif event.text == "q":
                    print ("bye")
                    return
                

                
        pygame.display.update()


def draw(g, board):
    # generates an interactive graphic surface for a board 
    # "g" is the graphic context that is used, which for example can be printContext.
    board.switchOn()
    g.clear()
    g.drawRaster()
    board.draw(g)    

def createImages(path):
    pygame.init()
    pygame.font.init()
    
    # If the function createImages() is executed, Images of all boards 
    # listed below are created. The function setClosed() changes the status
    # of the switches on the board.
        
    board, printSize, rasterCount, (s1, s2) = createAndGateBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "AND_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1, s2) = createAndGateBoard()
    s1.setClosed(True)
    s2.setClosed(True)    
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "AND_geschlossen.png")  
     
    board, printSize, rasterCount, s1 = createNotGateBoard()
    s1.setClosed(False)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "NOT_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1) = createNotGateBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "NOT_geschlossen.png")  
     
    board, printSize, rasterCount, (s1, s2) = createOrGateBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "OR_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1, s2) = createOrGateBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "OR_geschlossen.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s1.setPosition(1)    
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "XOR_oben.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s2.setPosition(1)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "XOR_unten.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s1.setPosition(1)
    s2.setPosition(1)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "XOR_wechsel1.png")  

    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s1.setPosition(0)
    s2.setPosition(0)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "XOR_wechsel2.png") 
    
    board, printSize, rasterCount, s1 = createSwitch12Board()
    s1.setPosition(1)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "Wechselschalter_oben.png")  
    
    board, printSize, rasterCount, s1 = createSwitch12Board()
    s1.setPosition(0)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "Wechselschalter_unten.png")  

    board, printSize, rasterCount, (s1, s2) = create2BitAddingBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "2Bit_Addierer_geoeffnet.png")     
    
    board, printSize, rasterCount, (s1, s2) = create2BitAddingBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "2Bit_Addierer_wechsel.png")     
    
    board, printSize, rasterCount, (s1, s2) = create2BitAddingBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "2Bit_Addierer_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createResultBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "result_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createResultBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "result_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "carry_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "carry_geschlossen1.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "carry_geschlossen2.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "3Bit_Addierer_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "3Bit_Addierer_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(path + "3Bit_Addierer_wechsel.png") 
    
    
    

# createImages() generates images of all boards listed above. 
# main() opens an interactive board (which board is opened
# can be changed in main() )
     
#main("C:/Users/nikst/ws/")
createImages("C:/Users/nikst/ws/")