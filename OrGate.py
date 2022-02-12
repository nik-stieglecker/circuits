import LogicalDualInputComponent
import Rotate

class OrGate(LogicalDualInputComponent.LogicalDualInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.logicalTable = [False, True, True, True]
        self.type = "OrGate"
        