import pygame
from .constants import *

def draw_score(score, highscore, game_is_running, pause, key_controls_on, highscores, AI):
    score_font = pygame.font.Font("Fonts/college.ttf", 30).render("Score: " + str(score), True, RED)
    screen.blit(score_font, (10, 10))

    highscore_text = pygame.font.Font("Fonts/college.ttf", 30).render("Highscore: " + str(highscore), True, BLUE)
    screen.blit(highscore_text, (WIDTH - highscore_text.get_width() - 10, 10))

    if not game_is_running and not highscores and not key_controls_on:
        shift_text = pygame.font.Font("Fonts/coolvetica.ttf", 35).render("Press [SHIFT] to start", True, WHITE)
        screen.blit(shift_text, (WIDTH//2 - shift_text.get_width()//2, HEIGHT//2))

        for i in range(7):
            mini_square = 12
            start_pos_x = mini_square*13 + 2
            start_pos_y = mini_square*12 + 2
            if i != 4:                                                                                                              # S
                pygame.draw.rect(screen, GREEN, (start_pos_x, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 0 or i == 3 or i == 6:
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*2, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i != 2:
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*3, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if True:                                                                                                                # N
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*5, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 2 or i == 3:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*6, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 3 or i == 4:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*7, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if True:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*8, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i != 0:                                                                                                              # A
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*10, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 0 or i == 3:
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*11, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*12, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i != 0:
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*13, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if True:                                                                                                                # K
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*15, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 3:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*16, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i >= 1 and i <= 5:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*17, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 0 or i == 1 or i == 5 or i == 6:
                pygame.draw.rect(screen, YELLOW_ADVANCED, (start_pos_x + mini_square*18, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if True:                                                                                                                # E
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*20, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
            if i == 0 or i == 3 or i == 6:
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*21, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*22, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))
                pygame.draw.rect(screen, GREEN, (start_pos_x + mini_square*23, start_pos_y + mini_square*i, mini_square - 4, mini_square - 4))

        author_font = pygame.font.Font("Fonts/coolvetica.ttf", 25).render("by Tomáš Alexa", True, RED)
        screen.blit(author_font, (WIDTH//2 - author_font.get_width()//2, mini_square * 20))

    if pause and not key_controls_on and not highscores:
        pause_text = pygame.font.Font("Fonts/coolvetica.ttf", 35).render("Pause", True, BLUE)
        screen.blit(pause_text, (WIDTH//2 - pause_text.get_width()//2, HEIGHT//2 - HEIGHT//10))

        pause_text_2 = pygame.font.Font("Fonts/coolvetica.ttf", 35).render("Press [SHIFT] to continue", True, WHITE)
        screen.blit(pause_text_2, (WIDTH//2 - pause_text_2.get_width()//2, HEIGHT//2))

    if (pause or not game_is_running) and not key_controls_on:
        key_controls_hind = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("Key controls [TAB]", True, RED)
        screen.blit(key_controls_hind, (30, HEIGHT - key_controls_hind.get_height() - 30))

    if AI and not key_controls_on and not highscores:
        ai_text = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("AI [A]", True, WHITE)
        screen.blit(ai_text, (WIDTH - ai_text.get_width() - 30, HEIGHT - ai_text.get_height() - 30))
    elif not AI and not game_is_running and not key_controls_on and not highscores:
        ai_text = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("AI [A]", True, DARK_GRAY)
        screen.blit(ai_text, (WIDTH - ai_text.get_width() - 30, HEIGHT - ai_text.get_height() - 30))

def check_highscore(score, highscore):
    if highscore < score:
        highscore = score
    return highscore


def highscores_tab(reseting):
    number_of_places = 0
    highscores_tab_font = pygame.font.Font("Fonts/coolvetica.ttf", 30)
    titul = highscores_tab_font.render("Highscores", True, BLUE)

    highscores = open("Snake_game/highscores.txt", "r", encoding="utf-8")

    contents = highscores.readlines()

    scores_numbers_names = []
    for i in range(len(contents)):
        if i % 2 == 1:
            scores_numbers_names.append([contents[i-1][:-1], int(contents[i])])

    scores_numbers = []
    for score in scores_numbers_names:
        if score[1] not in scores_numbers:
            scores_numbers.append(score[1])

    scores_numbers.sort(reverse=True)
    sorted_highscores = []
    for scores_number in scores_numbers:
        for scores_numbers_name in scores_numbers_names:
            if scores_number == scores_numbers_name[1]:
                sorted_highscores.append(scores_numbers_name)


    number_of_places = len(contents)//2

    highscores.close()
    screen.blit(titul, (WIDTH//2 - titul.get_width()//2, HEIGHT//6))

    reset_font = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("Reset [R]", True, BLUE)
    screen.blit(reset_font, (WIDTH - reset_font.get_width() - 30, HEIGHT - reset_font.get_height() - 30))
    if reseting:
        reset_ask_font = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("Are you sure [Y/N]", True, WHITE)
        screen.blit(reset_ask_font, (WIDTH - reset_ask_font.get_width() - 30, HEIGHT - reset_ask_font.get_height() - reset_font.get_height() - 30))


    for i in range(min(10, len(sorted_highscores))):
        content = sorted_highscores[i]
        writing_gap = 40
        writing_new_score_font = pygame.font.Font("Fonts/coolvetica.ttf", 30)
        place_name_text = writing_new_score_font.render(content[0], True, WHITE)
        place_value_text = writing_new_score_font.render(str(content[1]), True, WHITE)
        screen.blit(place_name_text, (WIDTH//2 - place_name_text.get_width(), HEIGHT//6 + (i + 2)*(writing_gap)))
        screen.blit(place_value_text, (5*(WIDTH//8), HEIGHT//6 + (i + 2)*(writing_gap)))


def writing_new_score(name_of_scorer):
    writing_gap = 40
    writing_new_score_font = pygame.font.Font("Fonts/coolvetica.ttf", 30).render(name_of_scorer, True, WHITE)
    screen.blit(writing_new_score_font, (8*(WIDTH//18) - writing_new_score_font.get_width()//2, HEIGHT//6 + writing_gap))

    shift_font = pygame.font.Font("Fonts/coolvetica.ttf", 30).render("[TAB]", True, WHITE)
    screen.blit(shift_font, (WIDTH//2 + writing_new_score_font.get_width()//2, HEIGHT//6 + writing_gap))

def max_score(score, game_is_running):
    if score >= 575:
        game_is_running = False

    return game_is_running

def exit_ask():
    exit_text = pygame.font.Font("Fonts/coolvetica.ttf", 40).render("Are you sure to quit [Y/N]", True, LIGHT_WOOD)
    screen.blit(exit_text, (WIDTH//2 - exit_text.get_width()//2, 4*(HEIGHT//6)))
