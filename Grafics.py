import random
import pygame
import pygame_menu
from PathFindingAlgorithm import PathFindingAlgorithm
from Maze import Maze
from pygame_menu.examples import create_example_window


class Graphics:

    def __init__(self, width: int, height: int, blockSize: int = 20):
        # obstacle draw size constants
        self.SMALL: int = 0
        self.BIG: int = 1

        # path finding algorithm mode constants
        self.A_STAR = 0
        self.DIJKSTRA = 1
        self.DEPTH_FIRST_SEARCH = 2

        # the number of main loop cycles the solution show in random mode
        self.SHOW_SOLUTION_LENGTH_IN_RANDOM_MODE = 5

        # color constants
        self.BLACK: tuple = (0, 0, 0)
        self.WHITE: tuple = (200, 200, 200)
        self.RED: tuple = (255, 87, 51)
        self.ORANGE: tuple = (200, 162, 34)
        self.GREEN: tuple = (50, 205, 50)
        self.PURPLE: tuple = (100, 34, 162)
        self.YELLOW: tuple = (255, 255, 0)
        self.LIGHT_BLUE: tuple = (102, 167, 197)
        self.LIGHT_PINK: tuple = (236, 181, 235)

        # graphics parameters
        self.blockSize: int = blockSize
        self.WINDOW_HEIGHT: int = width
        self.WINDOW_WIDTH: int = height

        # pygame graphics tools
        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(self.BLACK)

        # user input booleans
        self.mouseIsPressed: bool = False

        self.placeObstacle: bool = False
        self.placeStart: bool = False
        self.placeDestination: bool = False
        self.placeRandom: bool = False

        # the number of main loop cycles the solution is currently show in random mode
        self.showSolutionLengthInRandomModeCurrent = 0

        self.startSolvingAStar: bool = False
        self.startSolvingDijkstra: bool = False
        self.startSolvingDepthFirstSearched: bool = False
        self.searchSpeed = 1

        # is the program currently solving a maze
        self.isSolving: bool = False

        self.pathFindingAlgorithm = None

        # the draw size of obstacles; BIG = > 9x9; SMALL => 1x1
        self.drawSizeObstacle: int = self.BIG

    def resetButtons(self):
        # reset all hot keys
        self.placeObstacle = False
        self.placeStart = False
        self.placeDestination = False

    def drawGrid(self):
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                pygame.draw.rect(self.SCREEN, self.WHITE, rect, 1)

    def drawNodes(self, maze: Maze):
        # assign color to each node depending on its type
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                # default color
                COLOR = self.LIGHT_BLUE

                # get node for maze
                node = maze.getNode(int(x / self.blockSize), int(y / self.blockSize))

                if node.isStart():
                    COLOR = self.ORANGE
                elif node.isDestination():
                    COLOR = self.YELLOW
                elif node.isObstacle():
                    COLOR = self.BLACK
                elif node.isPath():
                    COLOR = self.GREEN
                elif node.isSearched():
                    # calculate color of searched node

                    # get the dist from start to destination
                    # this is used to make sure that the color spectrum reaches its minimum at the starting node and
                    # its maximum and the destination node
                    totalDist = self.pathFindingAlgorithm.distFromStartToDestination

                    # get the values node.h and node.g from range 1-node.h; 1-node.g
                    h, g = max(1, node.h), max(1, node.g)

                    # create a third value that is equal to the bigger value of h and g
                    # the third value is used in rbg to ensure that the color spectrum has a wider variety
                    hgMax = max(h, g)

                    # get the percents that h; g; hgMax makes of totalDist, then set to range 1-255
                    h, g = min(255, int(255 / (totalDist / h))), min(255, int(255 / (totalDist / g)))
                    hgMax = min(255, int(255 / (totalDist / hgMax)))

                    # get color; (255/h) is implemented for lighter colors
                    COLOR = (hgMax, int(255 / h), g)

                pygame.draw.rect(self.SCREEN, COLOR, (x, y, self.blockSize, self.blockSize))

    def manageInput(self, maze: Maze):

        pos: tuple = pygame.mouse.get_pos()

        mouseX: int = int(pos[0] / self.blockSize)
        mouseY: int = int(pos[1] / self.blockSize)

        if self.mouseIsPressed and self.placeObstacle and self.drawSizeObstacle == self.SMALL:
            # set the node that is currently being selected by mouse to obstacle
            maze.getNode(mouseX, mouseY).setToObstacle()

        elif self.mouseIsPressed and self.placeObstacle and self.drawSizeObstacle == self.BIG:
            # set the node that is currently being selected by mouse and all of its children (neighbours) to obstacles
            originNode = maze.getNode(mouseX, mouseY)
            originNode.setToObstacle()
            for node in maze.getChildren(originNode):
                node.setToObstacle()

        elif self.mouseIsPressed and self.placeStart:
            maze.setStart(mouseX, mouseY)

        elif self.mouseIsPressed and self.placeDestination:
            maze.setDestination(mouseX, mouseY)

        if maze.hasStart() and maze.hasDestination():
            # init path finding algorithm

            if self.startSolvingAStar:
                self.initPathFindingAlgorithm(maze, self.A_STAR)
                self.startSolvingAStar = False

            elif self.startSolvingDijkstra:
                self.initPathFindingAlgorithm(maze, self.DIJKSTRA)
                self.startSolvingDijkstra = False

            elif self.startSolvingDepthFirstSearched:
                self.initPathFindingAlgorithm(maze, self.DEPTH_FIRST_SEARCH)
                self.startSolvingDepthFirstSearched = False

        if self.placeRandom:
            if not self.isSolving:
                if maze.currentPath is not None and self.showSolutionLengthInRandomModeCurrent < self.SHOW_SOLUTION_LENGTH_IN_RANDOM_MODE:
                    self.showSolutionLengthInRandomModeCurrent += 1

                else:
                    # reset time
                    self.showSolutionLengthInRandomModeCurrent = 0

                    if maze.getStart() is None:
                        # set random start if no start has been selected yet
                        while maze.getStart() is None:
                            maze.setStart(random.randint(0, maze.width - 1), random.randint(0, maze.height - 1))
                    else:
                        # set random start if start has been selected
                        x, y = maze.getStart().x, maze.getStart().y
                        while maze.getStart().x is x or maze.getStart().y is y:
                            maze.setStart(random.randint(0, maze.width - 1), random.randint(0, maze.height - 1))

                    if maze.getDestination() is None:
                        # set random destination if no start has been selected yet
                        while maze.getDestination() is None:
                            maze.setDestination(random.randint(0, maze.width - 1), random.randint(0, maze.height - 1))
                    else:
                        # set random destination if start has been selected
                        x, y = maze.getDestination().x, maze.getDestination().y
                        while maze.getDestination().x is x or maze.getDestination().y is y:
                            maze.setDestination(random.randint(0, maze.width - 1), random.randint(0, maze.height - 1))

                    # set random solution algorithm
                    r = random.randint(0, 2)
                    if r == 0:
                        self.startSolvingAStar = True

                    elif r == 1:
                        self.startSolvingDijkstra = True

                    elif r == 2:
                        self.startSolvingDepthFirstSearched = True

    def initPathFindingAlgorithm(self, maze: Maze, solutionAlgorithmType: int):
        # if there was a search before => hide
        if self.pathFindingAlgorithm is not None:
            self.pathFindingAlgorithm.hideSearched()

        self.pathFindingAlgorithm = PathFindingAlgorithm(maze, solutionAlgorithmType)
        # the maze will now get gradually solved inside self.showSolution()
        self.isSolving = True

        # delete previous solution path
        maze.deletePath()

    def showSolution(self, maze):
        if self.isSolving:
            # solves a number of nodes equal to self.searchSpeed per a main loop cycle
            for _ in range(self.searchSpeed):
                # if self.pathFindingAlgorithm.solutionCycle() is True pathFindingAlgorithm has finished
                if self.pathFindingAlgorithm.solutionCycle():
                    # if .pathSolution is None => there is no solution
                    if self.pathFindingAlgorithm.pathSolution is not None:
                        maze.createPath(self.pathFindingAlgorithm.pathSolution)

                    self.isSolving = False

    def evenHandler(self, maze: Maze):
        while True:
            # graphics
            self.drawNodes(maze)
            self.drawGrid()

            # logic
            self.manageInput(maze)
            self.showSolution(maze)

            # pygame events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    # key is pressed
                    if event.key == pygame.K_ESCAPE:
                        if maze.HasObstacles:
                            maze.deleteObstacles()
                        else:
                            self.createMenu(False, maze)

                    elif event.key == pygame.K_s:
                        self.resetButtons()
                        self.placeStart = True

                    elif event.key == pygame.K_d:
                        self.resetButtons()
                        self.placeDestination = True

                    elif event.key == pygame.K_o:
                        self.resetButtons()
                        self.placeObstacle = True
                        # for optimization
                        maze.setHasObstacles()

                    elif event.key == pygame.K_r:
                        self.resetButtons()
                        self.placeRandom = not self.placeRandom

                    elif event.key == pygame.K_1:
                        self.resetButtons()
                        self.startSolvingAStar = True

                    elif event.key == pygame.K_2:
                        self.resetButtons()
                        self.startSolvingDijkstra = True

                    elif event.key == pygame.K_3:
                        self.resetButtons()
                        self.startSolvingDepthFirstSearched = True

                    elif event.unicode == "+":

                        if self.placeObstacle:
                            self.drawSizeObstacle = self.BIG

                        if self.isSolving:
                            self.searchSpeed += 1
                            # search speed can only range from 1-5
                            self.searchSpeed = min(5, self.searchSpeed)

                    elif event.unicode == "-":

                        if self.placeObstacle:
                            self.drawSizeObstacle = self.SMALL

                        if self.isSolving:
                            self.searchSpeed -= 1
                            # search speed can only range from 1-5
                            self.searchSpeed = max(1, self.searchSpeed)

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.mouseIsPressed = True

                elif event.type == pygame.MOUSEBUTTONUP:
                    self.mouseIsPressed = False

            pygame.display.update()

    def createMenu(self, gameHasStarted: bool, maze: Maze):
        def resumeGame():
            self.evenHandler(maze)

        playString = "START"
        if not gameHasStarted:
            playString = "RESUME"

        # create menu
        surface = create_example_window('Maze Solver', (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        menu = pygame_menu.Menu('Maze Solver', self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.label('--------------------------------------------------')
        menu.add.button(playString, resumeGame)
        menu.add.button('QUIT', pygame_menu.events.EXIT)
        menu.add.label('--------------------------------------------------')
        menu.add.label("")
        menu.add.label("|   ------------- CONTROLS ------------   |")
        menu.add.label('| S + MOUSE => selects start           |')
        menu.add.label('| D + MOUSE => selects finish         |')
        menu.add.label('| O + MOUSE => adds obstacle       |')
        menu.add.label('| R => random searches                   |')
        menu.add.label('| ESC => remove obstacles / menu |')
        menu.add.label('| 1 => solves maze with A*              |')
        menu.add.label('| 2 => solves maze with Dijkstra     |')
        menu.add.label('| 3 => solves maze with DFS            |')
        menu.add.label("--------------------------------------------------")
        menu.add.label('|          Author: Oliver Morgan          |')
        menu.add.label("")

        menu.mainloop(surface)
