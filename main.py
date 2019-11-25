# By Jacob Sanford & Alec Barker
# Date: 10/1/19
# Description: Load the basic Code

import pygame
import graphicswindow

class Main:
    def __init__(self):
        self.menu_map = {
			"play": self.play,
			"instructions": self.instructions,
			"quit": self.quit,
		}
    
        print()
        self.printLogo()
        print()
        
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
    
    def play(self):
        graphicswindow.GraphicsWindow()
        
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
        print("will end. Monster have a chance to dodge or counter attack, so try to avoid")
        print("attacking them in large groups.")
        print()
        print("                         Controls")
        print("    W or ↑  :  Move Up            S or ↓  :  Move Down")
        print("    A or ←  :  Move Left          D or →  :  Move Right")
        print("    E       :  Attack             Esc     :  Exit Game")
        print()
        print("===============================================================================")
        print()
        
    def quit(self):
        raise SystemExit()
        
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
        
    def printOptions(self):
        print("                            Please enter a command:                            ")
        print("                                      Play                                     ")
        print("                                  Instructions                                 ")
        print("                                      Quit                                     ")
        
        

if __name__ == '__main__':
    try:
        import pygame
    except ImportError:
        print("Error: pygame not installed. Please type the following to install pygame on a Windows machine:")
        print("py -m pip install -U pygame --user")
        quit()
    Main()
