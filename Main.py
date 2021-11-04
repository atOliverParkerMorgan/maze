# import AStarAlgorithm
from Maze import Maze
from Grafics import Graphics
# from Node import Node


class Main:

    def __init__(self, gameHasStarted):
        HEIGHT: int = 100
        WIDTH: int = 100
        GRAPHIC_NODE_SIZE: int = 10

        self.maze = Maze(WIDTH, HEIGHT)
        self.maze.createMap()
        print("\n")

        # x1,y1,x2,y2 = 0,0,WIDTH-1,HEIGHT-1
        # path = AStarAlgorithm.solve(self.maze, Node(x1,y1), Node(x2,y2))
        # if path is not None:
        #    self.maze.createPath(path)
        #    self.maze.printMaze()

        graphics = Graphics(WIDTH * GRAPHIC_NODE_SIZE, HEIGHT * GRAPHIC_NODE_SIZE, GRAPHIC_NODE_SIZE)
        graphics.createMenu(gameHasStarted, self.maze)


if __name__ == '__main__':
    main = Main(True)
