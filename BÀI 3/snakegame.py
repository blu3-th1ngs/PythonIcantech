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


clock = pygame.time.Clock()


randFoodX = random.randrange(0, screen_width - 10)
surplusFoodX = randFoodX % 10
foodx = round(randFoodX - surplusFoodX)

randFoodY = random.randrange(0, screen_height - 10)
surplusFoodY = randFoodY % 10
foody = round(randFoodY - surplusFoodY)


print('foodx, foody', foodx, foody)


snake_list = []
snake_length = 1


def show_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(screen, BLACK, [x[0], x[1], snake_block, snake_block])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -10
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = 10
                y_head_change = 0
            elif event.key == pygame.K_UP:
                y_head_change = -10
                x_head_change = 0
            elif event.key == pygame.K_DOWN:
                y_head_change = 10
                x_head_change = 0

 
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLUE, [foodx, foody, snake_block, snake_block])


    x_head += x_head_change
    y_head += y_head_change


    snake_head = []
    snake_head.append(x_head)
    snake_head.append(y_head)
    snake_list.append(snake_head)

    if len(snake_list) > snake_length:
        del snake_list[0]


    show_snake(snake_block, snake_list)


    if x_head == foodx and y_head == foody:
        randFoodX = random.randrange(0, screen_width - 10)
        surplusFoodX = randFoodX % 10
        foodx = round(randFoodX - surplusFoodX)

        randFoodY = random.randrange(0, screen_height - 10)
        surplusFoodY = randFoodY % 10
        foody = round(randFoodY - surplusFoodY)

        snake_length += 1


    pygame.display.update()
    clock.tick(12)
