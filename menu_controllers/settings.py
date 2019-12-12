class Settings:
    """Stores the settings values that can be edited to modify the gameplay."""
    
    def __init__(self):
        """Sets the default values for the settings."""
        
        self.num_health = 3
        self.num_walls = 8
        self.num_loot = 5
        self.num_enemies = 6
        self.grid_size = 10

# ======================================================== #
# PUBLIC SETTERS
# ======================================================== #

    def set_spawn_settings(self, menu):
        """Prompts the user for new settings values and checks if the values are acceptable."""
        
        # Runs a loop until the user has entered an acceptable value for the number of walls.
        self._walls_done = False
        while not self._walls_done:
            self._set_num_walls()
        
        print()
        
        # Runs a loop until the user has entered an acceptable value for the number of loot items.
        self._loot_done = False
        while not self._loot_done:
            self._set_num_loot()
        
        print()
        
        # Runs a loop until the user has entered an acceptable value for the number of enemies.
        self._enemies_done = False
        while not self._enemies_done:
            self._set_num_enemies()
        
        print()
        
        # Runs a loop until the user has entered an acceptable value for the size of the grid.
        self._grid_size_done = False
        while not self._grid_size_done:
            self._set_grid_size()
        
        # Calculates how many tiles will be in the grid.
        _area = self._grid_size_temp * self._grid_size_temp
        
        # Checks if the sum of the enemies, walls, and the player character is too large to fit within the selected grid size.
        if self._num_enemies_temp + self._num_walls_temp + 1 > _area:
            print()
            print("There is not enough grid space to spawn everything you requested. Please")
            print("decrease the number of walls and/or enemies, or increase the length/width")
            print("of the grid.")
            print()
            
            raise InvalidInputError
            
        # Checks if the sum of the loot items, walls, and the player character is too large to fit within the selected grid size.
        elif self._num_loot_temp + self._num_walls_temp + 1 > _area:
            print()
            print("There is not enough grid space to spawn everything you requested. Please")
            print("decrease the number of walls and/or loot items, or increase the length/")
            print("width of the grid.")
            print()
            
            raise InvalidInputError
        
        # If all checks pass, the settings are saved.
        else:
            self.num_walls = self._num_walls_temp
            self.num_enemies = self._num_enemies_temp
            self.num_loot = self._num_loot_temp
            self.grid_size = self._grid_size_temp
            
    def set_num_health(self, menu):
        """Sets the amount of health the player character will have. The health value must be a positive integer."""
        
        try:
            _possible_health = int(input("Please type the number of health points the player will have: "))
            if _possible_health <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
                raise InvalidInputError
            else:
                self.num_health = _possible_health
        except ValueError:
            print("The value entered is not an integer value.")
            raise InvalidInputError

# ======================================================== #
# PRIVATE SETTERS
# ======================================================== #

    def _set_num_walls(self):
        """Sets the number of walls that will appear on the grid. The number of walls must be a positive integer."""
        
        try:
            _possible_walls = int(input("Please type the number of tiles that will be walls: "))
            if _possible_walls <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
            else:
                self._num_walls_temp = _possible_walls
                self._walls_done = True
        except ValueError:
            print("The value entered is not an integer value.")

    def _set_num_enemies(self):
        """Sets the number of enemies that will appear on the grid. The number of enemies must be a positive integer."""
        
        try:
            _possible_enemies = int(input("Please type the number of enemies that will generate on the map: "))
            if _possible_enemies <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
            else:
                self._num_enemies_temp = _possible_enemies
                self._enemies_done = True
        except ValueError:
            print("The value entered is not an integer value.")

    def _set_num_loot(self):
        """Sets the number of loot items that will appear on the grid. The number of loot items must be a positive integer."""
        
        try:
            _possible_loot = int(input("Please type the number of loot items that will generate on the map: "))
            if _possible_loot <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
            else:
                self._num_loot_temp = _possible_loot
                self._loot_done = True
        except ValueError:
            print("The value entered is not an integer value.")

    def _set_grid_size(self):
        """Sets the length and width of the square grid. The grid size must be a positive integer."""
        
        try:
            _possible_grid_size = int(input("Please type the number that represents the length and width of the grid: "))
            if _possible_grid_size <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
            else:
                self._grid_size_temp = _possible_grid_size
                self._grid_size_done = True
        except ValueError:
            print("The value entered is not an integer value.")
            
# ======================================================== #
# ERRORS
# ======================================================== #

class InvalidInputError(Exception):
    """An Exception to detect if the user has entered an incorrect value for a setting input."""
    
    pass

# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()