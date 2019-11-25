import sys
import colors
import player
import pygame
import enemy
import random


class GraphicsWindow:

    def __init__(self):
        pygame.init()

        self.createWindow()

        # The factor at which the tiles are divided from the window size
        self.divFactor = 10

        self.player = player.Player(0, 0, 0, 3)
        self.enemies = []
        self.generateEnemies(4)
        while True:
            self.calculateTileSize()
            self.calculateFontSize()

            self.draw()

            # Updates the objects being displayed
            pygame.display.update()

            # Runs listeners for various inputs
            self.runListeners()

    def calculateTileSize(self):
        # Calculates the size of each tile by determining if the width or height is smallest
        if self.surface.get_height() < self.surface.get_width():
            self.tileSize = self.surface.get_height() / (self.divFactor + 2)
        else:
            self.tileSize = self.surface.get_width() / self.divFactor

    def calculateFontSize(self):
        # Calculates the size of the font based on the window size
        if self.surface.get_height() < self.surface.get_width():
            self.fontSize = int(self.surface.get_height() / self.divFactor / 1.5)
        else:
            self.fontSize = int(self.surface.get_width() / self.divFactor / 1.5)

    def createWindow(self):
        # Create the window and change settings
        self.surface = pygame.display.set_mode((350, 420), pygame.RESIZABLE)
        pygame.display.set_caption("Rogue Dungeon")
        try:
            self.icon = pygame.image.load('rd-logo.png')
            pygame.display.set_icon(self.icon)
        except pygame.error:
            print('Could not load logo')

    def runListeners(self):
        # For loop to detect event changes
        for event in pygame.event.get():
            # Shuts everything down if the program closes
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Listens for specific key presses
            if event.type == pygame.KEYDOWN:
                # Closes the program if the escape key is pressed
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if not self.player.isDead: #Check if player is not dead
                    # Moves player to the right as long as they are within the grid boundaries
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.x < self.divFactor - 1:
                        self.player.moveRight()
                        self.calculateCPUMovement()
                    # Moves player to the left as long as they are within the grid boundaries
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.x > 0:
                        self.player.moveLeft()
                        self.calculateCPUMovement()
                    # Moves player up as long as they are within the grid boundaries
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.y > 0:
                        self.player.moveUp()
                        self.calculateCPUMovement()
                    # Moves player down as long as they are within the grid boundaries
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.y < self.divFactor - 1:
                        self.player.moveDown()
                        self.calculateCPUMovement()
                    # The player attacks any target in each direction touching him and gain 50 points for each one killed.
                    if event.key == pygame.K_e:
                        for theEnemy in self.enemies:
                            if (theEnemy.x == self.player.x + 1 or theEnemy.x == self.player.x - 1) and (
                                    theEnemy.y == self.player.y + 1 or theEnemy.y == self.player.y - 1):
                                self.enemies.remove(theEnemy)
                                self.player.receivePoints(50)
                        self.calculateCPUMovement()

            # Refreshes window if size changes
            if event.type == pygame.VIDEORESIZE:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    def calculateCPUMovement(self):
        for theEnemy in self.enemies:
            # Move the enemy
            theEnemy.randomMovement()
            # Detect if it hits the player
            if theEnemy.x == self.player.x and theEnemy.y == self.player.y:
                self.enemies.remove(theEnemy)
                self.player.hurtPlayer()
                self.player.receivePoints(-100)

    def generateEnemies(self, numOfEnemies):
        # TODO:Check that it does not spawn on the player.
        for x in range(numOfEnemies):
            self.enemies.append(enemy.Enemy(
                random.randint(0, self.divFactor - 1), random.randint(0, self.divFactor - 1), self.divFactor
            ))

# =======================================================#
# DRAWING FUNCTIONS#

    def draw(self):
        # Background fill color
        self.surface.fill(colors.black)
        self.drawGrid()
        self.drawPlayer()
        self.drawText()
        self.drawEnemies()

    def drawText(self):
        font = pygame.font.SysFont('Tahoma', self.fontSize)
        if self.player.isDead:
            health = font.render('You Died', True, (255, 0, 0))
        else:
            health = font.render('Health: ' + str(self.player.health), True, (255, 255, 0))
        self.surface.blit(health, (0 + self.tileSize / 4, self.tileSize * self.divFactor))

        score = font.render('Score: ' + str(self.player.score), True, (255, 255, 0))
        self.surface.blit(score, (0 + self.tileSize / 4, self.tileSize * self.divFactor + self.tileSize))

    def drawGrid(self):
        # Draws a grid of specified size
        for y in range(self.divFactor):
            for x in range(self.divFactor):
                rect = pygame.Rect(x * self.tileSize, y * self.tileSize, self.tileSize, self.tileSize)
                pygame.draw.rect(self.surface, colors.blue, rect, 1)

        rect = pygame.Rect(0, self.tileSize * self.divFactor, self.tileSize * self.divFactor, self.tileSize * 2)
        pygame.draw.rect(self.surface, colors.blue, rect, 1)

    def drawPlayer(self):
        rect = pygame.Rect(self.player.x * self.tileSize, self.player.y * self.tileSize, self.tileSize, self.tileSize)
        if not self.player.isDead:
            pygame.draw.rect(self.surface, colors.green, rect)
        else:
            pygame.draw.rect(self.surface, colors.purple, rect)

    def drawEnemies(self):
        for theEnemy in self.enemies:
            rect = pygame.Rect(theEnemy.x * self.tileSize, theEnemy.y * self.tileSize, self.tileSize, self.tileSize)
            pygame.draw.rect(self.surface, colors.red, rect)
# =======================================================#
