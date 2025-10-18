import pygame, sys

pygame.init()

screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Snake game")
BACKGROUND = (255, 255, 255)
SNAKE = (0, 128, 0)
APPLE = (255, 0, 0)
clock = pygame.time.Clock()

snake_block = 10
x_head = 200
y_head = 300
x_head_change = 0
y_head_change = 0

apple_block = 10
apple_x = 300
apple_y = 200

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_head_change = -snake_block
                y_head_change = 0
            elif event.key == pygame.K_RIGHT:
                x_head_change = snake_block
                y_head_change = 0
            elif event.key == pygame.K_UP:
                y_head_change = -snake_block
                x_head_change = 0
            elif event.key == pygame.K_DOWN:
                y_head_change = snake_block
                x_head_change = 0

    
    x_head += x_head_change
    y_head += y_head_change

    screen.fill(BACKGROUND)
    pygame.draw.rect(screen, APPLE, [apple_x, apple_y, apple_block, apple_block])
    pygame.draw.rect(screen, SNAKE, [x_head, y_head, snake_block, snake_block])
    pygame.display.update()
    clock.tick(15)
