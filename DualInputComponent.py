import Component
import Rotate

class DualInputComponent(Component.Component):
    
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.maxIn = 2
        self.maxOut = 1
    
    def applyLogic(self):
        if len(self.incoming) != 2:
            raise Exception("{} '{}' Wrong number of incoming. ({})".format(self.type, self.name, len(self.incoming))) 
    
    def draw(self, gfx):

        compColour = gfx.getComponentColour(self.isOn())
        connColour = gfx.getConnectorColour(self.isOn())
        connLineWidth = gfx.getConnectorLineWidth(self.isOn())
        left, top = self.localToGlobalRaster((-2, -2))
        right, bottom = self.localToGlobalRaster((2, 2))
        gfx.drawRasterRect(compColour, connLineWidth, (left, top), (right, bottom))
        
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[0].isOn()), gfx.getConnectorLineWidth(self.incoming[0].isOn()), (-1, -2), self.getIncomingPos(0))
        self.drawLineAndConnector(gfx, gfx.getConnectorColour(self.incoming[1].isOn()), gfx.getConnectorLineWidth(self.incoming[1].isOn()), (1, -2), self.getIncomingPos(1))
        self.drawLineAndConnector(gfx, connColour, connLineWidth, (0, 2), self.getOutgoingPos())
        
        self.drawText(gfx, (0, 0), self.name)
        


    def getIncomingPos(self, number):
        positions = [(-1, -3),(1, -3)]
        return positions[number]

    def getOutgoingPos(self, number = 0):
        return (0, 3)
    
        