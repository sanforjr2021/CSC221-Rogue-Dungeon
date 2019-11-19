import sys
import colors
import player
import pygame

class GraphicsWindow:
        
    def __init__(self):    
        pygame.init()
        
        self.createWindow()
        
        # The factor at which the tiles are divided from the window size
        self.divFactor = 10
        
        self.player = player.Player(0, 0, 0, 3)

        while True:
            self.calculateTileSize()
            
            self.drawOnWindow()
            
            # Updates the objects being displayed
            pygame.display.update()
            
            # Runs listeners for various inputs
            self.runListeners()
               
    def calculateTileSize(self):
        # Calculates the size of each tile by determining if the width or height is smallest
        if self.surface.get_height() < self.surface.get_width():
            self.tileSize = self.surface.get_height()/self.divFactor
        else:
            self.tileSize = self.surface.get_width()/self.divFactor
    
    def createWindow(self):
        # Create the window and change settings
        self.surface = pygame.display.set_mode((350, 350), pygame.RESIZABLE)
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
                    
                # Moves player to the right as long as they are within the grid boundaries
                if (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and self.player.x < self.divFactor - 1:
                    self.player.moveRight()
                
                # Moves player to the left as long as they are within the grid boundaries
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and self.player.x > 0:
                    self.player.moveLeft()
                    
                # Moves player up as long as they are within the grid boundaries
                if (event.key == pygame.K_UP or event.key == pygame.K_w) and self.player.y > 0:
                    self.player.moveUp()
                    
                # Moves player down as long as they are within the grid boundaries
                if (event.key == pygame.K_DOWN or event.key == pygame.K_s) and self.player.y < self.divFactor - 1:
                    self.player.moveDown()

            # Refreshes window if size changes
            if event.type == pygame.VIDEORESIZE:
                self.surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            
#=======================================================#
#DRAWING FUNCTIONS#
    def drawOnWindow(self):
        # Background fill color
        self.surface.fill(colors.black)
        
        self.drawGrid()
        self.drawPlayer()
    
    def drawGrid(self):
        # Draws a grid of specified size
        for y in range(self.divFactor):
                for x in range(self.divFactor):
                    rect = pygame.Rect(x*self.tileSize, y*self.tileSize, self.tileSize, self.tileSize)
                    pygame.draw.rect(self.surface, colors.blue, rect, 1)
    
    def drawPlayer(self):
        rect = pygame.Rect(self.player.x*self.tileSize, self.player.y*self.tileSize, self.tileSize, self.tileSize)
        pygame.draw.rect(self.surface, colors.red, rect)
#=======================================================# 