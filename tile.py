class TileFloor:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canMoveTo = True  # this is to allow it to check if it can move to


class TileWall:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.canMoveTo = False  # this is to allow it to check if it can move to
