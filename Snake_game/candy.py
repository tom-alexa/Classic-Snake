import pygame, random
from .constants import *

def draw_candy(candy_pos):
    pygame.draw.rect(screen, DARK_RED, (candy_pos[0] * SQUARE + 2, candy_pos[1] * SQUARE + 2 + GAP, SQUARE - 4, SQUARE - 4))

def new_candy(possitions):
    while True:
        candy_pos = [random.randrange(0, NUMBER_OF_ROWS_AND_COLUMNS), random.randrange(0, NUMBER_OF_ROWS_AND_COLUMNS)]
        if candy_pos not in possitions:
            break
    return candy_pos

def check_if_is_eaten(possitions, candy_pos):
    if possitions[0] == candy_pos:
        is_eaten = True
    else:
        is_eaten = False
    return is_eaten
