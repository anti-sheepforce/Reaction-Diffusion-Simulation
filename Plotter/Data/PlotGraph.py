'''
Created on 18.07.2016

@author: max
'''
import png

class PlotGraph():
    #z (start 1, ende zgrid), dann y(start -gridradius, ende +gridradius), dann x (wie y), dann t (start von vorne)
    #es laeuft also von -x,-y,1 nach -x,-y,z, dann -x, -y+1, 1 nach -x, -y+1, z ... -x, y, 1 nach -x, y, z, dann -x+1, -y, 1 nach -x+1, -y, z bis x, y, 1 nach x, y, z
    #"Steps output
    
    file = []
    grid = []
    xgrid = 3
    ygrid = 3
    zgrid = 6
    tgrid = 3
    maxConcentration = 0
    
    
    def __init__(self, dataFile, xy, z):
        self.setColorScale(dataFile)
        line = 0
        x = 0
        y = 0
        z = 0
        t = 0
        while z < self.zgrid:
            self.grid.append([])
            while y < self.ygrid:
                self.grid[z].append([])
                while x < self.xgrid:
                    self.grid[z][y].append([])
                    while t < self.tgrid:
                        self.grid[z][y][x].append([])
                        self.grid[z][y][x][t] = self.file[line]
                        t += 1
                        line += 1
                    t = 0
                    x += 1
                x = 0
                y += 1
            y = 0
            z += 1
        
        x = 0
        y = 0
        z = 0
        t = 0
        while z < self.zgrid:
            while y < self.ygrid:
                while x < self.xgrid:
                    while t < self.tgrid:
                        self.writeXYLayer(z, t)
                        self.writeXZLayer(y, t)
                        self.writeYZLayer(x, t)
                        t += 1
                    t = 0
                    x += 1
                x = 0
                y += 1
            y = 0
            z += 1
           
            
    
    

    def setColorScale(self, inFile):
        for i in xrange(len(inFile)):
            inFile[i] = float(inFile[i].replace("\n",""))
            if inFile[i] > self.maxConcentration and inFile[i] != 1000:
                self.maxConcentration = inFile[i]
        for i in xrange(len(inFile)):
            self.file.append(int(round(inFile[i] / self.maxConcentration * 255)))
        
        
    
    def writeXYLayer(self, z, t):
        layer = []
        x = 0
        y = 0
        while y < self.xgrid:
            layer.append([])
            while x < self.ygrid:
                layer[y].append(self.grid[z][y][x][t])
                x += 1
            y += 1
            x = 0
        fileOut = open("XY_" + str(z) + "_" + str(t) + ".png", 'wb')
        writer = png.Writer(len(layer[0]),len(layer), greyscale=True)
        writer.write(fileOut, layer) ; fileOut.close()
        
        
    def writeXZLayer(self, y, t):
        layer = []
        x = 0
        z = 0
        while x < self.xgrid:
            layer.append([])
            print(layer)
            while z < self.zgrid:
                layer[x].append(self.grid[z][y][x][t])
                z += 1
            x += 1
            z = 0
        fileOut = open("XZ_" + str(y) + "_" + str(t) + ".png", 'wb')
        writer = png.Writer(len(layer[0]),len(layer), greyscale=True)
        writer.write(fileOut, layer) ; fileOut.close()
        
    def writeYZLayer(self, x, t):
        layer = []
        y = 0
        z = 0
        while y < self.ygrid:
            layer.append([])
            while z < self.zgrid:
                layer[y].append(self.grid[z][y][x][t])
                z += 1
            y += 1
            z = 0
        fileOut = open("YZ_" + str(x) + "_" + str(t) + ".png", 'wb')
        writer = png.Writer(len(layer[0]),len(layer), greyscale=True)
        writer.write(fileOut, layer) ; fileOut.close()
        
            