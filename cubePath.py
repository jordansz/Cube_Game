#class that is a subset path within the main Cube (the solution) or user input
# import cubeNode
import random
import utils
import cubeNode

class CubePath():
    def __init__(self):
        self.cube_count = 0
        self.path = []
        self.valid_next = [] # for a clear path the line should be atleast one square away from other vertices

    def generatePath(self, size):
        temp = [0, random.randrange(0, size + 1), random.randrange(0, size + 1)]   # one cord. at 0 guarentees outside cube start
        random.shuffle(temp)
        start_vertex = tuple(temp)
        cube1 = utils.createLegalVertex(start_vertex, size)
#         print(start_vertex)

# c = CubePath()
# c.generatePath(2)

# print(c.path)
