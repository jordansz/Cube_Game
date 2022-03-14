#Main cube class the user will reference for the path
from cubePath import CubePath
import utils

from OpenGL.GL import *
from OpenGL.GLU import *

class Cube():
    def __init__(self, size = 5, offset = 0):
        self.size = size
        self.vertices = ()
        self.edges = ()
        self.sol_path = []
        self.surfaces = ()
        self.offset = offset
    
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
                    self.vertices += ((x - self.size / 2 + self.offset, y - self.size / 2, z - self.size /2), )


    def generateEdges(self):
        self.edges = utils.generateEdges(self.size, self.vertices, self.offset)


    def generatePath(self):
        pass


    def generateSurfaces(self):
        for edge in self.edges:
            v1, v2 = self.vertices[edge[0]], self.vertices[edge[1]]
            if(v1[0] < v2[0] or v1[0] > v2[0]):     #edge along x axis, creates plane in reference to y (face to back of face)
                if(v1[1] + 1 <= self.size / 2):
                    self.surfaces += ((self.vertices.index(v1), self.vertices.index(v2), self.vertices.index((v1[0], v1[1] + 1, v1[2])), self.vertices.index((v2[0], v2[1] + 1, v2[2]))), )
        
            if(v1[1] < v2[1] or v1[1] > v2[1]):     #edge along y axis, creates plane in reference to z (side by side planes)
                if(v1[2] + 1 <= self.size / 2):
                    self.surfaces += ((self.vertices.index(v1), self.vertices.index(v2), self.vertices.index((v1[0], v1[1], v1[2] + 1)), self.vertices.index((v2[0], v2[1], v2[2] + 1))), )

            if(v1[2] < v2[2] or v1[2] > v2[2]):     #edge along z axis, creates plane in reference to x (top and bottom planes)
                if(v1[0] + 1 <= self.size / 2):
                    self.surfaces += ((self.vertices.index(v1), self.vertices.index(v2), self.vertices.index((v1[0] + 1, v1[1], v1[2])), self.vertices.index((v2[0] + 1, v2[1], v2[2]))), )


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