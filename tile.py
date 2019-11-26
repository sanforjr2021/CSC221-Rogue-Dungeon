class TileWall:
    # Creates a wall object that neither the player nor the enemies can pass through
    def __init__(self, x, y):
        self.x = x
        self.y = y


class TileLoot:
    # Creates a loot object at a position
    # and includes the number of points that a player will earn from picking it up
    def __init__(self, x, y, points):
        self.x = x
        self.y = y
        self.points = points
        


# Tells the user that they can't use this method and closes the program
if __name__ == '__main__':
    print("This file can't be run on its own. Please run main.py")
    quit()