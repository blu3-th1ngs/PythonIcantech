import pygame,sys,random



pygame.init()


width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Vẽ Hình Vuông Khi Nhấn SPACE")


WHITE = (255, 255, 255)
RED = (255, 0, 0)


squares = []
clock = pygame.time.Clock()


while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                x = random.randint(0, width - 50)
                y = random.randint(0, height - 50)
                squares.append((x, y))
    for x, y in squares:
        pygame.draw.rect(screen, RED, (x, y, 50, 50))
        

    pygame.display.update()
    clock.tick(12)