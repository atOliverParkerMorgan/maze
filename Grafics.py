import pygame
import pygame_menu
from PathFindingAlgorithm import PathFindingAlgorithm
from Maze import Maze
from pygame_menu.examples import create_example_window


class Graphics:

    def __init__(self, width: int, height: int, blockSize: int = 20):

        self.SMALL: int = 0
        self.BIG: int = 1

        self.A_STAR = 0
        self.DIJKSTRA = 1
        self.DEPTH_FIRST_SEARCH = 2

        self.BLACK: tuple = (0, 0, 0)
        self.WHITE: tuple = (200, 200, 200)
        self.RED: tuple = (255, 87, 51)
        self.ORANGE: tuple = (200, 162, 34)
        self.GREEN: tuple = (50, 205, 50)
        self.PURPLE: tuple = (100, 34, 162)
        self.YELLOW: tuple = (255, 255, 0)
        self.LIGHT_BLUE: tuple = (102, 167, 197)
        self.LIGHT_PINK: tuple = (236, 181, 235)

        self.blockSize: int = blockSize
        self.WINDOW_HEIGHT: int = width
        self.WINDOW_WIDTH: int = height

        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(self.BLACK)

        self.mouseIsPressed: bool = False

        self.placeObstacle: bool = False
        self.placeStart: bool = False
        self.placeDestination: bool = False
        self.startSolvingAStar: bool = False
        self.startSolvingDijkstra: bool = False
        self.startSolvingDepthFirstSearched: bool = False

        self.isSolving: bool = False

        self.pathFindingAlgorithm = None
        self.drawSizeObstacle: int = self.BIG

    def resetButtons(self):
        self.placeObstacle = False
        self.placeStart = False
        self.placeDestination = False
        self.startSolvingAStar = False

    def drawGrid(self):
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                pygame.draw.rect(self.SCREEN, self.WHITE, rect, 1)

    def drawNodes(self, maze: Maze):
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                # default color
                COLOR = self.LIGHT_BLUE
                node = maze.map[int(y / self.blockSize)][int(x / self.blockSize)]

                if node.isStart():
                    COLOR = self.ORANGE
                elif node.isDestination():
                    COLOR = self.YELLOW
                elif node.isObstacle():
                    COLOR = self.BLACK
                elif node.isPath():
                    COLOR = self.GREEN
                elif node.isSearched():
                    totalDist = self.pathFindingAlgorithm.distFromStartToDestination
                    h, g = max(1, node.h), max(1, node.g)
                    hgMax = max(h, g)
                    h, g = min(255, int(255 / (totalDist / h))), min(255, int(255 / (totalDist / g)))
                    hgMax = min(255, int(255 / (totalDist / hgMax)))
                    COLOR = (hgMax, int(255 / h), g)

                pygame.draw.rect(self.SCREEN, COLOR, (x, y, self.blockSize, self.blockSize))

    def manageInput(self, maze: Maze):
        pos: tuple = pygame.mouse.get_pos()

        mouseX: int = int(pos[0] / self.blockSize)
        mouseY: int = int(pos[1] / self.blockSize)

        if self.mouseIsPressed and self.placeObstacle and self.drawSizeObstacle == self.SMALL:
            maze.getNode(mouseX, mouseY).setToObstacle()

        elif self.mouseIsPressed and self.placeObstacle and self.drawSizeObstacle == self.BIG:
            originNode = maze.getNode(mouseX, mouseY)
            originNode.setToObstacle()
            for node in maze.getChildren(originNode):
                node.setToObstacle()

        elif self.mouseIsPressed and self.placeStart:
            maze.setStart(mouseX, mouseY)

        elif self.mouseIsPressed and self.placeDestination:
            maze.setDestination(mouseX, mouseY)

        elif self.startSolvingAStar and maze.hasStart() and maze.hasDestination():
            if self.pathFindingAlgorithm is not None:
                self.pathFindingAlgorithm.hideSearched()

            self.pathFindingAlgorithm = PathFindingAlgorithm(maze, self.A_STAR)
            self.startSolvingAStar = False
            self.isSolving = True
            maze.deletePath()

        elif self.startSolvingDijkstra and maze.hasStart() and maze.hasDestination():
            if self.pathFindingAlgorithm is not None:
                self.pathFindingAlgorithm.hideSearched()

            self.pathFindingAlgorithm = PathFindingAlgorithm(maze, self.DIJKSTRA)
            self.startSolvingDijkstra = False
            self.isSolving = True
            maze.deletePath()

    def showSolution(self, maze):
        if self.isSolving:
            if self.pathFindingAlgorithm.solutionCycle():
                if self.pathFindingAlgorithm.pathSolution is not None:
                    maze.createPath(self.pathFindingAlgorithm.pathSolution)

                self.isSolving = False

    def evenHandler(self, maze: Maze):
        while True:
            self.drawNodes(maze)
            self.drawGrid()
            self.manageInput(maze)
            self.showSolution(maze)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()
                    elif event.key == pygame.K_s:
                        self.resetButtons()
                        self.placeStart = True

                    elif event.key == pygame.K_d:
                        self.resetButtons()
                        self.placeDestination = True

                    elif event.key == pygame.K_o:
                        self.resetButtons()
                        self.placeObstacle = True

                    elif event.key == pygame.K_a:
                        self.resetButtons()
                        self.startSolvingAStar = True

                    elif event.unicode == "+":
                        self.drawSizeObstacle = self.BIG

                    elif event.unicode == "-":
                        self.drawSizeObstacle = self.SMALL

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
        surface = create_example_window('Maze Solver', (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        menu = pygame_menu.Menu('Maze Solver', self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)
        menu.add.label('--------------------------------------------------')
        menu.add.button(playString, resumeGame)
        menu.add.button('QUIT', pygame_menu.events.EXIT)
        menu.add.label('--------------------------------------------------')
        menu.add.label("")
        menu.add.label("| ------------ CONTROLS ----------- |")
        menu.add.label('|   S + MOUSE => selects start   |')
        menu.add.label('|  D + MOUSE => selects finish  |')
        menu.add.label('| O + MOUSE => adds obstacle |')
        menu.add.label('|    A => solves maze with A*     |')
        menu.add.label("--------------------------------------------------")
        menu.add.label('|       Author: Oliver Morgan      |')
        menu.add.label("")

        menu.mainloop(surface)
