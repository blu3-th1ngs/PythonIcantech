import pygame, sys

pygame.init()
W, H = 640, 360
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Hiển thị phím nhấn")
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 40)

display_text = ""     
text_color = (0, 0, 0)
bg_color = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.unicode and event.unicode.strip() != "":
                display_text = event.unicode
            else:
                display_text = pygame.key.name(event.key)

    screen.fill(bg_color)
    if display_text != "":
        text_surf = font.render(display_text, True, text_color)
        text_rect = text_surf.get_rect(center=(W // 2, H // 2))
        screen.blit(text_surf, text_rect)

    pygame.display.update()
    clock.tick(60)
