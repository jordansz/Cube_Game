# class representing a single cube
import utils

class CubeNode():
    def __init__(self, vertex1, vertex2, max_len = 0):
        self.verticies = ()
        self.edges = ()
        self.surfaces = ()
        self.bounds = max_len 
        self.vert1 = vertex1
        self.vert2 = vertex2

    def generateEdges(self):
        self.edges = utils.generateEdges(1, self.verticies)

    def generateSurfaces(self):
        pass

    def getNeighbors():
        pass
