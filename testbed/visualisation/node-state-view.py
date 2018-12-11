import pygame
from pygame.locals import *
from time import sleep

def text_objects(font, text, color, text_center):
    rendered = font.render(text, True, color)
    return rendered, rendered.get_rect(center=text_center)

def print_node(screen, message, font, color, text_center, circ_pos):
    circ = pygame.draw.circle(screen, BLUE, circ_pos, 50)
    font = pygame.font.Font(None, 50)
    color = pygame.Color("red")
    message = "Hej"
    screen.blit(*text_objects(font, message, color, circ_pos))

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)

pygame.init()
screen = pygame.display.set_mode((500,500))

pos = (200, 200)
print_node(screen, "", None, None, pos, pos)

pos = (100, 100)
print_node(screen, "", None, None, pos, pos) 
pygame.display.update()

while True:
    i=1

pygame.quit()