import pygame
import random

# Initializing pygame
pygame.init()

#Screen dimensions
WIDTH, HEIGHT = 600, 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Shooter")

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 40)

# colors
WHITE = (255, 255, 255)
RED = (255, 50, 50)
BLUE = (50, 150, 255)
BLACK = (0, 0, 0)

# Player class
class player(pygame.sprite.Sprite):
    def_init_(self):




