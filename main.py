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

# colors and screen details
WIDTH, HEIGHT = 1000, 600
CUBE_SIZE = 1
LINE_COLOR = ((0.1, 0.1, 0.1))  # play with colors later
CUBE_COLOR = ((0.5, 0.5, 0.5))
#BG_COLOR = 0.7, 0.7, 0.7, 0

# for mouse movement
lastPosX = 0
lastPosY = 0
xRot = 0
yRot = 0
zRot = 0

cubev = ((0,0,0), (1, 0, 0), (0, 0, 1), (1, 0, 1),
        (0, 1, 0), (1, 1, 0), (0, 1, 1), (1, 1, 1) )

edgesc = ((0,1), (0,2), (0, 4),
        (1,3), (1,5),
        (2,6), (2,3),
        (3,7),
        (4,5), (4,6),
        (5, 7),
        (6,7), (6,2))


# def drawCube2(offset):
#     # glTranslatef(offset[0], offset[1], offset[2])
#     glBegin(GL_LINES)
#     for edge in edgesc:
#         for vertex in edge:
#             glColor3fv((0.1, 0.1, 0.2))
#             glVertex3fv(cubev[vertex])
#     glEnd()
#     # glTranslatef(offset[0], offset[1], offset[2])


def drawCube(rcube):
    # draw the outline of the cube
    # glTranslatef(-offset, 0, 0)
    glBegin(GL_LINES)     # GL_lines for lines, GL_QUADS for surfaces
    for edge in rcube.edges:
        for vertex in edge:
            glColor3fv((0.1, 0.1, 0.2))
            glVertex3fv(rcube.vertices[vertex])
    glEnd()
    # glTranslatef(offset, 0, 0)

    

    

    # draw the correct path
    # glBegin(GL_QUADS)
    # for surface in cube.surfaces:
    #     glColor3fv((0, 1, 0))
    #     for vertex in surface:
    #         glVertex3fv(cube.vertices[vertex])
    # glEnd()


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
            # glTranslate(8, 0, 10)
            glRotatef(math.sqrt(dx*dx+dy*dy) / 2, temp[0]/norm_xy, temp[1]/norm_xy, temp[2]/norm_xy)
            # glTranslate(-8, 0, -10)

        lastPosX = x
        lastPosY = y

def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    screen_surface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, (display[0]/display[1]), 0.1, 50.0)
    center = CUBE_SIZE / 2.0

    reference_cube = Cube(CUBE_SIZE, 0)
    reference_cube.generatevertices()
    reference_cube.generateEdges()
    reference_cube.generateSurfaces()
    player_cube = Cube(CUBE_SIZE, 8)
    player_cube.generatevertices()
    player_cube.generateEdges()
    player_cube.generateSurfaces()
    offset = (CUBE_SIZE / 2)
    # player_cube.vertices = utils.offsetVerticies(8, player_cube.vertices)
    # player_cube = copy.deepcopy(reference_cube)
    # print(len(player_cube.vertices))
    # print(player_cube.edges)

    glTranslate(-8, 0, -10.0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    print("here")
                    glTranslatef(1, 0, 0)
            #         reset(original_edges)
            mouseMovement(event)
        glClearColor(0.7, 0.7, 0.7, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        drawCube(reference_cube)
        drawCube(player_cube)
        pygame.display.flip()
        pygame.time.wait(10)


main()