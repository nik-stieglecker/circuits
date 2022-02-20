import Logger
import Rotate
import SingleInputComponent


class Switch(SingleInputComponent.SingleInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0, closed = False):
        super().__init__(center, name, rotation)
        self.type = "Switch"
        self.closed = closed
    
    def setClosed(self, closed):
        self.closed = closed

    def output(self):
        Logger.debug("Switch: " + self.closed)
    
    def applyLogic(self):

        if self.incoming[0].isOn() and self.closed:
            self.setVolt(self.standardVolt)
        else: 
            self.setVolt(0)
        
    def draw(self, gfx):
        connColour = gfx.getConnectorColour(self.isOn())
        connLineWidth = gfx.getConnectorLineWidth(self.isOn())
        
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (0, -1), self.getIncomingPos())
        self.drawConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), (0, -1))
        self.drawLineAndConnector(gfx, connColour, connLineWidth, (0, 1), self.getOutgoingPos())
        self.drawConnector(gfx, connColour, (0, 1))
        
        if self.closed:
            self.drawLine(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (0, -1), (0, 1))
        else:  
            self.drawLine(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (0, -1), (1.4, 0.4))
            
        self.drawText(gfx, (-1, 0), self.name)
            
        
        
    def getIncomingPos(self, number = 0):
        return (0, -2)
    
    def getOutgoingPos(self, number = 0):
        return (0, 2)

    def isClickedLocalRaster(self, localRaster):
        return -1 <= localRaster[0] <= 1 and -2 <= localRaster[1] <= 2

    def handleClicked(self, globalRaster = None):
        self.closed = not self.closed
        Logger.info("Switch {name} closed: {closed}".format(name = self.name, closed = self.closed))
            