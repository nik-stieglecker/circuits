class Connection:
    
    def __init__(self, fromComponent, toComponent, volt = 0):
        self.volt = volt
        self.fromComponent = fromComponent
        self.toComponent = toComponent
        self.voltThreshold = 0.5
        
    def receive(self):
        self.toComponent.receive()
        
    def hasVoltage(self):
        return self.volt is not None
    
    def isOn(self):
        return self.hasVoltage() and self.volt > self.voltThreshold
            
    def getVolt(self):
        return self.volt

    def setVolt(self, volt):
        self.volt = volt
        
    def getFromComponent(self):
        return self.fromComponent

    def setFromComponent(self, fromComponent):
        self.fromComponent = fromComponent
        
    def getToComponent(self):
        return self.toComponent

    def setToComponent(self, toComponent):
        self.toComponent = toComponent
        
    def __str__(self):
        result = "{0} - {1} Volt: {2}".format(self.fromComponent.getName(), self.toComponent.getName(), self.getVolt())
        return result
        