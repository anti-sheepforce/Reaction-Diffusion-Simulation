'''
Created on 22.01.2016

@author: maximilian
'''



class BlockGenerator:
   
    commentTag = "//"
    startTags = ["***reactions", "***startingconcentrations", "***reactionrateconstants", "***integrationmethod", "***integrationstepwidth"]
    endTag = "***end"
    clean = []
    foundBlocks = []
    blocks = []
    minimumInfo = False
   
    def __init__(self, sourceFile):
        self.clean = self.cleanData(sourceFile)     #entferne stoerende Zeilen aus den Rohdaten
        self.generateBlocks()
        completedata = "***reactions" in self.foundBlocks and "***startingconcentrations" in self.foundBlocks and "***reactionrateconstants" in self.foundBlocks 
        self.minimumInfo = completedata and len(self.blocks[self.foundBlocks.index("***reactions")]) == len(self.blocks[self.foundBlocks.index("***reactionrateconstants")])
    
    def cleanData(self, data):
        i = 0
        while i < len(data):
            data[i] = data[i].replace(" ","") #entferne saemtliche Leerzeichen aus der Reaktionsgleichung
            data[i] = data[i].replace("\n","")#entferne Zeilenumbrueche
            if data[i][0:len(self.commentTag)] == self.commentTag:  #mache Kommentare zu Leerzeilen
                data[i] = "" 
            i = i + 1    
        while "" in data:       #entferne Leerzeilen
            data.remove("")                        
        return data 
    
    def generateBlocks(self):
        storage = []                                        #Zwischenspeicher fuer den gerade bearbeiteten Block
        i = 0
        while i < len(self.clean):
            if self.clean[i] in self.startTags:             #suche nach einem Blockanfang
                self.foundBlocks.append(self.clean[i])      #notiere, welche Blocks in welcher Reihenfolge gefunden wurden
                i += 1
                while self.clean[i] != self.endTag:         #lade alles zwischen Anfangs- und Endtag in den storage
                    storage.append(self.clean[i])
                    i += 1
                self.blocks.append(storage)                 #und wenn der Endtag erreicht ist den storage in die Blockliste
                storage = []                                # dann setze den storage zurueck
            i += 1
    
   
    def getReactions(self):
        return self.blocks[self.foundBlocks.index("***reactions")]  
    
    def getConcentrations(self):
        return self.blocks[self.foundBlocks.index("***startingconcentrations")]  
    
    def getRateConstants(self):
        return self.blocks[self.foundBlocks.index("***reactionrateconstants")]                    
       