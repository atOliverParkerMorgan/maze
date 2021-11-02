class AStarAlgorithm:
    def __init__(self, startNode, endNode):
        endNode.f = endNode.g = endNode.h = 0
        startNode.f = startNode.g = startNode.h = 0

        self.startNode = startNode
        self.endNode = endNode

    def solve(self):

        openList = []
        closedList = []

        while len(openList) > 0:
            currentNode = openList[0]
            currentNodeIndex = 0

            for index, item in enumerate(openList):
                if item.f < currentNode.f:
                    currentNode = item
                    currentNodeIndex = index

            openList.pop(currentNodeIndex)
            closedList.pop(currentNode)
