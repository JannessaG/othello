import pygame
from constants import *
from othello import *

def rowcol_to_xy(row, col):
    return 12 + 68 * col, 578 - 68 * row

def xy_to_rowcol(x, y):
    row_y = (643, 575, 507, 439, 371, 303, 235, 167)
    col_x = (12, 80, 148, 216, 284, 352, 420, 488)

    if x > 12 and y > 102 and x < 553 and y < 643:
        for row in range(8):
            if y < row_y[row] and y > row_y[row] - SQUARE_HEIGHT:
                break
        for col in range(8):
            if x > col_x[col] and x < col_x[col] + SQUARE_WIDTH:
                break
        return row, col     
    else:
        return -1, -1

def draw_board():
    screen.blit(img_board, (0, 0))


def draw_play_color():
    if play[Othello.BLACK] == "human":
        human_plays_color = img_black_disc
        ai_plays_color = img_white_disc
    else:
        human_plays_color = img_white_disc
        ai_plays_color = img_black_disc

    screen.blit(human_plays_color, (HUMAN_PLAYS_X, HUMAN_PLAYS_Y))
    screen.blit(ai_plays_color, (AI_PLAYS_X, AI_PLAYS_Y))
    
def draw_disc_counter():
    if play[Othello.BLACK] == "human":
        human_discs_on_board = str(game.black_discs)
        ai_discs_on_board = str(game.white_discs)
    else:
        human_discs_on_board = str(game.white_discs)
        ai_discs_on_board = str(game.black_discs)

    text = text_font.render(human_discs_on_board, True, WHITE)
    text_rect = text.get_rect()
    text_rect.left = RECT_LEFT
    text_rect.top = RECT_TOP
    screen.blit(text, text_rect)

    text = text_font.render(ai_discs_on_board, True, WHITE)
    text_rect = text.get_rect()
    text_rect.right = RECT_RIGHT
    text_rect.top = RECT_TOP
    screen.blit(text, text_rect)

def draw_discs_on_board():
    for row in range(8):
        for col in range(8):
            if [row, col] not in game.flip_discs:
                if game.board[row][col] == Othello.BLACK:
                    x, y = rowcol_to_xy(row, col)
                    screen.blit(img_black_disc, (x+1, y+2))
                elif game.board[row][col] == Othello.WHITE:
                    x, y = rowcol_to_xy(row, col)
                    screen.blit(img_white_disc, (x+1, y+2))


def draw_screen():
    if len(game.flip_discs) > 0:
        first_disc = game.flip_discs[0]

        for index in range(start, stop, step):
            draw_board()
            draw_play_color()
            draw_disc_counter()
            draw_discs_on_board()
            pygame.display.update()
    else:
        draw_board()
        draw_play_color()
        draw_disc_counter()
        draw_discs_on_board()
        pygame.display.update()


# Initialize Pygame
pygame.init()
pygame.font.init()

# Font to display disc counter for both players
text_font = pygame.font.SysFont("Arial", 53, True)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WITH, SCREEN_HEIGHT))

# Title and icon
pygame.display.set_caption("Othello")


# Load images
img_board = pygame.image.load(r"images\board.png").convert()
img_disc = pygame.image.load(r"images\disc.png").convert_alpha()
img_white_disc = img_disc.subsurface((0, 0, DISC_WIDTH, DISC_HEIGHT))
img_black_disc = img_disc.subsurface((DISC_WIDTH * 8, 0, DISC_WIDTH, DISC_HEIGHT))



game = Othello()
play = {Othello.BLACK:"human", Othello.WHITE:"ai"}
last_turn = None
draw_screen()

# Game loop  
while True:
		if game:
			game = Othello()
			draw_screen()
		else:
			pygame.quit()
			exit()
