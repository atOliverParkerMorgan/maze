from Maze import Maze
from Grafics import Graphics
# from Node import Node
# from PathFindingAlgorithm import PathFindingAlgorithm


class Main:

    def __init__(self, gameHasStarted: bool):
        # const for window size; node size; node number => WIDTH * HEIGHT
        HEIGHT: int = 100
        WIDTH: int = 100
        GRAPHIC_NODE_SIZE: int = 10

        self.maze = Maze(WIDTH, HEIGHT)

        # initials node map
        self.maze.createMap()

        # FOR CONSOLE TEST
        # x1, y1, x2, y2 = 0, 0, WIDTH - 1, HEIGHT - 1
        # self.maze.setStart(x1, y1)
        # self.maze.setDestination(x2, y2)
        # A_STAR_MODE = 0

        # pathFindingAlgorithm = PathFindingAlgorithm(self.maze, A_STAR_MODE)

        # pathFindingAlgorithm.solve()
        # print(pathFindingAlgorithm.pathSolution)

        # self.maze.createPath(pathFindingAlgorithm.pathSolution)
        # self.maze.printMaze()

        graphics = Graphics(WIDTH * GRAPHIC_NODE_SIZE, HEIGHT * GRAPHIC_NODE_SIZE, GRAPHIC_NODE_SIZE)
        graphics.createMenu(gameHasStarted, self.maze)


if __name__ == '__main__':
    main = Main(True)
