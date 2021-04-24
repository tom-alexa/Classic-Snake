import pygame, random
from Snake_game.constants import *
from Snake_game.snake import moving, check_if_out_of_map, draw_snake, check_collision, check_grow
from Snake_game.drawing_text import draw_score, check_highscore, highscores_tab, writing_new_score, max_score, exit_ask
from Snake_game.candy import new_candy, draw_candy, check_if_is_eaten
from Snake_game.key_controls import show_key_controls

# Initialize pygame
pygame.init()

# Background music
music_volume = 0.4
pygame.mixer.music.load("Music/Pirates Of The Caribbean.wav")
pygame.mixer.music.set_volume(music_volume)
pygame.mixer.music.play(-1)
pygame.mouse.set_visible(False)


def reset(AI):
    possitions = [[START_X, START_Y]]
    previous_pos = possitions[:]
    candy_pos = new_candy(possitions)
    count = 0
    direction = "right"
    previous_dir = direction

    score = 0
    pause = False
    can_change_direction = True
    key_controls_on = False
    highscores = False
    can_write = True
    if AI:
        velocity = 30
        FPS = 960
    else:
        velocity = START_VELOCITY
        FPS = 240

    return possitions, previous_pos, count, direction, candy_pos, velocity, score, pause, can_change_direction, key_controls_on, highscores, can_write, FPS


# Draw the window
def renew_window(possitions, SQUARE, candy_pos, game_is_running, score, highscore, pause, key_controls_on, highscores, writing, name_of_scorer, reseting, AI, running_first):
    screen.fill(BLACK)
    pygame.draw.rect(screen, DARK_GRAY, (0, 0, WIDTH, GAP))
    if game_is_running:
        draw_candy(candy_pos)
        draw_snake(possitions)
    draw_score(score, highscore, game_is_running, pause, key_controls_on, highscores, AI)
    if key_controls_on and (pause or not game_is_running):
        show_key_controls()
    if highscores and (pause or not game_is_running):
        highscores_tab(reseting)
    if writing and not game_is_running:
        writing_new_score(name_of_scorer)
    if not running_first:
        exit_ask()
    pygame.display.update()


# Main loop
def main():
    global music_volume
    running = True
    AI = False
    clock = pygame.time.Clock()
    possitions, previous_pos, count, direction, candy_pos, velocity, score, pause, can_change_direction, key_controls_on, highscores, can_write, FPS = reset(AI)
    highscore = 0
    writing = False
    name_of_scorer = ""
    new_game = False
    game_is_running = False
    reseting = False
    running_first = True
    one = True

    # Main loop
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if game_is_running and not pause and not AI:
                    if event.key == pygame.K_DOWN and direction != "up" and can_change_direction:
                        direction = "down"
                        can_change_direction = False
                    elif event.key == pygame.K_UP and direction != "down" and can_change_direction:
                        direction = "up"
                        can_change_direction = False
                    elif event.key == pygame.K_LEFT and direction != "right" and can_change_direction:
                        direction = "left"
                        can_change_direction = False
                    elif event.key == pygame.K_RIGHT and direction != "left" and can_change_direction:
                        direction = "right"
                        can_change_direction = False
                if (not game_is_running or pause or AI) and (event.key == pygame.K_DOWN or event.key == pygame.K_UP):
                    if event.key == pygame.K_DOWN:
                        music_volume -= 0.05
                        if music_volume < 0:
                            music_volume = 0
                    elif event.key == pygame.K_UP:
                        music_volume += 0.05
                        if music_volume > 1:
                            music_volume = 1
                    pygame.mixer.music.set_volume(music_volume)
                if (event.key == pygame.K_LSHIFT or event.key == pygame.K_RSHIFT) and not writing and running_first:
                    if not game_is_running:
                        game_is_running = not game_is_running
                        new_game = True
                    else:
                        if pause:
                            key_controls_on = False
                            highscores = False
                        pause = not pause
                elif event.key == pygame.K_a and not game_is_running and running_first and not writing:
                    AI = not AI
                elif event.key == pygame.K_ESCAPE:
                    if writing and running_first:
                        writing = False
                    if game_is_running and not pause:
                        pause = True
                    elif game_is_running and pause:
                        game_is_running = False
                        pause = False
                        highscores = False
                        key_controls_on = False
                    elif not game_is_running and (highscores or key_controls_on):
                        highscores = False
                        key_controls_on = False
                    elif not game_is_running:
                        running_first = not running_first
                elif event.key == pygame.K_TAB and (pause or not game_is_running) and not writing and running_first:
                    key_controls_on = not key_controls_on
                    highscores = False
                elif event.key == pygame.K_q and (pause or not game_is_running) and not writing and running_first:
                    highscores = not highscores
                    key_controls_on = False
                elif writing:
                    if event.key == pygame.K_TAB:
                        highscores_file = open("Snake_game/highscores.txt", "a", encoding="utf-8")
                        highscores_file.write(f'{name_of_scorer}\n    {score}\n')
                        highscores_file.close()
                        writing = False
                        name_of_scorer = ""
                        can_write = False
                    elif event.key == pygame.K_BACKSPACE:
                        name_of_scorer = name_of_scorer[:-1]
                    elif len(name_of_scorer) >= 20:
                        name_of_scorer = name_of_scorer[:21]
                    else:
                        name_of_scorer += event.unicode

                elif event.key == pygame.K_s and not game_is_running and not pause and score != 0 and can_write and running_first:
                    highscores = True
                    key_controls_on = False
                    writing = True
                    break
                elif event.key == pygame.K_r and highscores:
                    reseting = True
                elif reseting:
                    if event.key == pygame.K_y:
                        highscores_file = open("Snake_game/highscores.txt", "w", encoding="utf-8").close()
                        reseting = False
                    elif event.key == pygame.K_n:
                        reseting = False
                elif not running_first:
                    if event.key == pygame.K_y:
                        running = False
                    elif event.key == pygame.K_n:
                        running_first = True

        # Where to move next
        if new_game and not pause:
            new_game = False
            possitions, previous_pos, count, direction, candy_pos, velocity, score, pause, can_change_direction, key_controls_on, highscores,can_write, FPS = reset(AI)

        if game_is_running and not pause:
            count, possitions, previous_pos, can_change_direction, direction = moving(count, possitions, previous_pos, velocity, can_change_direction, direction, AI)
            possitions, previous_pos = check_if_out_of_map(possitions, previous_pos)
            game_is_running = check_collision(possitions)
            is_eaten = check_if_is_eaten(possitions, candy_pos)
            possitions, candy_pos, velocity, score = check_grow(possitions, previous_pos, is_eaten, candy_pos, velocity, score, AI)
        if score == 520 and one and AI:
            pause = True
            one = False
        game_is_running = max_score(score, game_is_running)
        highscore = check_highscore(highscore, score)
        renew_window(possitions, SQUARE, candy_pos, game_is_running, score, highscore, pause, key_controls_on, highscores, writing, name_of_scorer, reseting, AI, running_first)

if __name__ == "__main__":
    main()

pygame.quit()