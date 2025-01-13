import pygame
from pygame.locals import *
import random
import sys

def nettoyage():
    pygame.sprite.Group.empty(all_sprites)
    pygame.sprite.Group.empty(platforms)
    pygame.sprite.Group.empty(enemies)
    pygame.sprite.Group.empty(invisible_walls)
    pygame.sprite.Group.empty(bullets)
    pygame.sprite.Group.empty(blocks)

pygame.init()

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]

camera = pygame.math.Vector2((0, 0))
vec = pygame.math.Vector2 #2 for two dimensional

WIDTH = 1280
HEIGHT = 720
ACC = 0.5
FRIC = -0.05#-0.12 You can tweak the value of the FRIC variable to adjust the movement. The higher the value, the faster the player will stop moving.
FPS = 60

deadzone = 0.3#for joystick
 
FramePerSec = pygame.time.Clock()
 
flags = pygame.NOFRAME
screen = pygame.display.set_mode((WIDTH, HEIGHT), flags, 32, 0, 1)

pygame.mouse.set_visible(False)

pygame.display.set_caption("Epsilon")

epsilon_img = pygame.image.load("assets/epsilon.png").convert_alpha()
psi_img = pygame.image.load("assets/psi.png").convert_alpha()
phi_img = pygame.image.load("assets/phi.png").convert_alpha()

shot_sound = pygame.mixer.Sound("assets/laser-gun-sound.mp3")

all_sprites = pygame.sprite.Group()
platforms = pygame.sprite.Group()
enemies = pygame.sprite.Group()
invisible_walls = pygame.sprite.Group()
bullets = pygame.sprite.Group()
blocks = pygame.sprite.Group()