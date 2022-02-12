import Logger
import Rotate
import SingleInputComponent


class Lamp (SingleInputComponent.SingleInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "Lamp"
    
    def output(self):
        if self.volt > 0:
            Logger.debug("Light")
        else:
            Logger.debug("No Light")
        
        Logger.debug("Lamp")
        
        
    def applyLogic(self):
        
        if self.incoming[0].isOn():
            self.volt = self.standardVolt
            Logger.debug("Lamp '{}' is on".format(self.name))
        else: 
            self.volt = 0
            Logger.debug("Lamp '{}' is off".format(self.name))
            
        self.setVolt(self.incoming[0].getVolt())
    
    def draw(self, gfx):
        connColour = gfx.getConnectorColour(self.isOn())
        connLineWidth = gfx.getConnectorLineWidth(self.isOn())
        circleWidth = 0
        if not self.isOn():
            circleWidth = gfx.getConnectorLineWidth(False)
        self.drawLineAndConnector(gfx,
                                  gfx.getConnectorColour(self.incoming[0].isOn()),
                                  gfx.getConnectorLineWidth(self.incoming[0].isOn()),
                                  (0, -1), self.getIncomingPos())
        self.drawLineAndConnector(gfx, connColour, connLineWidth, (0, 1), self.getOutgoingPos())
        gfx.drawRasterCircle(gfx.getLampColour(self.isOn()), self.localToGlobalRaster((0, 0)), 1, circleWidth)
        
        self.drawText(gfx, (-2, 0), self.name)
    
    def getIncomingPos(self, number = 0):
        return (0, -2)
    
    def getOutgoingPos(self, number = 0):
        return (0, 2)
    
    def isClickedLocalRaster(self, localRaster):
        return -1 <= localRaster[0] <= 1 and -1 <= localRaster[1] <= 1
