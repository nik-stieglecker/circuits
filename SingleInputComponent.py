import Component
import Rotate

class SingleInputComponent(Component.Component):
    
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.maxIn = 1
        self.maxOut = 0
        
    def applyLogic(self):
        if len(self.incoming) != 1:
            raise Exception("{} '{}' Wrong number of incoming. ({})".format(self.type, self.name, len(self.incoming)))

    def draw(self, gfx):
        
        compColour = gfx.getComponentColour(self.isOn())
        connColour = gfx.getConnectorColour(self.isOn())
        connLineWidth = gfx.getConnectorLineWidth(self.isOn())
        
        left, top = self.localToGlobalRaster((-2, -2))
        right, bottom = self.localToGlobalRaster((2, 2))
        gfx.drawRasterRect(compColour, (left, top), (right, bottom))
        
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (0, -2), self.getIncomingPos())
        self.drawLineAndConnector(gfx, connColour, connLineWidth, (0, 2), self.getOutgoingPos())
        
        
        
        self.drawText(gfx, (0, 0), self.name)
        
    def getIncomingPos(self, number = 0):
        return (0, -3)
    
    def getOutgoingPos(self, number = 0):
        return (0, 3)
    

        