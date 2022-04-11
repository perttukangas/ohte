import pygame
from enum import Enum


class Difficulty(Enum):
    EASY = 10
    MEDIUM = 20
    HARD = 30


class Color(Enum):
    BLACK = pygame.Color(0, 0, 0)
    DARK_BLUE = pygame.Color(0, 0, 170)
    DARK_GREEN = pygame.Color(0, 170, 0)
    DARK_AQUA = pygame.Color(0, 170, 170)
    DARK_RED = pygame.Color(170, 0, 0)
    DARK_PURPLE = pygame.Color(170, 0, 170)
    GOLD = pygame.Color(255, 170, 0)
    GRAY = pygame.Color(170, 170, 170)
    DARK_GRAY = pygame.Color(85, 85, 85)
    BLUE = pygame.Color(85, 85, 255)
    GREEN = pygame.Color(85, 255, 85)
    AQUA = pygame.Color(85, 255, 255)
    RED = pygame.Color(255, 85, 85)
    LIGHT_PURPLE = pygame.Color(255, 85, 255)
    YELLOW = pygame.Color(255, 255, 85)
    WHITE = pygame.Color(255, 255, 255)


class Direction(Enum):
    LEFT = [-10, 0]
    RIGHT = [10, 0]
    UP = [0, -10]
    DOWN = [0, 10]