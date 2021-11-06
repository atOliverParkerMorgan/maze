import math


class Node:
    def __init__(self, x, y, symbol="#", parent=None):
        self.parent: Node = parent

        self.x: int = x
        self.y: int = y

        # values for pathFindingAlgorithm
        # g+h
        self.f: int = 0

        # distance from destination
        self.h: int = 0

        # distance from start
        self.g: int = 0

        # type of node => (START, DESTINATION, OBSTACLE, PATH, SEARCH, DEFAULT)
        self.symbol: str = symbol

    def setToObstacle(self):
        if not self.isStart() and not self.isDestination():
            self.symbol = "o"

    def setToPath(self):
        if not self.isStart() and not self.isDestination():
            self.symbol = "x"

    def setToStart(self):
        if not self.isObstacle():
            self.symbol = "s"

    def setToDestination(self):
        if not self.isObstacle():
            self.symbol = "d"

    def setToDefault(self):
        self.symbol = "#"

    def setToSearched(self):
        if not self.isStart() and not self.isDestination():
            self.symbol = "*"

    def isObstacle(self):
        return self.symbol == "o"

    def isPath(self):
        return self.symbol == "x"

    def isDefault(self):
        return self.symbol == "#"

    def isStart(self):
        return self.symbol == "s"

    def isDestination(self):
        return self.symbol == "d"

    def isSearched(self):
        return self.symbol == "*"

    def getDist(self, node):
        return math.sqrt((node.x - self.x) ** 2 + (node.y - self.y) ** 2)
