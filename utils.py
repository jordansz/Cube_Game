from enum import Enum

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


# to fill the surfaces, each connecting edge can be used as reference for 2 faces
# this will loop through and look if each plane in the xyz planes are possible and adds them to surfaces
# reminder matplotlib can probably do this   

def generateEdges(size, verticies):
    edges = ()
    for vertex in verticies:
        x, y, z = vertex[0], vertex[1], vertex[2]
        if x < size - 1:
            edges += ((verticies.index(vertex), verticies.index((x + 1, y, z))), )

        if x > 0:
            edges += ((verticies.index(vertex), verticies.index((x - 1, y, z))), )

        if y < size- 1:
            edges += ((verticies.index(vertex), verticies.index((x, y + 1, z))), )

        if y > 0:
            edges += ((verticies.index(vertex), verticies.index((x, y - 1, z))), )

        if z < size - 1:
            edges += ((verticies.index(vertex), verticies.index((x, y, z + 1))), )

        if z > 0:
            edges += ((verticies.index(vertex), verticies.index((x, y, z - 1))), )
        
    return edges