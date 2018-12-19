import pygame
from block import Block

BLUE = (0, 0, 255)

class Chain:
    def __init__(self, screen, x, y):
        self.x = x
        self.y = y
        self.blocks = []
        self.screen = screen

    def add_block(self):
        block = Block(self.x, self.y, 150, 150)
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

        pygame.display.update()

    def connect_blocks(self, start, end):
        pygame.draw.lines(self.screen, pygame.Color("red"), False, [start.get_center(), end.get_center()], 15)

    def print_block(self, block):
        pygame.draw.rect(self.screen, BLUE, block.get_area())

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