from OpenGL.GL import *

color = {'red': [1, 0, 0, 1], 'green': [0, 1, 0, 1], 'blue': [0, 0, 1, 1], 'orange': [1.0, 0.64, 0.0, 1]}


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
