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
