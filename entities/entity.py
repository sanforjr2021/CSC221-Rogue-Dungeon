class Entity:
    """An object that the user interacts with in some way during gameplay."""
    
    def __init__(self, x, y):
        """Sets the x and y position of the entity."""
        self.x = x
        self.y = y
    
class MovableEntity(Entity):
    """An object that the user interacts with in some way during gameplay that is capable of movement."""
    
    def __init__(self, x, y, grid_size):
        """Sets the x and y position of the entity and saves the grid size."""
        super().__init__(x, y)
        self._grid_size = grid_size
        
    def move_right(self):
        """Moves the entity one tile to the right as long as it is not moving past the edge of the grid."""
        if self.x < self._grid_size - 1:
            self.x = self.x + 1

    def move_left(self):
        """Moves the entity one tile to the left as long as it is not moving past the edge of the grid."""
        if self.x > 0:
            self.x = self.x - 1

    def move_up(self):
        """Moves the entity one tile up as long as it is not moving past the edge of the grid."""
        if self.y > 0:
            self.y = self.y - 1
    
    def move_down(self):
        """Moves the entity one tile down as long as it is not moving past the edge of the grid."""
        if self.y < self._grid_size - 1:
            self.y = self.y + 1
            
# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()