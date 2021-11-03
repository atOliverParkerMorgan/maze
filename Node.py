import math


class Node:
    def __init__(self, x, y, symbol="#", parent=None):
        self.parent: Node = parent

        self.x: int = x
        self.y: int = y

        self.f: int = 0
        self.h: int = 0
        self.g: int = 0

        self.symbol: str = symbol

    def setToObstacle(self):
        self.symbol = "o"
        return self

    def setToPath(self):
        self.symbol = "x"

    def isObstacle(self):
        return self.symbol == "o"

    def isPath(self):
        return self.symbol == "x"

    def isDefault(self):
        return self.symbol == "#"

    def getDist(self, node):
        return math.sqrt((node.x - self.x) ** 2 + (node.y - self.y) ** 2)
