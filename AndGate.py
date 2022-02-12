import LogicalDualInputComponent
import Rotate

class AndGate(LogicalDualInputComponent.LogicalDualInputComponent):
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        super().__init__(center, name, rotation)
        self.logicalTable = [False, False, False, True]
        self.type = "AndGate"
