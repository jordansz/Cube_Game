#Main cube class the user will reference for the path
from cubePath import CubePath
import utils

class Cube():
    def __init__(self, size = 5):
        self.size = size
        self.verticies = ()
        self.edges = ()
        self.sol_path = []

    
    def __eq__(self, cube):
        print("might need this later")
        pass
    

# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
# or try making every cube a seperate item

    def generateVerticies(self):
        for x in range(0, self.size + 1):
            for y in range(0, self.size + 1):
                for z in range(0, self.size + 1):
                    self.verticies += ((x, y, z), )


    def generateEdges(self):
        self.edges = utils.generateEdges(self.size, self.verticies)


    def generatePath(self):
        pass


# render base cube with solution path highlighted
    def drawCubes(self):
        pass
    
# c = Cube(1)
# c.generateVerticies()
# c.generateEdges()
# print(c.verticies)