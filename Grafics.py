import pygame
import pygame_menu
from Maze import Maze
from pygame_menu.examples import create_example_window


class Graphics:

    def __init__(self, width: int, height: int, blockSize: int = 20):

        self.BLACK: tuple = (0, 0, 0)
        self.WHITE: tuple = (200, 200, 200)
        self.RED: tuple = (255, 87, 51)
        self.GREEN: tuple = (106, 162, 34)
        self.PURPLE: tuple = (100, 34, 162)
        self.LIGHT_BLUE: tuple = (102, 167, 197)
        self.LIGHT_PINK: tuple = (236, 181, 235)

        self.blockSize: int = blockSize
        self.WINDOW_HEIGHT: int = width
        self.WINDOW_WIDTH: int = height

        self.SCREEN = pygame.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.SCREEN.fill(self.BLACK)

    def drawGrid(self):
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                rect = pygame.Rect(x, y, self.blockSize, self.blockSize)
                pygame.draw.rect(self.SCREEN, self.WHITE, rect, 1)

    def evenHandler(self, maze):
        while True:
            self.drawNodes(maze)
            self.drawGrid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        exit()

            pygame.display.update()

    def drawNodes(self, maze: Maze):
        for x in range(0, self.WINDOW_WIDTH, self.blockSize):
            for y in range(0, self.WINDOW_HEIGHT, self.blockSize):
                # default color
                COLOR = self.LIGHT_BLUE
                node = maze.map[int(y / self.blockSize)][int(x / self.blockSize)]

                if node.isObstacle():
                    COLOR = self.RED
                elif node.isPath():
                    COLOR = self.PURPLE

                pygame.draw.rect(self.SCREEN, COLOR, (x, y, self.blockSize, self.blockSize))

    def createMenu(self, gameHasStarted: bool, maze: Maze):
        def resumeGame():
            self.evenHandler(maze)

        playString = "START"
        if not gameHasStarted:
            playString = "RESUME"
        surface = create_example_window('Maze Solver', (self.WINDOW_WIDTH, self.WINDOW_HEIGHT))

        menu = pygame_menu.Menu('Maze Solver', self.WINDOW_WIDTH, self.WINDOW_HEIGHT,
                                theme=pygame_menu.themes.THEME_BLUE)

        menu.add.label('----------------------------------')
        menu.add.button(playString, resumeGame)
        menu.add.button('QUIT', pygame_menu.events.EXIT)
        menu.add.label('----------------------------------')
        menu.add.label("")
        menu.add.label("CONTROLS")
        menu.add.label('Ctr + S => selects start      ')
        menu.add.label('Ctr + G => selects finish     ')
        menu.add.label('Ctr + O => adds obstacle      ')
        menu.add.label('Ctr + A => solves maze with A*')
        menu.add.label("")
        menu.add.label('Author: Oliver Morgan')
        menu.add.label("")

        menu.mainloop(surface)

        return False
