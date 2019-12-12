import random
from entities import entity

class Enemy(entity.MovableEntity):
    """An enemy that the player character must defeat to win the game."""
    
    def __init__(self, x, y, grid_size):
        """Creates an enemy in a desired x and y position and takes in the width/height of the grid."""
        super().__init__(x, y, grid_size)
        
        self._movement = {
            0: super().move_right,
            1: super().move_left,
            2: super().move_up,
            3: super().move_down,
            4: self._idle
        }

    def random_movement(self):
        """Moves the enemy in a random direction or causes it to idle."""
        _direction = self._movement.get(random.randint(0, 4))
        _direction()
        
    def _idle(self):
        """The enemy stays in the same position."""
        pass

# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()