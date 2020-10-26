column_count = 7
row_count = 6


class Board:
    def __init__(self):
        self.board = [[0, 0, 0, 0, 0, 0, 0] for i in range(row_count)]

    def getBoard(self):
        return self.board

    def printBoard(self, ):
        for i in range(row_count):
            print(self.board[i])

    def gameOver(self, ):
        return self.checkRow() or self.checkColumn() or self.checkDiagonal() or self.checkRevDiagonal()

    def checkRow(self):
        for row in self.board:
            for col in range(column_count - 3):
                if row[col] == 0:
                    continue
                if row[col] == row[col + 1] and row[col] == row[col + 2] and row[col] == row[col + 3]:
                    return True
        return False

    def checkColumn(self):
        board = self.board
        for col in range(column_count):
            for row in range(row_count - 3):
                if board[row][col] == 0:
                    continue
                if board[row][col] == board[row + 1][col] and \
                        board[row][col] == board[row + 2][col] and \
                        board[row][col] == board[row + 3][col]:
                    return True
        return False

    def checkDiagonal(self):
        board = self.board
        for row in range(row_count - 3):
            for col in range(column_count - 3):
                if board[row][col] == 0:
                    continue
                if board[row][col] == board[row + 1][col + 1] and \
                        board[row][col] == board[row + 2][col + 2] and \
                        board[row][col] == board[row + 3][col + 3]:
                    return True
        return False

    def checkRevDiagonal(self):
        board = self.board
        for row in range(row_count - 3):
            for col in range(-1, -5, -1):
                if board[row][col] == 0:
                    continue
                if board[row][col] == board[row + 1][col - 1] and \
                        board[row][col] == board[row + 2][col - 2] and \
                        board[row][col] == board[row + 3][col - 3]:
                    return True
        return False

