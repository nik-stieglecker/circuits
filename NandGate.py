import LogicalDualInputComponent
import Rotate

class NandGate(LogicalDualInputComponent.LogicalDualInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.logicalTable = [True, False, False, False]
        self.type = "NandGate"
