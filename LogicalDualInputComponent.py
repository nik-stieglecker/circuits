import DualInputComponent
import Rotate

class LogicalDualInputComponent(DualInputComponent.DualInputComponent):
    
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.logicalTable = []
    
    def applyLogic(self):
        super().applyLogic()
        
        index = 0
        
        if self.incoming[0].isOn():
            index += 2
        if self.incoming[1].isOn():
            index += 1
        
        if self.logicalTable[index]:
            self.setVolt(self.standardVolt)
        else: 
            self.setVolt(0)
        