# Rogue Dungeon
# Created by Alec Barker and Jacob Sanford

from menu_controllers import menu

class Main:
    """Acts as the main controller of the program."""
    
    def __init__(self):
        """Creates a menu in the console that the user can select."""
        
        _main_menu = menu.Menu()

        # Prints the game logo.
        print()
        _main_menu.print_logo()
        print()

        # While the program is running, asks the player which menu option they want.
        while True:
            _main_menu.print_menu_options()
            
            print()
            
            _answer = input("Please enter a command: ").lower()
            try:
                func = _main_menu.menu_map[_answer]
            except KeyError:
                print()
                print("'{}' is not a valid command.".format(_answer))
                print()
            else:
                func()

# ======================================================== #

# Checks if the user has pygame installed.
# If so, it will run the program.
if __name__ == '__main__':
    try:
        import pygame
    except ImportError:
        print("Error: pygame not installed. Please type the following to install pygame on a Windows machine:")
        print("py -m pip install -U pygame --user")
        quit()
    Main()
