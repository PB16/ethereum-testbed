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

chain = Chain(screen, 1100, 200, "../docker/composer/filecontainer/miner1/geth.ipc")
chain1 = Chain(screen, 200, 400, "../docker/composer/filecontainer/miner2/geth.ipc")

for i in range(0, 2):
    chain.add_block(i)
#    chain1.add_block(i)

#chain.print_chain()
#chain1.print_chain()


running = True

while running:
    screen.fill(BLACK)
    chain.move_x(-300)
    print("end x: " + str(chain.get_x_y()[0]+75))
    chain.print_chain()
    chain.add_block(i)
    pygame.display.update()

    sleep(1)
    i += 1
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                chain.move_x(-30)
            if event.key == pygame.K_RIGHT:
                chain.move_x(30)
            if event.key == pygame.K_q:
               running = False
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit();

print("exiting")

sleep(1)
