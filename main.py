from curses import KEY_DOWN
# from turtle import width
import pygame
from pygame.locals import *
import math
import copy

from cube import Cube
import utils

from OpenGL.GL import *
from OpenGL.GLU import *
import numpy as np
# colors and screen details
WIDTH, HEIGHT = 1000, 600
display = (WIDTH, HEIGHT)
CUBE_SIZE = 5

# for mouse movement
lastPosX = 0
lastPosY = 0
xRot = 0
yRot = 0
zRot = 0

GRID_SIZE = 10
GRID_CENTER = GRID_SIZE / 2.0
grid_vertices = ()
grid_edges = ()

for x in np.arange(-GRID_CENTER, GRID_CENTER + 1, 1.0):
    for z in np.arange(-GRID_CENTER, GRID_CENTER + 1, 1.0):
        grid_vertices += ((x, 0.0, z), )
# for x in range(0, GRID_SIZE + 1):
#     for z in range(0, GRID_SIZE + 1):
#         grid_vertices += ((x - GRID_CENTER, 0.0, z - GRID_CENTER + 1), )

for vertex in grid_vertices:
    x, z = vertex[0], vertex[2]
    if x + 1 <= GRID_CENTER:
        grid_edges += ((grid_vertices.index(vertex), grid_vertices.index((x + 1.0, 0.0, z))), )

    if x - 1 >= -GRID_CENTER:
        grid_edges += ((grid_vertices.index(vertex), grid_vertices.index((x - 1, 0.0, z))), )

    if z + 1 <= GRID_CENTER:         # vertex exist in positive y
        grid_edges += ((grid_vertices.index(vertex), grid_vertices.index((x, 0.0, z + 1))), )

    if z - 1 >= -GRID_CENTER:         # vertex exist in negative z
        grid_edges += ((grid_vertices.index(vertex), grid_vertices.index((x, 0.0, z - 1))), )



def mouseMovement(event):
    global lastPosX, lastPosY, xRot, yRot, zRot

    if event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:  # scroll in
        glScaled(1.03, 1.03, 1.03)
    elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5: # scroll out
        glScaled(0.97, 0.97, 0.97)
    
    if event.type == pygame.MOUSEMOTION:
        x, y = event.pos
        dx = x - lastPosX
        dy = y - lastPosY
        
        mouseState = pygame.mouse.get_pressed()
        if mouseState[0]:   # left click occured
            modelView = (GLfloat * 16)()
            mvm = glGetFloatv(GL_MODELVIEW_MATRIX, modelView)

            temp = (GLfloat * 3)()
            temp[0] = modelView[0]*dy + modelView[1]*dx
            temp[1] = modelView[4]*dy + modelView[5]*dx
            temp[2] = modelView[8]*dy + modelView[9]*dx
            norm_xy = math.sqrt(temp[0]*temp[0] + temp[1]*temp[1] + temp[2]*temp[2])
            # glRotatef(math.sqrt(dx*dx+dy*dy) / 2, temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)
            return [math.sqrt(dx*dx+dy*dy) / 2, temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy]
        lastPosX = x
        lastPosY = y
    return [0, 0, 0, 0]
        

def draw(c1, c2):
    glClearColor(0.7, 0.7, 0.7, 0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    # glViewport(0, 0, WIDTH, HEIGHT)
    # glLoadIdentity()
    # glBegin(GL_LINES)
    # for edge in grid_edges:
    #     for vertex in edge:
    #         glColor3fv((0.0, 0.0, 0.0))
    #         glVertex3fv(grid_vertices[vertex])
    # glEnd()

    glViewport(0, 0, WIDTH // 2, HEIGHT)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]) / 2, 0.1, 50.0) 
    gluLookAt(c1.center_pos[0], c1.center_pos[1], c1.center_pos[2] + 8, c1.center_pos[0], c1.center_pos[1], c1.center_pos[2], 0, 1, 0)


    glPushMatrix()
    glTranslatef(c1.center_pos[0], c1.center_pos[1], c1.center_pos[2])
    glRotatef(c1.rotation[0], c1.rotation[1], c1.rotation[2], c1.rotation[3])
    glTranslatef(-c1.center_pos[0], -c1.center_pos[1], -c1.center_pos[2])
    glBegin(GL_LINES)
    for edge in c1.edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(c1.vertices[vertex])
    glEnd()
    glPopMatrix()

    glViewport(WIDTH // 2, 0, WIDTH // 2, HEIGHT)
    glLoadIdentity()
    gluPerspective(90, (display[0] / display[1]) / 2, 0.1, 50.0) 
    gluLookAt(c2.center_pos[0], c2.center_pos[1], c2.center_pos[2] + 8, c2.center_pos[0], c2.center_pos[1], c2.center_pos[2], 0, 1, 0)
    glPushMatrix()
    glTranslatef(c2.center_pos[0], c2.center_pos[1], c2.center_pos[2])
    glRotatef(c2.rotation[0], c2.rotation[1], c2.rotation[2], c2.rotation[3])
    glTranslatef(-c2.center_pos[0], -c2.center_pos[1], -c2.center_pos[2])
    glBegin(GL_LINES)
    for edge in c2.edges:
        for vertex in edge:
            glColor3fv((0, 0, 0))
            glVertex3fv(c2.vertices[vertex])
    glEnd()
    glPopMatrix()



def main():
    pygame.init()
    screen_surface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    glMatrixMode(GL_MODELVIEW)                                              # ensure in modelview mode
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    glTranslate(0, 0, -10.0)                                                # push world view back

    c1 = Cube(CUBE_SIZE, [-6, 0, 0])
    c2 = Cube(CUBE_SIZE, [6, 0, 0])

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:             # reset world view to original position
                    glMatrixMode(GL_MODELVIEW)
                    glLoadIdentity()
                    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
                    glTranslatef(0, 0, -10)
                    c1.rotation = [0, 0, 0, 0]
                    c2.rotation = [0, 0, 0, 0]

            rotation = mouseMovement(event) 
            if rotation[1] != 0 or rotation[2] != 0:
                c1.rotation = rotation
                c2.rotation = rotation
        

        draw(c1, c2)
        pygame.display.flip()
        pygame.time.wait(10)
main()