from PowerSource import PowerSource
import Connection

class Board:    
    def __init__(self):
        self.components = []
        self.powerSource = None
    
    def addComponent(self, component):
        if isinstance(component, PowerSource):
            if self.powerSource is not None:
                raise Exception("PowerSource was already defined, only one is allowed")
            else:
                self.powerSource = component
        self.components.append(component)
        return component
    
    def connect(self, component1, component2):
        connection = Connection.Connection(component1, component2)
        component1.addOutgoing(connection)
        component2.addIncoming(connection)
    
    def switchOn(self):
        self.resetVolt()
        self.powerSource.switchOn(5.0)
    
    def resetVolt(self):
        for component in self.components:
            component.setVolt(None)
    
    def draw(self, gfx):
        for c in self.components:
            c.draw(gfx)
            c.drawConnections(gfx)
            
    
    def getComponents(self):
        return self.components
    
    def getClicked(self, globalRaster):
        for component in self.components:
            if component.isClickedGlobalRaster(globalRaster):
                return component
        return None
            
    def __str__(self):
        result = "Board"
        for c in self.components:
            result += "\n"
            result += "  {0}".format(c)
        return result
            
            
            