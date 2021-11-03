from AStarAlgorithm import AStarAlgorithm
from Maze import Maze
from Node import Node


class Main:

    def __init__(self):
        HEIGHT = 100
        WIDTH = 100

        self.maze = Maze(WIDTH, HEIGHT)
        self.maze.createMap()
        print("\n")
        path = AStarAlgorithm.solve(self.maze, Node(0, 0), Node(100, 0))
        if path is not None:
            self.maze.createPath(path)
            self.maze.printMaze()


if __name__ == '__main__':
    main = Main()
