import Logger
import Rotate
import SingleInputComponent


class Switch12(SingleInputComponent.SingleInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "Switch12"
        self.position = 0
    
    def output(self):
        Logger.debug("Switch12: " + self.position)
    
    def applyLogic(self):

        self.setVolt(0)
        
        self.outgoing[self.position].setVolt(self.incoming[0].getVolt())

        
    def draw(self, gfx):

        inOn = self.incoming[0].isOn()
        
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (0, -1), self.getIncomingPos())
        
        if self.position == 0:
            self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (0, -1), (-1, 1))
        else:
            self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (0, -1), (1, 1))

        outOn = inOn and self.position == 0
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(outOn), gfx.getConnectorLineWidth(outOn), (-1, 1), self.getOutgoingPos(0))

        outOn = inOn and self.position == 1
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(outOn), gfx.getConnectorLineWidth(outOn), (1, 1), self.getOutgoingPos(1))
    
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (-1.5, -1.5), (1.5, -1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (1.5, -1.5), (1.5, 1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (1.5, 1.5), (-1.5, 1.5))
        self.drawLine(gfx, gfx.getConnectorColour(inOn), gfx.getConnectorLineWidth(inOn), (-1.5, 1.5), (-1.5, -1.5))            
        self.drawText(gfx, (-2, 0), self.name)
            
    def setPosition(self, position):
        self.position = position   
        
    def getIncomingPos(self, number = 0):
        return (0, -2)
    
    def getOutgoingPos(self, number = 0):
        positions = [(-1, 2),(1, 2)]
        return positions[number]

    def isClickedLocalRaster(self, localRaster):
        return -1 <= localRaster[0] <= 1 and -2 <= localRaster[1] <= 2

    def handleClicked(self, globalRaster = None):
        self.position = (self.position + 1) % 2
        Logger.info("Switch12 {name} position: {position}".format(name = self.name, position = self.position))
            