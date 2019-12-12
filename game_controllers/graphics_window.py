import sys
import pygame
from entities import player
from entities import enemy
from game_controllers import gameplay

class GraphicsWindow:
    """A graphics window that displays the game and allows the user to interact with it."""

    def __init__(self, _settings):
        """Creates the graphics window, sets up a dictionary of colors to use, sets the size of the grid, instantiates entities, and runs the gameplay loop."""
        
        pygame.init()
        self._create_window()
        self._gameplay = gameplay.Gameplay(_settings)
        
        # A dictionary of colors that can be used for a standard look.
        self._colors = {
            "black" : (0, 0, 0),
            "gray" : (128, 128, 128),
            "white" : (255, 255, 255),
            "red" : (255, 0, 0),
            "green" : (0, 255, 0),
            "blue" : (0, 0, 255),
            "purple" : (255, 0, 255),
            "yellow" : (255, 255, 0),
            "aqua" : (0, 255, 255),
            "orange" : (255, 128, 0),
            "pink" : (255, 0, 128)
        }
        
        # The length and width of the grid.
        self._grid_size = _settings.grid_size
        
        # The player character.
        self._player = self._gameplay.player

        # Continually runs the following as long as the game is running
        while True:
            # Calculates how large GUI elements need to be based on the window size.
            self._calculate_tile_size()
            self._calculate_font_size()

            # Draws all objects.
            self._draw()

            # Updates the window.
            pygame.display.update()

            # Listens for various user-created events.
            self._run_listeners()
            
            # Checks if the user has killed all the enemies and won the game.
            if not self._gameplay.enemies:
                self._gameplay.has_won = True
    
    # ======================================================== #
    # CONTROL PYGAME COMPONENTS
    # ======================================================== #
    
    def _create_window(self):
        """Creates the window and changes its settings."""
    
        # Creates the window and makes it resizable.
        self._surface = pygame.display.set_mode((350, 420), pygame.RESIZABLE)
        
        # Sets the name of the window.
        pygame.display.set_caption("Rogue Dungeon")
        
        # Attempts to load the logo and set it as the window icon.
        try:
            _icon = pygame.image.load('rd-logo.png')
            pygame.display.set_icon(_icon)
        except pygame.error:
            pass
            
    def _quit_game(self):
        """Makes sure pygame closes before exiting the program."""
        
        pygame.quit()
        sys.exit()

    # ======================================================== #
    # RUN CALCULATIONS
    # ======================================================== #

    def _calculate_tile_size(self):
        """Calculates the size of each tile by determining if the width or height of the window is smallest."""
        
        # Makes the tile size fit correctly against a window that is wider than it is tall.
        if self._surface.get_height() < self._surface.get_width():
            self._tile_size = self._surface.get_height() / (self._grid_size + 2)
        
        # Makes the tile size fit correctly against a window that is taller than it is wide.
        else:
            self._tile_size = self._surface.get_width() / self._grid_size

    def _calculate_font_size(self):
        """Calculates the size of the font by determining if the width or height of the window is smallest."""
        
        # Makes the font size fit correctly against a window that is wider than it is tall.
        if self._surface.get_height() < self._surface.get_width():
            self._font_size = int(self._surface.get_height() / self._grid_size / 1.5)
            
        # Makes the font size fit correctly against a window that is taller than it is wide.
        else:
            self._font_size = int(self._surface.get_width() / self._grid_size / 1.5)
            
    def _can_player_move(self, _x, _y):
        """Checks if the user is trying to move the player character over top of a wall.
        _x and _y represent the direction values that the player character is going to move in."""
        
        _can_move = True
               
        for _wall in self._gameplay.walls:
            if _wall.x == self._player.x + _x and _wall.y == self._player.y + _y:
                _can_move = False
                break
                
        return _can_move

    # ======================================================== #
    # USER-CONTROLLED ACTIONS
    # ======================================================== #

    def _run_listeners(self):
        """Listens for various types of user input and reacts accordingly."""
        
        # Loops through all pygame events.
        for _event in pygame.event.get():
        
            # Closes all applicable modules if the program closes.
            if _event.type == pygame.QUIT:
                self._quit_game()
                
            # Refreshes the window if the user changes the window size.
            if _event.type == pygame.VIDEORESIZE:
                self._surface = pygame.display.set_mode((_event.w, _event.h), pygame.RESIZABLE)

            # Listens for specific key presses.
            if _event.type == pygame.KEYDOWN:
            
                # Closes the program if the escape key is pressed.
                if _event.key == pygame.K_ESCAPE:
                    self._quit_game()
                
                # Checks that player is not dead and has not won yet.
                # If they are not dead and have not already won, they can move, which moves enemies as well.
                if not (self._player.is_dead or self._gameplay.has_won):
                
                    # Moves the player character to the right when the D or → keys are pressed and causes the enemies to move.
                    if _event.key == pygame.K_RIGHT or _event.key == pygame.K_d:
                        _can_move = self._can_player_move(1, 0)
                        
                        if _can_move:
                            self._player.move_right()
                            self._gameplay.does_player_collect_loot()
                        
                        self._gameplay.move_enemies()
                    
                    # Moves the player character to the left when the A or ← keys are pressed and causes the enemies to move.
                    if _event.key == pygame.K_LEFT or _event.key == pygame.K_a:
                        _can_move = self._can_player_move(-1, 0)
                        
                        if _can_move:
                            self._player.move_left()
                            self._gameplay.does_player_collect_loot()
                        
                        self._gameplay.move_enemies()
                    
                    # Moves the player character up when the W or ↑ keys are pressed and causes the enemies to move.
                    if _event.key == pygame.K_UP or _event.key == pygame.K_w:
                        _can_move = self._can_player_move(0, -1)
                        
                        if _can_move:
                            self._player.move_up()
                            self._gameplay.does_player_collect_loot()
                        
                        self._gameplay.move_enemies()
                    
                    # Moves the player character down when the S or ↓ keys are pressed and causes the enemies to move.
                    if _event.key == pygame.K_DOWN or _event.key == pygame.K_s:
                        _can_move = self._can_player_move(0, 1)
                        
                        if _can_move:
                            self._player.move_down()
                            self._gameplay.does_player_collect_loot()
                        
                        self._gameplay.move_enemies()
                    
                    # The player character attacks all enemies within 1 tile of their position when the E key is pressed.
                    if _event.key == pygame.K_e:
                        self._gameplay.move_enemies()
                        for _the_enemy in self._gameplay.enemies:
                            if (_the_enemy.x == self._player.x + 1 or _the_enemy.x == self._player.x - 1 or _the_enemy.x == self._player.x) \
                                    and (_the_enemy.y == self._player.y + 1 or _the_enemy.y == self._player.y - 1 or _the_enemy.y == self._player.y):
                                self._gameplay.enemies.remove(_the_enemy)
                                self._player.receive_points(50)

    # ======================================================= #
    # DRAWING FUNCTIONS
    # ======================================================= #

    def _draw(self):
        """Draws all objects."""
        
        # Background fill color.
        self._surface.fill(self._colors.get("black"))
        
        self._draw_grid()
        self._draw_text()
        
        self._draw_walls()
        self._draw_loot()
        self._draw_enemies()
        self._draw_player()

    def _draw_text(self):
        """Draws the text that displays if the player is dead, their points, and their health."""
        
        _font = pygame.font.SysFont('Tahoma', self._font_size)
        
        # Displays text showing the player character's health, if they won, or if they died.
        if self._player.is_dead:
            _health = _font.render('You Died', True, self._colors.get("red"))
            _health = _font.render('You Died', True, self._colors.get("red"))
        elif self._gameplay.has_won:
            _health = _font.render('You Won', True, self._colors.get("green"))
        else:
            _health = _font.render('Health: ' + str(self._player.health), True, self._colors.get("yellow"))
        self._surface.blit(_health, (0 + self._tile_size / 4, self._tile_size * self._grid_size))

        # Displays text showing the user's score.
        _score = _font.render('Score: ' + str(self._player.score), True, self._colors.get("yellow"))
        self._surface.blit(_score, (0 + self._tile_size / 4, self._tile_size * self._grid_size + self._tile_size))
    
    def _draw_grid(self):
        """Draws a square grid with width and length of grid_size."""
        
        # Draws the grid squares.
        for _y in range(self._grid_size):
            for _x in range(self._grid_size):
                _rect = pygame.Rect(_x * self._tile_size, _y * self._tile_size, self._tile_size, self._tile_size)
                pygame.draw.rect(self._surface, self._colors.get("blue"), _rect, 1)

        # Draws a box at the bottom of the window that is used to display text.
        _rect = pygame.Rect(0, self._tile_size * self._grid_size, self._tile_size * self._grid_size, self._tile_size * 2)
        pygame.draw.rect(self._surface, self._colors.get("blue"), _rect, 1)

    def _draw_player(self):
        """Draws the player character."""
        
        _rect = pygame.Rect(self._player.x * self._tile_size, self._player.y * self._tile_size, self._tile_size, self._tile_size)
        
        if not self._player.is_dead:
            pygame.draw.rect(self._surface, self._colors.get("green"), _rect)
        else:
            pygame.draw.rect(self._surface, self._colors.get("purple"), _rect)

    def _draw_enemies(self):
        """Draws all living enemies."""
        
        for _enemy in self._gameplay.enemies:
            _rect = pygame.Rect(_enemy.x * self._tile_size, _enemy.y * self._tile_size, self._tile_size, self._tile_size)
            pygame.draw.rect(self._surface, self._colors.get("red"), _rect)

    def _draw_loot(self):
        """Draws all loot items."""
        
        for _loot in self._gameplay.loot:
            _rect = pygame.Rect(_loot.x * self._tile_size, _loot.y * self._tile_size, self._tile_size, self._tile_size)
            pygame.draw.rect(self._surface, self._colors.get("yellow"), _rect)

    def _draw_walls(self):
        """Draws all walls."""
        
        for _wall in self._gameplay.walls:
            _rect = pygame.Rect(_wall.x * self._tile_size, _wall.y * self._tile_size, self._tile_size, self._tile_size)
            pygame.draw.rect(self._surface, self._colors.get("blue"), _rect)
   
# ======================================================== #
   
# Tells the user that they can't use this file and closes the program
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()
