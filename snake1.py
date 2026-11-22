# встановити pygame
# python -m pip install pygame-ce
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
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()

    if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_LEFT and dx == 0:
                dx, dy = -20, 0
            if e.key == pygame.K_RIGHT and dx == 0:
                dx, dy = 20, 0
            if e.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -20
            if e.key == pygame.K_DOWN and dy == 0:
                dx, dy = 0, 20
    head = [snake[-1][0] + dx, snake[-1][1] + dy]
    snake.append(head)
    if head == food:
        food = [random.randint(0, 19) * 20,
    random.randint(0, 19) * 20]
    else:
        snake.pop(0)
        win.fill((0, 0, 0))
        for x, y in snake:
            pygame.draw.rect(win, (0, 255, 0), (x, y, 20, 20))
        pygame.draw.rect(win, (255, 0, 0), (food[0], food[1], 20, 20))
    pygame.display.update()
    clock.tick(10)
    exit()