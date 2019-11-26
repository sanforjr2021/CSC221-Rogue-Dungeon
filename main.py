# By Jacob Sanford & Alec Barker
# Date: 10/1/19
# Description: Load the basic Code

import pygame
import graphicswindow

class Main:
    # Creates a menu that the player can select
    def __init__(self):
        self.menu_map = {
			"play": self.play,
			"instructions": self.instructions,
			"quit": self.quit,
		}
    
        # Prints the logo for the game
        print()
        self.printLogo()
        print()
        
        # While the game is running, asks the player which menu option they want
        while True:
            self.printOptions()
            print()
            answer = input("Please enter a command: ").lower()
            try:
                func = self.menu_map[answer]
            except KeyError:
                print()
                print("{} is not a valid option".format(answer))
                print()
            else:
                func()
    
    # Opens the graphics window for the game
    def play(self):
        graphicswindow.GraphicsWindow()
     
    # Displays the instructions for playing the game
    def instructions(self):
        print()
        print("===============================================================================")
        print()
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
        print("                         Objects")
        print("    Green Box    : Player       Red Boxes  : Monsters")
        print("    Yellow Boxes : Loot         Blue Boxes : Walls")
        print("                Black Boxes : Empty Tiles")
        print()
        print("                         Controls")
        print("    W or ↑  :  Move Up            S or ↓  :  Move Down")
        print("    A or ←  :  Move Left          D or →  :  Move Right")
        print("    E       :  Attack             Esc     :  Exit Game")
        print()
        print("===============================================================================")
        print()
        
    # Exits the game
    def quit(self):
        raise SystemExit()
    
    # Prints the game logo
    def printLogo(self):
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
    
    # Prints the menu options for the user to select
    def printOptions(self):
        print("                            Please enter a command:                            ")
        print("                                      Play                                     ")
        print("                                  Instructions                                 ")
        print("                                      Quit                                     ")
        
        
# Checks if the user has pygame installed
# If so, it will run the program
if __name__ == '__main__':
    try:
        import pygame
    except ImportError:
        print("Error: pygame not installed. Please type the following to install pygame on a Windows machine:")
        print("py -m pip install -U pygame --user")
        quit()
    Main()
