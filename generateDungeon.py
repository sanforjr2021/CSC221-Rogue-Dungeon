from random import random
from enemy import Enemy
from player import Player

class Dungeon:
    def __init__(self, div=10, numEnemies=3):
        self.player = Player(0, 0, 0, 3)
        self.div = div
        self.numEnemies = numEnemies
        self.enemies = []
        self.Floor = []
        self.genEnemies()

    def genEnemies(self):
        for x in range(self.numEnemies):
            self.enemies.append(Enemy(random.randInt(0, self.div)), random.randInt(0, self.div))

    def genMap(self):
        # todo: generate room
        pass

    def genHero(self):
        # todo: to develop random posistion later on.
        pass


class TileFloor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
