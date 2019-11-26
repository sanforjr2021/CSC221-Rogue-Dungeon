import random

class Enemy:
    # Creates an enemy in a desired position and takes in the width/height of the grid
    def __init__(self, x, y, limit):
        self.x = x
        self.y = y
        self.limit = limit
        self.movement = {0: self.moveRight, 1: self.moveLeft, 2: self.moveUp, 3: self.moveDown, 4: self.idle}

    # Moves the enemy over one tile to the right
    def moveRight(self):
        if self.x < self.limit - 1:
            self.x = self.x + 1

    # Moves the enemy over one tile to the left
    def moveLeft(self):
        if self.x > 0:
            self.x = self.x - 1

    # Moves the enemy over one tile up
    def moveUp(self):
        if self.y > 0:
            self.y = self.y - 1
    
    # Moves the enemy over one tile down
    def moveDown(self):
        if self.y < self.limit - 1:
            self.y = self.y + 1

    # The enemy stays in the same position
    def idle(self):
        pass

    # Creates a random number
    # Based on that number, the enemy will move in a direction
    def randomMovement(self):
        direction = self.movement.get(random.randint(0, 4))
        direction()


# Tells the user that they can't use this method and closes the program
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()
