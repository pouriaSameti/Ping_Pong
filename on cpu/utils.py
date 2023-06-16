from OpenGL.GL import *
import time

color = {'red': [1, 0, 0, 1], 'green': [0, 0.9, 0, 1], 'blue': [0, 0, 1, 1], 'orange': [1.0, 0.64, 0.0, 1],
         'white': [1, 1, 1, 1], 'gray': [0.93, 0.93, 0.93, 1.0], 'shamrock_green': [0, 0.61, 0.27, 1],
         'malachite': [0.043, 0.85, 0.31, 1],'tangerine': [0.94, 0.50, 0.0, 1.0],
         'yellow_orange': [1.0, 0.66, 0.2, 1.0], 'sunset_orange': [0.98, 0.37, 0.33, 1.0]}


class GamePlane:

    @staticmethod
    def show_border(border_color: str):
        glColor4f(*color[border_color])
        glLineWidth(12)
        glBegin(GL_LINE_LOOP)
        glVertex2f(0.0, 0.0)
        glVertex2f(640.0, 0.0)
        glVertex2f(640.0, 480.0)
        glVertex2f(0.0, 480.0)
        glEnd()

    @staticmethod
    def show_separation_line(s_point, border_color: str):
        glColor4f(*color[border_color])
        glLineWidth(15)

        length = 50
        gap = 30

        glBegin(GL_LINES)
        for i in range(10):
            glVertex2f(s_point.x, s_point.y)
            glVertex2f(s_point.x, s_point.y + gap)
            s_point.y += length
        glEnd()


class Point:

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def get_coordinate(self):
        return self.x, self.y


class Rocket:

    def __init__(self, point1: Point, point2: Point, color_name: str):
        self.point1 = point1
        self.point2 = point2
        self.__color = color[color_name]

    def __str__(self):
        return f"p1{self.point1}, p2{self.point2}"

    def show_rocket(self):
        glColor(*self.__color)
        glLineWidth(15)
        glBegin(GL_LINES)
        glVertex2i(self.point1.x, self.point1.y)
        glVertex2i(self.point2.x, self.point2.y)
        glEnd()

    def move(self, amount):
        if self.point2.y < 25:
            self.point2.y = 25
            self.point1.y = 125

        if self.point1.y > 455:
            self.point2.y = 355
            self.point1.y = 455

        else:
            self.point1.y += amount
            self.point2.y += amount


class Ball:
    def __init__(self, point: Point, color_name: str):
        self.coordinate = point
        self.__color = color[color_name]

    def __str__(self):
        return f"{self.coordinate}"

    def set_coordinate(self, coordinate: tuple):
        self.coordinate.x = coordinate[0]
        self.coordinate.y = coordinate[1]

    def show_ball(self):
        glColor4f(*self.__color)
        glPointSize(15)
        glBegin(GL_POINTS)
        glVertex2f(self.coordinate.x, self.coordinate.y)
        glEnd()

    def move(self, ball_move_factor_x, ball_move_factor_y):

        self.coordinate.x += ball_move_factor_x
        self.coordinate.y += ball_move_factor_y

    def collision_r1(self, rocket: Rocket):
        return not (rocket.point2.y > self.coordinate.y or rocket.point1.y < self.coordinate.y) and \
                    (rocket.point2.x >= self.coordinate.x)

    def collision_r2(self, rocket: Rocket):
        return not (rocket.point2.y > self.coordinate.y or rocket.point1.y < self.coordinate.y) and \
                    (rocket.point2.x <= self.coordinate.x)


class Numbers:

    def __init__(self, start_coordinate: Point, color_name: str):
        self.coordinate = start_coordinate
        self.__color = color[color_name]

    def show_number(self, number):
        constant_var = 30
        glLineWidth(5)
        glColor4f(*self.__color)

        match number:
            case 0:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))

                # e
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glEnd()

            case 1:
                glBegin(GL_LINES)
                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 2:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # e
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 3:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 4:
                glBegin(GL_LINES)
                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 5:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 6:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))

                # e
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glEnd()

            case 7:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glEnd()

            case 8:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))

                # e
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glEnd()

            case 9:
                glBegin(GL_LINES)
                # a
                glVertex2f(self.coordinate.x, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)

                # b
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)

                # c
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))

                # d
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - (2 * constant_var))
                glVertex2f(self.coordinate.x, self.coordinate.y - (2 * constant_var))

                # f
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x, self.coordinate.y)

                # g
                glVertex2f(self.coordinate.x, self.coordinate.y - constant_var)
                glVertex2f(self.coordinate.x + constant_var, self.coordinate.y - constant_var)
                glEnd()


class Timer:

    def __init__(self, minute: int, second: int):
        self.__min = minute
        self.__sec = second

    @property
    def minutes(self):
        return self.__min

    @property
    def seconds(self):
        return self.__sec

    @property
    def is_terminated(self):
        return self.__min == 0 and self.__sec == 0

    def start_timer(self):

        while 1:
            if self.__min == 0 and self.__sec <= 0:
                break

            if self.__sec == 0 and self.__min != 0:
                self.__sec = 60
                self.__min -= 1

            self.__sec -= 1
            time.sleep(1)

    def show_timer(self):

        p1 = Point(250, 80)
        min_digit = Numbers(p1, 'blue')

        p2 = Point(340, 80)
        p3 = Point(380, 80)
        sec_digit_second = Numbers(p2, 'blue')
        sec_digit_first = Numbers(p3, 'blue')

        min_digit.show_number(self.__min)

        if self.__sec < 10:
            sec_digit_second.show_number(0)
            sec_digit_first.show_number(self.__sec)

        else:
            sec_digit_second.show_number(self.__sec // 10)
            sec_digit_first.show_number(self.__sec % 10)



