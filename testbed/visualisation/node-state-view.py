import re
import pexpect
import numpy as np
import pygame
from pygame.locals import *
from time import sleep
from node import Node

def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)

def print_circle_node(screen, message, font, color, text_center, circ_pos):
    circ = pygame.draw.circle(screen, BLUE, circ_pos, 50)
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    message = "Hej"
    screen.blit(*text_objects(font, message, color, circ_pos))

def print_rectangular_node(screen, message, font, color, rect_area):
    rect = pygame.draw.rect(screen, BLUE, rect_area)
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    screen.blit(*text_objects(font, message, color, (rect_area[0]+50,rect_area[1]+50)))

def connect_nodes(start_node, end_node):
	pygame.draw.lines(screen, pygame.Color("red"), False, [start_node.get_center(), end_node.get_center()], 5)

def connect_to_all_other_nodes(node, nodes_list):
	for nodes in nodes_list:
		if nodes is not node:
			connect_nodes(node, nodes)

def get_blocknumber(node):
    node.send("eth.getBlock(eth.blockNumber)\r")

    node.expect("{(.*)}")

    data = node.after.decode()

    result = re.search('number: (.*),', data)

    number = result.group(1).split("m")[1].split("\x1b")[0]
    return number

def transfer_packet(start, end):
    coefficients = np.polyfit(start.get_center(), end.get_center(), 1)
    x = start.get_center()[0]
    while True:
        y = np.floor(coefficients[0]*x+coefficients[1])
        circ = pygame.draw.circle(screen, BLUE, (int(x), int(y)), 50)
        pygame.display.update()

        if (x, y) is end.get_center():
            break
        else:
            x += 1

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1800,1100))

miner1_node = Node(100, 200, 250, 350)
miner2_node = Node(400, 700, 250, 350)
node1_node = Node(700, 20, 250, 350)
node2_node = Node(1000, 700, 250, 350)
node3_node = Node(1300, 200, 250, 350)

nodes_list = [miner1_node, miner2_node, node1_node, node2_node, node3_node]

miner1 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner1/geth.ipc")
miner2 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/miner2/geth.ipc")
node1 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node1/geth.ipc")
node2 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node2/geth.ipc")
node3 = pexpect.spawn("geth attach ipc:/home/peter/ethereum-testbed/testbed/docker/composer/filecontainer/node3/geth.ipc")

miner1.expect(">")

while True:
    connect_to_all_other_nodes(miner1_node, nodes_list)
    connect_to_all_other_nodes(miner2_node, nodes_list)
    connect_to_all_other_nodes(node1_node, nodes_list)
    connect_to_all_other_nodes(node2_node, nodes_list)
    connect_to_all_other_nodes(node3_node, nodes_list)

    print_rectangular_node(screen, get_blocknumber(miner1), None, None, miner1_node.get_node_area())
    print_rectangular_node(screen, get_blocknumber(miner2), None, None, miner2_node.get_node_area())
    print_rectangular_node(screen, get_blocknumber(node1), None, None, node1_node.get_node_area())
    print_rectangular_node(screen, get_blocknumber(node2), None, None, node2_node.get_node_area())
    print_rectangular_node(screen, get_blocknumber(node3), None, None, node3_node.get_node_area())

    pygame.display.update()

    transfer_packet(miner1_node, miner2_node)
    sleep(0.5)

pygame.quit()