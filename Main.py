from AStarAlgorithm import AStarAlgorithm
from Maze import Maze
from Node import Node
from Grafics import Graphics


class Main:

    def __init__(self, gameHasStarted):
        HEIGHT: int = 100
        WIDTH: int = 100
        GRAPHIC_NODE_SIZE: int = 10

        self.maze = Maze(WIDTH, HEIGHT)
        self.maze.createMap()
        print("\n")
        path = AStarAlgorithm.solve(self.maze, Node(0, 0), Node(99, 5))
        if path is not None:
            self.maze.createPath(path)
            self.maze.printMaze()
        graphics = Graphics(WIDTH * GRAPHIC_NODE_SIZE, HEIGHT * GRAPHIC_NODE_SIZE, GRAPHIC_NODE_SIZE)
        gameHasStarted = graphics.createMenu(gameHasStarted, self.maze)


if __name__ == '__main__':
    main = Main(True)
