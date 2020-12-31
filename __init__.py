from BoardGame import BoardTicTacToe
from GameService import GameService
from GameDatabase import GameDb


def statusNow(board):
    print(board.drawBoard())
    print('X wins - ' + str(board.isWinner('X')))
    print('O wins - ' + str(board.isWinner('O')))
    print('Board Full - ' + str(board.isBoardFull()))
    print('Space Free at 1 - ' + str(board.isSpaceFree(1)))
    return

def move(board, letter, move):
    board.makeMove(letter, move)
    statusNow(board)

gameDb = GameDb()
gameService = GameService()

gameId = gameService.createGame(gameDb, 'Edison')
gameService.joinGame(gameDb, gameId, 'Charlotte')
gameInfo = gameService.getLatestGameStatus(gameDb, gameId)
gameBoard = gameInfo[0]
statusNow(gameBoard)
gameService.advance(gameBoard, 'O', 4)
gameService.saveGame(gameDb, gameId, gameBoard)
statusNow(gameBoard)
gameInfo = gameService.getGame(gameDb, gameId)
gameBoard2 = gameInfo[0]
gameService.advance(gameBoard2, 'X', 5)
gameService.advance(gameBoard2, 'O', 2)
gameService.saveGame(gameDb, gameId, gameBoard2)
statusNow(gameBoard2)



#ticTacToe1 = BoardTicTacToe()
# ticTacToe1 = BoardTicTacToe(['-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '])
# move(ticTacToe1, 'X', 2)
# move(ticTacToe1, 'O', 3)
# move(ticTacToe1, 'X', 4)
# move(ticTacToe1, 'O', 5)
# move(ticTacToe1, 'X', 1)
# move(ticTacToe1, 'O', 6)
# move(ticTacToe1, 'X', 7)
# move(ticTacToe1, 'O', 8)
# move(ticTacToe1, 'X', 9)

#ticTacToe2 = BoardTicTacToe(['-', 'X', ' ', ' ', 'O', ' ', ' ', 'X', ' ', ' '])
#$move(ticTacToe2, 'O', 2)




