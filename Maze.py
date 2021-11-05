from Node import Node
from typing import List


class Maze:
    def __init__(self, width: int, height: int, obstacles=None, startNodePos: tuple = None,
                 goalNodePos: tuple = None, currentPath: List[Node] = None):
        if obstacles is None:
            obstacles = []
        self.width: int = width
        self.height: int = height
        self.map: List[List[Node]] = []

        # starting point and ending point
        self.startNodePos: tuple = goalNodePos
        self.destinationNodePos: tuple = startNodePos

        # current Solution path
        self.currentPath: List[Node] = currentPath

        # all obstacle Nodes
        self.obstacles: List[tuple] = obstacles

    def createMap(self):
        for y in range(self.height):
            helperList = []
            for x in range(self.width):
                helperList.append(Node(x, y, "#"))
            self.map.append(helperList)

        for x, y in self.obstacles:
            self.getNode(x, y).setToObstacle()

    def createPath(self, path: List[Node]):
        if path is not None:
            for node in path:
                self.getNode(node.x, node.y).setToPath()
            self.currentPath = path

    def deletePath(self):
        if self.currentPath is not None:
            for node in self.currentPath:
                if node.isPath() and not node.isStart() and not node.isDestination():
                    self.getNode(node.x, node.y).setToDefault()

    def printMaze(self):
        for y in range(self.height):
            line = ""
            for x in range(self.width):
                line += self.map[y][x].symbol
            print(line)

    def getChildren(self, node: Node):
        children = []
        positionOfChildren = [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for newPosition in positionOfChildren:
            x = node.x + newPosition[0]
            y = node.y + newPosition[1]
            if 0 <= x < self.width and 0 <= y < self.height and not self.getNode(x, y).isObstacle():
                children.append(self.getNode(x, y))

        return children

    def setStart(self, x: int, y: int):
        if self.startNodePos is not None:
            self.getNode(self.startNodePos[0], self.startNodePos[1]).setToDefault()

        self.startNodePos = (x, y)
        self.getNode(self.startNodePos[0], self.startNodePos[1]).setToStart()

    def setDestination(self, x: int, y: int):
        if self.destinationNodePos is not None:
            self.getNode(self.destinationNodePos[0], self.destinationNodePos[1]).setToDefault()

        self.destinationNodePos = (x, y)
        self.getNode(self.destinationNodePos[0], self.destinationNodePos[1]).setToDestination()

    def getStart(self):
        if self.startNodePos is None:
            return None
        return self.getNode(self.startNodePos[0], self.startNodePos[1])

    def getDestination(self):
        if self.destinationNodePos is None:
            return None
        return self.getNode(self.destinationNodePos[0], self.destinationNodePos[1])

    def hasStart(self):
        return self.startNodePos is not None

    def hasDestination(self):
        return self.destinationNodePos is not None

    def getNode(self, x: int, y: int):
        return self.map[y][x]
