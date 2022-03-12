import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

from collections import defaultdict

#Screen size
WIDTH = 1000
HEIGHT = 600

#get the cube grid ready
CUBE_SIZE = 1
centered = CUBE_SIZE / 2
vertices, edges = (), ()
surfaces = ()

# calculate the vertices
for x in range(0, CUBE_SIZE + 1):
    for y in range(0, CUBE_SIZE + 1):
        for z in range(0, CUBE_SIZE + 1):
            vertices = vertices + ((x - centered, y - centered ,z - centered), )


# calculate the edges from each connected vertex
# theres probably a better way but this is the best I could come up with quickly
# or try making every cube a seperate item
for vertex in vertices:
    x, y, z = vertex[0], vertex[1], vertex[2]
    if x < CUBE_SIZE - 1:
        edges = edges + ((vertices.index(vertex), vertices.index((x + 1, y, z))), )
    
    if x > 0:
        edges = edges + ((vertices.index(vertex), vertices.index((x - 1, y, z))), )

    if y < CUBE_SIZE - 1:
        edges = edges + ((vertices.index(vertex), vertices.index((x, y + 1, z))), )
    
    if y > 0:
        edges = edges + ((vertices.index(vertex), vertices.index((x, y - 1, z))), )

    if z < CUBE_SIZE - 1:
        edges = edges + ((vertices.index(vertex), vertices.index((x, y, z + 1))), )
    
    if z > 0:
        edges = edges + ((vertices.index(vertex), vertices.index((x, y, z - 1))), )

# to fill the surfaces, each connecting edge can be used as reference for 2 faces
# this will loop through and look if each plane in the xyz planes are possible and adds them to surfaces
# reminder matplotlib can probably do this

for edge in edges:
    v1, v2 = vertices[edge[0]], vertices[edge[1]]
    if(v1[0] < v2[0] or v1[0] > v2[0]):     #edge along x axis, creates plane in reference to y (face to back of face)
        if(v1[1] + 1 <= CUBE_SIZE):
            surfaces += ((vertices.index(v1), vertices.index(v2), vertices.index((v1[0], v1[1] + 1, v1[2])), vertices.index((v2[0], v2[1] + 1, v2[2]))), )
   
    if(v1[1] < v2[1] or v1[1] > v2[1]):     #edge along y axis, creates plane in reference to z (side by side planes)
        if(v1[2] + 1 <= CUBE_SIZE):
            surfaces += ((vertices.index(v1), vertices.index(v2), vertices.index((v1[0], v1[1], v1[2] + 1)), vertices.index((v2[0], v2[1], v2[2] + 1))), )

    if(v1[2] < v2[2] or v1[2] > v2[2]):     #edge along z axis, creates plane in reference to x (top and bottom planes)
        if(v1[0] + 1 <= CUBE_SIZE):
            surfaces += ((vertices.index(v1), vertices.index(v2), vertices.index((v1[0] + 1, v1[1], v1[2])), vertices.index((v2[0] + 1, v2[1], v2[2]))), )


def drawCube():
    glBegin(GL_LINES)     # not GL_LINES is changed to GL_QUADS for surfaces
    for edge in edges:
        for vertex in edge:
            glColor3fv((0.1, 0.1, 0.2))
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    screen_surface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    # gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)
    gluPerspective(90, (display[0]/display[1]), 0.1, 20.0)


    glTranslatef((WIDTH - (WIDTH + CUBE_SIZE)) * 2, 0.0, -10.0)
    axis_rotate_count = 0
    print(vertices)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # if(axis_rotate_count < 250):
        #     glRotatef(0.4, 1, 0, 1)
        
        # elif(axis_rotate_count >= 250):
        #     glRotatef(0.4, -1, 0, -1)
        # if axis_rotate_count > 500:
        #     axis_rotate_count = 0

        # axis_rotate_count += 1
        # print(axis_rotate_count)
        glClearColor(0.7, 0.7, 0.7, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawCube()
        pygame.display.flip()
        pygame.time.wait(10)


main()