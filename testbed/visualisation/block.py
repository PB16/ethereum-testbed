class Block:
    def __init__(self, x, y, width, height, blocknumber, hashstr, parenthashstr):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blocknumber = blocknumber
        self.hashstr = hashstr
        self.parenthashstr = parenthashstr

    def get_area(self):
        return [self.x, self.y, self.width, self.height]

    def get_center(self):
        return (self.x + (self.width / 2), self.y + (self.height / 2))

    def move_x(self, x):
    	self.x += x

    def get_blocknumber(self):
    	return self.blocknumber

    def set_hash(self, hashstr):
        self.hashstr = hashstr

    def get_hash(self):
        return self.hashstr

    def set_parenthash(self, hashstr):
        self.parenthashstr = hashstr

    def get_parenthash(self):
        return self.parenthashstr
