# By Jacob Sanford & Alec Barker
# Date: 10/1/19
# Description: Load the basic Code

import sys
import colors

def main():
    pygame.init()
    
    # Create the window, saving it to a variable.
    surface = pygame.display.set_mode((350, 250), pygame.RESIZABLE)
    pygame.display.set_caption("Rogue Dungeon")
    
    # The factor at which the tiles are divided from the window size
    divFactor = 10

    while True:
        # Calculates the size of each tile
        tileSize = surface.get_height()/divFactor
        
        """ DRAW OBJECTS AFTER HERE """
        
        # Background fill color
        surface.fill(colors.black)
        
        drawPlayer(surface, tileSize)
        
        """ DRAW OBJECTS BEFORE HERE """
        
        # Updates the objects being displayed
        pygame.display.update()
        
        # Runs listeners for various inputs
        runListeners(surface)
        
def runListeners(surface):
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

        # Refreshes window if size changes
        if event.type == pygame.VIDEORESIZE:
            surface = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
def drawPlayer(surface, tileSize):
    # Draws the player character in the center of the screen
    x = surface.get_width()/2 - tileSize/2
    y = surface.get_height()/2 - tileSize/2
    pygame.draw.rect(surface, colors.red, (x, y, tileSize, tileSize))
    


if __name__ == '__main__':
    try:
        import pygame
    except ImportError:
        print("Error: pygame not installed")
        print("Type this to install pygame on a windows machine: py -m pip install -U pygame --user")
        quit()
    main()
