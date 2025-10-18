import pygame, sys

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (66, 212, 245)
EXBLUE = (51, 149, 171)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
RED = (255, 0, 0)

pygame.init()

screen_width = 300
screen_height = 300
title = 'Tic Tac Toe'
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(title)

line_width = 10
cell_size = screen_width // 3
BOARD_ROWS = 3
BOARD_COLS = 3
CIRCLE_RADIUS = cell_size // 3
CIRCLE_WIDTH = 8
CROSS_WIDTH = 12
SPACE = 25

board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
player = 1
game_over = False

def draw_grid():
    pygame.draw.line(screen, EXBLUE, (cell_size, 0), (cell_size, screen_height), line_width)
    pygame.draw.line(screen, EXBLUE, (cell_size * 2, 0), (cell_size * 2, screen_height), line_width)
    pygame.draw.line(screen, EXBLUE, (0, cell_size), (screen_width, cell_size), line_width)
    pygame.draw.line(screen, EXBLUE, (0, cell_size * 2), (screen_width, cell_size * 2), line_width)

def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.line(screen, CROSS_COLOR,
                    (col * cell_size + SPACE, row * cell_size + SPACE),
                    (col * cell_size + cell_size - SPACE, row * cell_size + cell_size - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR,
                    (col * cell_size + SPACE, row * cell_size + cell_size - SPACE),
                    (col * cell_size + cell_size - SPACE, row * cell_size + SPACE), CROSS_WIDTH)
            elif board[row][col] == 2:
                center = (col * cell_size + cell_size // 2, row * cell_size + cell_size // 2)
                pygame.draw.circle(screen, CIRCLE_COLOR, center, CIRCLE_RADIUS, CIRCLE_WIDTH)

def mark_square(row, col, p):
    board[row][col] = p

def available_square(row, col):
    return board[row][col] == 0

def draw_vertical_winning_line(col):
    posX = col * cell_size + cell_size // 2
    pygame.draw.line(screen, RED, (posX, 15), (posX, screen_height - 15), 5)

def draw_horizontal_winning_line(row):
    posY = row * cell_size + cell_size // 2
    pygame.draw.line(screen, RED, (15, posY), (screen_width - 15, posY), 5)

def draw_asc_diagonal():
    pygame.draw.line(screen, RED, (15, screen_height - 15), (screen_width - 15, 15), 5)

def draw_desc_diagonal():
    pygame.draw.line(screen, RED, (15, 15), (screen_width - 15, screen_height - 15), 5)

def check_winner(p):
    for c in range(BOARD_COLS):
        if board[0][c] == p and board[1][c] == p and board[2][c] == p:
            draw_vertical_winning_line(c)
            return True
    for r in range(BOARD_ROWS):
        if board[r][0] == p and board[r][1] == p and board[r][2] == p:
            draw_horizontal_winning_line(r)
            return True
    if board[2][0] == p and board[1][1] == p and board[0][2] == p:
        draw_asc_diagonal()
        return True
    if board[0][0] == p and board[1][1] == p and board[2][2] == p:
        draw_desc_diagonal()
        return True
    return False

def restart():
    global board, player, game_over
    screen.fill(BLUE)
    draw_grid()
    board = [[0 for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    player = 1
    game_over = False

screen.fill(BLUE)
draw_grid()
pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            mouseX, mouseY = event.pos
            clicked_row = mouseY // cell_size
            clicked_col = mouseX // cell_size
            if available_square(clicked_row, clicked_col):
                mark_square(clicked_row, clicked_col, player)
                draw_figures()
                if check_winner(player):
                    game_over = True
                else:
                    player = 2 if player == 1 else 1

        if event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            restart()

    pygame.display.update()
