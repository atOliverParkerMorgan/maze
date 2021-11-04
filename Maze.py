from Node import Node
from typing import List


class Maze:
    def __init__(self, width: int, height: int, obstacles: List[tuple] = None):
        self.width: int = width
        self.height: int = height
        self.map: List[List[Node]] = []
        self.obstacles: List[tuple] = obstacles
        self.startNodePos: tuple = None
        self.goalNodePos: tuple = None

    def createMap(self):
        for y in range(self.height):
            helperList = []
            for x in range(self.width):
                helperList.append(Node(x, y, "#"))
            self.map.append(helperList)

        if self.obstacles is not None:
            for ob in self.obstacles:
                self.getNode(ob[0], ob[1]).setToObstacle()

    def createPath(self, path: List[Node]):
        for node in path:
            self.getNode(node.x, node.y).setToPath()

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
            if 0 <= x < self.width and 0 <= y < self.height and not self.map[y][x].isObstacle():
                children.append(self.map[y][x])

        return children

    def setStart(self, x: int, y: int):
        if self.startNodePos is not None:
            self.getNode(self.startNodePos[0], self.startNodePos[1]).setToDefault()

        self.startNodePos = (x, y)
        self.getNode(self.startNodePos[0], self.startNodePos[1]).setToStart()

    def setGoal(self, x: int, y: int):
        if self.goalNodePos is not None:
            self.getNode(self.goalNodePos[0], self.goalNodePos[1]).setToDefault()

        self.goalNodePos = (x, y)
        self.getNode(self.goalNodePos[0], self.goalNodePos[1]).setToStart()

    def getStart(self):
        if self.startNodePos is None:
            return None
        return self.getNode(self.startNodePos[0], self.startNodePos[1])

    def getGoal(self):
        if self.goalNodePos is None:
            return None
        return self.getNode(self.goalNodePos[0], self.goalNodePos[1])

    def hasStart(self):
        return self.startNodePos is not None

    def hasGoal(self):
        return self.goalNodePos is not None

    def getNode(self, x: int, y: int):
        return self.map[y][x]
