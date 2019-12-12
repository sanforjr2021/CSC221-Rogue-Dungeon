from entities import entity

class Player(entity.MovableEntity):
    """A player character that the user controls."""
    
    def __init__(self, x, y, score, health, grid_size):
        """Creates a player character in a desired x and y position with the desired score and health."""

        super().__init__(x, y, grid_size)
        
        self.score = score
        self.health = health

        self.is_dead = False
        self._check_if_dead()

    def hurt_player(self):
        """Makes the player lose health."""
        
        self.health = self.health - 1
        self._check_if_dead()

    def receive_points(self, amount):
        """Adds an amount of points to the player's score."""
        self.score = self.score + amount
        
    def _check_if_dead(self):
        """Checks to see if the player character has reached 0 or less health and should be considered dead."""
        if self.health <= 0:
            self.is_dead = True

# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()
