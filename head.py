import pygame
from pygame.locals import *
import random
import sys

def nettoyage():
    pygame.sprite.Group.empty(all_sprites)
    pygame.sprite.Group.empty(platforms)
    pygame.sprite.Group.empty(enemies)
    pygame.sprite.Group.empty(InvisibleWalls)

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional

WIDTH = 1280
HEIGHT = 720
ACC = 0.5
FRIC = -0.05#-0.12
FPS = 60

deadzone = 0.3#for joystick
 
FramePerSec = pygame.time.Clock()
 
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Epsilon")

epsilon_img = pygame.image.load("assets/epsilon.png").convert_alpha()
psi_img = pygame.image.load("assets/psi.png").convert_alpha()
phi_img = pygame.image.load("assets/phi.png").convert_alpha()

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
InvisibleWalls = pygame.sprite.Group()