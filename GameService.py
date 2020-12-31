from BoardGame import BoardTicTacToe

class GameService:

    def __init__(self):
        super()

    def createGame(self, gameDb, username):
        gameId = gameDb.createGame(username)
        gameDb.updateUser(username, gameId)
        return gameId

    def joinGame(self, gameDb, gameId, username):
        return gameDb.joinGame(username, gameId)

    def getLatestGameStatus(self, gameDb, gameId):
        [game_id, user_x, user_o, next_turn, positions, x_win, o_win] = gameDb.getGame(gameId)
        gameBoard = BoardTicTacToe(positions.split(","))
        return [gameBoard, user_x, user_o, next_turn]

    def advance(self, gameBoard, letter, move):
        gameBoard.makeMove(letter, move)

    def saveGame(self, gameDb, gameId, gameBoard, next_turn):
        gameDb.saveGame(gameId, gameBoard.getPositions(), gameBoard.isWinner('X'), gameBoard.isWinner('O'), next_turn)

    def getListofGame(self, gameDb):
        gameDb.getListofGame();

    def loadJoinableGames (self, gameDb, username):
        return gameDb.loadFirstJoinableGame(username)

    def addSecondUserToGame(self, gameDb, un, gameId):
        gameDb.joinGame(un, gameId)
        gameDb.updateUser(un, gameId)

    def deleteJoinedGame1(self, gameDb, gameId):
        gameDb.deleteJoinedGame(gameId)