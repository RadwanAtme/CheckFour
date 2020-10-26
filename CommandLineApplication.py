import Player
import Board

Board = Board.Board()
player1 = Player.Player("player 1")
player2 = Player.Player("player 2")
turn = 1
while not Board.gameOver():
    turn = (turn + 1) % 2
    if turn == 0:
        player = player1
    else:
        player = player2
    Board.printBoard()
    move = player.getMove(Board.getBoard())
    player.doMove(Board.getBoard(), move, turn)
Board.printBoard()
print(f"Winner is {player.getName()}")
