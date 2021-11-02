class Node:
    def __init__(self, position, symbol="o", parent=None):
        self.parent = parent
        self.position = position

        self.f = 0
        self.h = 0
        self.g = 0

        self.symbol = symbol

    def setToObstacle(self):
        self.symbol = "x"


    def isObstacle(self):
        return self.symbol == "x"


class Maze:
    def __init__(self, width, height, obstacles=None):
        self.width = width
        self.height = height
        self.map = []
        self.obstacles = obstacles

    def createMap(self):
        for y in range(self.height):
            helperList = []
            for x in range(self.width):
                helperList.append(Node((x, y)))
            self.map.append(helperList)

        if self.obstacles is not None:
            for ob in self.obstacles:
                self.map[ob[1]][ob[0]].setToObstacle()

    def printMaze(self):

        line = ""
        for y in range(self.height):
            print(line)
            line = ""
            for x in range(self.width):
                line += self.map[y][x].symbol

    def getChildren(self, node):
        children = []
        positionOfChildren = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in positionOfChildren:
            x = node.position[0] + newPosition[0]
            y = node.position[1] + newPosition[1]
            if 0 <= x < self.width and 0 <= y < self.height and not self.map[y][x].isObstacle():
                children.append(Node((x, y)))

        return children
