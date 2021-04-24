import pygame, os


# Width, height, size of squre etc.
GAP = 50
WIDTH = 600
HEIGHT = 600 + GAP
SQUARE = 25
NUMBER_OF_ROWS_AND_COLUMNS = WIDTH//SQUARE
START_VELOCITY = 10 #    |{0,30}|
START_X, START_Y = NUMBER_OF_ROWS_AND_COLUMNS//2, NUMBER_OF_ROWS_AND_COLUMNS//2

# Set the window
os.environ['SDL_VIDEO_WINDOW_POS'] = f"{600},{200}"
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_icon(pygame.image.load("IMG/snake_pic.png"))
pygame.display.set_caption("Snake - By Tomáš Alexa")


# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_RED = (150, 0, 0)
DARK_BLUE = (0, 0, 150)
LIGHT_WOOD = (180, 120, 70)
DARK_WOOD = (70, 30, 6)
DARKER_WOOD = (40, 20, 6)
YELLOW = (255, 255, 0)
DARK_GRAY = (20, 20, 20)
NICE_YELLOW = (250, 230, 20)
NICE_RED = (250, 60, 0)
LIGHT_BLUE = (0, 100, 200)

DARK_BLUE_ADVANCED = (0, 30, 90)
HUMAN_COLOUR = (242, 188, 148)
YELLOW_ADVANCED = (244, 175, 27)
