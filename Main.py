from Maze import Maze
from Grafics import Graphics


class Main:

    def __init__(self, gameHasStarted: bool):

        # const for window size; node size; node number => WIDTH * HEIGHT
        HEIGHT: int = 100
        WIDTH: int = 100
        GRAPHIC_NODE_SIZE: int = 10

        self.maze = Maze(WIDTH, HEIGHT)
        # inits node map
        self.maze.createMap()

        # FOR CONSOLE TEST
        # x1,y1,x2,y2 = 0,0,WIDTH-1,HEIGHT-1
        # path = AStarAlgorithm.solve(self.maze, Node(x1,y1), Node(x2,y2))
        # if path is not None:
        #    self.maze.createPath(path)
        #    self.maze.printMaze()

        graphics = Graphics(WIDTH * GRAPHIC_NODE_SIZE, HEIGHT * GRAPHIC_NODE_SIZE, GRAPHIC_NODE_SIZE)
        graphics.createMenu(gameHasStarted, self.maze)


if __name__ == '__main__':
    main = Main(True)
