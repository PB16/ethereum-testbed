class Block:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def get_area(self):
        return [self.x, self.y, self.width, self.height]

    def get_center(self):
        return (self.x + (self.width / 2), self.y + (self.height / 2))