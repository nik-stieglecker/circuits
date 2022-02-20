import pygame

class GfxContext():
    
    def __init__(self, surface, rasterCount):  

        self.surfaceSize = (surface.get_width(), surface.get_height()) 
        self.rasterSize = (self.surfaceSize[0] / rasterCount[0], self.surfaceSize[1] / rasterCount[1])
        self.rasterCount = rasterCount
        self.surface = surface
        self.backgroundColour = (0, 0, 0)
        self.rasterColour = (32, 32, 32)
        self.rasterColourHigh = (64, 64, 64)
        self.rasterLineWidth = 1
        self.connectorLineWidth = 1
        self.connectorColour = (128, 128, 128)
        self.componentColour = (128, 128, 128)   
        self.lampColour = (128, 128, 128)     
        self.activeConnectorLineWidth = 1
        self.activeConnectorColour = (0, 200, 0)
        self.activeComponentColour = (0, 200, 0)
        self.activeLampColour = (255, 255, 0)
        self.font = pygame.font.SysFont('Arial', int(self.rasterSize[1] * 0.75))
        self.fontColour = self.componentColour

    def getSurfaceSize(self):
        return self.surfaceSize
    
    def getRasterCount(self):
        return self.rasterCount
    
    def save(self, path):
        pygame.image.save(self.surface, path)
    
    def rasterToSurface(self, raster):
        return (raster[0] * self.rasterSize[0], raster[1] * self.rasterSize[1])
    
    def surfaceToRaster(self, surface):
        return (surface[0]/ self.rasterSize[0], surface[1] / self.rasterSize[1])
    
    def clear(self):
        self.surface.fill(self.backgroundColour)
        
    def drawRaster(self):
        X = 0
        Y = 1
        
        leftTop = self.rasterToSurface((0, 0))
        rightTop = self.rasterToSurface((self.rasterCount[X], 0))
        rightBottom = self.rasterToSurface((self.rasterCount[X], self.rasterCount[Y]))
        leftBottom = self.rasterToSurface((0, self.rasterCount[Y]))
        
        pygame.draw.line(self.surface, self.rasterColour, leftTop, rightTop, self.rasterLineWidth)
        pygame.draw.line(self.surface, self.rasterColour, rightTop, rightBottom, self.rasterLineWidth)
        pygame.draw.line(self.surface, self.rasterColour, rightBottom, leftBottom, self.rasterLineWidth)        
        pygame.draw.line(self.surface, self.rasterColour, leftBottom, leftTop, self.rasterLineWidth)
        
        lx = 2
        ly = 2
        
        for y in range(0, self.rasterCount[Y] + 1):
            for x in range(0, self.rasterCount[X] + 1):
                color = self.rasterColour
                if x % 5 == 0 or y % 5 == 0:
                    color = self.rasterColourHigh
                cx, cy = self.rasterToSurface((x, y))
                if x == 0:
                    pygame.draw.line(self.surface, color, (cx, cy), (cx + lx, cy), self.rasterLineWidth) 
                elif x == self.rasterCount[X]:
                    pygame.draw.line(self.surface, color, (cx - lx, cy), (cx, cy), self.rasterLineWidth)
                else:
                    pygame.draw.line(self.surface, color, (cx - lx, cy), (cx + lx, cy), self.rasterLineWidth)
                if y == 0:
                    pygame.draw.line(self.surface, color, (cx, cy), (cx, cy + ly), self.rasterLineWidth)   
                elif y == self.rasterCount[Y]:
                    pygame.draw.line(self.surface, color, (cx, cy - ly), (cx, cy), self.rasterLineWidth)
                else:                 
                    pygame.draw.line(self.surface, color, (cx, cy - ly), (cx, cy + ly), self.rasterLineWidth)
    
    def drawRasterLine(self, colour, width, start, end):
        """Draw line in raster coordinates."""
        # print ("Draw line start: {0} end: {1} width: {2} colour: {3}".format(start, end, width, colour))
        pygame.draw.line(self.surface, colour, self.rasterToSurface(start), self.rasterToSurface(end), width)
    
    def drawRasterCircle(self, colour, pos, radius, width):
        pygame.draw.circle(self.surface, colour, self.rasterToSurface(pos), self.rasterSize[1] * radius, width)      

    def drawRasterRect(self, colour, leftTop, rightBottom):
        """Draw rectangle in raster coordinates.
        
        Note: Rect is also in raster units.
        """
        (left, top) = self.rasterToSurface(leftTop)
        (right, bottom) = self.rasterToSurface(rightBottom)
        if left > right:
            left, right = right, left
        
        if top > bottom:
            top, bottom = bottom, top
        pygame.draw.rect(self.surface, colour, (left, top, right - left, bottom - top), 1)

            
    def drawRasterText(self, center, text):
        
        textsurface = self.font.render(text, True, self.fontColour)
        (textsurface_size) = textsurface.get_size()
        surfaceCenter = self.rasterToSurface(center)
        self.surface.blit(textsurface, (surfaceCenter[0] - textsurface_size[0]/2, surfaceCenter[1]-textsurface_size[1]/2))
    
    def getWindow(self):
        return self.surface
    
    def getConnectorLineWidth(self, active):
        if active:
            return self.activeConnectorLineWidth
        else:
            return self.connectorLineWidth
    
    def setConnectorLineWidth(self, connectorLineWidth):
        self.connectorLineWidth = connectorLineWidth
        
    def setActiveConnectorLineWidth(self, activeConnectorLineWidth):
        self.activeConnectorLineWidth = activeConnectorLineWidth

    def setRasterColour(self, rasterColour):
        self.rasterColour = rasterColour
        
    def setRasterColourHigh(self, rasterColourHigh):
        self.rasterColourHigh = rasterColourHigh
    
    def getRasterColour(self):
        return self.rasterColour
    
    def getConnectorColour(self, active):
        if active:
            return self.activeConnectorColour
        else:
            return self.connectorColour

    def setConnectorColour(self, connectorColour):
        self.connectorColour = connectorColour

    def setActiveConnectorColour(self, activeConnectorColour):
        self.activeConnectorColour = activeConnectorColour

    def getComponentColour(self, active):
        if active:
            return self.activeComponentColour
        else:
            return self.componentColour
        
    def setComponentColour(self, componentColour):
        self.componentColour = componentColour

    def setActiveComponentColour(self, activeComponentColour):
        self.activeComponentColour = activeComponentColour

        
    def getLampColour(self, active):
        if active:
            return self.activeLampColour
        else:
            return self.lampColour

    def setLampColour(self, lampColour):
        self.lampColour = lampColour

    def setActiveLampColour(self, activeLampColour):
        self.activeLampColour = activeLampColour
    
    def getFont(self):
        return self.font
    
    def setFont(self, font):
        self.font = font
    
    def getFontColour(self):
        return self.fontColour
    
    def setFontColour(self, fontColour):
        self.fontColour = fontColour
    
    def getBackgroundColour(self):
        return self.backgroundColour
    
    def setBackgroundColour(self, backgroundColour):
        self.backgroundColour = backgroundColour
    


    

        
        
        
        
        
    