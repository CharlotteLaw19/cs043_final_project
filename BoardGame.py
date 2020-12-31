class BoardGame:
    def __init__(self):
        super().__init__()

    def isWinner(self, letter):
        pass

    def makeMove(self, letter, move):
        pass

    def drawBoard(self):
        pass

    def isBoardFull(self):
        pass

    def getPositions(self):
        pass


class BoardTicTacToe(BoardGame):
    def __init__(self):
        self.theBoard = [''] * 10
        super().__init__()

    def __init__(self, board):
        self.theBoard = board
        super().__init__()

    def isWinner(self, letter):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        bo = self.theBoard
        le = letter

        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def makeMove(self, letter, move):
        self.theBoard[move] = letter

    def drawBoard(self):
        # This function prints out the board that it was passed.
        board = self.theBoard

        # "board" is a list of 10 strings representing the board (ignore index 0)
        message = '\n'
        message += '\n   |   |'
        message += '\n ' + board[7] + ' | ' + board[8] + ' | ' + board[9]
        message += '\n   |   |'
        message += '\n-----------'
        message += '\n   |   |'
        message += '\n ' + board[4] + ' | ' + board[5] + ' | ' + board[6]
        message += '\n   |   |'
        message += '\n-----------'
        message += '\n   |   |'
        message += '\n ' + board[1] + ' | ' + board[2] + ' | ' + board[3]
        message += '\n   |   |'
        message += '\n'
        return message

    def isBoardFull(self):
        board = self.theBoard

        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(i):
                return False
        return True

    def isSpaceFree(self, move):
        board = self.theBoard
        # Return true if the passed move is free on the passed board.
        return board[move] == '' or board[move] == ' '

    def getPositions(self):
        return self.theBoard
