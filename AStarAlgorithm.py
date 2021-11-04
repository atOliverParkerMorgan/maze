from Maze import Maze
from Node import Node


def solve(maze: Maze, startNode: Node = None, goalNode: Node = None):

    if startNode is None:
        startNode: Node = maze.getStart()
        goalNode: Node = maze.getGoal()

    startNode.f = startNode.g = startNode.h = 0
    openSet = [startNode]
    closedSet = []

    while len(openSet) > 0:

        # find the node with the best score f (the node that is closet to start and end)
        currentNode = openSet[0]
        currentIndex = 0

        for index, item in enumerate(openSe):
            if item.f < currentNode.f:
                currentNode = item
                currentIndex = index

        # remove node from open set => the nodes that haven't been searched yet
        openSet.pop(currentIndex)

        # add to close set => the nodes that have been searched
        closedSet.append(currentNode)

        # if the current node that is being searched is the end node
        # add the parents of this node through .parent to a list
        # reverse said list and return
        if currentNode.x == goalNode.x and currentNode.y == goalNode.y:
            pathToEnd = [currentNode]

            while pathToEnd[len(pathToEnd) - 1].parent is not None:
                pathToEnd.append(pathToEnd[len(pathToEnd) - 1].parent)

            return pathToEnd[::-1]

        # get the all the children of the currentNode (the node that is currently being search)
        # children are the neighboring nodes of currentNode
        for child in maze.getChildren(currentNode):

            # node has already been search => skip
            if child in closedSet:
                continue

            # update node distance from start
            currentScore = currentNode.g + currentNode.getDist(child)

            isBetter = False
            if child not in openSet:
                # this node hasn't been searched yet, therefore add this node to search set (openSet) and
                # calculate values
                openSet.append(child)
                isBetter = True

            elif currentScore < child.g:
                isBetter = True

            if isBetter:
                # set Parent
                child.parent = currentNode

                # the distance from start
                child.g = currentScore
                # the distance from end
                child.h = goalNode.getDist(child)
                # total value of node
                child.f = child.g + child.h

    return None
