import pexpect
import re

class Node:
    def __init__(self, x, y, width, height, name, geth_instance):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.name = name
        self.geth = pexpect.spawn("geth attach ipc:" + geth_instance)

    def get_center(self):
        return (self.x + (self.width / 2), self.y + (self.height / 2))

    def get_node_area(self):
        return [self.x, self.y, self.width, self.height]

    def move(self, x):
        self.x += x

    def get_name(self):
        return self.name

    def get_blocknumber(self):
        self.geth.send("eth.getBlock(eth.blockNumber)\r")

        self.geth.expect("{(.*)}")

        data = self.geth.after.decode()

        result = re.search('number: (.*),', data)

        number = result.group(1).split("m")[1].split("\x1b")[0]
        return number
        