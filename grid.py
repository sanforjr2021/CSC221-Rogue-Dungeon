# A grid that contains tiles with objects.

import random

class InvalidInputError(Exception):
    pass

class Grid:
    def __init__(self, numHorTiles, numVerTiles):
        if numHorTiles <= 0 or numVerTiles <= 0:
            raise InvalidInputError()
        else:
            self.gridArray = [[0 for x in range(numHorTiles + 1)] for y in range(numVerTiles + 1)]
        
        # Checks if a player exists yet on the grid
        playerExists = False
        
        # Fills the grid with the player, enemies, loot, or blank tiles randomly
        for y in range(numVerTiles):
            for x in range(numHorTiles):
                # Creates a random number between 0-19
                rand = random.randrange(20)
                
                # If it is the last tile in the grid and no player has spawned yet,
                # the player is guaranteed to spawn in the last tile
                if x == numHorTiles - 1 and y == numVerTiles - 1 and playerExists == False:
                    self.gridArray[x][y] = 'Player'
                    playerExists = True
                    
                # 1/20 chance of being the player spawn if they do not already have a spawn
                elif rand == 0 and playerExists == False:
                    self.gridArray[x][y] = 'Player'
                    playerExists = True
                    
                # 3/20 chance of being an enemy
                elif 1 <= rand and rand < 4:
                    self.gridArray[x][y] = 'Enemy'
                
                # 6/20 chance of being loot
                elif 4 <= rand and rand < 10:
                    self.gridArray[x][y] = 'Loot'
                
                # 10/20 chance of being a blank tile
                else:
                    self.gridArray[x][y] = 'Blank'
                
                print(str(x) + ' ' + str(y) + ' ' + self.gridArray[x][y])