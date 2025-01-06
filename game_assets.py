import pygame
import os

pygame.font.init()

# Constants
WIN_WIDTH = 500
WIN_HEIGHT = 800

# Assets
BIRD_IMGS = [
    pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird1.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird2.png"))),
    pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bird3.png")))
]
PIPE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "pipe.png")))
BASE_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "base.png")))
BG_IMG = pygame.transform.scale2x(pygame.image.load(os.path.join("assets", "bg.png")))

STAT_FONT = pygame.font.SysFont("comicsans", 50)
