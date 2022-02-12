import Logger
import Rotate
import SingleInputComponent


class PowerSource(SingleInputComponent.SingleInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.type = "PowerSource"
        self.maxIn = 1
        self.maxOut = 1    
    
    def receive(self):
        Logger.debug("Back at PowerSource, Circuit finished.")
    
    def switchOn(self, volt):
        self.volt = volt
        for out in self.outgoing:
            out.setVolt(volt)
        for out in self.outgoing:
            out.receive() 
        