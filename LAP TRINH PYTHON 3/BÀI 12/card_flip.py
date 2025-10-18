import pygame
import os
import random
import time

pygame.init()
pygame.mixer.init()


def load_sound(path):
    if not os.path.exists(path):
        print(f"⚠️ Warning: Sound file not found: {path}")
        return None
    return pygame.mixer.Sound(path)


correct_sound = load_sound("Sounds/correct-choice-43861.mp3")
error_sound   = load_sound("Sounds/error-126627.mp3")
win_sound     = load_sound("Sounds/level-win-6416.mp3")


WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Card Flip Game")


CARD_BACK = pygame.Surface((100, 150))
CARD_BACK.fill((0, 0, 0))


card_files = [
    "Images/01_of_spades_A.svg.png",
    "Images/Playing_card_heart_A.svg.png",
    "Images/Playing_card_diamond_A.svg.png",
    "Images/Playing_card_club_A.svg.png"
]

cards = []
for file in card_files:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Image file not found: {file}")
    img = pygame.image.load(file)
    img = pygame.transform.scale(img, (100, 150))
    cards.append(img)


deck = cards * 2
random.shuffle(deck)


flipped = []   # indices of currently flipped cards
matched = []   # indices of matched cards
card_positions = []


rows, cols = 2, 4
spacing_x, spacing_y = 120, 180
offset_x, offset_y = 100, 100

for row in range(rows):
    for col in range(cols):
        x = offset_x + col * spacing_x
        y = offset_y + row * spacing_y
        card_positions.append(pygame.Rect(x, y, 100, 150))


def draw():
    SCREEN.fill((34, 139, 34)) 
    for i, rect in enumerate(card_positions):
        if i in matched or i in flipped:
            SCREEN.blit(deck[i], rect)
        else:
            SCREEN.blit(CARD_BACK, rect)
    pygame.display.flip()

clock = pygame.time.Clock()
running = True
check_time = 0
checking = False

while running:
    draw()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not checking:
            pos = pygame.mouse.get_pos()
            for i, rect in enumerate(card_positions):
                if rect.collidepoint(pos) and i not in flipped and i not in matched:
                    flipped.append(i)
                    break

           
            if len(flipped) == 2:
                checking = True
                check_time = time.time()

    
    if checking and time.time() - check_time > 1:
        if deck[flipped[0]] == deck[flipped[1]]:
            matched.extend(flipped)
            if correct_sound:
                correct_sound.play()
        else:
            if error_sound:
                error_sound.play()
        flipped.clear()
        checking = False

   
    if len(matched) == len(deck):
        SCREEN.fill((0, 128, 0))
        font = pygame.font.Font(None, 74)
        text = font.render("YOU WIN!", True, (255, 215, 0))
        SCREEN.blit(text, (WIDTH//2 - 150, HEIGHT//2 - 50))
        pygame.display.flip()
        if win_sound:
            win_sound.play()
        pygame.time.wait(3000)
        running = False

    clock.tick(30)

pygame.quit()
