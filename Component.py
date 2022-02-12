import pygame

import Logger
import Rotate


class Component:
    
    def __init__(self, center, name = "", rotation = Rotate.Rotate.ROTATE0):
        self.type = "Component"
        self.name = name
        self.incoming = []
        self.outgoing = []
        self.maxIn = 0
        self.maxOut = 0
        self.center = center
        self.rotation = rotation
        self.standardVolt = 5.0
    
    def getCenter(self):
        return self.center
    
    def setCenter(self, center):
        self.center = center
    
    def getName(self):
        return self.name
    
    def getRotation(self):
        return self.rotation
    
    def setRotation(self, rotation):
        self.rotation = rotation

    def addOutgoing(self, connection):
        if self.maxOut == 0 or len(self.outgoing) < self.maxOut:
            self.outgoing.append(connection)
        else:
            raise Exception("{} '{}' Max outgoing reached ({})".format(self.type, self.name, self.maxOut)) 
    
    def addIncoming(self, connection):
        if self.maxIn == 0 or len(self.incoming) < self.maxIn:
            self.incoming.append(connection)
        else:
            raise Exception("{} '{}' Max incoming reached ({})".format(self.type, self.name, self.maxIn)) 
    
    def setIncoming(self, index, connection):
        if self.maxIn == 0 or index < self.maxIn:
            self.incoming[index] = connection
        else:
            raise Exception("{} '{}' Max outgoing reached ({})".format(self.type, self.name, self.maxOut)) 
        
    def output(self):
        Logger.debug("Component: {}".format(self.type))

    def setVolt(self, volt):
        for o in self.outgoing:
            o.setVolt(volt)

    def isOn(self):
        result = False
        for o in self.outgoing:
            if o.isOn():
                result = True
                break
        return result

    def receive(self):
        ready = True
        for i in self.incoming:
            if not i.hasVoltage():
                ready = False
                break
            
        if ready:
            self.applyLogic()
            for out in self.outgoing:
                out.receive() 
    
    def applyLogic(self):
        raise Exception("Not implemented")
    
    def localToGlobalRaster(self, raster):
        if self.rotation == Rotate.Rotate.ROTATE0:
            return self.center[0] + raster[0], self.center[1] + raster[1]
        elif self.rotation == Rotate.Rotate.ROTATE90:
            return self.center[0] + raster[1], self.center[1] - raster[0]
        elif self.rotation == Rotate.Rotate.ROTATE180:
            return self.center[0] - raster[0], self.center[1] - raster[1]
        elif self.rotation == Rotate.Rotate.ROTATE270:
            return self.center[0] - raster[1], self.center[1] + raster[0]
    
    def globalToLocalRaster(self, raster):
        lx, ly = raster[0] - self.center[0], raster[1] - self.center[1]
        if self.rotation == Rotate.Rotate.ROTATE0:
            return lx, ly        
        elif self.rotation == Rotate.Rotate.ROTATE90:
            return -ly, lx
        elif self.rotation == Rotate.Rotate.ROTATE180:
            return -lx, -ly
        elif self.rotation == Rotate.Rotate.ROTATE270:
            return ly, -lx

    def localRasterToSurface(self, gfx, raster):
        return gfx.rasterToSurface(self.localToGlobalRaster(raster))
    
    def drawConnections(self, gfx):
        number = 0
        for o in self.outgoing:
            start = self.getOutgoingPos(number)
            # end = o.getIncomingPosByComponent(self)
            toComponent = o.getToComponent()
            end = toComponent.getIncomingPosByConnection(o)
            gfx.drawRasterLine(gfx.getConnectorColour(o.isOn()), gfx.getConnectorLineWidth(o.isOn()), self.localToGlobalRaster(start), toComponent.localToGlobalRaster(end))
            number += 1
    
    def drawLine(self, gfx, colour, width, start, end):
        gfx.drawRasterLine(colour, width, self.localToGlobalRaster(start), self.localToGlobalRaster(end))
    
    def drawLineAndConnector(self, gfx, colour, width, start, end):
        self.drawLine(gfx, colour, width, start, end)
        self.drawConnector(gfx, colour, end)
    
    def drawConnector(self, gfx, colour, pos):
        gfx.drawRasterCircle(colour, self.localToGlobalRaster(pos), 0.1, 0)
        
    def drawText(self, gfx, center, text):
        gfx.drawRasterText(self.localToGlobalRaster(center), text)
        
    def getIncomingPosByConnection(self, connection):
        result = None
        number = 0
        for i in self.incoming:
            if i == connection:
                result = self.getIncomingPos(number)
                break
            number += 1
        return result
      
    def getIncomingPos(self, number):
        return (0, 0)
    
    def getOutgoingPos(self, number):
        return (0, 0)
    
    def isClickedGlobalRaster(self, globalRaster):
        localRaster = self.globalToLocalRaster(globalRaster)
        return self.isClickedLocalRaster(localRaster)
    
    def isClickedLocalRaster(self, localRaster):
        return -2 <= localRaster[0] <= 2 and -2 <= localRaster[1] <= 2
    
    def handleClicked(self, globalRaster = None):
        Logger.debug("component {name} was clicked".format(name = self.name))
            
    
    def __str__(self):
        result = "Component {0}".format(self.name)
        for i in self.incoming:
            result += "\n"
            result += "    <: {0}".format(i)
        for o in self.outgoing:
            result += "\n"
            result += "    >: {0}".format(o)
        return result
            
    
    
          
    
       
            