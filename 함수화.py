import time
import pygame
from time import localtime
import random

screen_width = 1500 #가로크기
screen_height = 750 #세로크기
screen = pygame.display.set_mode((screen_width, screen_height))

def run():
    global screen, clock
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()
        clock.tick(60)
    pygame.quit()

def initGame():
    global screen, clock

    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height))
    screen.display.set_caption('lala')

    clock = pygame.time.Clock()

initGame()