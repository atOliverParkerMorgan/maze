import math


class Node:
    def __init__(self, x, y, symbol="#", parent=None):
        self.parent = parent

        self.x = x
        self.y = y

        self.f = 0
        self.h = 0
        self.g = 0

        self.symbol = symbol

    def setToObstacle(self):
        self.symbol = "o"
        return self

    def setToPath(self):
        self.symbol = "x"

    def isObstacle(self):
        return self.symbol == "o"

    def getDist(self, node):
        return math.sqrt((node.x - self.x) ** 2 + (node.y - self.y) ** 2)
