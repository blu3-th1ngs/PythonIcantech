import pygame, sys, random

WHITE = (255, 255, 255)
YELLOW = (255, 255, 102)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)

pygame.init()

screen_width = 600
screen_height = 400
title = 'Rắn săn mồi'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

snake_block = 10
x_head = 300
y_head = 200
x_head_change = 0
y_head_change = 0
snake_list = []
snake_length = 1

clock = pygame.time.Clock()
font_style = pygame.font.SysFont("Arial", 25)

def random_food():
    x = random.randrange(0, screen_width - snake_block, snake_block)
    y = random.randrange(0, screen_height - snake_block, snake_block)
    return x, y

foodx, foody = random_food()

def show_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])

def show_score(score):
    value = font_style.render("Score: " + str(score), True, BLACK)
    screen.blit(value, [0, 0])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and x_head_change == 0:
                x_head_change = -snake_block
                y_head_change = 0
            elif event.key == pygame.K_RIGHT and x_head_change == 0:
                x_head_change = snake_block
                y_head_change = 0
            elif event.key == pygame.K_UP and y_head_change == 0:
                y_head_change = -snake_block
                x_head_change = 0
            elif event.key == pygame.K_DOWN and y_head_change == 0:
                y_head_change = snake_block
                x_head_change = 0

    x_head += x_head_change
    y_head += y_head_change

    if x_head >= screen_width or x_head < 0 or y_head >= screen_height or y_head < 0:
        pygame.quit()
        sys.exit()

    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [foodx, foody, snake_block, snake_block])

    snake_head = [x_head, y_head]
    snake_list.append(snake_head)
    if len(snake_list) > snake_length:
        del snake_list[0]

    for block in snake_list[:-1]:
        if block == snake_head:
            pygame.quit()
            sys.exit()

    show_snake(snake_block, snake_list)
    show_score(snake_length - 1)

    if x_head == foodx and y_head == foody:
        foodx, foody = random_food()
        snake_length += 1

    pygame.display.update()
    clock.tick(12)
