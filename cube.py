#Main cube class the user will reference for the path
from cubePath import CubePath
import utils

from OpenGL.GL import *
from OpenGL.GLU import *

class Cube():
    def __init__(self, size = 5):
        self.size = size
        self.vertices = ()
        self.edges = ()
        self.sol_path = []

    
    def __eq__(self, cube):
        print("might need this later")
        pass
    

# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
# or try making every cube a seperate item

    def generatevertices(self):
        for x in range(0, self.size + 1):
            for y in range(0, self.size + 1):
                for z in range(0, self.size + 1):
                    self.vertices += ((x, y, z), )


    def generateEdges(self):
        self.edges = utils.generateEdges(self.size, self.vertices)


    def generatePath(self):
        pass


# render base cube with solution path highlighted
    # def drawCube(self):
    #     glBegin(GL_LINES)     # not GL_LINES is changed to GL_QUADS for surfaces
    #     for edge in self.edges:
    #         for vertex in edge:
    #             glColor3fv((0.1, 0.1, 0.2))
    #             glVertex3fv(self.vertices[vertex])
    #     glEnd()
    
# c = Cube(1)
# c.generatevertices()
# c.generateEdges()
# print(c.vertices)