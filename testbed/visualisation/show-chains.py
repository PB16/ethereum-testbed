import os
import re
import pexpect
import numpy as np
import pygame
from pygame.locals import *
from time import sleep
from node import Node
from packet import Packet
from block import Block
from chain import Chain
import sys

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1800,1100))

chain = Chain(screen, 200, 200)
chain1 = Chain(screen, 200, 400)

for i in range(0, 40000):
    chain.add_block()

chain.print_chain()

while True:
    screen.fill(BLACK)
    chain.print_chain()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                chain.move_x(-30)
            if event.key == pygame.K_RIGHT:
                chain.move_x(30)
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
