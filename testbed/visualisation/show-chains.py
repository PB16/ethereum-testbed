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

chain = Chain(screen, 200, 200, "../docker/composer/filecontainer/miner1/geth.ipc")
chain1 = Chain(screen, 200, 400, "../docker/composer/filecontainer/miner2/geth.ipc")

for i in range(0, 20):
    chain.add_block(i+10)
    chain1.add_block(i+10)

chain.print_chain()
chain1.print_chain()

while True:
    screen.fill(BLACK)
    chain.print_chain()
    chain1.print_chain()
    pygame.display.update()

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                chain.move_x(-30)
            if event.key == pygame.K_RIGHT:
                chain.move_x(30)
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();
