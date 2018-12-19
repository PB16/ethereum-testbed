import pygame
import pexpect
import re
from block import Block

BLUE = (0, 0, 255)

class Chain:
    def __init__(self, screen, x, y, geth):
        self.x = x
        self.y = y
        self.blocks = []
        self.screen = screen
        self.geth = pexpect.spawn("geth attach ipc:" + geth)

    def text_objects(self, font, text, color, text_center):
        rendered = font.render(text, True, color)
        return rendered, rendered.get_rect(center=text_center)

    def add_block(self, x=0):
        block = Block(self.x, self.y, 150, 150, x)
        self.blocks.append(block)
        self.x += 300

    def print_chain(self):
        oldblock = None
        newblock = None

        startblock = self.blocks[0]
        prevblock = self.blocks[1]

        self.connect_blocks(startblock, prevblock)

        for nextblock in self.blocks[2:]:
            self.connect_blocks(prevblock, nextblock)
            prevblock = nextblock

        for block in self.blocks:
            if (block.get_center()[0] >= 0 and block.get_center()[0] <= 1800) and (block.get_center()[1] >= 0 and block.get_center()[1] <= 1100):
                self.print_block(block)

    def connect_blocks(self, start, end):
        pygame.draw.lines(self.screen, pygame.Color("red"), False, [start.get_center(), end.get_center()], 15)

    def print_block(self, block):
        pygame.draw.rect(self.screen, BLUE, block.get_area())
        font = pygame.font.Font(None, 30)
        color = pygame.Color("red")
        self.screen.blit(*self.text_objects(font, self.get_block(block.get_blocknumber())[0], color, (block.get_area()[0]+65,block.get_area()[1]+20)))
        self.screen.blit(*self.text_objects(font, self.get_block(block.get_blocknumber())[1], color, (block.get_area()[0]+65,block.get_area()[1]+50)))

    def move_x(self, x):
        for block in self.blocks:
            block.move_x(x)

    def is_block_within_screen(self, block):
        result = False

        width, height = pygame.display.get_surface().get_size()
        if (block.get_center()[0] >= 0 and block.get_center()[0] <= 1800) and (block.get_center()[1] >= 0 and block.get_center()[1] <= 1100):
            result = True

        if (block.get_area()[2] >= 0 and block.get_area()[2] <= 1800) and (block.get_area()[3] >= 0 and block.get_area()[3] <= 1100):
            result = True

        return result

    def get_block(self, blocknumber):
        self.geth.send("eth.getBlock(" + str(blocknumber) + ")\r")

        self.geth.expect("{(.*)}")

        data = self.geth.after.decode()

        result = re.search('hash: (.*),', data)

        hashstr = result.group(1)

        result = re.search('parentHash: (.*),', data)

        parentHashstr = result.group(1)

        #print(hashstr.split('0x')[1].split('"')[0])
        hashstr = hashstr.split('0x')[1].split('"')[0]
        hashstr = hashstr[:4] + "...." + hashstr[-4:]

        parentHashstr = parentHashstr.split('0x')[1].split('"')[0]
        parentHashstr = parentHashstr[:4] + "...." + parentHashstr[-4:]

        return (hashstr, parentHashstr)
