# Rogue Dungeon
# By Jacob Sanford & Alec Barker

# Description: Acts as the main controller of the program

import graphicswindow

class Main:
    # Creates a menu that the player can select
    def __init__(self):
        self.numHealth = 3
        self.numWall = 8
        self.numLoot = 5
        self.numEnemy = 6
        self.divFactor = 10
        self.menu_map = {
            "play": self.play,
            "instructions": self.instructions,
            "options": self.options,
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
        graphicswindow.GraphicsWindow(self.numWall, self.numHealth, self.numLoot, self.numEnemy, self.divFactor)

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

    # Prints the default values and presents the user with prompts to enter their own values
    def options(self):
        print()
        print("===============================================================================")
        print()
        print("           Default Values")
        print("   Player Health : " + str(self.numHealth))
        print("   Number of Wall Tiles : " + str(self.numWall))
        print("   Number of Enemies : " + str(self.numEnemy))
        print("   Number of Loot Tiles : " + str(self.numLoot))
        print("   Division Factor For Grid : " + str(self.divFactor))
        print()
        
        self.healthDone = False
        while not self.healthDone:
            self.setNumHealth();
        
        print()
        
        self.spawnOptionsDone = False
        while not self.spawnOptionsDone:
            self.setSpawnOptions()
        
        print()
        print("===============================================================================")
        print()

    # Presents all the settings to the user
    def setSpawnOptions(self):
        self.wallsDone = False
        while not self.wallsDone:
            self.setNumWall()
        
        print()
        
        self.enemiesDone = False
        while not self.enemiesDone:
            self.setNumEnemy()
        
        print()
        
        self.lootDone = False
        while not self.lootDone:
            self.setNumLoot()
        
        print()
        
        self.divFactorDone = False
        while not self.divFactorDone:
            self.setDivFactor()
        
        area = self.divFactorTemp * self.divFactorTemp
        
        if self.numEnemiesTemp + self.numWallsTemp + 1 > area:
            print()
            print("There is not enough grid space to spawn everything you requested. Please")
            print("decrease the number of walls and/or enemies, or increase the length/width")
            print("of the grid.")
            print()
        elif self.numLootTemp + self.numWallsTemp + 1 > area:
            print()
            print("There is not enough grid space to spawn everything you requested. Please")
            print("decrease the number of walls and/or loot items, or increase the length/")
            print("width of the grid.")
            print()
        else:
            self.numWall = self.numWallsTemp
            self.numEnemy = self.numEnemiesTemp
            self.numLoot = self.numLootTemp
            self.divFactor = self.divFactorTemp
            self.spawnOptionsDone = True

    # Sets the amount of health the player character will have
    def setNumHealth(self):
        try:
            possibleHealth = int(input("Please type the number of health points the player will have: "))
            if possibleHealth <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable health value.")
            else:
                self.numHealth = possibleHealth
                self.healthDone = True
        except ValueError:
            print("The value entered is not an integer value.")

    # Sets the number of walls that will appear on the grid
    def setNumWall(self):
        try:
            possibleWalls = int(input("Please type the number of tiles that will be walls: "))
            if possibleWalls <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable value.")
            else:
                self.numWallsTemp = possibleWalls
                self.wallsDone = True
        except ValueError:
            print("The value entered is not an integer value.")

    # Sets the number of enemies that will appear on the grid
    def setNumEnemy(self):
        try:
            possibleEnemies = int(input("Please type the number of enemies that will generate on the map: "))
            if possibleEnemies <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable health value.")
            else:
                self.numEnemiesTemp = possibleEnemies
                self.enemiesDone = True
        except ValueError:
            print("The value entered is not an integer value.")

    # Sets the number of loot items that will appear on the grid
    def setNumLoot(self):
        try:
            possibleLoot = int(input("Please type the number of loot items that will generate on the map: "))
            if possibleLoot <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable health value.")
            else:
                self.numLootTemp = possibleLoot
                self.lootDone = True
        except ValueError:
            print("The value entered is not an integer value.")

    # Sets the divFactor of the grid, which determines the length and width of the grid
    def setDivFactor(self):
        try:
            possibleDivFactor = int(input("Please type the number that represents the length and width of the grid: "))
            if possibleDivFactor <= 0:
                print("The entered value is less than or equal to 0. This is not an acceptable health value.")
            else:
                self.divFactorTemp = possibleDivFactor
                self.divFactorDone = True
        except ValueError:
            print("The value entered is not an integer value.")


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
        print("                                     Options                                   ")
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
