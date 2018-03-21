# Simply snake game based on pygame


import pygame
import sys
import random
import time


check_errors = pygame.init()
if check_errors[1] > 0:
    print("(!) Had {0} initializing errors, exiting...".format(check_errors[1]))
    sys.exit(-1)
else:
    print("(+) Pygame successfully initialized!")

# Playground
play_ground = pygame.display.set_mode((720, 560))
pygame.display.set_caption('Snake game')

# Color of playgroung

red = pygame.Color(255, 0, 0) # gameover
green = pygame.color.Color(0, 255, 0) # colour of snake
black = pygame.color.Color(0, 0, 0) # score
white = pygame.color.Color(255, 255, 255) # background
brown = pygame.color.Color(255, 255, 50) # food

# time controller by frame per seconds
fps_controller = pygame.time.Clock()

# Variables
snake_position = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

food_position = [random.randrange(1, 72) * 10, random.randrange(1, 56) * 10]
food_spawn = True

direction = 'RIGHT'
change_to = direction

# GameOver
def game_over():
    game_over_font = pygame.font.SysFont('Monospace Regular', 70)
    game_over_text = game_over_font.render('Game Over !', True, red)
    game_over_rect = game_over_text.get_rect()
    game_over_rect.midtop = (360, 15)
    play_ground.blit(game_over_text, game_over_recat)
    pygame.display.flip()
    time.sleep(5)
    pygame.quit() # pygame exit
    sys.exit() # close console


