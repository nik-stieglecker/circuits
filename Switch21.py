import DualInputComponent
import Logger
import Rotate


class Switch21(DualInputComponent.DualInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "Switch21"
        self.position = 0
    
    def output(self):
        Logger.debug("Switch21: " + self.position)
    
    def applyLogic(self):
        if self.incoming[self.position].isOn():
            self.setVolt(self.standardVolt)
        else: 
            self.setVolt(0)
        
    def propagate(self):
        self.outgoing[self.position].receive()
        self.outgoing[(self.position + 1) % 2].receive()
        
    def draw(self, gfx):
        
        connColour = gfx.getConnectorColour(self.isOn())
        connLineWidth = gfx.getConnectorLineWidth(self.isOn())
        
        (x0, y0) = self.getIncomingPos(0)
        y0 = y0 + 1
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (x0, y0), self.getIncomingPos(0))
        self.drawConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), (x0, y0))
        (x1, y1) = self.getIncomingPos(1)
        y1 = y1 + 1
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[1].isOn()), gfx.getConnectorLineWidth(self.incoming[1].isOn()), (x1, y1), self.getIncomingPos(1))
        self.drawConnector(gfx, gfx.getConnectorColour(self.incoming[1].isOn()), (x1, y1))
        
        if self.position == 0:
            self.drawLine(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (x0, y0), (0, 1))
        else:
            self.drawLine(gfx, gfx.getConnectorColour(self.incoming[1].isOn()), gfx.getConnectorLineWidth(self.incoming[1].isOn()), (x1, y1), (0, 1))

        self.drawLineAndConnector(gfx, connColour, connLineWidth, (0, 1), self.getOutgoingPos())
        self.drawConnector(gfx, connColour, (0, 1))
        
        inOn = self.isOn()
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (-1.5, -1.5), (1.5, -1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (1.5, -1.5), (1.5, 1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (1.5, 1.5), (-1.5, 1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (-1.5, 1.5), (-1.5, -1.5))            
        self.drawText(gfx, (-2, 0), self.name)
            
    def setPosition(self, position):
        self.position = position    
        
    def getIncomingPos(self, number = 0):
        positions = [(1, -2),(-1, -2)]
        return positions[number]
    
    def getOutgoingPos(self, number = 0):
        return (0, 2)

    def isClickedLocalRaster(self, localRaster):
        return -1 <= localRaster[0] <= 1 and -2 <= localRaster[1] <= 2

    def handleClicked(self, globalRaster = None):
        self.position = (self.position + 1) % 2
        Logger.info("Switch21 {name} position: {position}".format(name = self.name, position = self.position))
            