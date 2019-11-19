class Enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.isDead = False

    def moveRight(self):
        self.x = self.x + 1

    def moveLeft(self):
        self.x = self.x - 1

    def moveUp(self):
        self.y = self.y - 1

    def moveDown(self):
        self.y = self.y + 1

    def setDead(self):
        self.isDead = True

if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()