#Main cube class the user will reference for the path
from cubePath import CubePath
import utils

from OpenGL.GL import *
from OpenGL.GLU import *

class Cube():
    def __init__(self, size, center_pos):
        self.center_pos = center_pos
        self.size = size
        self.vertices = ()
        self.edges = ()
        self.surfaces = ()
        self.sol_path = []
        self.rotation = [0, 0, 0, 0]
        self.generatevertices()
        self.generateEdges()

    
    def __eq__(self, cube):
        print("might need this later")
        pass
    

# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
# or try making every cube a seperate item

    def generatevertices(self):
        offset = self.size / 2.0
        for x in range(0, self.size + 1):
            for y in range(0, self.size + 1):
                for z in range(0, self.size + 1):
                    self.vertices += ((x - offset + self.center_pos[0], y - offset + self.center_pos[1], z - offset + self.center_pos[2]), )


    def generateEdges(self):
        # self.edges = utils.generateEdges(self.size, self.vertices, self.offset)
        offset = self.size - (self.size / 2.0)           # for range of cube
        for vertex in self.vertices:
            x,y, z = vertex[0], vertex[1], vertex[2]
            if x + 1 <= offset + self.center_pos[0]:         # vertex exist in positive x
                self.edges += ((self.vertices.index(vertex), self.vertices.index((x + 1, y, z))), )

            # if x - 1 > -offset:         # vertex exist in negative x
            #     self.edges += ((self.vertices.index(vertex), self.vertices.index((x - 1, y, z))), )

            if y + 1 <= offset + self.center_pos[1]:         # vertex exist in positive y
                self.edges += ((self.vertices.index(vertex), self.vertices.index((x, y + 1, z))), )

            # if y - 1 > -offset:         # vertex exist in negative y
            #     self.edges += ((self.vertices.index(vertex), self.vertices.index((x, y - 1, z))), )

            if z + 1 <= offset + self.center_pos[2]:         # vertex exist in positive y
                self.edges += ((self.vertices.index(vertex), self.vertices.index((x, y, z + 1))), )

            # if z - 1 > -offset:         # vertex exist in negative z
            #     self.edges += ((self.vertices.index(vertex), self.vertices.index((x, y, z - 1))), )


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