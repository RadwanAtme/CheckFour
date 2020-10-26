column_count = 7
row_count = 6


class Player:
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def getMove(self, board):
        move = int(input(f"{self.name} Turn (Select Column 0, 1, 2, 3, 4, 5, 6):"))
        while move < 0 or move > 6 or not self.checkLegalMove(board, move):
            print("Illegal Move")
            move = int(input(f"{self.name} Turn (Select Column 0, 1, 2, 3, 4, 5, 6):"))
        return move

    def doMove(self, board, move, turn):
        for row in range(-1, -8, -1):
            if board[row][move] == 0:
                board[row][move] = turn + 1
                break
        return row

    def checkLegalMove(self, board, move):
        if move < 0 or move > 6:
            return False
        for row in range(row_count):
            if board[row][move] == 0:
                return True
        return False
