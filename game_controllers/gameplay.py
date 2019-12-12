import random
from entities import static_entities
from entities import player
from entities import enemy

class Gameplay:
    """Controls the actions that the player takes."""
    
    def __init__(self, _settings):
        """Instantiates a variable to check if the user has won and generates a player character, walls, loot, and enemies."""
        
        # Sets a variable that the player has not won the game yet.
        self.has_won = False
        
        # Saves the length and width of the grid.
        self._grid_size = _settings.grid_size
        
        # Creates arrays to hold the walls, loot, and enemies.
        self.walls = []
        self.loot = []
        self.enemies = []
        
        # Generates walls, loot, enemies, and a player.
        self._generate_entities(_settings)

    # ======================================================== #
    # GENERATE ENEMIES ON THE GRID
    # ======================================================== #
    
    def _generate_entities(self, _settings):
        """Generates each of the entity types."""
        
        self._generate_player(_settings.num_health)
        self._generate_walls(_settings.num_walls)
        self._generate_loot(_settings.num_loot)
        self._generate_enemies(_settings.num_enemies)
        
    def _generate_player(self, _num_health):
        """Generates a player character in a random position on the grid."""
        
        self.player = player.Player(random.randint(0, self._grid_size - 1), random.randint(0, self._grid_size - 1), 0, _num_health, self._grid_size)
    
    def _generate_walls(self, _num_walls):
        """Generates a number of walls in random positions on the grid."""
        
        for _x in range(_num_walls):
            try:
                # Checks to see if a wall generated on another wall.
                _temp_wall = static_entities.Wall(random.randint(0, self._grid_size - 1), random.randint(0, self._grid_size - 1))
                
                for _wall in self.walls:
                    if _temp_wall.x == _wall.x and _temp_wall.y == _wall.y:
                        raise StackedObjectError
                
                self.walls.append(_temp_wall)
            except StackedObjectError:
                # Forces the program to regenerate a wall in said spot.
                self._generate_walls(1)

    def _generate_loot(self, _num_loot):
        """Generates a number of loots items in random positions on the grid."""
        
        for _x in range(_num_loot):
            try:
                _temp_loot = static_entities.Loot(random.randint(0, self._grid_size - 1), random.randint(0, self._grid_size - 1),
                                         (random.randint(1, 12) * 25))
                # Checks to see if the loot generated ontop of the player.
                if self.player.x == _temp_loot.x and self.player.y == _temp_loot.y:
                    raise StackedObjectError
                
                # Check to see if the loot generated on the wall.
                for _wall in self.walls:
                    if _temp_loot.x == _wall.x and _temp_loot.y == _wall.y:
                        raise StackedObjectError
                
                # Check to see if loot generated on top of other loot.
                for _loot in self.loot:
                    if _temp_loot.x == _loot.x and _temp_loot.y == _loot.y:
                        raise StackedObjectError
                
                self.loot.append(_temp_loot)
            except StackedObjectError:
                # Forces the program to regenerate loot in said spot.
                self._generate_loot(1)

    def _generate_enemies(self, _num_enemies):
        """Generates a number of walls in random positions on the grid."""
        
        for _x in range(_num_enemies):
            try:
                _temp_enemy = enemy.Enemy(random.randint(0, self._grid_size - 1), random.randint(0, self._grid_size - 1), self._grid_size)
                
                # Checks to see if the enemy spawned on a wall.
                for _wall in self.walls:
                    if _temp_enemy.x == _wall.x and _temp_enemy.y == _wall.y:
                        raise StackedObjectError
                
                # Checks to see if the enemy spawned on the player.
                if _temp_enemy.x == self.player.x and _temp_enemy.y == self.player.y:
                    raise StackedObjectError
                
                # Checks to see if the enemy spawned on top of another enemy.
                for _enemy in self.enemies:
                    if _enemy.x == _temp_enemy.x and _enemy.y == _temp_enemy.y:
                        raise StackedObjectError

                self.enemies.append(_temp_enemy)
            except StackedObjectError:
                # Forces the program to regenerate an enemy in said spot.
                self._generate_enemies(1)

    # ======================================================== #
    # CONTROLS ENTITY INTERACTIONS
    # ======================================================== #
                
    def move_enemies(self):
        """Determines how each enemy should move around the grid."""
        
        for _enemy in self.enemies:
            try:
                _x = _enemy.x
                _y = _enemy.y
                _enemy.random_movement()
                
                # Stops the enemy from walking through another enemy.
                for _other_enemy in self.enemies:
                    if _enemy.x == _other_enemy.x and _enemy.y == _other_enemy.y and _enemy != _other_enemy:
                        _enemy.x = _x
                        _enemy.y = _y
                        raise StackedObjectError
                
                # Stops the enemy from walking into a wall.
                for _wall in self.walls:
                    if _enemy.x == _wall.x and _enemy.y == _wall.y:
                        _enemy.x = _x
                        _enemy.y = _y
                        raise StackedObjectError
            except StackedObjectError:
                pass
            
            # Detects if an enemy hits the player.
            # If so, the enemy dies, but the player is hurt and loses points.
            if _enemy.x == self.player.x and _enemy.y == self.player.y:
                self.enemies.remove(_enemy)
                self.player.hurt_player()
                self.player.receive_points(-100)
        
    def does_player_collect_loot(self):
        """Checks if the player character walks over loot. If so, user receives points, and the loot disappears."""
        
        for _loot in self.loot:
            if _loot.x == self.player.x and _loot.y == self.player.y:
                self.player.receive_points(_loot.points)
                self.loot.remove(_loot)

# ======================================================== #
# ERRORS
# ======================================================== #
                
class StackedObjectError(Exception):
    """ An Exception to detect if an entity has incorrectly moved onto another entity."""
    
    pass
    
# ======================================================== #
   
# Tells the user that they can't use this file and closes the program
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()