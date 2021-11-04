from Maze import Maze
from Node import Node
from typing import List


class AStar:

    def __init__(self, maze: Maze):
        self.maze: Maze = maze
        self.startNode = None
        self.destinationNode = None

        self.startNode.f = self.startNode.g = self.startNode.h = 0
        self.openSet = [self.startNode]
        self.closedSet = []

        self.pathSolution: List[Node] = []

    def solutionCycle(self):

        # find the node with the best score f (the node that is closet to start and end)
        currentNode = self.openSet[0]
        currentIndex = 0

        for index, item in enumerate(self.openSet):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        # remove node from open set => the nodes that haven't been searched yet
        self.openSet.pop(currentIndex)

        # add to close set => the nodes that have been searched
        self.closedSet.append(currentNode)

        # if the current node that is being searched is the end node
        # add the parents of this node through .parent to a list
        # reverse said list and return
        if currentNode.x == self.destinationNode.x and currentNode.y == self.destinationNode.y:
            pathToEnd = [currentNode]

            while pathToEnd[len(pathToEnd) - 1].parent is not None:
                pathToEnd.append(pathToEnd[len(pathToEnd) - 1].parent)

            self.pathSolution = pathToEnd[::-1]
            return False

        # get the all the children of the currentNode (the node that is currently being search)
        # children are the neighboring nodes of currentNode
        for child in self.maze.getChildren(currentNode):

            # node has already been search => skip
            if child in self.closedSet:
                continue

            # update node distance from start
            currentScore = currentNode.g + currentNode.getDist(child)

            isBetter = False
            if child not in self.openSet:
                # this node hasn't been searched yet, therefore add this node to search set (openSet) and
                # calculate values
                self.openSet.append(child)
                isBetter = True

            elif currentScore < child.g:
                isBetter = True

            if isBetter:
                # set Parent
                child.parent = currentNode

                # the distance from start
                child.g = currentScore
                # the distance from end
                child.h = self.destinationNode.getDist(child)
                # total value of node
                child.f = child.g + child.h

        return len(self.openSet) > 0

    def solve(self, startNode: Node = None, destinationNode: Node = None):
        while self.solutionCycle(startNode, destinationNode):
            pass
        return self.pathSolution

    def setStartAndDestination(self, startNode: Node, destinationNode: Node):
        self.startNode: Node = startNode
        self.destinationNode: Node = destinationNode
