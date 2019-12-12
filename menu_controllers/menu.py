from game_controllers import graphics_window
from menu_controllers import settings

class Menu:
    """Displays menu items in the console for the player to select."""

    def __init__(self):
        """Create a dictionary of menu options and an instance of game settings."""
        
        self.menu_map = {
            "play": self._play,
            "instructions": self._instructions,
            "settings": self._settings,
            "quit": self._quit
        }
        
        self._settings = settings.Settings()

    # ======================================================== #
    # PRINT FUNCTIONS
    # ======================================================== #

    def print_logo(self):
        """Prints the game logo."""
        
        print("            ▄████████  ▄██████▄     ▄██████▄  ███    █▄     ▄████████ ")
        print("           ███    ███ ███    ███   ███    ███ ███    ███   ███    ███ ")
        print("           ███    ███ ███    ███   ███    █▀  ███    ███   ███    █▀  ")
        print("          ▄███▄▄▄▄██▀ ███    ███  ▄███        ███    ███  ▄███▄▄▄     ")
        print("         ▀▀███▀▀▀▀▀   ███    ███ ▀▀███ ████▄  ███    ███ ▀▀███▀▀▀     ")
        print("         ▀███████████ ███    ███   ███    ███ ███    ███   ███    █▄  ")
        print("           ███    ███ ███    ███   ███    ███ ███    ███   ███    ███ ")
        print("           ███    ███  ▀██████▀    ████████▀  ████████▀    ██████████ ")
        print("           ███    ███                                                 ")
        print()
        print("████████▄  ███    █▄  ███▄▄▄▄      ▄██████▄     ▄████████  ▄██████▄  ███▄▄▄▄   ")
        print("███   ▀███ ███    ███ ███▀▀▀██▄   ███    ███   ███    ███ ███    ███ ███▀▀▀██▄ ")
        print("███    ███ ███    ███ ███   ███   ███    █▀    ███    █▀  ███    ███ ███   ███ ")
        print("███    ███ ███    ███ ███   ███  ▄███         ▄███▄▄▄     ███    ███ ███   ███ ")
        print("███    ███ ███    ███ ███   ███ ▀▀███ ████▄  ▀▀███▀▀▀     ███    ███ ███   ███ ")
        print("███    ███ ███    ███ ███   ███   ███    ███   ███    █▄  ███    ███ ███   ███ ")
        print("███   ▄███ ███    ███ ███   ███   ███    ███   ███    ███ ███    ███ ███   ███ ")
        print("████████▀  ████████▀   ▀█   █▀    ████████▀    ██████████  ▀██████▀   ▀█   █▀  ")
        print()
        print("                   Created by Alec Barker and Jacob Sanford                    ")
        
    def print_menu_options(self):
        """Prints the menu options that the user can select."""
        
        print("                            Please enter a command:                            ")
        print("                                      Play                                     ")
        print("                                  Instructions                                 ")
        print("                                    Settings                                   ")
        print("                                      Quit                                     ")
    
    def _print_settings_values(self):
        """Prints the current values for each setting."""
        
        print("              Current Values")
        print("   Player Health : " + str(self._settings.num_health))
        print("   Number of Walls : " + str(self._settings.num_walls))
        print("   Number of Enemies : " + str(self._settings.num_enemies))
        print("   Number of Loot Items: " + str(self._settings.num_loot))
        print("   Length and Width of Grid : " + str(self._settings.grid_size) + " x " + str(self._settings.grid_size))
        
    def _print_line(self):
        """Prints a line across the console to separate sections."""
        
        print()
        print("===============================================================================")
        print()

    # ======================================================== #
    # FUNCTIONS FOR MENU OPTIONS
    # ======================================================== #
        
    def _play(self):
        """Opens the graphics window that contains the actual game."""
        
        graphics_window.GraphicsWindow(self._settings)

    def _instructions(self):
        """Displays the instructions for playing the game."""
        
        self._print_line()
        print("The objective of the game is to obtain points while avoiding death. You can get")
        print("points by killing monsters or collecting loot in a level.")
        print()
        print("The game remains static until you move the player character. This means that")
        print("monsters can't move until you choose to move. Therefore, you should be strategic")
        print("about every move you make.")
        print()
        print("You will take damage by moving onto the same tile or staying within one tile of")
        print("a monster. If you receive too much damage, your character will die and the game")
        print("will end. Monsters have a chance to dodge or counter attack, so try to avoid")
        print("attacking them in large groups.")
        print()
        print("To collect loot, simply move the player character move over top of the loot.")
        print()
        print("To win, kill all monsters in the level.")
        print()
        print("                         Objects")
        print("    Green Box    : Player       Red Boxes  : Monsters")
        print("    Yellow Boxes : Loot         Blue Boxes : Walls")
        print("                Black Boxes : Empty Tiles")
        print()
        print("                         Controls")
        print("    W or ↑  :  Move Up            S or ↓  :  Move Down")
        print("    A or ←  :  Move Left          D or →  :  Move Right")
        print("    E       :  Attack             Esc     :  Exit Game")
        self._print_line()

    def _settings(self):
        """Prints the default values for each setting and presents the user with prompts to enter their own values."""
        
        self._print_line()
    
        # Prints the current values for each setting.
        self._print_settings_values()
        
        print()
        
        # Runs a loop until the user has entered an acceptable value for the player character health.
        self._health_done = False
        while not self._health_done:
            try:
                self._settings.set_num_health(self)
                self._health_done = True
            except settings.InvalidInputError:
                pass
        
        print()
        
        # Runs a loop until the user has entered acceptable values for each of the spawn settings.
        self._spawn_settings_done = False
        while not self._spawn_settings_done:
            try:
                self._settings.set_spawn_settings(self)
                self._spawn_settings_done = True
            except settings.InvalidInputError:
                pass
        
        self._print_line()

    def _quit(self):
        """Exits the program."""
        
        raise SystemExit()

# ======================================================== #

# Tells the user that they can't use this file and closes the program.
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()