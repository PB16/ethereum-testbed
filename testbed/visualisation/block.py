class Block:
    def __init__(self, x, y, width, height, blocknumber, hashstr, parenthashstr, timestamp):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.blocknumber = blocknumber
        self.hashstr = hashstr
        self.parenthashstr = parenthashstr
        self.timestamp = timestamp

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

    def get_timestamp(self):
        return self.timestamp

    def to_string(self):
    	return str(self.x) + "," + str(self.y) + "," + str(self.width) + "," + str(self.height) + "," + str(self.blocknumber) + "," + str(self.hashstr) + "," + str(self.parenthashstr) + "," + str(self.timestamp)
    	