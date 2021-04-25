
import networkx as nX

class Repository:
    def __init__(self,fileName):
        self.__fileName = fileName
        self.__data = self.readNet(self.__fileName)

    # read the network details
    def readNet(self,fileName):
        g = nX.read_gml(fileName,label="id")
        return g


    def getData(self):
        return self.__data