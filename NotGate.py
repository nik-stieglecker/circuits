import Rotate
import SingleInputComponent


class NotGate(SingleInputComponent.SingleInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "NotGate"
        
    def applyLogic(self):
        if self.incoming[0].isOn():
            self.setVolt(0)
        else: 
            self.setVolt(self.standardVolt)
