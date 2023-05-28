import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
from utils import Point, Rocket, Ball


def init_orthographic():  # this function sets the orthographic view for viewer
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(0, 640, 0, 480)  # this function sets the range of the execution panel


if __name__ == '__main__':

    p1 = Point(10, 300)
    p2 = Point(10, 200)
    r1 = Rocket(p1, p2, 'red')

    p3 = Point(630, 300)
    p4 = Point(630, 200)
    r2 = Rocket(p3, p4, 'blue')

    p5 = Point(280, 200)
    base_coordinate = (280, 200)
    ball = Ball(p5, 'orange')

    pygame.init()  # initialization for the execution window by using pygame engine

    width = 1000
    height = 800

    screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("ping pong")

    init_orthographic()

    done = False
    while not done:
        for event in pygame.event.get():  # this loop checks event queue every 100 millisecond's
            if event.type == pygame.QUIT:
                done = True

            glClear(GL_COLOR_BUFFER_BIT)  # This function clears buffers to preset values
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()

        pygame.display.flip()  # this functions from pygame checks frame buffer and flush it every 100 millisecond's

    pygame.quit()


