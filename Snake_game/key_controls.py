import pygame
from .constants import *

def show_key_controls():
    key_controls_font = pygame.font.Font("Fonts/coolvetica.ttf", 27)

    text_titul = "Key controls"
    titul = key_controls_font.render(text_titul, True, BLUE)

    move_up_text = "Move up"
    move_down_text = "Move down"
    move_left_text = "Move left"
    move_right_text = "Move right"

    move_up = key_controls_font.render(move_up_text, True, WHITE)
    move_down = key_controls_font.render(move_down_text, True, WHITE)
    move_left = key_controls_font.render(move_left_text, True, WHITE)
    move_right = key_controls_font.render(move_right_text, True, WHITE)

    highscores = key_controls_font.render("Highscores", True, WHITE)
    save_score = key_controls_font.render("Save score", True, WHITE)
    pause = key_controls_font.render("Pause", True, WHITE)
    start_game = key_controls_font.render("Start game", True, WHITE)
    key_controls = key_controls_font.render("Key controls", True, WHITE)
    increase_volume = key_controls_font.render("Increase volume", True, WHITE)
    decrease_volume = key_controls_font.render("Decrease volume", True, WHITE)
    ai_text = key_controls_font.render("Turn AI on/off", True, WHITE)
    back_text = key_controls_font.render("Back", True, WHITE)

    move_up_key = key_controls_font.render("[UP]", True, WHITE)
    move_down_key = key_controls_font.render("[DOWN]", True, WHITE)
    move_left_key = key_controls_font.render("[LEFT]", True, WHITE)
    move_right_key = key_controls_font.render("[RIGHT]", True, WHITE)

    highscores_key = key_controls_font.render("[Q]", True, WHITE)
    save_score_key = key_controls_font.render("[S]", True, WHITE)
    key_controls_key = key_controls_font.render("[TAB]", True, WHITE)
    start_game_key = key_controls_font.render("[SHIFT]", True, WHITE)
    ai_text_key = key_controls_font.render("[A]", True, WHITE)
    back_text_key = key_controls_font.render("[ESC]", True, WHITE)


    mini_gap = 34
    screen.blit(titul, (WIDTH//2 - (len(text_titul)*12)//2, HEIGHT//6))
    screen.blit(start_game, (WIDTH//4, HEIGHT//6 + 2*mini_gap))
    screen.blit(move_up, (WIDTH//4, HEIGHT//6 + 3*mini_gap))
    screen.blit(move_down, (WIDTH//4, HEIGHT//6 + 4*mini_gap))
    screen.blit(move_left, (WIDTH//4, HEIGHT//6 + 5*mini_gap))
    screen.blit(move_right, (WIDTH//4, HEIGHT//6 + 6*mini_gap))
    screen.blit(pause, (WIDTH//4, HEIGHT//6 + 7*mini_gap))
    screen.blit(highscores, (WIDTH//4, HEIGHT//6 + 8*mini_gap))
    screen.blit(save_score, (WIDTH//4, HEIGHT//6 + 9*mini_gap))
    screen.blit(key_controls, (WIDTH//4, HEIGHT//6 + 10*mini_gap))
    screen.blit(increase_volume, (WIDTH//4, HEIGHT//6 + 11*mini_gap))
    screen.blit(decrease_volume, (WIDTH//4, HEIGHT//6 + 12*mini_gap))
    screen.blit(ai_text, (WIDTH//4, HEIGHT//6 + 13*mini_gap))
    screen.blit(back_text, (WIDTH//4, HEIGHT//6 + 14*mini_gap))
    screen.blit(start_game_key, (3*(WIDTH//5), HEIGHT//6 + 2*mini_gap))
    screen.blit(move_up_key, (3*(WIDTH//5), HEIGHT//6 + 3*mini_gap))
    screen.blit(move_down_key, (3*(WIDTH//5), HEIGHT//6 + 4*mini_gap))
    screen.blit(move_left_key, (3*(WIDTH//5), HEIGHT//6 + 5*mini_gap))
    screen.blit(move_right_key, (3*(WIDTH//5), HEIGHT//6 + 6*mini_gap))
    screen.blit(start_game_key, (3*(WIDTH//5), HEIGHT//6 + 7*mini_gap))
    screen.blit(highscores_key, (3*(WIDTH//5), HEIGHT//6 + 8*mini_gap))
    screen.blit(save_score_key, (3*(WIDTH//5), HEIGHT//6 + 9*mini_gap))
    screen.blit(key_controls_key, (3*(WIDTH//5), HEIGHT//6 + 10*mini_gap))
    screen.blit(move_up_key, (3*(WIDTH//5), HEIGHT//6 + 11*mini_gap))
    screen.blit(move_down_key, (3*(WIDTH//5), HEIGHT//6 + 12*mini_gap))
    screen.blit(ai_text_key, (3*(WIDTH//5), HEIGHT//6 + 13*mini_gap))
    screen.blit(back_text_key, (3*(WIDTH//5), HEIGHT//6 + 14*mini_gap))
