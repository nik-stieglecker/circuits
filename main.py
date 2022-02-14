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
import NotGate
import PowerSource
from Rotate import Rotate
import Switch
import Switch12
import Switch21
import XorGate
import XnorGate
import OrGate


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

def createSimpleBoard():
    
    board = Board.Board()
    
    powerSource = board.addComponent(PowerSource.PowerSource(nextPos()))
    toLamp = board.addComponent(Connector.Connector(nextPos(), "to Lamp"))
    lamp = board.addComponent(Lamp.Lamp(nextPos()))
    fromLamp = board.addComponent(Connector.Connector(nextPos(), "from Lamp"))        
    
    board.connect(powerSource, toLamp)
    board.connect(toLamp, lamp)
    board.connect(lamp, fromLamp)
    board.connect(fromLamp, powerSource)

    rasterCount = (80, 40)
    rasterSize = 20
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
    
    return board, printSize, rasterCount

def createBitAddingBoard():
     
    board = Board.Board();
     
    powerSource = board.addComponent(PowerSource.PowerSource(nextPos(), ))
    c1 = board.addComponent(Connector.Connector(nextPos(), "to Connector"))
    c2_1 = board.addComponent(Connector.Connector(nextPos(), "to Switch 1"))            
    c2_2 = board.addComponent(Connector.Connector(nextPos(), "to Switch 2"))
    s1 = board.addComponent(Switch.Switch(nextPos(), "Switch 1"))
    s2 = board.addComponent(Switch.Switch(nextPos(), "Switch 2")) 
    c3_1 = board.addComponent(Connector.Connector(nextPos(), "to XorGate in 1"))
    c3_2 = board.addComponent(Connector.Connector(nextPos(), "to XorGate in 2"))
    xorGate = board.addComponent(XorGate.XorGate(nextPos(), ))
    c4 = board.addComponent(Connector.Connector(nextPos(), "to Lamp"))    
    lamp = board.addComponent(Lamp.Lamp(nextPos(), ))
    c5 = board.addComponent(Connector.Connector(nextPos(), "to PowerSource"))    
 
    board.connect(powerSource, c1)
 
    board.connect(c1, c2_1)
    board.connect(c2_1, s1)
    board.connect(s1, c3_1)
    board.connect(c3_1, xorGate)
     
    board.connect(c1, c2_2)
    board.connect(c2_2, s2)
    board.connect(s2, c3_2)
    board.connect(c3_2, xorGate)
     
    board.connect(xorGate, c4)
    board.connect(c4, lamp)
    board.connect(lamp, c5)
    board.connect(c5, powerSource)
     
    s1.setClosed(True)
    s2.setClosed(False)   
      
    rasterCount = (80, 40)
    rasterSize = 20
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)
    
    return board, printSize, rasterCount


def createCarryBitBoard():
     
    board = Board.Board();
     
    powerSource = board.addComponent(PowerSource.PowerSource((3, 4), "Power"))
    c1 = board.addComponent(Connector.Connector((3, 10), ""))
    c2 = board.addComponent(Connector.Connector((3, 16), ""))
    s1 = board.addComponent(Switch.Switch((7, 10), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((7, 16), "", Rotate.ROTATE90)) 
 
    andGate = board.addComponent(AndGate.AndGate((25, 16), "AND", Rotate.ROTATE90))
    c3 = board.addComponent(Connector.Connector((38, 16), ""))
    c4 = board.addComponent(Connector.Connector((38, 10), ""))
          
    xorGate = board.addComponent(XorGate.XorGate((25, 10), "XOR", Rotate.ROTATE90))   
    lamp = board.addComponent(Lamp.Lamp((34, 10), "result", Rotate.ROTATE90))
    #lamp for result
    lamp_c = board.addComponent(Lamp.Lamp((34, 16), "carry bit", Rotate.ROTATE90))
    #lamp for carrybit
    c5 = board.addComponent(Connector.Connector((38, 1), ""))
     
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

def createOrGateBoard():
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 4), "Power", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((8, 4), ""))
    s1 = board.addComponent(Switch.Switch((10, 2), "A", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((10, 6), "B", Rotate.ROTATE90))
    c2 = board.addComponent(Connector.Connector((12, 4), ""))
    c3 = board.addComponent(Connector.Connector((13, 4), ""))
    c4 = board.addComponent(Connector.Connector((13, 9), ""))
    c5 = board.addComponent(Connector.Connector((1, 9), ""))
    out = board.addComponent(Lamp.Lamp((7 , 9), "OUT", Rotate.ROTATE270))        

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

def createAndGateBoard():
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 3), "Power", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((9, 3), "A", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((13, 3), "B", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((17, 3), ""))
    c2 = board.addComponent(Connector.Connector((17, 8), ""))       
    c3 = board.addComponent(Connector.Connector((1, 8), ""))
    out = board.addComponent(Lamp.Lamp((11 ,8 ), "OUT", Rotate.ROTATE270))        
    
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

def createNotGateBoard():
    
    board = Board.Board();
    powerSource = board.addComponent(PowerSource.PowerSource((4, 3), "Power", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((10, 3), "A", Rotate.ROTATE90, True))
    c1 = board.addComponent(Connector.Connector((12, 8), ""))
    c2 = board.addComponent(Connector.Connector((1, 8), ""))
    out = board.addComponent(Lamp.Lamp((7 ,8 ), "OUT", Rotate.ROTATE270))        


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
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 10), "Power", Rotate.ROTATE180))
    s1 = board.addComponent(Switch12.Switch12((3, 2), "A", Rotate.ROTATE90))
    c1 = board.addComponent(Connector.Connector((1, 7), ""))
    c_weg1 = board.addComponent(Connector.Connector((5, 1), "1"))
    c_weg2 = board.addComponent(Connector.Connector((5, 3), "2"))

    s2 = board.addComponent(Switch21.Switch21((20, 2), "B", Rotate.ROTATE90)) 

    c_b = board.addComponent(Connector.Connector((26, 13), ""))
     
    lamp = board.addComponent(Lamp.Lamp((24, 2), "OUT", Rotate.ROTATE90))

    board.connect(powerSource, c1)
    
    board.connect(c1, s1) 

    board.connect(s1, c_weg2) 
    board.connect(s1, c_weg1) 


    board.connect(c_weg2, s2)    
    board.connect(c_weg1, s2) 
     
    board.connect(s2, lamp)
    
    board.connect(lamp, c_b)
    board.connect(c_b, powerSource)  
    
    
    rasterCount = (7, 5)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, s1
    
def createXorGateBoard():
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((3, 5), "Power", Rotate.ROTATE180))
    c1 = board.addComponent(Connector.Connector((8, 2), ""))
    s1 = board.addComponent(Switch12.Switch12((10, 2), "A", Rotate.ROTATE90))


    s2 = board.addComponent(Switch21.Switch21((20, 2), "B", Rotate.ROTATE90)) 

    c_b = board.addComponent(Connector.Connector((26, 8), ""))
     
    lamp = board.addComponent(Lamp.Lamp((24, 2), "OUT", Rotate.ROTATE90))

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

def createResultBoard():
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 6), "Power", Rotate.ROTATE90))
    s1 = board.addComponent(Switch.Switch((14, 2), "", Rotate.ROTATE90))
    s2 = board.addComponent(Switch.Switch((14, 6), "", Rotate.ROTATE90))
    s3 = board.addComponent(Switch.Switch((14, 10), "", Rotate.ROTATE90))
    
    lamp_a = board.addComponent(Lamp.Lamp((18, 2), "a", Rotate.ROTATE90))
    lamp_b = board.addComponent(Lamp.Lamp((18, 6), "b", Rotate.ROTATE90))
    lamp_c = board.addComponent(Lamp.Lamp((18, 10), "c", Rotate.ROTATE90))

    xnorGate1 = board.addComponent(XnorGate.XnorGate((24, 3), "XNOR", Rotate.ROTATE90))
    xnorGate2 = board.addComponent(XnorGate.XnorGate((32, 5), "XNOR", Rotate.ROTATE90))
    
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
    board.connect(c_xnor1, xnorGate1) 
    
    board.connect(lamp_a, xnorGate1)
    board.connect(lamp_c, c4)
    
    board.connect(c4, c5) 
    board.connect(c5, xnorGate2)
    board.connect(xnorGate1, c_xnor2)
    board.connect(c_xnor2, xnorGate2) 
 
    board.connect(xnorGate2, out)
    board.connect(out, c6) 
    board.connect(c6, c7)
    board.connect(c7, powerSource) 
 

    rasterCount = (42, 14)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2, s3)    

def createCarryBoard():
   
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 9), "Power", Rotate.ROTATE90))
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
    
    board = Board.Board();
    
    powerSource = board.addComponent(PowerSource.PowerSource((4, 24), "Power", Rotate.ROTATE90))
    
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
    
    XnorGate1 = board.addComponent(XnorGate.XnorGate((26, 21), "XNOR", Rotate.ROTATE90))
    XnorGate2 = board.addComponent(XnorGate.XnorGate((33, 22), "XNOR", Rotate.ROTATE90))

    carry = board.addComponent(Lamp.Lamp((30, 36), "carry", Rotate.ROTATE270))
    result = board.addComponent(Lamp.Lamp((30, 31), "result", Rotate.ROTATE270))

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
 
    # curcuit for carry bit
    
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

    # curcuit for result
    
    board.connect(c_x, XnorGate1)
    board.connect(c1, XnorGate1)
    board.connect(c3, c4)
    board.connect(c4, c5)
    board.connect(c5, XnorGate2)
    board.connect(XnorGate1, XnorGate2)
    board.connect(XnorGate2, c6)
    board.connect(c6, result)
    board.connect(result, c7)
    board.connect(c7, c8)
    board.connect(c8, powerSource)

    
    rasterCount = (51, 38)
    rasterSize = 80
    printSize = (rasterCount[0] * rasterSize, rasterCount[1] * rasterSize)

    return board, printSize, rasterCount, (s1, s2, s3)     
 
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
    printContext.setActiveConnectorLineWidth(6)
    printContext.setActiveConnectorColour((50, 200, 50))
    printContext.setActiveComponentColour((0, 0, 0))
    printContext.setActiveLampColour((50, 200, 50))
    
    return printContext

def main():
    
    pygame.init()
    pygame.font.init()
    
    Logger.setLogLevel(3)
    
    Logger.info("creating board...")

    
    board, printSize, rasterCount, (s1, s2) = createSwitch12Board
    # board, printSize, rasterCount, () = createBitAddingBoard()
    # board, printSize, rasterCount, () = createCarryBitBoard()
    # board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    # board, printSize, rasterCount, (s1, s2) = createCarryBitBoard()
    
    printContext = createPrintContext(printSize, rasterCount)
    screenRasterFactor = 1500/printContext.getSurfaceSize()[0]
    surface = pygame.display.set_mode((round(printContext.getSurfaceSize()[0]*screenRasterFactor), round(printContext.getSurfaceSize()[1]*screenRasterFactor)))
    screenContext = GfxContext.GfxContext(surface, printContext.getRasterCount())  
    
    board.resetVolt()
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

def createImages():
    pygame.init()
    pygame.font.init()
        
    board, printSize, rasterCount, (s1, s2) = createAndGateBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\AND_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1, s2) = createAndGateBoard()
    s1.setClosed(True)
    s2.setClosed(True)    
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\AND_geschlossen.png")  
     
    board, printSize, rasterCount, s1 = createNotGateBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\NOT_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1) = createNotGateBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\NOT_geschlossen.png")  
     
    board, printSize, rasterCount, (s1, s2) = createOrGateBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\OR_geoeffnet.png")  
     
    board, printSize, rasterCount, (s1, s2) = createOrGateBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\OR_geschlossen.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s1.setPosition(1)
    s2.setPosition(1)    
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\XOR_oben.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s1.setPosition(0)
    s2.setPosition(0)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\XOR_unten.png")  
    
    board, printSize, rasterCount, (s1, s2) = createXorGateBoard()
    s2.setPosition(1)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\XOR_wechsel.png")  
    
    board, printSize, rasterCount, s1 = createSwitch12Board()
    s1.setPosition(1)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\Wechselschalter_oben.png")  
    
    board, printSize, rasterCount, s1 = createSwitch12Board()
    s1.setPosition(0)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\Wechselschalter_unten.png")  

    board, printSize, rasterCount, (s1, s2) = createCarryBitBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\2Bit_Addierer_geoeffnet.png")     
    
    board, printSize, rasterCount, (s1, s2) = createCarryBitBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\2Bit_Addierer_wechsel.png")     
    
    board, printSize, rasterCount, (s1, s2) = createCarryBitBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\2Bit_Addierer_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createResultBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\result_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createResultBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\result_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\carry_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\carry_geschlossen1.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = createCarryBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\carry_geschlossen2.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\3Bit_Addierer_geoeffnet.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    s3.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\3Bit_Addierer_geschlossen.png") 
    
    board, printSize, rasterCount, (s1, s2, s3) = create3BitAddingBoard()
    s1.setClosed(True)
    s2.setClosed(True)
    printContext = createPrintContext(printSize, rasterCount)
    draw(printContext, board)
    printContext.save(r"C:\Users\nikst\ws\3Bit_Addierer_wechsel.png") 
    
    
    

createResultBoard
     
     
main()
#createImages()