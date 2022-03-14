from enum import Enum
from collections import defaultdict

# class Directions(Enum):     # directions are based on looking from normal x,y graph, where forward
#     forward = forward            # and backward move through the z plane
#     backward = backward
#     right = right
#     left = left
#     up = up
#     down = down

DIRECTIONS = {
    0: lambda vertex: forward(vertex),
    1: lambda vertex: backward(vertex),
    2: lambda vertex: right(vertex),
    3: lambda vertex: left(vertex),
    4: lambda vertex: up(vertex),
    5: lambda vertex: down(vertex),

}

def forward():
    pass

def backward():
    pass

def right():
    pass

def left():
    pass
def up():
    pass

def down():
    pass


# find the first possible cube, start moving in front facing direction
# then back direction, then sides, then y direction.

def createLegalVertex(v, size):
    pass

def offsetVerticies(xchange, verts):
    temp = ()
    for vert in verts:
        x, y, z = vert[0], vert[1], vert[2]
        temp += ((vert[0] + xchange), vert[1], vert[2])
    return temp
    
# to fill the surfaces, each connecting edge can be used as reference for 2 faces
# this will loop through and look if each plane in the xyz planes are possible and adds them to surfaces
# reminder numpy can probably do this   

def generateEdges(size, vertices, offset):
    offset2 = size / 2.0           # for center of cube
    edges = ()
    for vertex in vertices:
        x, y, z = vertex[0], vertex[1], vertex[2]
        if x + 1 <= offset + offset2:         # vertex exist in positive x
            edges += ((vertices.index(vertex), vertices.index((x + 1, y, z))), )

        if x - 1 >= offset + offset2:         # vertex exist in negative x
            edges += ((vertices.index(vertex), vertices.index((x - 1, y, z))), )

        if y + 1 <= offset2:         # vertex exist in positive y
            edges += ((vertices.index(vertex), vertices.index((x, y + 1, z))), )

        if y - 1 >= offset2:         # vertex exist in negative y
            edges += ((vertices.index(vertex), vertices.index((x, y - 1, z))), )

        if z + 1 <= offset2:         # vertex exist in positive y
            edges += ((vertices.index(vertex), vertices.index((x, y, z + 1))), )

        if z - 1 >= offset2:         # vertex exist in negative z
            edges += ((vertices.index(vertex), vertices.index((x, y, z - 1))), )
        
    return edges