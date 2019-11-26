class Player:
    # Creates a player object with a certain position in the grid with a score and health
    def __init__(self, x, y, score, health):
        self.x = x
        self.y = y
        self.score = score
        self.health = health

        if self.health > 0:
            self.isDead = False
        else:
            self.isDead = True

    # Moves the player over one tile to the right
    def moveRight(self):
        self.x = self.x + 1

    # Moves the player over one tile to the left
    def moveLeft(self):
        self.x = self.x - 1

    # Moves the player over one tile up
    def moveUp(self):
        self.y = self.y - 1

    # Moves the player over one tile down 
    def moveDown(self):
        self.y = self.y + 1

    # Makes the player lose health
    def hurtPlayer(self):
        self.health = self.health - 1
        if self.health <= 0:
            self.isDead = True

    # Gives the player points
    def receivePoints(self, amount):
        self.score = self.score + amount


# Tells the user that they can't use this method and closes the program
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()
