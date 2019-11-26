import sys
import colors
import player
import pygame
import enemy
import random

import tile


class GraphicsWindow:

    def __init__(self):
        pygame.init()
        self.createWindow()

        # The factor at which the tiles are divided from the window size
        self.divFactor = 10

        self.player = player.Player(0, 0, 0, 3)
        self.walls = []
        self.loots = []
        self.enemies = []
        # Generation
        self.generateWalls(8)
        self.generatePlayer()
        self.generateLoot(5)
        self.generateEnemies(6)

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
                if not self.player.isDead:  # Check if player is not dead
                    # Moves player to the right as long as they are within the grid boundaries
                    if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.x < self.divFactor - 1:
                        for theWall in self.walls:
                            if theWall.x == self.player.x+1 and theWall.y == self.player.y:
                                self.calculateCPUMovement()
                                return
                        self.player.moveRight()
                        self.calculateCPUMovement()
                    # Moves player to the left as long as they are within the grid boundaries
                    if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.x > 0:
                        for theWall in self.walls:
                            if theWall.x == self.player.x-1 and theWall.y == self.player.y:
                                self.calculateCPUMovement()
                                return
                        self.player.moveLeft()
                        self.calculateCPUMovement()
                    # Moves player up as long as they are within the grid boundaries
                    if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.y > 0:
                        for theWall in self.walls:
                            if theWall.x == self.player.x and theWall.y == self.player.y - 1:
                                self.calculateCPUMovement()
                                return
                        self.player.moveUp()
                        self.calculateCPUMovement()
                    # Moves player down as long as they are within the grid boundaries
                    if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.y < self.divFactor - 1:
                        for theWall in self.walls:
                            if theWall.x == self.player.x and theWall.y == self.player.y + 1:
                                self.calculateCPUMovement()
                                return
                        self.player.moveDown()
                        self.calculateCPUMovement()
                    # The player attacks any target in each direction touching him
                    if event.key == pygame.K_e:
                        self.calculateCPUMovement()
                        for theEnemy in self.enemies:
                            if (
                                    theEnemy.x == self.player.x + 1 or theEnemy.x == self.player.x - 1 or theEnemy.x == self.player.x) \
                                    and (
                                    theEnemy.y == self.player.y + 1 or theEnemy.y == self.player.y - 1 or theEnemy.y == self.player.y):
                                self.enemies.remove(theEnemy)
                                self.player.receivePoints(50)

            # Refreshes window if size changes
            if event.type == pygame.VIDEORESIZE:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)

    def calculateCPUMovement(self):
        for theEnemy in self.enemies:
            try:
                x = theEnemy.x
                y = theEnemy.y
                theEnemy.randomMovement()
                # Stop the enemy from walking through another enemy
                for theOtherEnemy in self.enemies:
                    if theEnemy.x == theOtherEnemy.x and theEnemy.y == theOtherEnemy.y and theEnemy != theOtherEnemy:
                        theEnemy.x = x
                        theEnemy.y = y
                        raise StackedObjectError
                # Stop the enemy from walking into a wall
                for theWall in self.walls:
                    if theEnemy.x == theWall.x and theEnemy.y == theWall.y:
                        theEnemy.x = x
                        theEnemy.y = y
                        raise StackedObjectError
            except StackedObjectError:
                print("Enemy moved on top of enemy in line 111")
                pass
            # Detect if it hits the player
            if theEnemy.x == self.player.x and theEnemy.y == self.player.y:
                self.enemies.remove(theEnemy)
                self.player.hurtPlayer()
                self.player.receivePoints(-100)
            for theLoot in self.loots:
                if theLoot.x == self.player.x and theLoot.y == self.player.y:
                    self.player.receivePoints(theLoot.points)
                    self.loots.remove(theLoot)
    # =================================================== #
    # Generation
    # =================================================== #
    def generateWalls(self, numOfWalls):
        for x in range(numOfWalls):
            try:
                # Check to see if a wall generated on another wall
                tempWall = tile.TileWall(random.randint(0, self.divFactor - 1), random.randint(0, self.divFactor - 1))
                for theWall in self.walls:
                    if tempWall.x == theWall.x and tempWall.y == theWall.y:
                        raise StackedObjectError
                self.walls.append(tempWall)
            except StackedObjectError:
                print("Regenerating Wall")
                self.generateWalls(1)

    def generatePlayer(self):

        try:
            # Check to see if the player generated on a wall
            for theWall in self.walls:
                if self.player.x == theWall.x and self.player.y == theWall.y:
                    raise StackedObjectError
            self.player = player.Player(random.randint(0, self.divFactor - 1), random.randint(0, self.divFactor - 1), 0,
                                        3)
        except StackedObjectError:
            print("Regenerating Player")
            self.generatePlayer()

    def generateLoot(self, numOfLoots):
        for x in range(numOfLoots):
            try:
                tempLoot = tile.TileLoot(random.randint(0, self.divFactor - 1), random.randint(0, self.divFactor - 1),
                                         (random.randint(1, 12) * 25))
                # Check to see if the loot generated ontop of the player
                if self.player.x == tempLoot.x and self.player.y == tempLoot.y:
                    raise StackedObjectError
                # Check to see if the loot generated on the wall
                for theWall in self.walls:
                    if tempLoot.x == theWall.x and tempLoot.y == theWall.y:
                        raise StackedObjectError
                # Check to see if loot generated ontop of other loot.
                for theLoot in self.loots:
                    if tempLoot.x == theLoot.x and tempLoot.y == theLoot.y:
                        raise StackedObjectError
                self.loots.append(tempLoot)
            except StackedObjectError:
                print("Regenerating loot")
                self.generateLoot(1)

    def generateEnemies(self, numOfEnemies):
        for x in range(numOfEnemies):
            try:
                tempEnemy = enemy.Enemy(random.randint(0, self.divFactor - 1), random.randint(0, self.divFactor - 1),
                                        self.divFactor)
                # Check to see if the enemy spawned on a wall
                for theWall in self.walls:
                    if tempEnemy.x == theWall.x and tempEnemy.y == theWall.y:
                        raise StackedObjectError
                # Check to see if the enemy spawned on the player
                if tempEnemy.x == self.player.x and tempEnemy.y == self.player.y:
                    raise StackedObjectError
                # Check to see if the enemy spawned ontop of another enemy
                for theEnemy in self.enemies:
                    if theEnemy.x == tempEnemy.x and theEnemy.y == tempEnemy.y:
                        raise StackedObjectError

                self.enemies.append(tempEnemy)
            except StackedObjectError:
                # Force the program to regenerate an enemy in said spot.
                print("Regenerating Enemy")
                self.generateEnemies(1)

    # =======================================================#
    # DRAWING FUNCTIONS#
    # =======================================================#

    def draw(self):
        # Background fill color
        self.surface.fill(colors.black)
        self.drawGrid()
        self.drawLoots()
        self.drawPlayer()
        self.drawText()
        self.drawEnemies()
        self.drawWalls()

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

    def drawLoots(self):
        for theLoot in self.loots:
            rect = pygame.Rect(theLoot.x * self.tileSize, theLoot.y * self.tileSize, self.tileSize, self.tileSize)
            pygame.draw.rect(self.surface, colors.yellow, rect)

    def drawWalls(self):
        for theWall in self.walls:
            rect = pygame.Rect(theWall.x * self.tileSize, theWall.y * self.tileSize, self.tileSize, self.tileSize)
            pygame.draw.rect(self.surface, colors.blue, rect)


# =======================================================#
# Exceptions
# ========================================================#

class StackedObjectError(Exception):
    """ An Exception to detect if an enemy was moved onto another enemy."""
    pass
