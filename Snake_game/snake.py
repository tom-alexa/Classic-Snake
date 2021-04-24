import pygame
from .constants import *
from .candy import new_candy

# Initialize pygame
pygame.init()

# Snake
def moving(count, possitions, previous_pos, velocity, can_change_direction, direction, AI):
    count += 1
    if count >= (30 - velocity):
        count = 0
        for i in range(1, len(possitions)):
            possitions[i] = previous_pos[i-1]

        if AI:
            if possitions[0][0] == 0 and possitions[0][1] == NUMBER_OF_ROWS_AND_COLUMNS - 1:
                direction = "up"
            elif possitions[0][0] == 0 and possitions[0][1] == 0:
                direction = "right"
            elif ((possitions[0][0] == 1 and possitions[0][1] != 0) or possitions[0][0] == NUMBER_OF_ROWS_AND_COLUMNS - 1)  and possitions[0][1] != NUMBER_OF_ROWS_AND_COLUMNS - 1 and direction != "down":
                direction = "down"
            elif possitions[0][0] == 1 and possitions[0][1] != NUMBER_OF_ROWS_AND_COLUMNS - 1:
                direction = "right"
            elif possitions[0][0] == NUMBER_OF_ROWS_AND_COLUMNS - 1 and possitions[0][1] != 0:
                direction = "left"

        if direction == "down":
            possitions[0] = [possitions[0][0], possitions[0][1] + 1]
        elif direction == "up":
            possitions[0] = [possitions[0][0], possitions[0][1] - 1]
        elif direction == "right":
            possitions[0] = [possitions[0][0] + 1, possitions[0][1]]
        elif direction == "left":
            possitions[0] = [possitions[0][0] - 1, possitions[0][1]]


        can_change_direction = True
        previous_pos = possitions[:]


    return count, possitions, previous_pos, can_change_direction, direction

def check_if_out_of_map(possitions, previous_pos):
    if possitions[0][0] < 0:
        possitions[0] = [NUMBER_OF_ROWS_AND_COLUMNS - 1, possitions[0][1]]
    elif possitions[0][0] >= NUMBER_OF_ROWS_AND_COLUMNS:
        possitions[0] = [0, possitions[0][1]]
    elif possitions[0][1] < 0:
        possitions[0] = [possitions[0][0], NUMBER_OF_ROWS_AND_COLUMNS - 1]
    elif possitions[0][1] >= NUMBER_OF_ROWS_AND_COLUMNS:
        possitions[0] = [possitions[0][0], 0]

    previous_pos = possitions[:]

    return possitions, previous_pos

def draw_snake(possitions):
    for possition in possitions:
        pygame.draw.rect(screen, YELLOW_ADVANCED, (SQUARE * possition[0] + 2, SQUARE * possition[1] + 2 + GAP, SQUARE - 4, SQUARE - 4))

def check_collision(possitions):
    game_is_running = True
    if len(possitions) > 2:
        for i in range(1, len(possitions)):
            if possitions[0] == possitions[i]:
                game_is_running = False
    return game_is_running

def check_grow(possitions, previous_pos, is_eating, candy_pos, velocity, score, AI):
    if is_eating:
        possitions.append([previous_pos[-1][0], previous_pos[-1][1]])
        candy_pos = new_candy(possitions)
        score += 1
        if velocity < 20:
            velocity += 0.2
        if score > 550 and AI:
            velocity = 24
    return possitions, candy_pos, velocity, score
