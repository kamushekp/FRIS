class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return hex(id(self)) + " Point ( " + str(self.x) + " : " + str(self.y) + " ) "

    def __str__(self):
        return hex(id(self)) + " Point ( " + str(self.x) + " : " + str(self.y) + " ) "



