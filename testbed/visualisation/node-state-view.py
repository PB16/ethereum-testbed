import os
import re
import pexpect
import numpy as np
import pygame
from pygame.locals import *
from time import sleep
from node import Node
from packet import Packet

def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)

def print_packet(screen, packet):
    circ = pygame.draw.circle(screen, BLUE, (packet.get_x(), packet.get_y()), 50)

def print_node(screen, message, node):
    rect = pygame.draw.rect(screen, BLUE, node.get_node_area())
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    screen.blit(*text_objects(font, message, color, (node.get_node_area()[0]+50,node.get_node_area()[1]+50)))
    screen.blit(*text_objects(font, node.get_name(), color, (node.get_node_area()[0]+100,node.get_node_area()[1]+150)))

def connect_nodes(start_node, end_node):
    pygame.draw.lines(screen, pygame.Color("red"), False, [start_node.get_center(), end_node.get_center()], 5)

def connect_to_all_other_nodes(node, nodes_list):
    for nodes in nodes_list:
        if nodes is not node:
            connect_nodes(node, nodes)

def transfer_packet(packet):
	print_packet(screen, packet)
	return packet.has_packet_arrived()

def print_nodes():
    connect_to_all_other_nodes(miner1_node, nodes_list)
    connect_to_all_other_nodes(miner2_node, nodes_list)
    connect_to_all_other_nodes(node1_node, nodes_list)
    connect_to_all_other_nodes(node2_node, nodes_list)
    connect_to_all_other_nodes(node3_node, nodes_list)

    print_node(screen, miner1_node.get_blocknumber(), miner1_node)
    print_node(screen, miner2_node.get_blocknumber(), miner2_node)
    print_node(screen, node1_node.get_blocknumber(), node1_node)
    print_node(screen, node2_node.get_blocknumber(), node2_node)
    print_node(screen, node3_node.get_blocknumber(), node3_node)

def move_map(x):
    for node in nodes_list:
        node.move(x)

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((1800,1100))

miner1_node = Node(100, 100, 250, 350, "miner1", "../docker/composer/filecontainer/miner1/geth.ipc")
miner2_node = Node(400, 700, 250, 350, "miner2", "../docker/composer/filecontainer/miner2/geth.ipc")
node1_node = Node(700, 20, 250, 350, "node1", "../docker/composer/filecontainer/node1/geth.ipc")
node2_node = Node(1000, 700, 250, 350, "node2", "../docker/composer/filecontainer/node2/geth.ipc")
node3_node = Node(1300, 200, 250, 350, "node3", "../docker/composer/filecontainer/node3/geth.ipc")

nodes_list = [miner1_node, miner2_node, node1_node, node2_node, node3_node]

#miner1 = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/miner1/geth.ipc")
#miner2 = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/miner2/geth.ipc")
#node1 = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/node1/geth.ipc")
#node2 = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/node2/geth.ipc")
#node3 = pexpect.spawn("geth attach ipc:../docker/composer/filecontainer/node3/geth.ipc")

x = node2_node.get_center()[0]
x1 = miner1_node.get_center()[0]

packet = Packet(miner1_node, miner2_node)
packet1 = Packet(miner1_node, node1_node)
packet2 = Packet(miner1_node, node2_node)
packet3 = Packet(miner1_node, node3_node)

while True:
    screen.fill(BLACK)
    print_nodes()
    transfer_packet(packet)
    transfer_packet(packet1)
    transfer_packet(packet2)
    transfer_packet(packet3)
    pygame.display.update()
    if packet.has_packet_arrived() is True and packet1.has_packet_arrived() is True and packet2.has_packet_arrived() is True and packet3.has_packet_arrived() is True:
    	break

    #print_nodes()
    #pygame.display.update()
    #events = pygame.event.get()
    #for event in events:
    #    if event.type == pygame.KEYDOWN:
    #        if event.key == pygame.K_LEFT:
    #            move_map(-30)
    #        if event.key == pygame.K_RIGHT:
    #            move_map(30)

pygame.quit()