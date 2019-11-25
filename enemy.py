import random


class Enemy:
    def __init__(self, x, y, limit):
        self.x = x
        self.y = y
        self.limit = limit
        self.movement = {0: self.moveRight, 1: self.moveLeft, 2: self.moveUp, 3: self.moveDown, 4: self.idle}

    def moveRight(self):
        if self.x < self.limit - 1:
            self.x = self.x + 1

    def moveLeft(self):
        if self.x > 0:
            self.x = self.x - 1

    def moveUp(self):
        if self.y > 0:
            self.y = self.y - 1

    def moveDown(self):
        if self.y < self.limit - 1:
            self.y = self.y + 1

    def idle(self):
        pass

    def randomMovement(self):
        direction = self.movement.get(random.randint(0, 4))
        direction()


if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()
