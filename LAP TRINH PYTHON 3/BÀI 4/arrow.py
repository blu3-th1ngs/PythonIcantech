import pygame
import random


def color():
    return random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)


pygame.init()


screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Arrow Keys")

WHITE = (255,255,255)
BLACK = (0, 0, 0)


arrow_up_color = color()
arrow_down_color = color()
arrow_left_color = color()
arrow_right_color = color()
square = color()


running = True
while running:
    screen.fill(BLACK)

    
    pygame.draw.rect(screen, square , (175, 175, 50, 50))
    arrow_up = pygame.draw.polygon(screen, arrow_up_color, [(200, 100), (190, 125), (210, 125)])
    arrow_down = pygame.draw.polygon(screen, arrow_down_color, [(200, 300), (190, 275), (210, 275)])
    arrow_left = pygame.draw.polygon(screen, arrow_left_color, [(100, 200), (125, 190), (125, 210)])
    arrow_right = pygame.draw.polygon(screen, arrow_right_color, [(300, 200), (275, 190), (275, 210)])


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                arrow_up_color = color()
            elif event.key == pygame.K_SPACE:
                square = color()
            elif event.key == pygame.K_DOWN:
                arrow_down_color = color()
            elif event.key == pygame.K_LEFT:
                arrow_left_color = color()
            elif event.key == pygame.K_RIGHT:
                arrow_right_color = color()

    pygame.display.update()

pygame.quit()
