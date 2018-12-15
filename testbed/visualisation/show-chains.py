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

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1800,1100))

block = Block(500, 500, 150, 150)

pygame.draw.rect(screen, BLUE, block.get_area())

pygame.display.update()

sleep(2)

pygame.quit()