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

    move_factor = 10
    ball_move_factor_x = 0.045
    ball_move_factor_y = 0.045

    score_red = 0
    score_blue = 0

    pygame.init()  # initialization for the execution window by using pygame engine

    width = 1000
    height = 800

    screen = pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)
    pygame.display.set_caption("ping pong")

    init_orthographic()

    done = False
    while not done:
        while True:
            if ball.coordinate.y >= 480 or ball.coordinate.y <= 0:
                ball_move_factor_y = -ball_move_factor_y

            if ball.coordinate.x >= 640 or ball.coordinate.x <= 0:
                ball_move_factor_x = -ball_move_factor_x

            if ball.collision_r1(r1) or ball.collision_r2(r2):
                ball_move_factor_x = -ball_move_factor_x
            ball.move(ball_move_factor_x, ball_move_factor_y)

            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)  # This function clears buffers to preset values
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glClearColor(0.2, 1.0, 0.5, 1.0)

            for event in pygame.event.get():  # this loop checks event queue every 100 millisecond's

                if event.type == pygame.QUIT:
                    done = True

                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_w:
                            r1.move(move_factor)

                        case pygame.K_s:
                            r1.move(-move_factor)

                        case pygame.K_e:
                            r2.move(move_factor)

                        case pygame.K_d:
                            r2.move(-move_factor)

            r1.show_rocket()
            r2.show_rocket()
            ball.show_ball()

            pygame.display.flip()  # this functions from pygame checks frame buffer and flush it every 100 millisecond's

    pygame.quit()


