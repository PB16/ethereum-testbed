import re
import pexpect
import pygame
from pygame.locals import *
from time import sleep

def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)

def print_circle_node(screen, message, font, color, text_center, circ_pos):
    circ = pygame.draw.circle(screen, BLUE, circ_pos, 50)
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    message = "Hej"
    screen.blit(*text_objects(font, message, color, circ_pos))

def print_rectangular_node(screen, message, font, color, text_center, rect_area):
    rect = pygame.draw.rect(screen, BLUE, rect_area)
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    screen.blit(*text_objects(font, message, color, text_center))

def get_blocknumber(node):
    node.send("eth.getBlock(eth.blockNumber)\r")

    node.expect("{(.*)}")

    data = node.after.decode()

    result = re.search('number: (.*),', data)

    number = result.group(1).split("m")[1].split("\x1b")[0]
    return number


BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1800,1100))

#pos = (200, 200)
#print_circle_node(screen, "", None, None, pos, pos)

#pos = (100, 100)
#print_circle_node(screen, "", None, None, pos, pos)
miner1_area = [100, 100, 150, 150]
miner2_area = [300, 100, 150, 150]

miner1 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner1/geth.ipc")
miner2 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner2/geth.ipc")
node1 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node1/geth.ipc")
node2 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node2/geth.ipc")
node3 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node3/geth.ipc")

miner1.expect(">")

while True:
    print_rectangular_node(screen, get_blocknumber(miner1), None, None, (150, 150), miner1_area)

    print_rectangular_node(screen, get_blocknumber(miner2), None, None, (350, 150), miner2_area)
    #print_rectangular_node(screen, number, None, None, (150, 150), node1_area)
    #print_rectangular_node(screen, number, None, None, (150, 150), node2_area)
    #print_rectangular_node(screen, number, None, None, (150, 150), node3_area)
    pygame.display.update()
    sleep(0.5)

pygame.quit()