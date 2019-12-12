from entities import entity

class Wall(entity.Entity):
    """A wall that neither the player nor the enemies can pass through."""
    
    def __init__(self, x, y):
        """Sets the position of a wall."""
        
        super().__init__(x, y)

class Loot(entity.Entity):
    """A loot item that the player can pick up and enemies can pass over."""
    
    def __init__(self, x, y, points):
        """Sets the position of a loot item and how many points it is worth when collected by the player character."""
        
        super().__init__(x, y)
        self.points = points
        
# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()