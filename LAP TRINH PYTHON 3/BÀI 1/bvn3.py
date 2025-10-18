import pygame, sys

pygame.init()

screen = pygame.display.set_mode((500, 500))
ROOF = (255, 0, 0)
GRASS = (0, 255, 0)
BACKGROUND = (255, 255, 255)
HOUSE = (221, 184, 245)
WHITE = (245, 245, 245)
screen.fill(BACKGROUND)


pygame.draw.line(screen, WHITE, [100,100],[200,200])
pygame.display.set_caption("BTVN MinhThuyet")
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
