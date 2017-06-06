import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

vertecies = (
    (0.469, 0.469, 0.469),
    (0.290, 0.000, 0.759),
    (-0.759, -0.290, 0.000),
    (0.759, 0.290, 0.000),
    (-0.469, 0.469, -0.469),
    (0.000, -0.759, -0.290),
    (-0.759, 0.290, 0.000),
    (0.469, -0.469, 0.469),
    (-0.469, 0.469, 0.469),
    (-0.469, -0.469, 0.469),
    (0.469, -0.469, -0.469),
    (0.290, 0.000, -0.759),
    (-0.469, -0.469, -0.469),
    (0.000, -0.759, 0.290),
    (0.000, 0.759, -0.290),
    (-0.290, 0.000, 0.759),
    (0.759, -0.290, 0.000),
    (-0.290, 0.000, -0.759),
    (0.469, 0.469, -0.469),
    (0.000, 0.759, 0.290),
)

edges = (
    (0,1),(1,7),(7,16),(16,3),(3,0),
    (8,6),(6,2),(2,9),(9,15),(15,8),
    (13,9),(15,1),(1,7),(7,13),
    (8,19),(19,0),
    (5,13),(13,7),(7,16),(16,10),(10,5),
    (2,9),(9,13),(13,5),(5,12),(12,2),
    (19,14),(14,4),(4,6),(6,8),(8,19),
    (19,0),(0,3),(3,18),(18,14),(14,19),

    (4,6),(6,2),(2,12),(12,17),(17,4),
    (18,3),(3,16),(16,10),(10,11),(11,18),
    (11,17)
)

colors = (
    (0,1,0),
    (1,0,0),
    (0,0,1),
    (1,1,0),
    (0,1,1),
    (1,0,1),
)

surfaces = (
    (0,1,3,7), (0,7,16,3), (0,3,16,7),
    (8,6,2,9), (8,2,9,15), (8,6,9,15),
    (13,9,15,1), (13,15,1,7), (13,9,1,7),
    (8,19,0,1), (8,0,1,15), (8,19,1,15),
    (5,13,7,16), (5,7,16,10), (5,13,16,10),
    (2,9,13,5), (2,9,5,12), (2,13,5,12),
    (19,14,4,6), (19,4,6,8), (19,14,6,8),
    (19,0,3,18), (19,0,18,14), (19,3,18,14),
    (4,6,2,12), (4,6,12,17), (4,2,12,17),
    (18,3,16,10), (18,3,10,11), (18,16,10,11),
    (4,17,11,18), (4,17,18,14), (4,11,18,14),
    (12,17,11,10), (12,17,10,5), (12,11,10,5)
)

# 0-1-7-16-3-0
# 8-6-2-9-15-8
# 13-9-15-1-7-13
# 8-19-0-1-15-8
# 5-13-7-16-10-5
# 2-9-13-5-12-2
# 19-14-4-6-8-19
# 19-0-3-18-14-19
# 4-6-2-12-17-4
# 18-3-16-10-11-18
# 4-14-18-11-17-4
# 12-17-11-10-5-12

def Cube():

    glBegin(GL_QUADS)

    for surface in surfaces:
        x = 0
        for vertex in surface:
            x += 1
            glColor3fv(colors[x%6])
            glVertex3fv(vertecies[vertex])

    glEnd()

    glBegin(GL_LINES)

    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertecies[vertex])

    glEnd()
    glBegin(GL_LINES)


    glEnd()


def main():
    pygame.init()

    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glTranslatef(0, 0, -5)
    glRotatef(0, 0, 0, 0)

    isRotating = False

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    glTranslatef(-1, 0, 0)
                if event.key == pygame.K_RIGHT:
                    glTranslatef(1, 0, 0)
                if event.key == pygame.K_UP:
                    glTranslatef(0, 1, 0)
                if event.key == pygame.K_DOWN:
                    glTranslatef(0, -1, 0)
                if event.key == pygame.K_SPACE:
                    if isRotating:
                        isRotating = False
                    else:
                        isRotating = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 4:
                    glTranslatef(0,0,1.0)
                if event.button == 5:
                    glTranslatef(0,0,-1.0)

            glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        if isRotating:
            glRotatef(1, 1, 1, 1)

        Cube()
        pygame.display.flip()

main()
