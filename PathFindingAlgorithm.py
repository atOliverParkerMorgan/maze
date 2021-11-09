from Maze import Maze
from Node import Node
from typing import List


class PathFindingAlgorithm:

    def __init__(self, maze: Maze, mode: int):

        # modes
        self.A_STAR = 0
        self.DIJKSTRA = 1
        self.DEPTH_FIRST_SEARCH = 2

        self.mode = mode

        self.destinationNode: Node = maze.getDestination()
        self.startNode: Node = maze.getStart()

        # total dist from start to destination for graphics
        self.distFromStartToDestination: int = self.startNode.getDist(self.destinationNode)

        # to save nodes that have already been searched
        self.closedSet = []
        # to save nodes that haven't been searched yet
        self.openSet = [self.startNode]

        self.maze: Maze = maze
        self.pathSolution: List[Node] = []

    def hideSearched(self):
        # used to restart graphics output
        for node in self.closedSet:
            # reset all nodes that are not a obstacle or start or destination
            if not node.isStart() and not node.isDestination() and not node.isObstacle():
                node.setToDefault()
                node.f = node.h = node.g = 0

    def solutionCycle(self):
        # prevents opentSet out of range
        if len(self.openSet) == 0:
            return True

        # find the node with the best score f (the node that is closet to start and end)

        currentNode = self.openSet[0]
        currentIndex = 0

        for index, item in enumerate(self.openSet):

            # A_STAR algorithm uses f value (f=g+h)
            if item.f < currentNode.f and self.mode == self.A_STAR:
                currentNode = item
                currentIndex = index

            # DIJKSTRA algorithm uses g value (distance from start)
            if item.g < currentNode.g and self.mode == self.DIJKSTRA:
                currentNode = item
                currentIndex = index
            # DEPTH_FIRST_SEARCH algorithm uses h value (distance to finish)
            if item.h < currentNode.h and self.mode == self.DEPTH_FIRST_SEARCH:
                currentNode = item
                currentIndex = index

        # remove node from open set => the nodes that haven't been searched yet
        self.openSet.pop(currentIndex)

        # add to close set => the nodes that have been searched
        self.closedSet.append(currentNode)

        # change the visual representation of node
        currentNode.setToSearched()

        # if the current node that is being searched is the end node
        # add the parents of this node through .parent to a list
        # reverse said list and return
        if currentNode.x == self.destinationNode.x and currentNode.y == self.destinationNode.y:
            pathToEnd = [currentNode]

            while pathToEnd[len(pathToEnd) - 1].parent is not self.startNode:
                pathToEnd.append(pathToEnd[len(pathToEnd) - 1].parent)

            # path found => save path and return to True to signal success
            self.pathSolution = pathToEnd[::-1]
            return True

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
                child.f = child.g + child.h + child.getBetterHeuristics(self.startNode, self.destinationNode)

        # return True if no valid path
        # return len(self.openSet) == 0 doesn't work here
        for _ in self.openSet:
            return False

        return True

    def solve(self):
        # solve completely
        while self.solutionCycle():
            pass
        return self.pathSolution
