import pygame
import random

pygame.init()
win = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
snake = [[100, 100]]
dx, dy = 20, 0
food = [200, 200]

while True:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()