import numpy as np

class Packet:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.x = start.get_center()[0]
        self.slope = (end.get_center()[1]-start.get_center()[1])/(end.get_center()[0]-start.get_center()[0])
        self.orientation = (end.get_center()[0] - start.get_center()[0])
    
    def get_orientation(self):
        return self.orientation

    def get_slope(self):
        return self.slope

    def get_x(self):
        if self.has_packet_arrived() is True:
            return int(self.x)
        else:
            if self.orientation < 0:
                self.x -= 20
            elif self.orientation >= 0:
                self.x += 20
            return int(self.x)

    def get_y(self):
        if self.has_packet_arrived() is True:
            return int(self.y)
        else:
            self.y = np.ceil(self.slope*(self.x-self.end.get_center()[0])+self.end.get_center()[1])
            return int(self.y)

    def has_packet_arrived(self):
        if self.x > self.end.get_center()[0] - 5 and self.x < self.end.get_center()[0] + 5 and self.y > self.end.get_center()[1] - 5 and self.y < self.end.get_center()[1] + 5:
            return True
