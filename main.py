from maze import Maze


class Main:

    def __init__(self):
        HEIGHT = 100
        WIDTH = 100

        self.maze = Maze(WIDTH, HEIGHT, )
        self.maze.createMap()
        self.maze.printMaze()








if __name__ == '__main__':
    main = Main()
