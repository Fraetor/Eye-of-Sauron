import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (-5, 1, 1),
    (-5, -1, 1),
    (5, 1, 1),
    (5, -1, 1),
    (2, 3, 1),
    (2, -3, 1),
    (-2, 3, 1),
    (-2, -3, 1),
    (1, 0.5, -3),
    (1, -0.5, -3),
    (-1, 0.5, -3),
    (-1, -0.5, -3)
    )

edges = (
    (0, 1),
    (0, 6),
    (0, 10),
    (1, 11),
    (1, 7),
    (2, 3),
    (2, 4),
    (2, 8),
    (3, 5),
    (3, 9),
    (4, 6),
    (4, 8),
    (5, 9),
    (5, 7),
    (6, 10),
    (7, 11),
    (8, 9),
    (8, 10),
    (9, 11),
    (10, 11),
    )


def eye():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0.0,0.0, -15)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glRotatef(1, 3, 1, 1)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        eye()
        pygame.display.flip()
        pygame.time.wait(10)


main()
