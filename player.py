class Player:
    def __init__(self, x, y, score, health):
        self.x = x
        self.y = y
        self.score = score
        self.health = health
        
        if self.health > 0:
            self.isDead = False
        else:
            self.isDead = True
    
    def moveRight(self):
        self.x = self.x + 1
        
    def moveLeft(self):
        self.x = self.x - 1
        
    def moveUp(self):
        self.y = self.y - 1
        
    def moveDown(self):
        self.y = self.y + 1
        
    def hurtPlayer(self):
        self.health = self.health - 1
        if self.health <= 0:
            self.isDead = True
        
    def receivePoints(self, amount):
        self.score = self.score + amount
        
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()