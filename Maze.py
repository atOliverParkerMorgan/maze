from Node import Node
from typing import List


class Maze:
    def __init__(self, width: int, height: int, startNodePos: tuple = None,
                 goalNodePos: tuple = None, currentPath: List[Node] = None):

        self.width: int = width
        self.height: int = height
        self.map: List[List[Node]] = []

        # starting point and ending point
        self.startNodePos: tuple = goalNodePos
        self.destinationNodePos: tuple = startNodePos

        # current Solution path
        self.currentPath: List[Node] = currentPath

        # all obstacle Nodes
        self.HasObstacles: bool = False

    def createMap(self):
        for y in range(self.height):
            helperList = []
            for x in range(self.width):
                helperList.append(Node(x, y, "#"))
            self.map.append(helperList)

    def createPath(self, path: List[Node]):
        if path is not None:
            for node in path:
                self.getNode(node.x, node.y).setToPath()
            self.currentPath = path

    def deletePath(self):
        if self.currentPath is not None:
            for node in self.currentPath:
                if node.isPath():
                    self.getNode(node.x, node.y).setToDefault()

    def deleteObstacles(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.getNode(x, y).isObstacle():
                    self.getNode(x, y).setToDefault()
        self.HasObstacles = False

    def setHasObstacles(self):
        self.HasObstacles = True

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
        # if node is obstacle => skip; start cannot be placed on obstacle
        if self.getNode(x, y).isObstacle():
            return

        self.getNode(x, y).setToStart()

        # set previous position of start to default if the new position is different than the last and is not None
        if self.startNodePos is not None:
            node = self.getNode(self.startNodePos[0], self.startNodePos[1])
            if self.startNodePos[0] is not x or self.startNodePos[1] is not y:
                node.setToDefault()

        # update position
        self.startNodePos = (x, y)

    def setDestination(self, x: int, y: int):
        # if node is obstacle => skip; destination cannot be placed on obstacle
        if self.getNode(x, y).isObstacle():
            return

        self.getNode(x, y).setToDestination()

        # set previous position of start to default if the new position is different than the last and is not None
        if self.destinationNodePos is not None:

            node = self.getNode(self.destinationNodePos[0], self.destinationNodePos[1])
            if self.destinationNodePos[0] is not x or self.destinationNodePos[1] is not y:
                node.setToDefault()

        # update position
        self.destinationNodePos = (x, y)

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
