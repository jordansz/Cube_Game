import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

#get the cube grid ready
CUBE_SIZE = 1
verticies = ()
edges = set()

# calculate the vertices
for x in range(0, CUBE_SIZE + 1):
    for y in range(0, CUBE_SIZE + 1):
        for z in range(0, CUBE_SIZE + 1):
            verticies = verticies + ((x, y ,z), )

# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
for vertex in verticies:
    x, y, z = vertex[0], vertex[1], vertex[2]
    if x < CUBE_SIZE - 1:
        edges.add((verticies.index(vertex), verticies.index((x + 1, y, z))) )
    
    if x > 0:
        edges.add((verticies.index(vertex), verticies.index((x - 1, y, z))))

    if y < CUBE_SIZE - 1:
        edges.add((verticies.index(vertex), verticies.index((x, y + 1, z))))
    
    if y > 0:
        edges.add((verticies.index(vertex), verticies.index((x, y - 1, z))))

    if z < CUBE_SIZE - 1:
        edges.add((verticies.index(vertex), verticies.index((x, y, z + 1))))
    
    if z > 0:
        edges.add((verticies.index(vertex), verticies.index((x, y, z - 1))))

edges = tuple(set(edges))

print(len(edges))

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
    gluPerspective(135, (display[0]/display[1]), 0.1, 20.0)

    glTranslatef(0.0,0.0, -5)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        Cube()
        pygame.display.flip()
        pygame.time.wait(10)


main()