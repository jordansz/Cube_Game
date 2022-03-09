import pygame
from pygame.locals import *

from cube import Cube

from OpenGL.GL import *
from OpenGL.GLU import *

WIDTH, HEIGHT = 1000, 600
CUBE_SIZE = 5
LINE_COLOR = ((0.1, 0.1, 0.1))  # play with colors later
CUBE_COLOR = ((0.5, 0.5, 0.5))
#BG_COLOR = 0.7, 0.7, 0.7, 0

def main():
    pygame.init()
    display = (WIDTH, HEIGHT)
    screen_surface = pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(90, (display[0]/display[1]), 0.1, 20.0)
    glTranslatef((WIDTH - (WIDTH + CUBE_SIZE)) * 2, 0.0, -10.0)
    
    reference_cube = Cube(CUBE_SIZE)
    reference_cube.generateVerticies()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # glClearColor(0.7, 0.7, 0.7, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        reference_cube.drawCube()
        pygame.display.flip()
        pygame.time.wait(10)


main()