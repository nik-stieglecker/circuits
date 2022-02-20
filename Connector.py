import Component
import Rotate

class Connector(Component.Component):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "Connector"    
        
    def applyLogic(self):
        volt = 0
        for i in self.incoming:
            if i.getVolt() > volt:
                volt = i.getVolt();
        
        self.setVolt(volt)
    
    def draw(self, gfx):
        colour = gfx.getConnectorColour(self.isOn())
        # self.drawConnector(gfx, colour, (0, 0))
        
        self.drawText(gfx, (0, 1), self.name)
    
    def isClickedGlobalRaster(self, globalRaster):
        return False

    
    