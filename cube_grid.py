# not now but I could consider flattening each cube and connecting them that way
import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from collections import defaultdict

#get the cube grid ready
CUBE_SIZE = 1
verticies, edges = (), ()
surfaces = defaultdict(list)

# calculate the vertices
for x in range(0, CUBE_SIZE + 1):
    for y in range(0, CUBE_SIZE + 1):
        for z in range(0, CUBE_SIZE + 1):
            verticies = verticies + ((x, y ,z), )

# function to get surrounding surfaces
# def getSurfaces(max_size, )

# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
# or try making every cube a seperate item
for vertex in verticies:
    x, y, z = vertex[0], vertex[1], vertex[2]
    if x < CUBE_SIZE - 1:
        edges = edges + ((verticies.index(vertex), verticies.index((x + 1, y, z))), )
    
    if x > 0:
        edges = edges + ((verticies.index(vertex), verticies.index((x - 1, y, z))), )

    if y < CUBE_SIZE - 1:
        edges = edges + ((verticies.index(vertex), verticies.index((x, y + 1, z))), )
    
    if y > 0:
        edges = edges + ((verticies.index(vertex), verticies.index((x, y - 1, z))), )

    if z < CUBE_SIZE - 1:
        edges = edges + ((verticies.index(vertex), verticies.index((x, y, z + 1))), )
    
    if z > 0:
        edges = edges + ((verticies.index(vertex), verticies.index((x, y, z - 1))), )

#to fill the surfaces, each connecting edge can be used as reference for 2 faces
# reminder matplotlib can probably do this
for edge in edges:
    v1, v2 = verticies[edge[0]], verticies[edge[1]]
    if(v1[0] < v2[0] or v1[0] > v2[0]):     #edge along x axis
        if(v1[1] + 1 <= CUBE_SIZE):
            surfaces[verticies.index(v1)].append((verticies.index(v1), verticies.index(v2), verticies.index((v1[0], v1[1] + 1, v1[2])), verticies.index((v2[0], v2[1] + 1, v2[2]))))
        # if(v1[1] - 1 >= 0):
        #     surfaces[verticies.index(v1)].append((verticies.index(v1), verticies.index(v2), verticies.index((v1[0], v1[1] - 1, v1[2])), verticies.index((v2[0], v2[1] - 1, v2[2]))))
    
    if(v1[1] < v2[1] or v1[1] > v2[1]):     #edge along y axis
        if(v1[2] + 1 <= CUBE_SIZE):
            surfaces[verticies.index(v1)].append((verticies.index(v1), verticies.index(v2), verticies.index((v1[0], v1[1], v1[2] + 1)), verticies.index((v2[0], v2[1], v2[2] + 1))))
    #     if(v1[2] - 1 >= 0):
    #         surfaces[verticies.index(v1)].append((verticies.index(v1), verticies.index(v2), verticies.index((v1[0], v1[1], v1[2] + 1)), verticies.index((v2[0], v2[1], v2[2] - 1))))

    if(v1[2] < v2[2] or v1[2] > v2[2]):
        if(v1[0] + 1 <= CUBE_SIZE):
            surfaces[verticies.index(v1)].append((verticies.index(v1), verticies.index(v2), verticies.index((v1[0] + 1, v1[1], v1[2])), verticies.index((v2[0] + 1, v2[1], v2[2]))))
    #     if(v1[0]) - 1 >= 0):


print(len(surfaces))




    # elif(v1[1] < v2[1]): #edge along y axis
    
    # elif(v1[2] < v2[2]): #edge along z axis

# print()
# print(verticies)
# print(edges[0])

def Cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()


def main():
    pygame.init()
    display = (1000,800)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluPerspective(90, (display[0]/display[1]), 0.1, 20.0)

    glTranslatef(0.0,0.0, -10)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(20)


main()