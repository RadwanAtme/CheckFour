import pygame
import Board
import Player
import sys

BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)

column_count = 7
row_count = 6


def draw_board(board):
    for col in range(column_count):
        for row in range(row_count):
            pygame.draw.rect(screen, BLUE,
                             (col * square_size, row * square_size + square_size, square_size, square_size))
            if board[row][col] == 0:
                pygame.draw.circle(screen, BLACK,
                                   (int(col * square_size + square_size / 2),
                                    int(row * square_size + 3 * square_size / 2)),
                                   RADIUS)
            elif board[row][col] == 1:
                pygame.draw.circle(screen, RED,
                                   (int(col * square_size + square_size / 2),
                                    int(row * square_size + 3 * square_size / 2)),
                                   RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW,
                                   (int(col * square_size + square_size / 2),
                                    int(row * square_size + 3 * square_size / 2)),
                                   RADIUS)


Board = Board.Board()
player1 = Player.Player("player 1")
player2 = Player.Player("player 2")
turn = 0

pygame.init()
square_size = 100
width = column_count * square_size
height = (row_count + 1) * square_size
size = (width, height)
RADIUS = int(square_size / 2 - 6)

screen = pygame.display.set_mode(size)
draw_board(Board.getBoard())
pygame.display.update()
font = pygame.font.SysFont("monospace", 75)

while not Board.gameOver():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(screen, BLACK, (0,0,width, square_size))
            pos = event.pos[0]
            if turn == 0:
                pygame.draw.circle(screen, RED, (pos, int(square_size / 2)), RADIUS)
            else:
                pygame.draw.circle(screen, YELLOW, (pos, int(square_size / 2)), RADIUS)
        pygame.display.update()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if turn == 0:
                player = player1
            else:
                player = player2
            move = int(event.pos[0] / 100)
            if not player.checkLegalMove(Board.getBoard(), move):
                continue
            row = player.doMove(Board.getBoard(), move, turn)
            draw_board(Board.getBoard())
            pygame.display.update()
            turn = (turn + 1) % 2
pygame.draw.rect(screen, BLACK, (0,0,width, square_size))
if player.getName() == "player 1":
    label = font.render(f"{player.getName()} wins!!", 1, RED)
else:
    label = font.render(f"{player.getName()} wins!!", 1, YELLOW)
screen.blit(label, (40, 10))
pygame.display.update()
pygame.time.wait(3000)
