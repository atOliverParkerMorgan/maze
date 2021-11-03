from Node import Node


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
                helperList.append(Node(x, y, "#"))
            self.map.append(helperList)

        if self.obstacles is not None:
            for ob in self.obstacles:
                self.map[ob[1]][ob[0]].setToObstacle()

    def createPath(self, path):
        for node in path:
            self.map[node.y][node.x].setToPath()

    def printMaze(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.map[y][x].symbol
            print(line)

    def getChildren(self, node):
        children = []
        positionOfChildren = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in positionOfChildren:
            x = node.x + newPosition[0]
            y = node.y + newPosition[1]
            if 0 <= x < self.width and 0 <= y < self.height and not self.map[y][x].isObstacle():
                children.append(self.map[y][x])

        return children
